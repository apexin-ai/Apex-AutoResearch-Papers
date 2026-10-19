#!/usr/bin/env bash
set -euo pipefail

BASE=.
FORMAL=$BASE/tasks/ablations/no_feedback/cifar10_airbench94
OUT=$BASE/results/formal_baselines/cifar10_airbench94/budget_baseline

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1}
export PYTHONPATH="$BASE:$BASE/.python_deps:$BASE/repositories/cifar10-airbench:${PYTHONPATH:-}"
python "$FORMAL/eval_cifar10_airbench94.py" \
  --results-dir "$OUT" \
  --epochs "${AIRBENCH_EPOCHS:-3.0}" \
  --batch-size 1024 \
  --eval-batch-size 2000 \
  --learning-rate 11.5 \
  --weight-decay 0.0153 \
  --momentum 0.85 \
  --label-smoothing 0.2 \
  --translate 2 \
  --tta-level 2 \
  --seed 42 \
  --verbose
