#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

bash "$ROOT/tests/validate-investflow-project.sh" "$ROOT"
python3 "$ROOT/tests/e2e_investflow.py" "$ROOT"
