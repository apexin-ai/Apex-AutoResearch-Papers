#!/bin/bash
# ConvNeXt-T ImageNet-100, Muon optimizer, 20 epochs
# Best lr from 5ep sweep: 0.08 (val_acc=46.32%)
# Sweep candidates: 0.005→35.21%, 0.02→42.54%, 0.08→46.32%
set -e
cd /root/spectral_optim_vision_geometry

python3 imagenet100_train.py \
    --arch convnext_tiny \
    --optimizer muon \
    --muon-lr 0.08 \
    --epochs 20 \
    --seed 42 \
    --batch-size 128 \
    --data-dir /root/autodl-tmp/imagenet100_deduped \
    --gpu 0
