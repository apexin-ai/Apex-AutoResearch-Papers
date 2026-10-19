#!/usr/bin/env bash
set -euo pipefail

BASE="."
OUT="$BASE/results/formal_baselines/tabm_california_rmse/baseline_plain_mlp"
mkdir -p "$OUT"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export PYTHONPATH="$BASE/repositories/tabm:$BASE/.python_deps:${PYTHONPATH:-}"
python "$BASE/baselines/tpe/tabm_california_rmse/eval_tabm_california.py" \
  --results-dir "$OUT" \
  --arch-type plain \
  --k 8 \
  --n-blocks 2 \
  --d-block 128 \
  --dropout 0.1 \
  --lr 0.001 \
  --weight-decay 0.0001 \
  --batch-size 256 \
  --epochs "${TABM_EPOCHS:-50}" \
  --no-use-scheduler \
  --early-stop \
  --patience 12 \
  --device cuda:0 \
  --seed 1
