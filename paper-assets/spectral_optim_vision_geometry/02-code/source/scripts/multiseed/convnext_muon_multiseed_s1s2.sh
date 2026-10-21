#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_optim_vision_geometry

LOG_DIR=/root/runs/spectral_optim_vision_geometry
mkdir -p "$LOG_DIR"

echo "=== ConvNeXt-T Muon seed=1 starting at $(date) ==="
python3 scripts/p1_new_arch/convnext_t_muon_train.py \
    --gpu 0 \
    --seed 1 \
    --epochs 20 \
    --batch-size 128 \
    --muon-lr 0.02 \
    --output-dir /root/autodl-tmp/checkpoints/spectral_optim/ \
    2>&1 | tee "$LOG_DIR/convnext_muon_lr0.02_s1.log"

echo "=== ConvNeXt-T Muon seed=2 starting at $(date) ==="
python3 scripts/p1_new_arch/convnext_t_muon_train.py \
    --gpu 0 \
    --seed 2 \
    --epochs 20 \
    --batch-size 128 \
    --muon-lr 0.02 \
    --output-dir /root/autodl-tmp/checkpoints/spectral_optim/ \
    2>&1 | tee "$LOG_DIR/convnext_muon_lr0.02_s2.log"

echo "=== All seeds done at $(date) ==="
