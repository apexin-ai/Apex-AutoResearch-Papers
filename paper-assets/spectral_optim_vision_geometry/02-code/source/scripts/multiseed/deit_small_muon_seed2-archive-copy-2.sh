#!/bin/bash
# Multi-seed Round 2: DeiT-S Muon, seed=2, 20 epochs
# Params copied from Round 1 seed=0: muon_lr=0.003, adam_lr=3e-4, wd=0.05, batch_size=128

set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_optim_vision_geometry

LOG_DIR=/root/runs/spectral_optim_vision_geometry
mkdir -p "$LOG_DIR"

echo "=== DeiT-S Muon seed=2 starting at $(date) ==="

python3 deit_muon_full_train.py \
    --gpu 0 \
    --seed 2 \
    --epochs 20 \
    --batch-size 128 \
    --muon-lr 0.003 \
    --output-dir /root/autodl-tmp/checkpoints/spectral_optim/ \
    2>&1 | tee "$LOG_DIR/multiseed_deit_small_muon_seed2.log"

echo "=== DeiT-S Muon seed=2 finished at $(date) ==="
