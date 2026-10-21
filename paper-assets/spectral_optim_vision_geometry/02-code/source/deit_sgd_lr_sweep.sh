#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/spectral_optim_vision_geometry

echo "=== DeiT SGD lr sweep: 3-point x 5ep ==="

for LR in 0.005 0.01 0.05; do
    echo "--- Starting lr=$LR ---"
    python3 baseline_train.py --model deit_small --optimizer sgd --lr $LR --gpu 0 --seed 42 --epochs 5 --batch-size 128 2>&1 | tee /tmp/deit_sgd_lr${LR}.log
    echo "--- lr=$LR done ---"
    grep "val_acc" /tmp/deit_sgd_lr${LR}.log | tail -5
    echo ""
done

echo "=== Sweep complete ==="
echo "Results summary:"
for LR in 0.005 0.01 0.05; do
    BEST=$(grep "TRAINING_COMPLETE" /tmp/deit_sgd_lr${LR}.log | tail -1)
    echo "  lr=$LR: $BEST"
done
