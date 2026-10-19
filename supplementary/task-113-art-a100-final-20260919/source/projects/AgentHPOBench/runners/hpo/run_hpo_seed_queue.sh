#!/usr/bin/env bash
set -euo pipefail

SEED="${1:?seed: 0, 1, or 42}"
GPU_ID="${2:?gpu id}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
ROOT="$(cd "$ROOT" && pwd)"
cd "$ROOT"
BRANCH="$ROOT/runners/hpo"

bash "$BRANCH/run_hpo_seed_phase.sh" random "$SEED" "$GPU_ID" nonray
bash "$BRANCH/run_hpo_seed_phase.sh" tpe "$SEED" "$GPU_ID" nonray
bash "$BRANCH/run_hpo_seed_phase.sh" bohb "$SEED" "$GPU_ID" nonray
bash "$BRANCH/run_hpo_seed_phase.sh" random "$SEED" "$GPU_ID" ray
bash "$BRANCH/run_hpo_seed_phase.sh" tpe "$SEED" "$GPU_ID" ray
bash "$BRANCH/run_hpo_seed_phase.sh" bohb "$SEED" "$GPU_ID" ray

echo "=== HPO SEED QUEUE COMPLETE $(date -Is) seed=$SEED gpu=$GPU_ID ==="
