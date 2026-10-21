#!/bin/bash
set -e
cd /root/spectral_optim_vision_geometry

echo "========== Muon lr=0.15 =========="
python3 imagenet100_train.py \
    --arch convnext_tiny \
    --optimizer muon \
    --muon-lr 0.15 \
    --epochs 5 \
    --seed 42 \
    --batch-size 128 \
    --data-dir /root/autodl-tmp/imagenet100_deduped \
    --gpu 0
echo "========== Done =========="
