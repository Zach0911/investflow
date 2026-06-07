# Skill Authoring

InvestFlow skills are agent-facing operating instructions.

Use this structure:

```markdown
---
name: skill-name
description: Use when ...
---

# Skill Name

## Overview
## When to Use
## Required Inputs
## Workflow
## Output Format
## Common Mistakes
```

Keep each skill concise. Move long examples, market-specific checklists, or data schemas into references only when needed.

Descriptions should describe trigger conditions, not summarize the full process.

## Required Boundaries

Every investment-facing skill should preserve these boundaries:

- Ask for missing instrument, horizon, position, risk, and data context before actionable analysis.
- Require source and timestamp when current market, filing, valuation, fund holding, or policy data matters.
- Avoid standalone `买入`, `卖出`, `buy`, or `sell` conclusions.
- Include risks, invalidation conditions, position context, and review triggers when producing an actionable label.

## When to Add a Template Instead of a Skill

Add a template when the improvement is mainly a reusable output structure:

- Research design brief.
- Research execution plan.
- Decision gate.
- Multi-agent handoff.
- Data-linked report brief.
- Report lifecycle.
- Community pack proposal.
- Platform adapter checklist.
- Postmortem loop.

Add a skill when the improvement changes agent behavior, routing, or reasoning procedure.
