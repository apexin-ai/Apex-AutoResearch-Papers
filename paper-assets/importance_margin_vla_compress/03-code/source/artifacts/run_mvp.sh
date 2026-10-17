#!/bin/bash
# MVP experiment: Baseline + IMM anchor in parallel on 2 GPUs.
# GPU 0 → baseline, GPU 1 → IMM anchor (delta=0.3, lambda=0.5)
set -e

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "Starting MVP experiments at $(date)"
echo "Working directory: $SCRIPT_DIR"

# Baseline on GPU 0
CUDA_VISIBLE_DEVICES=0 python train.py \
    --config configs/baseline.yaml \
    --gpu 0 --seed 42 \
    --wandb_run "baseline_seed42" &
PID_BASELINE=$!

# IMM anchor on GPU 1
CUDA_VISIBLE_DEVICES=1 python train.py \
    --config configs/imm_anchor.yaml \
    --gpu 0 --seed 42 \
    --wandb_run "imm_d03_l05_seed42" &
PID_IMM=$!

echo "Baseline PID: $PID_BASELINE (GPU 0)"
echo "IMM PID: $PID_IMM (GPU 1)"
echo "Monitor with: tail -f checkpoints/*/latest/..."

wait $PID_BASELINE
BASELINE_EXIT=$?

wait $PID_IMM
IMM_EXIT=$?

echo ""
echo "=== MVP Results ==="
echo "Baseline exit code: $BASELINE_EXIT"
echo "IMM exit code: $IMM_EXIT"
echo "Finished at $(date)"

if [ $BASELINE_EXIT -ne 0 ] || [ $IMM_EXIT -ne 0 ]; then
    echo "WARNING: One or more experiments failed"
    exit 1
fi
