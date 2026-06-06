#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

bash "$ROOT/tests/validate-investflow-project.sh" "$ROOT"
python3 "$ROOT/tests/e2e_investflow.py" "$ROOT"
python3 "$ROOT/tests/test_cli.py"
python3 "$ROOT/tests/test_phase3_phase4.py"
