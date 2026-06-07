# Getting Started

Use InvestFlow when an investment question needs structure.

## Run the Local Workflow

```bash
./scripts/investflow quickstart
./scripts/investflow validate work/quickstart/thesis.md
./scripts/investflow audit work/quickstart/thesis.md
./scripts/investflow render work/quickstart/thesis.md --output work/quickstart/thesis.html
```

## Agent Workflow

1. Start with `skills/using-investflow/SKILL.md`.
2. Route the task to the matching skill.
3. If the user asks for a decision, confirm instrument, horizon, position, and risk tolerance.
4. If current data matters, verify it and state the source time.
5. Use a template from `templates/`.
6. Run `investflow validate` for report structure.
7. Run `investflow audit` for evidence, timestamp, invalidation, and review-trigger checks.
8. End with bounded judgment, risks, invalidation conditions, and review triggers.

For a first run, try `examples/stock-research-example.md`.

## Scenario Workflow

List the 10 workflow scenarios:

```bash
./scripts/investflow scenario list
```

Generate a research task brief before deep analysis:

```bash
./scripts/investflow new design --output work/research-design.md
```

Generate a research execution plan:

```bash
./scripts/investflow new plan --output work/research-plan.md
```
