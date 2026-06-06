#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

need_file() {
  [[ -f "$ROOT/$1" ]] || fail "missing file: $1"
}

need_dir() {
  [[ -d "$ROOT/$1" ]] || fail "missing directory: $1"
}

need_text() {
  local file="$1"
  local pattern="$2"
  rg -q -- "$pattern" "$ROOT/$file" || fail "missing pattern in $file: $pattern"
}

need_dir "."
need_file "README.md"
need_file "README.zh-CN.md"
need_file "LICENSE"
need_file "DISCLAIMER.md"
need_file "CONTRIBUTING.md"
need_file "AGENTS.md"
need_file ".gitignore"
need_file ".codex-plugin/plugin.json"
need_file "scripts/install-codex-skills.sh"
need_dir "skills"
need_dir "docs"
need_dir "examples"
need_dir "templates"
need_dir "scripts"
need_dir "tests"

skills=(
  using-investflow
  investment-briefing
  company-research
  thesis-builder
  valuation-check
  risk-review
  dialectic-investment-decision
  postmortem
)

for skill in "${skills[@]}"; do
  need_file "skills/$skill/SKILL.md"
  need_text "skills/$skill/SKILL.md" "^---$"
  need_text "skills/$skill/SKILL.md" "^name: $skill$"
  need_text "skills/$skill/SKILL.md" "^description: Use when "
done

need_text "README.md" "InvestFlow"
need_text "README.md" "skills framework"
need_text "README.md" "not investment advice"
need_text "README.md" "README.zh-CN.md"
need_text "README.md" "Use Cases"
need_text "README.md" "Review a losing position"
need_text "README.md" "portfolio concentration"
need_text "README.zh-CN.md" "InvestFlow 是一个面向投资 Agent"
need_text "README.zh-CN.md" "不构成投资建议"
need_text "README.zh-CN.md" "核心 Skills"
need_text "README.zh-CN.md" "使用场景"
need_text "README.zh-CN.md" "复盘亏损持仓"
need_text "README.zh-CN.md" "组合集中度"
need_text "README.zh-CN.md" "README.md"
need_text ".gitignore" "\\.DS_Store"
need_text ".codex-plugin/plugin.json" "\"name\": \"investflow\""
need_text ".codex-plugin/plugin.json" "\"skills\": \"./skills/\""
need_text "scripts/install-codex-skills.sh" "CODEX_SKILLS_DIR"
need_text "scripts/install-codex-skills.sh" "rsync -a --delete"
need_text "scripts/install-codex-skills.sh" "using-investflow"
need_text "scripts/install-codex-skills.sh" "postmortem"
need_text "DISCLAIMER.md" "not investment advice"
need_text "DISCLAIMER.md" "does not execute trades"
need_text "skills/investment-briefing/SKILL.md" "标的"
need_text "skills/investment-briefing/SKILL.md" "周期"
need_text "skills/investment-briefing/SKILL.md" "仓位"
need_text "skills/investment-briefing/SKILL.md" "风险"
need_text "skills/risk-review/SKILL.md" "反方"
need_text "skills/dialectic-investment-decision/SKILL.md" "Do not output"
need_text "examples/stock-research-example.md" "信息不足"
need_text "tests/skill-boundary-cases.md" "expected behavior"

echo "InvestFlow project validation passed: $ROOT"
