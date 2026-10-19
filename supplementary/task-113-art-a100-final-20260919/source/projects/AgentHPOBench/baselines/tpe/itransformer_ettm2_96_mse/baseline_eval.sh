#!/usr/bin/env bash
set -euo pipefail

BASE="."
OUT="$BASE/results/formal_baselines/itransformer_ettm2_96_mse/baseline_small"
mkdir -p "$OUT"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export PYTHONPATH="$BASE/repositories/iTransformer:$BASE/.python_deps:${PYTHONPATH:-}"
export ITRANSFORMER_CUDA_VISIBLE_DEVICES="${ITRANSFORMER_CUDA_VISIBLE_DEVICES:-1}"
python "$BASE/baselines/tpe/itransformer_ettm2_96_mse/eval_itransformer_ettm2.py" \
  --results-dir "$OUT" \
  --run-name baseline \
  --d-model 64 \
  --d-ff 64 \
  --n-heads 4 \
  --e-layers 1 \
  --dropout 0.1 \
  --learning-rate 0.001 \
  --batch-size 512 \
  --epochs "${ITRANSFORMER_EPOCHS:-3}" \
  --patience 2
