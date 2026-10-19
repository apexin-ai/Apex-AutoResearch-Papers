#!/usr/bin/env bash
set -euo pipefail
BASE="."
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export PYTHONPATH="$BASE:$BASE/.python_deps:$BASE/repositories/binary-diffusion-tabular:${PYTHONPATH:-}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
python "$BASE/tasks/ablations/no_feedback/binary_diffusion_adult_rf/run_formal_binary_diffusion_adult_rf_agent.py"
