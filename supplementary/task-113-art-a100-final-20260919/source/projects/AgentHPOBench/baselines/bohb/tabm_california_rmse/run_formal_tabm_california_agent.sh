#!/usr/bin/env bash
set -euo pipefail

BASE="."
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export PYTHONPATH="$BASE:$BASE/repositories/tabm:$BASE/.python_deps:${PYTHONPATH:-}"
export TABM_CUDA_VISIBLE_DEVICES="${TABM_CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
python "$BASE/baselines/bohb/tabm_california_rmse/run_formal_tabm_california_agent.py"
