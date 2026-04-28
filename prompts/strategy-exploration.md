# Solution Strategy Exploration

## When to trigger

All of the following should be accepted in Plan.md before exploring strategies:
- Problem Statement
- Target Audience / Persona
- Evidence
- Hypothesis

## How it works

Spawn 3 or more sub-agents, each with a DIFFERENT system prompt. Each sub-agent independently proposes a fundamentally different approach to solving the validated problem. They do NOT see each other's work.

### Sub-agent prompt template

Each sub-agent receives:

```
You are a product strategist. You have been given a validated problem, target audience, evidence, and hypothesis. Your job is to propose ONE approach to solving this problem.

Your approach must be fundamentally different from a [description of the other approaches — e.g., "technology-driven solution" vs. "process/people solution" vs. "platform/ecosystem solution"]. Think creatively about different ways the problem could be addressed.

Problem: [from Plan.md]
Target Audience: [from Plan.md]
Evidence: [from Plan.md]
Hypothesis: [from Plan.md]

Propose your approach with:
1. **What it does** — the core idea in 2-3 sentences
2. **Why it might work** — how it connects to the evidence and addresses the problem
3. **Why it might not** — risks, assumptions, gaps in the evidence
4. **Does it solve the validated problem?** — explicitly check: does this approach address the specific problem we identified, for the specific audience, supported by the specific evidence? If it only partially addresses it, say so.
```

### Ensuring diversity

To get genuine diversity, vary the sub-agent prompts along dimensions like:
- Technology-driven vs. process-driven vs. people-driven
- Build new vs. modify existing vs. remove/simplify
- Direct solution vs. indirect/enabling solution
- Short-term tactical vs. long-term strategic

### Presenting results

After all sub-agents return, synthesize and present to the PM:

1. List each approach with its four fields
2. Highlight where approaches differ most — this is where the PM's judgment matters
3. Ask the PM which approach resonates and why — their reasoning reveals hidden insights
4. If the PM gravitates toward one, probe: "What made you lean toward that one? What would change your mind?"

Do NOT recommend one. Let the PM choose. Challenge their reasoning.
