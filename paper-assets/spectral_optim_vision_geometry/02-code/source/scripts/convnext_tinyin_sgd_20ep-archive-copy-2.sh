#!/bin/bash
# ConvNeXt-T TinyImageNet-200, SGD optimizer, 20 epochs
# lr=0.01 (sweep best: 4.60%), momentum=0.9, weight_decay=1e-4
# SGD barely learns on ConvNeXt (~4-7%), this is expected
set -e
cd /root/spectral_optim_vision_geometry

OUTPUT_DIR="/root/runs/spectral_optim_vision_geometry"
mkdir -p "$OUTPUT_DIR"

python3 tiny_imagenet_train.py \
    --model convnext_tiny \
    --optimizer sgd \
    --lr 0.01 \
    --epochs 20 \
    --seed 42 \
    --batch-size 128 \
    --data-dir /root/autodl-tmp/data/tiny-imagenet-200 \
    --output-dir "$OUTPUT_DIR" \
    --gpu 0
