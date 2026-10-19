#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_ROOT:-.}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec

export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
export ABLKIT_CUDA_VISIBLE_DEVICES="${ABLKIT_CUDA_VISIBLE_DEVICES:-0}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-0}"
export PYTHONPATH="$BASE/baselines/tpe/ablkit_mnist_add_reasoning_accuracy/stubs:$BASE/repositories/ABLkit:$BASE/repositories/ABLkit/examples/hwf:$BASE:$BASE/.python_deps:${PYTHONPATH:-}"

python "$BASE/baselines/tpe/ablkit_hwf_reasoning_accuracy/run_formal_ablkit_hwf_agent.py"
