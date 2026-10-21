#!/bin/bash
# Round 4: ResNet-50 AdamW, seed=0, 20 epochs
# Params from phase1_resnet50_adamw_baseline_v2: lr=3e-4, wd=0.05, batch_size=128

set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_optim_vision_geometry

LOG_DIR=/root/runs/spectral_optim_vision_geometry
mkdir -p "$LOG_DIR"

echo "=== ResNet-50 AdamW seed=0 starting at $(date) ==="

python3 baseline_train.py \
    --model resnet50 \
    --gpu 0 \
    --seed 0 \
    --epochs 20 \
    --batch-size 128 \
    --output-dir /root/autodl-tmp/checkpoints/spectral_optim/ \
    2>&1 | tee "$LOG_DIR/multiseed_resnet50_adamw_seed0.log"

echo "=== ResNet-50 AdamW seed=0 finished at $(date) ==="
