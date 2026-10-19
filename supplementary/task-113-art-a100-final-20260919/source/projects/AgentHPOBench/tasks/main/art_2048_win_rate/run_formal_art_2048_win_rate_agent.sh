#!/usr/bin/env bash
set -euo pipefail

ROOT="${AUTOREP_ROOT:-.}"
cd "${ROOT}"

export PYTHONPATH="${ROOT}:${ROOT}/.python_deps:${PYTHONPATH:-}"
python "${ROOT}/tasks/main/art_2048_win_rate/run_formal_art_2048_win_rate_agent.py"
