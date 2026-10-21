#!/bin/bash
set -e
cd /root/spectral_optim_vision_geometry

for LR in 0.003 0.01 0.05; do
    echo "========== SGD lr=$LR =========="
    python3 imagenet100_train.py \
        --arch convnext_tiny \
        --optimizer sgd \
        --lr $LR \
        --epochs 5 \
        --seed 42 \
        --batch-size 128 \
        --data-dir /root/autodl-tmp/imagenet100_deduped \
        --gpu 0
    echo "========== Done lr=$LR =========="
done
