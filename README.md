# InvestFlow

[English](README.md) | [中文](README.zh-CN.md)

InvestFlow is an open-source skills framework and research methodology for investment agents.

It helps AI agents stop answering "should I buy this?" too early. Instead, agents must clarify the investment question, check the data basis, build a thesis, challenge it with risks, and produce a reviewable research output.

InvestFlow is not investment advice. It does not execute trades, manage accounts, promise returns, or replace a licensed financial adviser.

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

## Repository Layout

```text
investflow/
├── README.md
├── README.zh-CN.md
├── DISCLAIMER.md
├── .codex-plugin/
├── AGENTS.md
├── CONTRIBUTING.md
├── docs/
├── examples/
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

More complete examples are available in [`examples/`](examples/), including losing-position review, ETF long-term review, company-to-thesis research, and investment postmortems.

## Quick Start

1. Pick the skill that matches the task.
2. Read that skill's `SKILL.md`.
3. Ask the required boundary questions before producing investment analysis.
4. Use templates from `templates/` for the final output.
5. If current market data is required, cite the data source and timestamp.

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
./scripts/investflow list skills
./scripts/investflow new thesis --output work/thesis.md
./scripts/investflow validate work/thesis.md
./scripts/investflow install codex
```

The CLI does not fetch market data, generate investment advice, or execute trades. It only works with local skills, templates, examples, and Markdown reports.

See [Phase 2 CLI Requirements](docs/phase-2-cli-requirements.zh-CN.md) for command contracts and acceptance criteria.

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

## License

MIT License.
