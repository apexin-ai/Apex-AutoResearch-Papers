#!/usr/bin/env bash
set -euo pipefail

cd .
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-0}"
export PYTHONPATH="$PWD/repositories/semi-supervised-regression:$PWD/.python_deps:$PWD:${PYTHONPATH:-}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda run -n autorep-vlm2vec python tasks/main/rankup_utkface_mae/run_formal_rankup_utkface_agent.py
