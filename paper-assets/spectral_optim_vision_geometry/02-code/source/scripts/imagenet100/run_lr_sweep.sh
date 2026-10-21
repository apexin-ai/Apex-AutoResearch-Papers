#!/bin/bash
# ImageNet-100 lr sweep launcher (B6 prep)
# Single-run wrapper: launches one (arch, optimizer, lr) combo.
# Reviewer-warning prerequisite — determines optimal lr for ImageNet-100 before B6.
#
# Usage:
#   bash scripts/imagenet100/run_lr_sweep.sh --arch resnet50 --optimizer muon --lr 0.02 --gpu 0
#   bash scripts/imagenet100/run_lr_sweep.sh --arch deit_small --optimizer adamw --lr 1e-4 --gpu 0
#   bash scripts/imagenet100/run_lr_sweep.sh --list-grid           # print all 18 combos
#
# Sweep grid (6 arch×optim combos × 3 lr = 18 runs):
#   resnet50  + muon  : 0.005, 0.02,  0.05
#   resnet50  + adamw : 3e-4,  1e-3,  3e-3
#   resnet50  + sgd   : 0.03,  0.1,   0.3
#   deit_small+ muon  : 0.005, 0.02,  0.05
#   deit_small+ adamw : 3e-5,  1e-4,  3e-4
#   deit_small+ sgd   : 0.01,  0.05,  0.1
#
# NOTE: convnext_tiny is NOT supported — imagenet100_train.py MODEL_REGISTRY
# only contains resnet50 / deit_small. Adding convnext_tiny requires patching
# imagenet100_train.py first.

set -euo pipefail

# ---- Defaults ----
GPU=0
ARCH=""
OPTIMIZER=""
LR=""
EPOCHS=5
SEED=42
BATCH_SIZE=128
NUM_WORKERS=4
LIST_GRID=""

# ---- Parse ----
while [[ $# -gt 0 ]]; do
    case $1 in
        --gpu)         GPU="$2"; shift 2 ;;
        --arch)        ARCH="$2"; shift 2 ;;
        --optimizer)   OPTIMIZER="$2"; shift 2 ;;
        --lr)          LR="$2"; shift 2 ;;
        --epochs)      EPOCHS="$2"; shift 2 ;;
        --seed)        SEED="$2"; shift 2 ;;
        --batch-size)  BATCH_SIZE="$2"; shift 2 ;;
        --num-workers) NUM_WORKERS="$2"; shift 2 ;;
        --list-grid)   LIST_GRID="1"; shift ;;
        -h|--help)
            sed -n '2,20p' "$0"
            exit 0 ;;
        *) echo "Unknown arg: $1" >&2; exit 1 ;;
    esac
done

if [[ -n "$LIST_GRID" ]]; then
    cat <<EOF
# ImageNet-100 lr sweep grid (18 runs)
# Format: arch optimizer lr
resnet50   muon   0.005
resnet50   muon   0.02
resnet50   muon   0.05
resnet50   adamw  3e-4
resnet50   adamw  1e-3
resnet50   adamw  3e-3
resnet50   sgd    0.03
resnet50   sgd    0.1
resnet50   sgd    0.3
deit_small muon   0.005
deit_small muon   0.02
deit_small muon   0.05
deit_small adamw  3e-5
deit_small adamw  1e-4
deit_small adamw  3e-4
deit_small sgd    0.01
deit_small sgd    0.05
deit_small sgd    0.1
EOF
    exit 0
fi

# ---- Validate ----
if [[ -z "$ARCH" || -z "$OPTIMIZER" || -z "$LR" ]]; then
    echo "ERROR: --arch, --optimizer, --lr are required (or use --list-grid)" >&2
    exit 1
fi
case "$ARCH" in
    resnet50|deit_small|convnext_tiny) ;;
    convnext_tiny) ;;
    *) echo "ERROR: unknown --arch '$ARCH' (resnet50|deit_small)" >&2; exit 1 ;;
esac
case "$OPTIMIZER" in
    muon|adamw|sgd|lion) ;;
    *) echo "ERROR: unknown --optimizer '$OPTIMIZER' (muon|adamw|sgd|lion)" >&2; exit 1 ;;
esac

# ---- Paths ----
PROJECT_DIR="/root/spectral_optim_vision_geometry"
DATA_DIR="/root/autodl-tmp/imagenet100_deduped"
LOG_DIR="$HOME/runs/spectral_optim_vision_geometry/lr_sweep_imagenet100"
# lr sweeps don't need checkpoints; route to scratch and skip via dataset-only run
CKPT_DIR="/root/autodl-tmp/checkpoints/spectral_optim/lr_sweep_imagenet100"

mkdir -p "$LOG_DIR" "$CKPT_DIR"

# Sanitize lr for filename (1e-4 -> 1e-4 is fine, but 3e-4 too)
LR_TAG=$(echo "$LR" | tr '.' 'p')
LOG_FILE="${LOG_DIR}/lr_${ARCH}_${OPTIMIZER}_lr${LR_TAG}_ep${EPOCHS}_s${SEED}.log"

echo "=== ImageNet-100 lr sweep ==="
echo "arch=${ARCH}, optimizer=${OPTIMIZER}, lr=${LR}, epochs=${EPOCHS}, seed=${SEED}, gpu=${GPU}"
echo "log: ${LOG_FILE}"
echo "============================="

cd "$PROJECT_DIR"

# Activate conda env (aml-train image uses conda, not venv)
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# muon uses --muon-lr; adamw/sgd use --lr
if [[ "$OPTIMIZER" == "muon" ]]; then
    LR_FLAG=(--muon-lr "$LR")
else
    LR_FLAG=(--lr "$LR")
fi

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
    "${LR_FLAG[@]}" \
    2>&1 | tee "$LOG_FILE"
