#!/usr/bin/env bash
set -euo pipefail

BASE=.
OUT="${1:-$BASE/results/formal_baselines/sparsetsf_ettm1_96_mse/baseline}"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec

CUDA_VISIBLE_DEVICES="${SPARSETSF_CUDA_VISIBLE_DEVICES:-1}" \
PYTHONPATH="$BASE/repositories/SparseTSF:$BASE:$BASE/.python_deps:${PYTHONPATH:-}" \
python "$BASE/baselines/tpe/sparsetsf_ettm1_96_mse/eval_sparsetsf_ettm1.py" \
  --results-dir "$OUT" \
  --seq-len 720 \
  --pred-len 96 \
  --period-len 24 \
  --model-type linear \
  --d-model 128 \
  --lr 0.02 \
  --weight-decay 0.0 \
  --batch-size 256 \
  --epochs "${SPARSETSF_EPOCHS:-1}" \
  --seed "${SPARSETSF_SEED:-2023}" \
  --device cuda:0
