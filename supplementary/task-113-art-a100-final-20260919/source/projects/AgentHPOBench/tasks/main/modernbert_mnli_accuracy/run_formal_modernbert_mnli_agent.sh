#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_ROOT:-.}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec

export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
export MODERNBERT_CUDA_VISIBLE_DEVICES="${MODERNBERT_CUDA_VISIBLE_DEVICES:-0}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-0}"
export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export TOKENIZERS_PARALLELISM=false
export PYTHONPATH="$BASE:$BASE/.python_deps:${PYTHONPATH:-}"

python "$BASE/tasks/main/modernbert_mnli_accuracy/run_formal_modernbert_mnli_agent.py"
