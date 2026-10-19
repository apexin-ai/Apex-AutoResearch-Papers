#!/usr/bin/env bash
set -euo pipefail

BASE=.
cd "$BASE"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1}
export NOISYGL_CUDA_VISIBLE_DEVICES=${NOISYGL_CUDA_VISIBLE_DEVICES:-1}
export QWEN_CUDA_VISIBLE_DEVICES=${QWEN_CUDA_VISIBLE_DEVICES:-1}
export PYTHONPATH="$BASE:$BASE/.python_deps:$BASE/repositories/NoisyGL:${PYTHONPATH:-}"
export TOKENIZERS_PARALLELISM=false
python "$BASE/baselines/bohb/noisygl_cora_uniform30_gcn/run_formal_noisygl_cora_gcn_agent.py"
