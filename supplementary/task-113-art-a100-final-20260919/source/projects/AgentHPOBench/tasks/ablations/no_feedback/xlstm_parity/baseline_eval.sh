#!/usr/bin/env bash
set -euo pipefail

BASE=.
FORMAL=$BASE/tasks/ablations/no_feedback/xlstm_parity
OUT=$BASE/results/formal_baselines/xlstm_parity/budget_baseline
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1}
export PYTHONPATH="$BASE/repositories/xlstm:${PYTHONPATH:-}"
python "$FORMAL/eval_xlstm_parity.py" \
  --results-dir "$OUT" \
  --train-steps "${XLSTM_TRAIN_STEPS:-120}" \
  --train-count "${XLSTM_TRAIN_COUNT:-8192}" \
  --eval-count "${XLSTM_EVAL_COUNT:-2048}" \
  --learning-rate 1e-4 \
  --weight-decay 0.1 \
  --warmup-ratio 0.1 \
  --batch-size 128 \
  --slstm-pattern last \
  --use-amp
