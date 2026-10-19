#!/usr/bin/env bash
set -euo pipefail

BASE=.
FORMAL=$BASE/baselines/bohb/cifar10_airbench94
OUT=$BASE/results/formal_data_checks/cifar10_airbench94

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1}
export PYTHONPATH="$BASE:$BASE/.python_deps:$BASE/repositories/cifar10-airbench:${PYTHONPATH:-}"
python "$FORMAL/eval_cifar10_airbench94.py" \
  --results-dir "$OUT" \
  --epochs 0.1 \
  --batch-size 1024 \
  --eval-batch-size 2000 \
  --learning-rate 11.5 \
  --weight-decay 0.0153 \
  --momentum 0.85 \
  --label-smoothing 0.2 \
  --translate 2 \
  --tta-level 0 \
  --seed 42 \
  --no-verbose
