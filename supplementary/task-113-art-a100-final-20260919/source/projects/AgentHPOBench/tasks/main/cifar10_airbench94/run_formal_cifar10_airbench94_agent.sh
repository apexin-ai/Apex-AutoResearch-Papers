#!/usr/bin/env bash
set -euo pipefail

BASE=.
cd "$BASE"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1}
export AIRBENCH_CUDA_VISIBLE_DEVICES=${AIRBENCH_CUDA_VISIBLE_DEVICES:-1}
export QWEN_CUDA_VISIBLE_DEVICES=${QWEN_CUDA_VISIBLE_DEVICES:-1}
export PYTHONPATH="$BASE:$BASE/.python_deps:$BASE/repositories/cifar10-airbench:${PYTHONPATH:-}"
export TOKENIZERS_PARALLELISM=false
python "$BASE/tasks/main/cifar10_airbench94/run_formal_cifar10_airbench94_agent.py"
