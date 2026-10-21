#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_optim_vision_geometry

echo "=== ConvNeXt-T TinyIN AdamW lr sweep ==="
echo "Start: $(date)"

for LR in 1e-4 3e-4 1e-3; do
    echo "--- lr=$LR ---"
    python3 tiny_imagenet_train.py \
        --model convnext_tiny \
        --optimizer adamw \
        --lr $LR \
        --epochs 5 \
        --seed 42 \
        --batch-size 128 \
        --data-dir /root/autodl-tmp/data/tiny-imagenet-200 \
        --gpu 0
    echo "--- lr=$LR done ---"
done

echo "End: $(date)"
