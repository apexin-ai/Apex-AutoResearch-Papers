#!/bin/bash
# Multi-seed Round 2: ResNet-50 AdamW, seed=1, 20 epochs
# Params copied from baseline_train.py: lr=3e-4, wd=0.05, batch_size=128

set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_optim_vision_geometry

LOG_DIR=/root/runs/spectral_optim_vision_geometry
mkdir -p "$LOG_DIR"

echo "=== ResNet-50 AdamW seed=1 starting at $(date) ==="

python3 baseline_train.py \
    --model resnet50 \
    --gpu 0 \
    --seed 1 \
    --epochs 20 \
    --batch-size 128 \
    --output-dir /root/autodl-tmp/checkpoints/spectral_optim/ \
    2>&1 | tee "$LOG_DIR/multiseed_resnet50_adamw_seed1.log"

echo "=== ResNet-50 AdamW seed=1 finished at $(date) ==="
