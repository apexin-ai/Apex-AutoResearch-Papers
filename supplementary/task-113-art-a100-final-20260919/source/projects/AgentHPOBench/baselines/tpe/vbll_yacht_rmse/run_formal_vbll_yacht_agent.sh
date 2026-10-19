#!/usr/bin/env bash
set -euo pipefail

BASE=.
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export VBLL_CUDA_VISIBLE_DEVICES="${VBLL_CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$BASE/repositories/vbll:$BASE/.python_deps:$BASE:${PYTHONPATH:-}"
python "$BASE/baselines/tpe/vbll_yacht_rmse/run_formal_vbll_yacht_agent.py"
