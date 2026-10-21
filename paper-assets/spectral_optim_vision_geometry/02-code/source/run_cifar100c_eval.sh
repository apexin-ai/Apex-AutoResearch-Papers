#!/bin/bash
# Batch CIFAR-100-C evaluation for all checkpoints
set -e

CKPT_DIR="/root/autodl-tmp/checkpoints/spectral_optim"
DATA_DIR="/root/autodl-tmp/data/CIFAR-100-C"
OUT_DIR="/root/autodl-tmp/checkpoints/spectral_optim/cifar100c_results"
GPU="${1:-0}"

mkdir -p "$OUT_DIR"

declare -A CHECKPOINTS
# ResNet-50 (BN)
CHECKPOINTS["resnet50|muon"]="resnet50_muon_s42_ep20.pt|resnet50"
CHECKPOINTS["resnet50|adamw"]="resnet50_adamw_s42_lr1e-3_best.pt|resnet50"
# ResNet-50-LN (GroupNorm)
CHECKPOINTS["resnet50_ln|muon"]="resnet50_ln_muon_s42_best.pt|resnet50_ln"
CHECKPOINTS["resnet50_ln|adamw"]="resnet50_ln_adamw_s42_lr1e-3_best.pt|resnet50_ln"
# DeiT-Small
CHECKPOINTS["deit_small|muon"]="deit_small_muon_s42_best.pt|deit_small"
CHECKPOINTS["deit_small|adamw"]="deit_small_adamw_s42_lr3e-4_best.pt|deit_small"
# ConvNeXt-Tiny
CHECKPOINTS["convnext_tiny|muon"]="convnext_tiny_muon_s42_best.pt|convnext_tiny"
CHECKPOINTS["convnext_tiny|adamw"]="convnext_tiny_adamw_s42_lr1e-3_best.pt|convnext_tiny"
# SOAP
CHECKPOINTS["resnet50|soap"]="resnet50_soap_s42_lr1e-2_best.pt|resnet50"
CHECKPOINTS["deit_small|soap"]="deit_small_soap_s42_lr1e-3_best.pt|deit_small"
CHECKPOINTS["convnext_tiny|soap"]="convnext_tiny_soap_s42_lr1e-2_best.pt|convnext_tiny"
# Shampoo
CHECKPOINTS["resnet50|shampoo"]="resnet50_shampoo_s42_lr5e-2_best.pt|resnet50"
CHECKPOINTS["deit_small|shampoo"]="deit_small_shampoo_s42_lr5e-3_best.pt|deit_small"
CHECKPOINTS["convnext_tiny|shampoo"]="convnext_tiny_shampoo_s42_lr7e-3_best.pt|convnext_tiny"

for key in "${!CHECKPOINTS[@]}"; do
    IFS='|' read -r arch optimizer <<< "$key"
    IFS='|' read -r ckpt_file model_name <<< "${CHECKPOINTS[$key]}"
    ckpt_path="$CKPT_DIR/$ckpt_file"

    if [ ! -f "$ckpt_path" ]; then
        echo "SKIP $key: $ckpt_path not found"
        continue
    fi

    out_csv="$OUT_DIR/${arch}_${optimizer}.csv"
    if [ -f "$out_csv" ]; then
        echo "SKIP $key: $out_csv already exists"
        continue
    fi

    echo "=== Evaluating $key ==="
    CUDA_VISIBLE_DEVICES=$GPU python3 -u eval_cifar100c.py \
        --checkpoint "$ckpt_path" \
        --model "$model_name" \
        --optimizer "$optimizer" \
        --data-dir "$DATA_DIR" \
        --output-csv "$out_csv" \
        --batch-size 16
    echo ""
done

echo "All evaluations complete. Results in $OUT_DIR/"
