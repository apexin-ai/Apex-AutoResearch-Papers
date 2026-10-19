#!/usr/bin/env bash
set -euo pipefail

ROOT="${AUTOREP_ROOT:-.}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
export TIMESFM_CUDA_VISIBLE_DEVICES="${TIMESFM_CUDA_VISIBLE_DEVICES:-1}"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec

python "$ROOT/tasks/ablations/no_feedback/timesfm_etth1_long_horizon/run_formal_timesfm_etth1_agent.py"
