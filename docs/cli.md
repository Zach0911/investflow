# InvestFlow CLI Guide

InvestFlow CLI helps with local report scaffolding, structure validation, HTML rendering, sample data access, and Codex skill installation.

It does not fetch live market data, connect to brokerages, execute trades, or generate investment advice.

## 1. Three-Minute Quick Start

Run this from the project root:

```bash
./scripts/investflow quickstart
```

This creates:

```text
work/quickstart/thesis.md
work/quickstart/thesis.html
```

If generated files already exist, the CLI refuses to overwrite them. Rebuild explicitly with:

```bash
./scripts/investflow quickstart --force
```

Use a custom output directory:

```bash
./scripts/investflow quickstart --output-dir work/demo
```

## 2. Common Commands

| Command | Purpose |
|---|---|
| `./scripts/investflow doctor` | Check project structure, skills, templates, MCP, and community packs. |
| `./scripts/investflow scenario list` | List the 10 Superpowers-inspired optimization scenarios. |
| `./scripts/investflow scenario show evidence-audit` | Show a scenario command and plan document. |
| `./scripts/investflow list skills` | List bundled skills. |
| `./scripts/investflow list templates` | List report templates. |
| `./scripts/investflow list examples` | List examples. |
| `./scripts/investflow new thesis --output work/thesis.md` | Create a thesis report scaffold. |
| `./scripts/investflow validate work/thesis.md` | Validate required report sections and boundaries. |
| `./scripts/investflow audit work/thesis.md` | Audit data sources, timestamps, contrarian view, invalidation, and review triggers. |
| `./scripts/investflow render work/thesis.md --output work/thesis.html` | Render a Markdown report to HTML. |
| `./scripts/investflow data list` | List registered read-only data sources. |
| `./scripts/investflow data read sample-market-snapshot` | Read a sample data source. |
| `./scripts/investflow pack list` | List community skill packs. |
| `./scripts/investflow install codex` | Install bundled skills into Codex. |

## 3. Recommended Workflow

### 3.1 Create a Report

```bash
./scripts/investflow new thesis --output work/my-thesis.md
```

Other templates:

```bash
./scripts/investflow new design --output work/research-design.md
./scripts/investflow new plan --output work/research-plan.md
./scripts/investflow new brief --output work/research-brief.md
./scripts/investflow new risk-review --output work/risk-review.md
./scripts/investflow new decision-gate --output work/decision-gate.md
./scripts/investflow new multi-agent --output work/multi-agent.md
./scripts/investflow new data-brief --output work/data-brief.md
./scripts/investflow new lifecycle --output work/lifecycle.md
./scripts/investflow new pack-proposal --output work/pack-proposal.md
./scripts/investflow new platform-adapter --output work/platform-adapter.md
./scripts/investflow new postmortem --output work/postmortem.md
./scripts/investflow new postmortem-loop --output work/postmortem-loop.md
```

### 3.2 Fill the Report

Clarify:

- Instrument: stock, ETF, fund, sector, or portfolio.
- Decision: research, hold, reduce, review, compare, etc.
- Horizon: short, medium, or long term.
- Position: current or planned exposure.
- Risk tolerance: drawdown, liquidity, and concentration limits.
- Data basis: sources, timestamps, and missing information.

### 3.3 Validate

```bash
./scripts/investflow validate work/my-thesis.md
```

Validation checks required sections and prevents standalone `买入` / `卖出` title-style conclusions.

### 3.4 Audit Evidence

```bash
./scripts/investflow audit work/my-thesis.md
```

The audit checks data source, timestamp, strongest contrarian view, invalidation conditions, review triggers, and position boundaries.

### 3.5 Render

```bash
./scripts/investflow render work/my-thesis.md --output work/my-thesis.html
```

Preview HTML even if validation fails:

```bash
./scripts/investflow render work/my-thesis.md --output work/my-thesis.html --force
```

## 4. JSON Output

Use JSON output from scripts, agents, or MCP tooling:

```bash
./scripts/investflow --json doctor
./scripts/investflow --json quickstart --output-dir work/demo
./scripts/investflow --json validate work/my-thesis.md
./scripts/investflow --json audit work/my-thesis.md
./scripts/investflow --json scenario list
./scripts/investflow --json list skills
```

## 5. Scenario Discovery

List all scenarios:

```bash
./scripts/investflow scenario list
```

Show one scenario:

```bash
./scripts/investflow scenario show research-design
```

## 6. Complete Example

Read the complete example report:

```text
examples/full-thesis-report-example.zh-CN.md
```

The example uses a fictional company and is for workflow demonstration only. It is not investment advice.
