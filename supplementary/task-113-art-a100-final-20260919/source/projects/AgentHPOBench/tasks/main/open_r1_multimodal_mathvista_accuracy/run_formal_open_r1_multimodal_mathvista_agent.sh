#!/usr/bin/env bash
set -euo pipefail

cd .
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$PWD/.python_deps:$PWD:${PYTHONPATH:-}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda run -n autorep-vlm2vec python tasks/main/open_r1_multimodal_mathvista_accuracy/run_formal_open_r1_multimodal_mathvista_agent.py
