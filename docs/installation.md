# Installation

InvestFlow is a source repository plus a set of Codex-compatible skills.

## Clone

```bash
git clone https://github.com/Zach0911/investflow.git
cd investflow
```

## Install for Codex

```bash
./scripts/install-codex-skills.sh
```

This copies the bundled skills into:

```text
~/.codex/skills/
```

After installation, Codex can discover these skills:

- `using-investflow`
- `investment-briefing`
- `company-research`
- `thesis-builder`
- `valuation-check`
- `risk-review`
- `dialectic-investment-decision`
- `postmortem`

## Custom Target

```bash
CODEX_SKILLS_DIR=/path/to/skills ./scripts/install-codex-skills.sh
```

## Update Installed Skills

The installer copies files. It does not create symlinks.

After editing files under `skills/`, run the installer again:

```bash
./scripts/install-codex-skills.sh
```

The script only updates InvestFlow's own skill directories and does not delete unrelated skills in `~/.codex/skills/`.

## Validate

```bash
./scripts/validate.sh
```

## Use the CLI

```bash
./scripts/investflow doctor
./scripts/investflow list skills
./scripts/investflow new thesis --output work/thesis.md
./scripts/investflow validate work/thesis.md
```

The CLI is local and offline. It does not fetch market data or produce investment recommendations.
