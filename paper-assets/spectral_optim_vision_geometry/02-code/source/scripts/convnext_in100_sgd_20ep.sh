#!/bin/bash
# ConvNeXt-T ImageNet-100, SGD optimizer, 20 epochs
# lr=0.01 (sweep best, Director D079 修正)
# 注意: 5ep sweep 结果 0.01→9.27%, 0.05→9.22%, 0.1→4.98%，sweep 最佳为 0.01
# Director D079: 每个 optimizer 用其最优 lr
set -e
cd /root/spectral_optim_vision_geometry

python3 imagenet100_train.py \
    --arch convnext_tiny \
    --optimizer sgd \
    --lr 0.01 \
    --epochs 20 \
    --seed 42 \
    --batch-size 128 \
    --data-dir /root/autodl-tmp/imagenet100_deduped \
    --gpu 0
