#!/bin/bash
# Evaluate attention steering at various beta values
# Usage: bash scripts/eval_attention_steering.sh <checkpoint_dir> [gate_type]
set -e
cd "$(dirname "$0")/.."

CKPT_DIR=${1:?"Usage: $0 <checkpoint_dir> [gate_type]"}
GATE_TYPE=${2:-threadgate}

mkdir -p results/attention_steering/

python src/eval_attention_steering.py \
  --checkpoint $CKPT_DIR \
  --gate-type $GATE_TYPE \
  --mode tf \
  --beta 0 0.5 1.0 2.0 3.0 5.0 10.0 \
  --gar-variant ours \
  --output-dir results/attention_steering/
