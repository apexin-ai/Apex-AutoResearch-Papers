#!/bin/bash
set -euo pipefail

PROJECT_DIR="/root/spectral_optim_vision_geometry"
DATA_DIR="/root/autodl-tmp/imagenet100_deduped"
LOG_DIR="$HOME/runs/spectral_optim_vision_geometry/resnet_in100_50ep"
CKPT_DIR="/root/autodl-tmp/checkpoints/spectral_optim/resnet_in100_50ep"

mkdir -p "$LOG_DIR" "$CKPT_DIR"

cd "$PROJECT_DIR"

CUDA_VISIBLE_DEVICES=1 python3 imagenet100_train.py \
    --arch resnet50 \
    --optimizer adamw \
    --gpu 0 \
    --seed 42 \
    --epochs 50 \
    --batch-size 128 \
    --num-workers 4 \
    --lr 3e-3 \
    --weight-decay 0.05 \
    --data-dir "$DATA_DIR" \
    --output-dir "$CKPT_DIR" \
    2>&1 | tee "${LOG_DIR}/resnet50_adamw_50ep_s42.log"
