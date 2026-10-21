#!/bin/bash
# B3 Multi-seed: ConvNeXt-T AdamW lr=1e-3, seeds 1 & 2, 20 epochs each (serial)
# Pairs with seed=42 (60.25%) to compute mean±std, compare against Muon multi-seed
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_optim_vision_geometry

LOG_DIR=/root/runs/spectral_optim_vision_geometry
mkdir -p "$LOG_DIR"

echo "=== ConvNeXt-T AdamW lr=1e-3 seed=1 starting at $(date) ==="
python3 scripts/p1_new_arch/convnext_t_adamw_train.py \
    --lr 0.001 \
    --gpu 0 \
    --seed 1 \
    --epochs 20 \
    --batch-size 128 \
    2>&1 | tee "$LOG_DIR/convnext_adamw_lr1e-3_s1.log"
echo "=== ConvNeXt-T AdamW lr=1e-3 seed=1 finished at $(date) ==="

echo "=== ConvNeXt-T AdamW lr=1e-3 seed=2 starting at $(date) ==="
python3 scripts/p1_new_arch/convnext_t_adamw_train.py \
    --lr 0.001 \
    --gpu 0 \
    --seed 2 \
    --epochs 20 \
    --batch-size 128 \
    2>&1 | tee "$LOG_DIR/convnext_adamw_lr1e-3_s2.log"
echo "=== ConvNeXt-T AdamW lr=1e-3 seed=2 finished at $(date) ==="

echo "ALL_SEEDS_DONE"
