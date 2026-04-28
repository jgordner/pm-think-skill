# Prototype Generation

## When to trigger

The PM has accepted a Scope in Plan.md.

## How it works

Generate a prototype the PM can react to. This serves two purposes:
1. The PM sees their idea made concrete, which surfaces hidden instincts and assumptions
2. The prototype becomes a communication tool for collaborating with Eng/Design/PMM

### Step 1 — Ask about fidelity

> "Want this to look like your actual app? You can:
> 1. Share a screenshot of the current UI and I'll match the style
> 2. If I'm running in your repo, I can use your existing components and design system
> 3. Or I'll make a generic mockup to get a feel for the feature
>
> Which works best?"

### Step 2 — Generate

Based on the PM's choice:

- **Screenshot match:** Read the screenshot, extract visual style (colors, fonts, spacing, component patterns). Generate HTML that looks like it belongs in that app.
- **In-repo:** Read the existing frontend code, identify the design system/component library. Generate using real components.
- **Generic:** Generate clean HTML with Tailwind CSS. Modern, professional, but not styled to any specific app.

The prototype should represent the SCOPED version (not the full vision). It should be concrete enough to react to — real content, real interactions, real UI patterns.

### Step 3 — Get reactions

After sharing the prototype:

> "Take a look and tell me what stands out. What feels right? What feels wrong? What are you noticing about the idea now that you can see it?"

The PM's reaction often reveals things that change the plan:
- "Seeing this, I realize the real problem is actually..." → revisit Problem Statement
- "This doesn't feel right because..." → hidden assumption about the solution
- "Oh, this should also show..." → scope creep signal, or legitimate gap in the scope
- "This is exactly what I meant" → confirmation, proceed to output

Record reactions in the Insight Journal. Update Plan.md if the reaction changes anything.
