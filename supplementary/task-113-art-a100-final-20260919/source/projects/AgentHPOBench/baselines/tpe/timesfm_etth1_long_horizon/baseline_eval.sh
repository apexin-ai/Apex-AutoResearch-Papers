#!/usr/bin/env bash
set -euo pipefail

ROOT="${AUTOREP_ROOT:-.}"
FORMAL_DIR="$ROOT/baselines/tpe/timesfm_etth1_long_horizon"
RESULTS_DIR="${RESULTS_DIR:-$ROOT/results/formal_baselines/timesfm_etth1_long_horizon/official_context512}"
DATA_PATH="${DATA_PATH:-$ROOT/data/formal/timesfm_long_horizon/ETT-small/ETTh1.csv}"
MODEL_PATH="${MODEL_PATH:-$ROOT/models/timesfm/timesfm-1.0-200m-pytorch/torch_model.ckpt}"
CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export CUDA_VISIBLE_DEVICES
export PYTHONPATH="$ROOT/repositories/timesfm/v1/src:${PYTHONPATH:-}"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec

python "$FORMAL_DIR/eval_timesfm_etth1.py" \
  --data-path "$DATA_PATH" \
  --model-path "$MODEL_PATH" \
  --results-dir "$RESULTS_DIR" \
  --context-len "${CONTEXT_LEN:-512}" \
  --pred-len 96 \
  --batch-size "${BATCH_SIZE:-64}" \
  --per-core-batch-size "${PER_CORE_BATCH_SIZE:-32}" \
  --normalize "${NORMALIZE:-true}" \
  --window-size "${WINDOW_SIZE:-0}" \
  --backend gpu \
  --max-windows "${MAX_WINDOWS:-0}"
