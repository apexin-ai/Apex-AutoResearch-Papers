#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/spectral_optim_vision_geometry

echo "=== ConvNeXt-T AdamW lr sweep: 3-point x 5ep ==="
for LR in 0.0001 0.0003 0.001; do
    echo "--- Starting lr=$LR ---"
    python3 scripts/p1_new_arch/convnext_t_adamw_train.py --lr $LR --gpu 1 --seed 42 --epochs 5 2>&1 | tee /root/autodl-tmp/tmp/convnext_adamw_lr${LR}.log
    echo "--- lr=$LR done ---"
    tail -5 /root/autodl-tmp/tmp/convnext_adamw_lr${LR}.log
    echo ""
done
echo "=== Sweep complete ==="
