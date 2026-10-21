#!/bin/bash
# D055: ResNet-50 5-seed experiment (SGD vs AdamW on CIFAR-100, 20ep)
# Usage:
#   bash scripts/run_d055_resnet_5seed.sh --gpu 0 --optimizer sgd
#   bash scripts/run_d055_resnet_5seed.sh --gpu 1 --optimizer adamw
# Run both in parallel:
#   bash scripts/run_d055_resnet_5seed.sh --gpu 0 --optimizer sgd &
#   bash scripts/run_d055_resnet_5seed.sh --gpu 1 --optimizer adamw &
#   wait

set -euo pipefail

GPU=""
OPTIMIZER=""
SEEDS="0 1 2 3 4"
EPOCHS=20
BATCH_SIZE=128
LOG_DIR="$HOME/runs/spectral_optim_vision_geometry/d055_resnet_5seed/logs"
CKPT_DIR="$HOME/runs/spectral_optim_vision_geometry/d055_resnet_5seed/checkpoints"
PROJECT_DIR="/root/spectral_optim_vision_geometry"

usage() {
    echo "Usage: $0 --gpu <GPU_ID> --optimizer <sgd|adamw>"
    echo ""
    echo "Options:"
    echo "  --gpu         GPU device ID (e.g. 0 or 1)"
    echo "  --optimizer   sgd or adamw"
    echo "  --seeds       Space-separated seed list (default: '0 1 2 3 4')"
    echo "  --dry-run     Print commands without executing"
    echo "  --help        Show this help"
    exit 0
}

DRY_RUN=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        --gpu) GPU="$2"; shift 2 ;;
        --optimizer) OPTIMIZER="$2"; shift 2 ;;
        --seeds) SEEDS="$2"; shift 2 ;;
        --dry-run) DRY_RUN=1; shift ;;
        --help|-h) usage ;;
        *) echo "Unknown option: $1"; usage ;;
    esac
done

if [[ -z "$GPU" || -z "$OPTIMIZER" ]]; then
    echo "ERROR: --gpu and --optimizer are required"
    usage
fi

if [[ "$OPTIMIZER" != "sgd" && "$OPTIMIZER" != "adamw" ]]; then
    echo "ERROR: optimizer must be sgd or adamw, got: $OPTIMIZER"
    exit 1
fi

# Hyperparameters matching seed=42 baselines
if [[ "$OPTIMIZER" == "sgd" ]]; then
    LR=0.1
    WD=1e-4
elif [[ "$OPTIMIZER" == "adamw" ]]; then
    LR=1e-3
    WD=0.05
fi

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd "$PROJECT_DIR"
mkdir -p "$LOG_DIR" "$CKPT_DIR"

echo "========================================"
echo "D055 ResNet-50 5-seed: $OPTIMIZER"
echo "GPU=$GPU, LR=$LR, WD=$WD, EPOCHS=$EPOCHS"
echo "Seeds: $SEEDS"
echo "Log dir: $LOG_DIR"
echo "Start: $(date)"
echo "========================================"

for SEED in $SEEDS; do
    LOG_FILE="$LOG_DIR/resnet50_${OPTIMIZER}_s${SEED}.log"
    echo ""
    echo "--- seed=$SEED starting at $(date) ---"

    CMD="python3 baseline_train.py \
        --model resnet50 \
        --optimizer $OPTIMIZER \
        --lr $LR \
        --weight-decay $WD \
        --gpu $GPU \
        --seed $SEED \
        --epochs $EPOCHS \
        --batch-size $BATCH_SIZE \
        --output-dir $CKPT_DIR"

    if [[ $DRY_RUN -eq 1 ]]; then
        echo "[DRY-RUN] $CMD 2>&1 | tee $LOG_FILE"
    else
        $CMD 2>&1 | tee "$LOG_FILE"
        echo "--- seed=$SEED finished at $(date), exit=$? ---"
    fi
done

echo ""
echo "========================================"
echo "D055 ALL SEEDS DONE: $OPTIMIZER on GPU $GPU"
echo "End: $(date)"
echo "========================================"
