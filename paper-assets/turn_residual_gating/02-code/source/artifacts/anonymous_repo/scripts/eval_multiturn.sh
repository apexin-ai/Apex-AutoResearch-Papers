#!/bin/bash
# Evaluate multi-turn instruction following
# Usage: bash scripts/eval_multiturn.sh <gate_type> <checkpoint_dir>
set -e
cd "$(dirname "$0")/.."

GATE_TYPE=${1:-threadgate}
CKPT_DIR=${2:-runs/threadgate_s42}

python src/eval_multiturn.py \
  --checkpoint-dir ${CKPT_DIR} \
  --gate-type ${GATE_TYPE} \
  --output-dir results/
