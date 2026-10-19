#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_BASE:-.}"
FORMAL="$BASE/tasks/main/ablkit_hwf_reasoning_accuracy"
OUT="$BASE/results/formal_baselines/ablkit_hwf_reasoning_accuracy/default_loops1"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec

export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$BASE/tasks/main/ablkit_mnist_add_reasoning_accuracy/stubs:$BASE/repositories/ABLkit:$BASE/repositories/ABLkit/examples/hwf:$BASE:$BASE/.python_deps:${PYTHONPATH:-}"

python "$FORMAL/eval_ablkit_hwf.py" \
  --results-dir "$OUT" \
  --lr 0.001 \
  --label-smoothing 0.2 \
  --batch-size 128 \
  --segment-size 1000 \
  --loops "${ABLKIT_HWF_LOOPS:-1}" \
  --epochs "${ABLKIT_HWF_EPOCHS:-1}" \
  --max-revision -1 \
  --seed 1 \
  --device cuda:0
