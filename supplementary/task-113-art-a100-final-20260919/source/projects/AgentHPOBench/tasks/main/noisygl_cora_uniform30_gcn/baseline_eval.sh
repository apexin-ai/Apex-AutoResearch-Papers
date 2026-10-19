#!/usr/bin/env bash
set -euo pipefail

BASE=.
cd "$BASE"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1}
export PYTHONPATH="$BASE:$BASE/.python_deps:$BASE/repositories/NoisyGL:${PYTHONPATH:-}"
python "$BASE/tasks/main/noisygl_cora_uniform30_gcn/eval_noisygl_cora_gcn.py" \
  --results-dir "$BASE/results/formal_baselines/noisygl_cora_uniform30_gcn/default_gcn_80ep" \
  --epochs "${NOISYGL_EPOCHS:-80}" \
  --hidden-dim 64 \
  --dropout 0.5 \
  --lr 0.01 \
  --weight-decay 0.0005 \
  --noise-rate 0.3 \
  --seed 3000 \
  --noise-seed 3000
