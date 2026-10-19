#!/usr/bin/env bash
set -euo pipefail

BASE=.
FORMAL=$BASE/tasks/main/hyperboliccv_cifar100_accuracy
OUT=$BASE/results/formal_baselines/hyperboliccv_cifar100_accuracy/baseline_e_resnet18_2ep_200b
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$BASE/repositories/HyperbolicCV/code/classification:$BASE/repositories/HyperbolicCV/code:$BASE/.python_deps:${PYTHONPATH:-}"
python "$FORMAL/eval_hyperboliccv_cifar100.py" \
  --results-dir "$OUT" \
  --dataset CIFAR-100 \
  --model-type E \
  --embedding-dim 512 \
  --lr 0.1 \
  --weight-decay 5e-4 \
  --batch-size 128 \
  --num-epochs "${HYPERCV_NUM_EPOCHS:-2}" \
  --train-batches "${HYPERCV_TRAIN_BATCHES:-200}" \
  --no-use-lr-scheduler \
  --device cuda:0 \
  --seed 1
