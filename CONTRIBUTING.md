# Contributing

InvestFlow contributions should improve agent behavior, not only add more prompts.

## Good Contributions

- New skills with clear trigger rules and boundary checks.
- Better investment research templates.
- Examples that show missing information, risk review, and invalidation conditions.
- Tests that catch unsafe, overconfident, or incomplete agent outputs.
- Documentation that clarifies compliance boundaries.

## Skill Requirements

Each skill must:

- Live in `skills/<skill-name>/SKILL.md`.
- Use YAML frontmatter with `name` and `description`.
- Start the description with `Use when`.
- Include when to use, required inputs, workflow, output format, and common mistakes.
- Avoid standalone buy or sell instructions.

## Review Checklist

- Does the skill prevent premature investment conclusions?
- Does it ask for missing context?
- Does it require current data when needed?
- Does it include risk, invalidation, and review triggers?
- Is it concise enough for an agent to load quickly?
