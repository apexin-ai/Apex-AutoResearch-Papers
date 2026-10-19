#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_BASE:-.}"
FORMAL="$BASE/baselines/tpe/modernbert_mnli_accuracy"
OUT="$BASE/results/formal_baselines/modernbert_mnli_accuracy/budget_baseline"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec

export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export HF_DATASETS_OFFLINE="${HF_DATASETS_OFFLINE:-1}"
export TRANSFORMERS_OFFLINE="${TRANSFORMERS_OFFLINE:-1}"
export TOKENIZERS_PARALLELISM=false

python "$FORMAL/eval_modernbert_mnli.py" \
  --model-dir "$BASE/models/modernbert/ModernBERT-base" \
  --data-dir "$BASE/data/paper_exact/modernbert_mnli/glue_mnli" \
  --cache-dir "$BASE/cache" \
  --results-dir "$OUT" \
  --eval-split "${MODERNBERT_MNLI_EVAL_SPLIT:-validation_matched}" \
  --learning-rate 2e-5 \
  --weight-decay 0.01 \
  --warmup-ratio 0.1 \
  --batch-size 8 \
  --eval-batch-size 32 \
  --max-length 64 \
  --max-steps "${MODERNBERT_MAX_STEPS:-120}" \
  --train-samples "${MODERNBERT_TRAIN_SAMPLES:-4096}" \
  --eval-samples "${MODERNBERT_EVAL_SAMPLES:-0}" \
  --bf16
