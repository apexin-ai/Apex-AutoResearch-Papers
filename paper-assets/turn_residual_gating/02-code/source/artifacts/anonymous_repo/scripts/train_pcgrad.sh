#!/bin/bash
# Train with PCGrad gradient conflict resolution (Yu et al., NeurIPS 2020)
# Usage: bash scripts/train_pcgrad.sh [seed]
set -e
cd "$(dirname "$0")/.."

SEED=${1:-42}
OUTPUT_DIR="runs/pcgrad_s${SEED}"

python src/train_pcgrad.py \
  --gate-type threadgate \
  --gar-loss-mode mse_target --gar-target 0.5 \
  --lambda-gar 1.0 --lambda-gate-div 1.0 \
  --min-gate-std 0.05 --init-bias 1.5 \
  --gate-lr-multiplier 10 \
  --lr 2e-4 --batch-size 1 --grad-accum 8 \
  --max-seq-len 2048 \
  --seed $SEED --epochs 3 \
  --output-dir $OUTPUT_DIR \
  --data-dir data/ultrachat_8k
