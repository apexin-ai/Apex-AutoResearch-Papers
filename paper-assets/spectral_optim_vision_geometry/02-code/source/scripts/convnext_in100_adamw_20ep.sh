#!/bin/bash
# ConvNeXt-T ImageNet-100, AdamW optimizer, 20 epochs
# Best lr from 5ep sweep: 3e-4 (val_acc=12.42%)
# Sweep candidates: 3e-4→12.42%, 1e-3→11.29%, 3e-3→10.91%
set -e
cd /root/spectral_optim_vision_geometry

python3 imagenet100_train.py \
    --arch convnext_tiny \
    --optimizer adamw \
    --lr 3e-4 \
    --epochs 20 \
    --seed 42 \
    --batch-size 128 \
    --data-dir /root/autodl-tmp/imagenet100_deduped \
    --gpu 0
