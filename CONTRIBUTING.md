# Contributing

InvestFlow contributions should improve agent behavior, not only add more prompts.

The project is currently an early MVP. Useful contributions should strengthen one of these areas:

- Core investment research skills.
- Report templates and workflow scenarios.
- CLI validation, audit, rendering, and install behavior.
- Read-only data and MCP integrations.
- Community skill packs.
- Documentation that makes boundaries clearer.

## Good Contributions

- New skills with clear trigger rules and boundary checks.
- Better investment research templates.
- Examples that show missing information, risk review, and invalidation conditions.
- Tests that catch unsafe, overconfident, or incomplete agent outputs.
- Documentation that clarifies compliance boundaries.

## Workflow Scenario Contributions

Scenario contributions should include:

- A plan document under `docs/superpowers/plans/`.
- A template under `templates/` when the scenario produces a user-facing artifact.
- CLI documentation when a new command or template alias is introduced.
- Tests in `tests/test_cli.py`, `tests/e2e_investflow.py`, or `tests/validate-investflow-project.sh`.

Run:

```bash
./scripts/investflow scenario list
./scripts/validate.sh
```

## Skill Requirements

Each skill must:

- Live in `skills/<skill-name>/SKILL.md`.
- Use YAML frontmatter with `name` and `description`.
- Start the description with `Use when`.
- Include when to use, required inputs, workflow, output format, and common mistakes.
- Avoid standalone buy or sell instructions.

## Community Pack Requirements

Community packs must:

- Live under `packs/community/<pack-name>`.
- Include a `pack.json` manifest.
- Include `not_investment_advice` in boundaries.
- Avoid `trade_execution`, `brokerage_write`, and `place_order`.
- Pass:

```bash
./scripts/investflow pack validate packs/community/<pack-name>
```

## Review Checklist

- Does the skill prevent premature investment conclusions?
- Does it ask for missing context?
- Does it require current data when needed?
- Does it include risk, invalidation, and review triggers?
- Is it concise enough for an agent to load quickly?
- Do `./scripts/validate.sh` and plugin manifest validation pass?
