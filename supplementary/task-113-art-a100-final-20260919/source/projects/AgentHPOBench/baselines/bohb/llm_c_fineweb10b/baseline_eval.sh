#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTOREP_ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"
REPO_DIR="${REPO_DIR:-$AUTOREP_ROOT/repositories/llm.c}"
BACKEND="${BACKEND:-cuda_c}"

if [[ ! -d "$REPO_DIR" ]]; then
  echo "Missing repo: $REPO_DIR" >&2
  exit 2
fi

if [[ "$BACKEND" == "pytorch" ]]; then
  cmd=(bash scripts/pyrun_gpt2_124M.sh)
else
  cmd=(bash scripts/run_gpt2_124M.sh)
fi

echo "Repo: $REPO_DIR"
printf 'Command:'
printf ' %q' "${cmd[@]}"
printf '\n'

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  exit 0
fi

cd "$REPO_DIR"
"${cmd[@]}"
