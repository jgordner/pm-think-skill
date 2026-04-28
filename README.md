# /think — PM Thinking Partner

A Claude Code skill that helps a PM go from instinct or directive to a high-quality plan. Walks through problem framing, solution strategy, scope, and prototyping with phase discipline and built-in critique.

## Install

```bash
git clone <repo-url> ~/.claude/skills/think
```

Restart Claude Code. The skill is now available as `/think` from any working directory.

## Use

In a fresh Claude Code session, in whatever directory you want your planning files to live:

```
/think
```

The skill will create `Plan.md`, `Parking Lot.md`, and `Insight Journal.md` in the current directory and walk you through a planning conversation.

## Comment.io sync

All three markdown files sync to [comment.io](https://comment.io) so you can edit them in a browser, leave comments, and share with collaborators.

**No setup required.** On first sync, `sync.py` creates anonymous comment.io docs and stores per-doc tokens in `.sync-manifest.json` in your working directory. You'll get URLs you can bookmark or share.

If your working directory is a git repo, add `.sync-manifest.json` to `.gitignore` — those tokens grant edit access to your docs.

Manual commands (the skill handles these for you, but they're available):

```bash
python3 sync.py init <file>     # Create a comment.io doc
python3 sync.py push <file>     # Push local → remote
python3 sync.py pull <file>     # Pull remote → local
python3 sync.py status          # List tracked files
```

## Requirements

- Claude Code
- Python 3 (for `sync.py`)
- `curl` (for comment.io API calls)

## Updates

```bash
cd ~/.claude/skills/think && git pull
```
