# InvestFlow

[English](README.md) | [中文](README.zh-CN.md)

[![Validate](https://github.com/Zach0911/investflow/actions/workflows/validate.yml/badge.svg)](https://github.com/Zach0911/investflow/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-early%20MVP-blue.svg)](#project-status)

InvestFlow is an open-source skills framework and research methodology for investment agents.

It helps AI agents stop answering "should I buy this?" too early. Instead, agents must clarify the investment question, check the data basis, build a thesis, challenge it with risks, and produce a reviewable research output.

InvestFlow is not investment advice. It does not execute trades, manage accounts, promise returns, or replace a licensed financial adviser.

## Project Status

InvestFlow is an early MVP with a working local toolchain:

| Module | Status |
|---|---|
| Core skills | 8 skills for briefing, company research, thesis building, valuation, risk review, decision pressure-testing, and postmortem |
| Report templates | 13 templates covering baseline reports and 10 Superpowers-inspired workflow scenarios |
| Examples | 8 examples, including a complete thesis report, losing-position review, ETF review, portfolio review, and postmortem |
| CLI | Generates, validates, audits, and renders reports; lists scenarios and local resources |
| MCP | Local read-only baseline for listing data sources, reading sample data, and rendering reports |
| Community packs | 1 sample pack with manifest validation |

The current priority is investment-agent workflow infrastructure, not trading, stock picking, or live market-data aggregation.

See [CHANGELOG.md](CHANGELOG.md) for release notes.

## Who This Is For

- Personal investors who want structured AI-assisted research records.
- AI agent builders who need reusable investment research skills, CLI tools, and MCP hooks.
- Research writers who want auditable, reviewable report templates.
- Open-source contributors who want to add skills, examples, templates, and boundary tests.

## What This Is Not

- Not a stock recommendation tool.
- Not an automated trading system.
- Not a live market-data or financial terminal.
- Not a substitute for licensed investment, tax, legal, or accounting advice.

## Why This Exists

Personal investors increasingly use AI to research stocks, ETFs, funds, sectors, and portfolios. The main failure mode is not that AI says too little. It is that AI says too much before it knows enough.

InvestFlow gives agents a stricter operating system:

- Ask for instrument, horizon, position, and risk context before actionable views.
- Separate facts, assumptions, thesis, valuation, risks, and missing data.
- Require the strongest opposing argument before a conclusion.
- Attach invalidation conditions and review triggers to every actionable label.
- Preserve outputs as reusable research records.

## Core Skills

| Skill | Purpose |
|---|---|
| `using-investflow` | Routes investment tasks to the right skill and enforces project-wide boundaries. |
| `investment-briefing` | Clarifies the investment question before analysis. |
| `company-research` | Structures business, financial, sector, and governance research. |
| `thesis-builder` | Converts research into a testable investment thesis. |
| `valuation-check` | Checks price versus assumptions and comparable valuation context. |
| `risk-review` | Runs a risk-first and contrarian review. |
| `dialectic-investment-decision` | Pressure-tests buy, hold, reduce, avoid, hedge, or compare decisions. |
| `postmortem` | Reviews decisions after outcomes are known. |

## Use Cases

InvestFlow is designed for investment research scenarios where an AI agent needs discipline before producing a conclusion.

| Scenario | Example Question | Suggested Flow |
|---|---|---|
| Clarify a vague stock question | "Can I still buy this stock?" | `investment-briefing` -> `company-research` -> `risk-review` |
| Research a company | "Help me understand this company's business quality." | `company-research` -> `thesis-builder` |
| Build an investment thesis | "What is the investable thesis for this company?" | `company-research` -> `thesis-builder` -> `risk-review` |
| Check valuation risk | "Is this ETF or stock expensive now?" | `valuation-check` -> `risk-review` |
| Review a losing position | "I am down 25%. Should I add more?" | `investment-briefing` -> `risk-review` -> `dialectic-investment-decision` |
| Review portfolio concentration | "My technology exposure is too high. Should I reduce it?" | `risk-review` -> `dialectic-investment-decision` |
| Compare two assets | "Which is more suitable for my long-term plan?" | `investment-briefing` -> `valuation-check` -> `risk-review` |
| Review a past decision | "Was this investment mistake avoidable?" | `postmortem` |

These flows are research workflows, not trading commands. If current market data matters, the agent should verify and cite the data source and timestamp.

### 10 Workflow Scenarios

Inspired by Superpowers, InvestFlow now includes workflow scaffolds for investment agents:

| Scenario | CLI Entry |
|---|---|
| Research design brief | `./scripts/investflow new design` |
| Research execution plan | `./scripts/investflow new plan` |
| Evidence-first audit | `./scripts/investflow audit report.md` |
| Pre-conclusion decision gate | `./scripts/investflow new decision-gate` |
| Multi-agent research handoff | `./scripts/investflow new multi-agent` |
| Data-linked report brief | `./scripts/investflow new data-brief` |
| Report lifecycle | `./scripts/investflow new lifecycle` |
| Community skill pack proposal | `./scripts/investflow new pack-proposal` |
| Platform adapter checklist | `./scripts/investflow new platform-adapter` |
| Postmortem loop | `./scripts/investflow new postmortem-loop` |

See [Scenario Overview](docs/scenarios.zh-CN.md) for details.

## Repository Layout

```text
investflow/
├── README.md
├── README.zh-CN.md
├── DISCLAIMER.md
├── .mcp.json
├── .codex-plugin/
├── AGENTS.md
├── CONTRIBUTING.md
├── data/
├── docs/
├── examples/
├── packs/
├── scripts/
├── skills/
│   ├── using-investflow/
│   ├── investment-briefing/
│   ├── company-research/
│   ├── thesis-builder/
│   ├── valuation-check/
│   ├── risk-review/
│   ├── dialectic-investment-decision/
│   └── postmortem/
├── templates/
└── tests/
```

More complete examples are available in [`examples/`](examples/), including a full thesis report, losing-position review, ETF long-term review, company-to-thesis research, and investment postmortems.

## Quick Start

Run the local workflow first:

```bash
git clone https://github.com/Zach0911/investflow.git
cd investflow
./scripts/investflow quickstart
```

This creates:

```text
work/quickstart/thesis.md
work/quickstart/thesis.html
```

Then validate and render:

```bash
./scripts/investflow validate work/quickstart/thesis.md
./scripts/investflow render work/quickstart/thesis.md --output work/quickstart/thesis.html
```

For a more complete report example, read:

```text
examples/full-thesis-report-example.zh-CN.md
```

When an agent uses InvestFlow, the recommended flow is:

1. Pick the skill that matches the task.
2. Read that skill's `SKILL.md`.
3. Ask the required boundary questions before producing investment analysis.
4. Use templates from `templates/` for the final output.
5. Validate the report with the CLI.
6. If current market data is required, cite the data source and timestamp.

Example prompt:

```text
Use InvestFlow to analyze whether I should keep holding this ETF.
```

If the user has not provided instrument, horizon, position, and risk tolerance, the agent should ask for those first.

## CLI

InvestFlow includes a lightweight local CLI for report scaffolding and validation:

```bash
./scripts/investflow --help
./scripts/investflow doctor
./scripts/investflow quickstart
./scripts/investflow scenario list
./scripts/investflow list skills
./scripts/investflow new thesis --output work/thesis.md
./scripts/investflow validate work/thesis.md
./scripts/investflow audit work/thesis.md
./scripts/investflow data list
./scripts/investflow data read sample-market-snapshot
./scripts/investflow render work/thesis.md --output work/thesis.html
./scripts/investflow pack list
./scripts/investflow install codex
```

The CLI does not fetch market data, generate investment advice, or execute trades. It only works with local skills, templates, examples, and Markdown reports.

See the [CLI Guide](docs/cli.md) for the full workflow.
See the [Scenario Overview](docs/scenarios.zh-CN.md) for the 10 Superpowers-inspired optimization scenarios.
See [Phase 2 CLI Requirements](docs/phase-2-cli-requirements.zh-CN.md) for command contracts and acceptance criteria.
See [Phase 3 MCP/Data Requirements](docs/phase-3-mcp-data-requirements.zh-CN.md) and [Phase 4 Report/Community Requirements](docs/phase-4-report-community-requirements.zh-CN.md) for the read-only data, MCP, report rendering, and community pack boundaries.

## MCP and Data Connectors

InvestFlow includes a local MCP server manifest:

```text
.mcp.json
```

The MCP server exposes read-only tools for listing registered data sources, reading registered sample data, and rendering local Markdown reports. It does not connect to brokerages, fetch live market data, or execute trades.

## Install for Codex

Install the bundled skills into Codex's local skill directory:

```bash
./scripts/install-codex-skills.sh
```

By default, this installs to `~/.codex/skills`. Override the target with `CODEX_SKILLS_DIR`:

```bash
CODEX_SKILLS_DIR=/path/to/skills ./scripts/install-codex-skills.sh
```

The installer copies skills rather than symlinking them. After editing `skills/`, run the installer again so Codex uses the latest version.

See [Installation](docs/installation.md) for clone, update, and validation details.

## Decision Labels

InvestFlow avoids standalone "buy" or "sell" conclusions. Use bounded labels instead:

- `信息不足`
- `不建议参与`
- `谨慎观察`
- `低仓位试错`
- `分批参与`
- `持有但设退出条件`
- `减仓控制风险`

Every actionable label must include assumptions, position sizing, invalidation conditions, and review triggers.

## Roadmap

- Phase 1: skills framework, templates, examples, boundary tests.
- Phase 2: CLI for report scaffolding and validation.
- Phase 3: MCP and read-only data connectors.
- Phase 4: report generation and community skill packs.

## Contributing

Contributions are welcome:

- New investment research skills.
- New report templates or complete examples.
- Community skill packs.
- Stricter boundary tests.
- Platform adapter documentation.

Before contributing, read [CONTRIBUTING.md](CONTRIBUTING.md) and [Compliance Boundaries](docs/compliance-boundaries.md).

## License

MIT License.
