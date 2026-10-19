#!/usr/bin/env bash
set -euo pipefail

BASE=.
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export HYPERCV_CUDA_VISIBLE_DEVICES="${HYPERCV_CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$BASE/repositories/HyperbolicCV/code/classification:$BASE/repositories/HyperbolicCV/code:$BASE/.python_deps:$BASE:${PYTHONPATH:-}"
python "$BASE/baselines/tpe/hyperboliccv_cifar100_accuracy/run_formal_hyperboliccv_cifar100_agent.py"
