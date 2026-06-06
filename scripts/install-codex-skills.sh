#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${CODEX_SKILLS_DIR:-$HOME/.codex/skills}"

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

mkdir -p "$TARGET"

for skill in "${skills[@]}"; do
  source_dir="$ROOT/skills/$skill"
  target_dir="$TARGET/$skill"

  if [[ ! -f "$source_dir/SKILL.md" ]]; then
    echo "Missing source skill: $source_dir/SKILL.md" >&2
    exit 1
  fi

  mkdir -p "$target_dir"
  rsync -a --delete --exclude ".DS_Store" "$source_dir/" "$target_dir/"
  echo "Installed $skill -> $target_dir"
done

echo "Installed ${#skills[@]} InvestFlow skills to $TARGET"
