# Quality Criteria Per Section

Use these criteria when critiquing a proposed section. If the proposal fails any criterion, iterate before presenting it as ready for acceptance.

## Problem Statement

**Universal criteria (must pass all):**
- Does not smuggle in a solution direction ("we need to build X" is a solution, not a problem)
- Is not a strategy question disguised as a problem ("how do we do X" is strategy)
- Names who specifically is affected — not "people" or "users" but a identifiable group in a specific situation. If you can't name who, the problem isn't understood well enough yet.
- Is specific enough that you could imagine solutions that address it and solutions that don't (if everything is a valid solution, the problem is too vague)
- Is grounded in evidence or observable reality, not just intuition or assumption

**Depending on the type of problem, one of these should also be true:**
- *Customer/user problem:* Describes something specific that a real, identifiable group experiences today — a pain, a gap, a workaround, a failure. Names who is affected.
- *Business problem:* Describes a specific, measurable impact on the business — revenue, churn, conversion, cost, growth ceiling. Quantified where possible.
- *Opportunity:* Describes a specific unmet need or underserved segment, with evidence that the need exists and is significant enough to pursue. Acknowledges that nothing is "broken" — the case rests on the size and accessibility of the opportunity.
- *Technical/platform problem:* Describes a specific limitation or failure mode in the system, with evidence of its impact on users, developers, or business outcomes.
- *External constraint:* Describes a specific requirement imposed by regulation, partners, or market conditions, with a clear consequence for not addressing it and a timeline.

## Target Audience / Persona

This section should cover multiple layers. Not all layers apply to every problem — use what's relevant.

**Segment (who is the organization or entity?):**
- Identifies a specific segment, not "all customers" or "everyone" (e.g., enterprise, mid-market, a specific industry, a partner type, an internal team)
- Describes the characteristics that make this segment particularly affected by the problem or valuable for the opportunity
- If multiple segments are affected, identifies which one to focus on first and why
- Is narrow enough to design a solution for, broad enough to matter commercially

**Personas within the segment (who are the specific people?):**
- Identifies the distinct personas involved — these may include end users, buyers, decision-makers, gatekeepers, admins, partners, etc.
- Does not conflate the buyer with the end user — if they're different people, they're listed separately
- Does not conflate the customer segment with the persona (e.g., "enterprise customers" is a segment, "HR managers at enterprise companies" is a persona)
- Each persona is described with enough specificity to have distinct needs from adjacent personas

**How each persona is affected:**
- For each persona, describes how they specifically experience the problem (or benefit from the opportunity)
- Different personas may experience the same problem differently — a gatekeeper blocking adoption is affected differently from an end user who can't access the tool
- Identifies which persona is the primary beneficiary of solving this problem and which personas need to be satisfied (even if not the primary beneficiary) for the solution to succeed

**Consistency checks:**
- Does the persona match the evidence collected? (e.g., if evidence is about enterprise customers, the persona shouldn't say mid-market)
- Are there segments or personas the evidence pointed to that are being ignored?
- If there's a buyer-user gap (the person paying is not the person using), is that explicitly acknowledged?

## Evidence

**Completeness:**
- Includes at least one data point that is not just the PM's personal belief (quantitative data, customer quotes, observed behavior, market data, expert input, competitive analysis — something external to the PM's head)
- If quantitative evidence exists, it is included (usage data, revenue impact, churn numbers, conversion rates, etc.)
- If qualitative evidence exists, it is included (customer quotes, observed workarounds, support patterns, sales conversation themes)
- Evidence covers the full problem — if the problem statement has multiple facets, each facet should have supporting evidence

**Relevance and connection:**
- Every piece of evidence clearly connects to the problem statement — not just generally interesting data about the space
- Evidence connects to the target audience — the data should be about the specific segment and personas identified, not a different group
- If evidence was gathered from a different segment than the target, that mismatch is acknowledged

**Honesty:**
- If some evidence contradicts the problem or weakens the case, that contradiction is acknowledged rather than hidden
- The strength of the evidence is honestly assessed — is this overwhelming, strong, directional, or thin? Don't overstate confidence.
- The source of each piece of evidence is identified — is this from direct observation, secondhand reports, the PM's memory, or formal research?
- Recency is noted where relevant — evidence from 2 years ago may not reflect current reality

