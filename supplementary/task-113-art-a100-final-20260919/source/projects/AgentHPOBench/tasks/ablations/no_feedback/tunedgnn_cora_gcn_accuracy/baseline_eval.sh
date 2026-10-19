#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_ROOT:-.}"
OUT_DIR="${OUT_DIR:-$BASE/results/formal_baselines/tunedgnn_cora_gcn_accuracy/budget_baseline}"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate "${AUTOREP_TUNEDGNN_CONDA_ENV:-autorep-vlm2vec}"

export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
export PYTHONPATH="$BASE:$BASE/.python_deps:$BASE/repositories/tunedGNN:${PYTHONPATH:-}"

python "$BASE/tasks/ablations/no_feedback/tunedgnn_cora_gcn_accuracy/eval_tunedgnn_cora.py" \
  --results-dir "$OUT_DIR" \
  --epochs "${TUNEDGNN_EPOCHS:-50}" \
  --seed "${TUNEDGNN_SEED:-123}" \
  --lr "${TUNEDGNN_LR:-0.001}" \
  --hidden-channels "${TUNEDGNN_HIDDEN_CHANNELS:-512}" \
  --local-layers "${TUNEDGNN_LOCAL_LAYERS:-3}" \
  --dropout "${TUNEDGNN_DROPOUT:-0.7}" \
  --weight-decay "${TUNEDGNN_WEIGHT_DECAY:-0.0005}" \
  --device "${TUNEDGNN_DEVICE:-cuda:0}"
