#!/usr/bin/env bash
set -euo pipefail

ROOT="${AUTOREP_ROOT:-.}"
OUT="${ROOT}/results/formal_baselines/art_2048_win_rate"
mkdir -p "${OUT}"

python "${ROOT}/tasks/ablations/no_feedback/art_2048_win_rate/eval_art_2048_win_rate.py" \
  --results-dir "${OUT}" \
  --lookahead-depth 2 \
  --empty-weight 2.0 \
  --merge-weight 1.0 \
  --max-tile-weight 2.0 \
  --corner-weight 2.0 \
  --smoothness-weight 0.2 \
  --move-order up_left_right_down \
  --games "${ART_2048_GAMES:-25}" \
  --max-moves "${ART_2048_MAX_MOVES:-70}" \
  --seed 42
