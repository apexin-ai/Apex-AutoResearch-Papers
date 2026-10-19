#!/usr/bin/env bash
set -euo pipefail

BASE="."
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export PYTHONPATH="$BASE/repositories/iTransformer:$BASE/.python_deps:$BASE:${PYTHONPATH:-}"
export ITRANSFORMER_CUDA_VISIBLE_DEVICES="${ITRANSFORMER_CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
python "$BASE/tasks/main/itransformer_ettm2_96_mse/run_formal_itransformer_ettm2_agent.py"
