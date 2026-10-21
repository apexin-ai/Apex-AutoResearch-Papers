#!/bin/bash
# B2.8 Multi-seed: ResNet-50 AdamW lr=1e-3, seeds 1 & 2, 20 epochs each (serial)
# Confirms ranking reversal SGD>AdamW (+1.32pp) is non-noise
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_optim_vision_geometry

LOG_DIR=/root/runs/spectral_optim_vision_geometry
mkdir -p "$LOG_DIR"

echo "=== ResNet-50 AdamW lr=1e-3 seed=1 starting at $(date) ==="
python3 baseline_train.py \
    --model resnet50 \
    --optimizer adamw \
    --lr 1e-3 \
    --weight-decay 0.05 \
    --gpu 0 \
    --seed 1 \
    --epochs 20 \
    --batch-size 128 \
    --output-dir /root/autodl-tmp/checkpoints/spectral_optim/ \
    2>&1 | tee "$LOG_DIR/resnet50_adamw_lr1e-3_s1.log"
echo "=== ResNet-50 AdamW lr=1e-3 seed=1 finished at $(date) ==="

echo "=== ResNet-50 AdamW lr=1e-3 seed=2 starting at $(date) ==="
python3 baseline_train.py \
    --model resnet50 \
    --optimizer adamw \
    --lr 1e-3 \
    --weight-decay 0.05 \
    --gpu 0 \
    --seed 2 \
    --epochs 20 \
    --batch-size 128 \
    --output-dir /root/autodl-tmp/checkpoints/spectral_optim/ \
    2>&1 | tee "$LOG_DIR/resnet50_adamw_lr1e-3_s2.log"
echo "=== ResNet-50 AdamW lr=1e-3 seed=2 finished at $(date) ==="

echo "ALL_SEEDS_DONE"
