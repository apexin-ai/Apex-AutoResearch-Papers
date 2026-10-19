#!/usr/bin/env bash
set -euo pipefail

BASE="."
OUT="$BASE/results/formal_baselines/timexer_pjm_168_24_mse/baseline_small"
mkdir -p "$OUT"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export TIMEXER_CUDA_VISIBLE_DEVICES="${TIMEXER_CUDA_VISIBLE_DEVICES:-1}"
python "$BASE/baselines/bohb/timexer_pjm_168_24_mse/eval_timexer_pjm.py" \
  --results-dir "$OUT" \
  --run-name baseline \
  --d-model 64 \
  --d-ff 64 \
  --e-layers 1 \
  --patch-len 24 \
  --learning-rate 0.0005 \
  --batch-size 64 \
  --epochs "${TIMEXER_EPOCHS:-1}" \
  --patience 1
