#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_ROOT:-.}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate "${AUTOREP_TUNEDGNN_CONDA_ENV:-autorep-vlm2vec}"

export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
export TUNEDGNN_CUDA_VISIBLE_DEVICES="${TUNEDGNN_CUDA_VISIBLE_DEVICES:-0}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-0}"
export PYTHONPATH="$BASE:$BASE/.python_deps:$BASE/repositories/tunedGNN:${PYTHONPATH:-}"
export TOKENIZERS_PARALLELISM=false

python "$BASE/baselines/tpe/tunedgnn_cora_gcn_accuracy/run_formal_tunedgnn_cora_agent.py"
