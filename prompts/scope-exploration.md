# Scope Exploration

## When to trigger

The PM has accepted a Solution Strategy in Plan.md. This phase explores how much of that strategy to build first.

## How it works

Spawn 3 sub-agents, each exploring a different scope level within the CHOSEN strategy. They do not see each other's work.

### Sub-agent 1 — Simplest validation

```
You are scoping the simplest possible version of a solution strategy. Your goal: what is the absolute cheapest thing that could test whether the hypothesis is right? This might not be a product feature at all — it could be a manual process, a concierge test, a survey, a landing page, or a one-off script.

Strategy: [from Plan.md]
Problem: [from Plan.md]
Hypothesis: [from Plan.md]

Propose the simplest validation with:
1. **What it is** — describe it concretely
2. **What it validates** — which part of the hypothesis does this test?
3. **What it assumes** — what must be true for this to work that we haven't proven yet?
4. **Time to ship** — realistic estimate
5. **What it sacrifices** — what don't you learn from this version?
```

### Sub-agent 2 — Focused product

```
You are scoping a right-sized product version of a solution strategy. Your goal: a real feature or product that solves the core problem well enough to learn from actual usage, but is scoped tightly.

Strategy: [from Plan.md]
Problem: [from Plan.md]
Hypothesis: [from Plan.md]

Propose the focused version with:
1. **What it is** — describe the feature/product concretely
2. **What it validates** — what do you learn from real usage?
3. **What it assumes** — what must be true that the simplest validation would have proven? (Make the dependency chain explicit)
4. **Time to ship** — realistic estimate
5. **What it sacrifices** — what's left out that the full vision would include?
```

### Sub-agent 3 — Full vision

```
You are describing the full realization of a solution strategy with no constraints. Your goal: what would this look like if fully built out?

Strategy: [from Plan.md]
Problem: [from Plan.md]
Hypothesis: [from Plan.md]

Describe the full vision with:
1. **What it is** — the complete picture
2. **What it validates** — what additional things do you learn beyond the focused version?
3. **What it assumes** — what must be true that hasn't been proven? (Full dependency chain from simplest through focused to here)
4. **Time to ship** — realistic estimate
5. **What it sacrifices** — what's the opportunity cost of building all this?
```

### Presenting results

After all sub-agents return:

1. Present all three scope options side by side
2. Highlight the assumption chain — the full vision assumes everything the focused version assumes, which assumes everything the simplest version assumes
3. Ask: "What would you lose by trying the simplest version first? Is there a reason you need more than that to learn what you need to learn?"
4. Challenge premature commitment to the complex option if the simpler one tests the same hypothesis
