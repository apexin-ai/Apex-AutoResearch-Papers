#!/bin/bash
# B6 ImageNet-100 experiment launcher
# Runs a single training job: 1 arch × 1 optimizer × 1 seed on a specified GPU.
# Logs to ~/runs/spectral_optim_vision_geometry/b6_imagenet100/
#
# Usage:
#   bash scripts/run_b6_imagenet100.sh --gpu 0 --arch resnet50 --optimizer adamw --seed 42
#   bash scripts/run_b6_imagenet100.sh --gpu 1 --arch deit_small --optimizer muon --seed 42
#
# Hyperparameters (from CIFAR-100 / Tiny-ImageNet validated configs):
#   AdamW: lr=3e-4, weight_decay=0.05
#   SGD:   lr=0.1,  momentum=0.9, weight_decay=1e-4
#   Muon:  lr=0.02, momentum=0.95 (+ AdamW lr=3e-4 for head/embed/norm)

set -euo pipefail

# Defaults
GPU=0
ARCH="resnet50"
OPTIMIZER="adamw"
SEED=42
EPOCHS=20
BATCH_SIZE=128
NUM_WORKERS=4
DRY_RUN=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --gpu)       GPU="$2"; shift 2 ;;
        --arch)      ARCH="$2"; shift 2 ;;
        --optimizer) OPTIMIZER="$2"; shift 2 ;;
        --seed)      SEED="$2"; shift 2 ;;
        --epochs)    EPOCHS="$2"; shift 2 ;;
        --batch-size) BATCH_SIZE="$2"; shift 2 ;;
        --num-workers) NUM_WORKERS="$2"; shift 2 ;;
        --dry-run)   DRY_RUN="--dry-run"; shift ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

PROJECT_DIR="/root/spectral_optim_vision_geometry"
DATA_DIR="/root/autodl-tmp/imagenet100"
LOG_DIR="$HOME/runs/spectral_optim_vision_geometry/b6_imagenet100"
CKPT_DIR="/root/autodl-tmp/checkpoints/spectral_optim/b6_imagenet100"

mkdir -p "$LOG_DIR" "$CKPT_DIR"

LOG_FILE="${LOG_DIR}/b6_${ARCH}_${OPTIMIZER}_s${SEED}.log"

echo "=== B6 ImageNet-100 ==="
echo "arch=${ARCH}, optimizer=${OPTIMIZER}, seed=${SEED}, gpu=${GPU}, epochs=${EPOCHS}"
echo "log: ${LOG_FILE}"
echo "======================="

cd "$PROJECT_DIR"

# Activate conda env (aml-train image uses conda, not venv)
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CUDA_VISIBLE_DEVICES="$GPU" python3 imagenet100_train.py \
    --arch "$ARCH" \
    --optimizer "$OPTIMIZER" \
    --gpu 0 \
    --seed "$SEED" \
    --epochs "$EPOCHS" \
    --batch-size "$BATCH_SIZE" \
    --num-workers "$NUM_WORKERS" \
    --data-dir "$DATA_DIR" \
    --output-dir "$CKPT_DIR" \
    $DRY_RUN \
    2>&1 | tee "$LOG_FILE"
