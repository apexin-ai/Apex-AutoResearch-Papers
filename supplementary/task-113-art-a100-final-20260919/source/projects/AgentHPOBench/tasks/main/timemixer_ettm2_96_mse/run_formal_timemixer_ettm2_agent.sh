#!/usr/bin/env bash
set -euo pipefail

BASE="."
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export PYTHONPATH="$BASE/repositories/TimeMixer:$BASE/.python_deps:${PYTHONPATH:-}"
export TIMEMIXER_CUDA_VISIBLE_DEVICES="${TIMEMIXER_CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
python "$BASE/tasks/main/timemixer_ettm2_96_mse/run_formal_timemixer_ettm2_agent.py"
