#!/bin/bash
# Run probe training for XNLI baseline data.
#
# Usage:
#   bash scripts/run_probes.sh <MODEL_KEY>
#
# Example:
#   bash scripts/run_probes.sh qwen3

set -e

MODEL_KEY=${1:?"Usage: $0 <MODEL_KEY>"}
XNLI_DIR="data/xnli/${MODEL_KEY}"

mkdir -p logs

echo "=== XNLI probe: ${MODEL_KEY} ==="
CUDA_VISIBLE_DEVICES="" python -u src/train_probe.py \
    --activation_dir "$XNLI_DIR/" \
    --output_dir "$XNLI_DIR/" \
    --seeds 42,123,456,789,1024 \
    --skip_permutation

echo "=== Done ==="
