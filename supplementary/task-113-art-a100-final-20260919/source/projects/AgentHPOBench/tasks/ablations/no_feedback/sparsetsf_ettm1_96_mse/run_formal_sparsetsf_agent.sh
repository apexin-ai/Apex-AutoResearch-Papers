#!/usr/bin/env bash
set -euo pipefail

BASE=.
export PYTHONPATH="$BASE/repositories/SparseTSF:$BASE:$BASE/.python_deps:${PYTHONPATH:-}"
export SPARSETSF_CUDA_VISIBLE_DEVICES="${SPARSETSF_CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec

python "$BASE/tasks/ablations/no_feedback/sparsetsf_ettm1_96_mse/run_formal_sparsetsf_agent.py"
