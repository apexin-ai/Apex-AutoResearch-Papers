#!/bin/bash
# Evaluate GAR (Goal Attention Ratio) recovery
# Usage: bash scripts/eval_gar.sh <checkpoint_dir> [gate_type]
set -e
cd "$(dirname "$0")/.."

CKPT_DIR=${1:?"Usage: $0 <checkpoint_dir> [gate_type]"}
GATE_TYPE=${2:-threadgate}

mkdir -p results/

python src/eval_gar.py \
  --checkpoint-dir $CKPT_DIR \
  --gate-type $GATE_TYPE \
  --gar-variant ours \
  --gate-profile \
  --output-dir results/
