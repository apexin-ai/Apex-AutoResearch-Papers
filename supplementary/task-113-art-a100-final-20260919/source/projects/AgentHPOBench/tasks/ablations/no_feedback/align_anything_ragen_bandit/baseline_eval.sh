#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_ROOT:-.}"
OUT="$BASE/results/formal_baselines/align_anything_ragen_bandit"
python "$BASE/tasks/ablations/no_feedback/align_anything_ragen_bandit/eval_align_anything_ragen_bandit.py" \
  --results-dir "$OUT" \
  --learning-rate 0.01 \
  --batch-size 16 \
  --entropy-coef 0.0 \
  --temperature 1.6 \
  --reward-baseline none \
  --optimizer sgd \
  --steps 20 \
  --seed 42
