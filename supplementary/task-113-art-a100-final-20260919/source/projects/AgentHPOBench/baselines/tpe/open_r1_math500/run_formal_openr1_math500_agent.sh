#!/usr/bin/env bash
set -euo pipefail

cd .
export PYTHONPATH=".:./.python_deps:${PYTHONPATH:-}"
export TOKENIZERS_PARALLELISM=false
export OPENR1_CUDA_VISIBLE_DEVICES="${OPENR1_CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-open-r1
python baselines/tpe/open_r1_math500/run_formal_openr1_math500_agent.py
