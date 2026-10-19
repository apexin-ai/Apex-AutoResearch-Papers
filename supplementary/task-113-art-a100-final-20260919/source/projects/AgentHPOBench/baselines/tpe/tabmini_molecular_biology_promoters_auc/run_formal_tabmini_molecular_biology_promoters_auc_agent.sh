#!/usr/bin/env bash
set -euo pipefail
BASE="."
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export PYTHONPATH="$BASE:$BASE/.python_deps:$BASE/repositories/TabMini:${PYTHONPATH:-}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
python "$BASE/baselines/tpe/tabmini_molecular_biology_promoters_auc/run_formal_tabmini_molecular_biology_promoters_auc_agent.py"
