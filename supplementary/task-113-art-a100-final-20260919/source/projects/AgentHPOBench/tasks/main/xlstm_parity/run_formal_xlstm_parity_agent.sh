#!/usr/bin/env bash
set -euo pipefail

BASE=.
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1}
export XLSTM_CUDA_VISIBLE_DEVICES=${XLSTM_CUDA_VISIBLE_DEVICES:-1}
export QWEN_CUDA_VISIBLE_DEVICES=${QWEN_CUDA_VISIBLE_DEVICES:-1}
export PYTHONPATH="$BASE/repositories/xlstm:${PYTHONPATH:-}"
python "$BASE/tasks/main/xlstm_parity/run_formal_xlstm_parity_agent.py"
