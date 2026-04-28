#!/usr/bin/env python3
"""
sync.py — Syncs local markdown files with comment.io docs

Usage:
    python3 sync.py init <file>     — Create a new comment.io doc for a local file
    python3 sync.py push <file>     — Push local file contents to its comment.io doc
    python3 sync.py pull <file>     — Pull comment.io doc contents to local file
    python3 sync.py status          — Show all tracked files and their comment.io URLs
    python3 sync.py url <file>      — Print the comment.io URL for a tracked file

Tracking is stored in .sync-manifest.json in the same directory as this script.
"""

import json
import os
import subprocess
import sys

MANIFEST_PATH = os.path.join(os.getcwd(), ".sync-manifest.json")
BASE_URL = "https://comment.io"


def load_manifest():
    if not os.path.exists(MANIFEST_PATH):
        return {}
    with open(MANIFEST_PATH) as f:
        return json.load(f)


def save_manifest(manifest):
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)


DISPLAY_NAME = "PM Thinking Partner"


def api_request(method, path, token=None, data=None):
    cmd = ["curl", "-s", "-X", method, f"{BASE_URL}{path}"]
    if token:
        cmd.extend(["-H", f"Authorization: Bearer {token}"])
    if data is not None:
        cmd.extend(["-H", "Content-Type: application/json", "-d", json.dumps(data)])
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)


def identify(slug, token):
    """Register a display name for an anonymous per-doc token. Required before writes."""
    response = api_request("POST", "/agents/identify", token=token, data={
        "display_name": DISPLAY_NAME,
        "slug": slug,
    })
    if "actor_id" not in response:
        print(f"Identify failed: {response}")
        sys.exit(1)
    return response


def ensure_identified(filepath, manifest, entry):
    """Lazily identify if we haven't already for this manifest entry."""
    if entry.get("identified"):
        return
    identify(entry["slug"], entry["token"])
    entry["identified"] = True
    manifest[filepath] = entry
    save_manifest(manifest)


def init_file(filepath):
    filepath = os.path.abspath(filepath)
    manifest = load_manifest()

    # If already tracked, just print the existing URL
    if filepath in manifest:
        print(f"Already tracked: {manifest[filepath]['url']}")
        return manifest[filepath]['url']

    basename = os.path.splitext(os.path.basename(filepath))[0]

    with open(filepath) as f:
        content = f.read()

    response = api_request("POST", "/docs", data={
        "title": basename,
        "markdown": content
    })

    slug = response["id"]
    token = response["access_token"]
    owner = response.get("owner_secret")
    url = f"https://comment.io/d/{slug}?token={token}"

    identify(slug, token)

    manifest = load_manifest()
    manifest[filepath] = {
        "slug": slug,
        "token": token,
        "owner_secret": owner,
        "url": url,
        "last_revision": response.get("revision", 1),
        "identified": True,
    }
    save_manifest(manifest)

    print(f"Created comment.io doc: {url}")
    return url


def push_file(filepath, force=False):
    filepath = os.path.abspath(filepath)
    manifest = load_manifest()

    if filepath not in manifest:
        print(f"File not tracked. Run: python3 sync.py init {filepath}")
        sys.exit(1)

    entry = manifest[filepath]
    ensure_identified(filepath, manifest, entry)

    # Read local content
    with open(filepath) as f:
        local_content = f.read()

    # Fetch remote content and revision
    remote = api_request("GET", f"/docs/{entry['slug']}", token=entry["token"])
    remote_content = remote.get("markdown", "")
    revision = remote.get("revision")

    if remote_content == local_content:
        print(f"Already up to date (revision: {revision})")
        return

    # Check if remote has been edited since our last sync
    last_known_revision = entry.get("last_revision")
    if last_known_revision is not None and revision != last_known_revision and not force:
        print(f"WARNING: Remote doc has been edited (expected revision {last_known_revision}, found {revision}).")
        print(f"Someone may have edited the comment.io doc directly.")
        print(f"Run 'python3 sync.py pull {os.path.basename(filepath)}' to get remote changes first,")
        print(f"or 'python3 sync.py push --force {os.path.basename(filepath)}' to overwrite.")
        sys.exit(1)

    # Replace entire remote content with local content
    response = api_request("PATCH", f"/docs/{entry['slug']}", token=entry["token"], data={
        "edits": [
            {
                "old_string": remote_content,
                "new_string": local_content
            }
        ],
        "base_revision": revision
    })

    if "revision" in response:
        failed = response.get("failed", 0)
        if failed > 0:
            print(f"Push failed: edit did not match remote content")
            sys.exit(1)
        # Update last known revision
        entry["last_revision"] = response["revision"]
        save_manifest(manifest)
        print(f"Pushed to comment.io (revision: {response['revision']})")
    else:
        print(f"Push failed: {response}")
        sys.exit(1)


def pull_file(filepath):
    filepath = os.path.abspath(filepath)
    manifest = load_manifest()

    if filepath not in manifest:
        print(f"File not tracked. Run: python3 sync.py init {filepath}")
        sys.exit(1)

    entry = manifest[filepath]

    response = api_request("GET", f"/docs/{entry['slug']}", token=entry["token"])

    with open(filepath, "w") as f:
        f.write(response["markdown"])

    # Update last known revision
    entry["last_revision"] = response.get("revision")
    save_manifest(manifest)

    print(f"Pulled from comment.io to {filepath} (revision: {response.get('revision')})")


def show_status():
    manifest = load_manifest()
    if not manifest:
        print("No files tracked.")
        return

    for path, info in manifest.items():
        exists = "✓" if os.path.exists(path) else "✗ (missing)"
        print(f"{exists} {path}")
        print(f"  URL: {info['url']}")
        print()


def show_url(filepath):
    filepath = os.path.abspath(filepath)
    manifest = load_manifest()

    if filepath not in manifest:
        print(f"File not tracked.")
        sys.exit(1)

    print(manifest[filepath]["url"])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "init" and len(sys.argv) >= 3:
        init_file(sys.argv[2])
    elif command == "push" and len(sys.argv) >= 3:
        force = "--force" in sys.argv
        filepath = [a for a in sys.argv[2:] if not a.startswith("--")][0]
        push_file(filepath, force=force)
    elif command == "pull" and len(sys.argv) >= 3:
        pull_file(sys.argv[2])
    elif command == "status":
        show_status()
    elif command == "url" and len(sys.argv) >= 3:
        show_url(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)
