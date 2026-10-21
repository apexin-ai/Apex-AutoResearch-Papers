#!/bin/bash
# ConvNeXt-T TinyImageNet-200, AdamW optimizer, 20 epochs
# Best lr from 5ep sweep: 1e-3 (val_acc=31.46%)
# weight_decay=0.05 (hardcoded in training script), cosine schedule
set -e
cd /root/spectral_optim_vision_geometry

OUTPUT_DIR="/root/runs/spectral_optim_vision_geometry"
LOG_FILE="${OUTPUT_DIR}/convnext_tinyin_adamw_20ep.log"
mkdir -p "$OUTPUT_DIR"

python3 tiny_imagenet_train.py \
    --model convnext_tiny \
    --optimizer adamw \
    --lr 1e-3 \
    --epochs 20 \
    --seed 42 \
    --batch-size 128 \
    --data-dir /root/autodl-tmp/data/tiny-imagenet-200 \
    --output-dir "$OUTPUT_DIR" \
    --gpu 0 \
    2>&1 | tee "$LOG_FILE"
