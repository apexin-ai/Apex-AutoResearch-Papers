#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/spectral_optim_vision_geometry

echo "=== ConvNeXt-T Muon lr sweep: 3-point x 5ep ==="
for LR in 0.003 0.01 0.02; do
    echo "--- Starting muon-lr=$LR ---"
    python3 scripts/p1_new_arch/convnext_t_muon_train.py --muon-lr $LR --gpu 0 --seed 42 --epochs 5 2>&1 | tee /root/autodl-tmp/tmp/convnext_muon_lr${LR}.log
    echo "--- muon-lr=$LR done ---"
    tail -5 /root/autodl-tmp/tmp/convnext_muon_lr${LR}.log
    echo ""
done
echo "=== Sweep complete ==="
