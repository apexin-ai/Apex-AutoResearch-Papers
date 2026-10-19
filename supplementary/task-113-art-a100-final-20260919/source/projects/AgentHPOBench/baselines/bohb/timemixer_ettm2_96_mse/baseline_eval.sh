#!/usr/bin/env bash
set -euo pipefail

BASE="."
OUT="$BASE/results/formal_baselines/timemixer_ettm2_96_mse/baseline_small"
mkdir -p "$OUT"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export TIMEMIXER_CUDA_VISIBLE_DEVICES="${TIMEMIXER_CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$BASE/repositories/TimeMixer:$BASE/.python_deps:${PYTHONPATH:-}"
python "$BASE/baselines/bohb/timemixer_ettm2_96_mse/eval_timemixer_ettm2.py" \
  --results-dir "$OUT" \
  --run-name baseline \
  --d-model 8 \
  --d-ff 16 \
  --e-layers 1 \
  --down-sampling-layers 1 \
  --down-sampling-window 2 \
  --learning-rate 0.01 \
  --batch-size 512 \
  --epochs "${TIMEMIXER_EPOCHS:-3}" \
  --patience 2
