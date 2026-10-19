#!/usr/bin/env bash
set -euo pipefail

BASE="."
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export PYTHONPATH="$BASE/repositories/TimeXer:$BASE/.python_deps:${PYTHONPATH:-}"
export TIMEXER_CUDA_VISIBLE_DEVICES="${TIMEXER_CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
python "$BASE/baselines/tpe/timexer_pjm_168_24_mse/run_formal_timexer_pjm_agent.py"
