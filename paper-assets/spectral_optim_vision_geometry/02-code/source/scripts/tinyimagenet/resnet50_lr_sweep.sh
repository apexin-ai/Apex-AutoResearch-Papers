#!/bin/bash
# Tiny-ImageNet ResNet-50 lr sweep: 3 Muon lrs + 3 AdamW lrs, each 5ep
set -e
cd /root/spectral_optim_vision_geometry
LOGDIR=/root/runs/spectral_optim_vision_geometry
mkdir -p $LOGDIR

echo "=== ResNet-50 Muon lr sweep ==="
for LR in 0.01 0.02 0.04; do
    echo ">>> Muon lr=$LR"
    python3 tiny_imagenet_train.py --model resnet50 --optimizer muon --gpu 0 --muon-lr $LR --seed 42 --epochs 5 2>&1 | tee ${LOGDIR}/tinyimagenet_resnet50_muon_lr${LR}_5ep.log
    echo "<<< Muon lr=$LR done"
done

echo "=== ResNet-50 AdamW lr sweep ==="
for LR in 0.0005 0.001 0.002; do
    echo ">>> AdamW lr=$LR"
    python3 tiny_imagenet_train.py --model resnet50 --optimizer adamw --gpu 0 --lr $LR --seed 42 --epochs 5 2>&1 | tee ${LOGDIR}/tinyimagenet_resnet50_adamw_lr${LR}_5ep.log
    echo "<<< AdamW lr=$LR done"
done

echo "=== ALL SWEEPS COMPLETE ==="