**Gaps:**
- Are there obvious questions that the evidence doesn't answer? These should be listed as known gaps.
- Is the PM relying on a single data point where multiple would be needed to be convincing?
- Is there evidence the PM likely has access to but hasn't gathered yet? (e.g., usage data they could pull, customers they could talk to)

## Hypothesis

**Specificity:**
- States a specific expected outcome, not a vague improvement ("engagement goes up" is vague; "dashboard abandonment drops from 40% to under 20%" is specific)
- Identifies what metric or observable change would indicate success — and is realistic about whether that metric is measurable with the PM's current tools
- If an exact number isn't possible, states a directional expectation with reasoning ("we expect at least X because Y")

**Logical grounding:**
- Logically follows from the problem and evidence — each step in the reasoning chain is explicit, not a leap
- The causal mechanism is stated: why would solving this problem produce this outcome? What's the theory of change?
- Does not assume the solution — the hypothesis should be about what happens if the problem is solved, not about a specific solution working

**Falsifiability and honesty:**
- Is falsifiable — you could imagine evidence that would disprove it
- Acknowledges uncertainty honestly — how confident are we and why?
- Identifies what would make you abandon this hypothesis (what evidence would prove it wrong?)
- Does not conflate multiple hypotheses into one — if there are multiple expected outcomes, each should be stated separately so they can be independently validated

**Consistency checks:**
- Does the hypothesis match the target audience? (the expected outcome should be about the personas identified)
- Does the hypothesis match the evidence? (if the evidence says X, the hypothesis shouldn't assume Y without explanation)
- Is the timeframe realistic? (expecting a metric to move in a week vs. a quarter changes everything)

## Solution Strategy

**What it is:**
- Is an approach, not a feature spec — describes the general strategy, not implementation details
- Is clearly distinguishable from other possible approaches — if you can't describe what an alternative strategy would look like, this isn't specific enough
- Can be summarized in 1-2 sentences without losing its meaning

**Connection to the problem:**
- Addresses the specific validated problem for the specific target audience — not a different problem, not a different audience
- The connection to the evidence is explicit — how does this strategy leverage what we know?
- Does not solve a problem we haven't validated (a common sign of scope creep or pet solutions)

**Rigor of selection:**
- Is one of several possible approaches that were considered — the PM should be able to name the alternatives and explain why this one was chosen over them
- The reasons for choosing this strategy over alternatives are grounded in evidence and the specific problem, not just preference or familiarity
- If the PM's initial instinct was a different strategy, the reason for the shift (or the reason for sticking with it) is articulated

**Risks and assumptions:**
- Acknowledges risks — what could go wrong with this approach?
- Acknowledges assumptions — what must be true for this strategy to work that we haven't proven?
- Identifies what would make this the wrong strategy (what would you need to see to pivot?)
- Passes a basic feasibility check — is this something the team could realistically pursue given their skills, resources, and timeline?

**Consistency checks:**
- Does the strategy actually address all facets of the problem, or just the easiest one?
- Does the strategy serve the primary persona identified in the target audience?
- If the strategy requires capabilities the team doesn't have, is that acknowledged?

## Scope

**Right-sizing:**
- Is the smallest version of the chosen strategy that would validate the hypothesis
- Does not try to validate multiple hypotheses at once — if there are multiple, pick the riskiest or most important one
- Is not a "phase 1" that's only useful if phase 2 also gets built — it should stand alone as a valid test even if nothing else is built after it
- Has a realistic time estimate grounded in the team's actual capacity, not aspirational timelines

**Assumption chain:**
- Makes the assumption chain explicit — what must be true for this scoped version to work that we haven't proven yet?
- Shows the dependency chain from simplest validation to this scope — what does this scope assume that a simpler version would have tested?
- If the PM chose a more complex scope over a simpler one, the reasoning is articulated (what do you learn from this scope that you wouldn't learn from the simpler version?)

**Boundaries:**
- Clearly defines what is included and what is not
- "Not included" items are genuine exclusions, not things being hand-waved ("we'll handle auth later" when auth is critical to the experience)
- Edge cases and known limitations are listed — not exhaustively, but the obvious ones
- There's a clear definition of "done" — when has this scope been fully shipped?

**Consistency checks:**
- Does the scope actually test the hypothesis? (it's possible to build the right strategy at the wrong scope and learn nothing)
- Does the scope serve the primary persona? (or has it been simplified so much that the persona's real needs aren't met?)
- Is the scope achievable in the timeframe stated? (sanity check against team size, complexity, dependencies)
