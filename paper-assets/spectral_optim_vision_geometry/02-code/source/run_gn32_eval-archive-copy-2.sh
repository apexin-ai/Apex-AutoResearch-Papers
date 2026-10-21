#!/bin/bash
set -e
cd /root/spectral_optim_vision_geometry
source /root/miniconda3/bin/activate
export CUDA_VISIBLE_DEVICES=1

CKPT_DIR=/root/autodl-tmp/checkpoints/spectral_optim

for ckpt in \
    resnet50_gn32_muon_s42_best.pt \
    resnet50_gn32_adamw_s42_lr3e-4_best.pt \
    resnet50_gn32_sgd_s42_lr1e-1_best.pt \
    resnet50_gn32_soap_s42_lr1e-3_best.pt \
    resnet50_gn32_shampoo_s42_lr7e-3_best.pt; do
    
    CKPT_PATH="${CKPT_DIR}/${ckpt}"
    if [ ! -f "$CKPT_PATH" ]; then
        echo "SKIP: $ckpt not found"
        continue
    fi
    echo "=== Evaluating $ckpt ==="
    python -u eval_cifar100c.py --checkpoint "$CKPT_PATH" --gpu 0
    echo ""
done

echo "=== ALL GN(32) EVAL COMPLETE ==="
