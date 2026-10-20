#!/bin/bash
# Train LoRA-only baseline (no gating)
# Usage: bash scripts/train_lora_only.sh [seed]
set -e
cd "$(dirname "$0")/.."

SEED=${1:-42}
OUTPUT_DIR="runs/lora_only_s${SEED}"

python src/train.py \
  --gate-type none \
  --lambda-gar 0.0 --lambda-gate-div 0.0 \
  --lr 2e-4 --batch-size 1 --grad-accum 8 \
  --max-seq-len 2048 \
  --seed $SEED --epochs 3 \
  --output-dir $OUTPUT_DIR \
  --data-dir data/ultrachat_8k
