#!/bin/bash
# ConvNeXt-T ImageNet-100 lr sweep: 3 optimizers × 3 lr = 9 runs, 5ep each
# Serial on single GPU (GPU 0 by default)
set -euo pipefail

GPU=${1:-0}
EPOCHS=5
SEED=42
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== ConvNeXt-T ImageNet-100 lr sweep (9 runs × ${EPOCHS}ep) ==="
echo "GPU=${GPU}, seed=${SEED}"
echo ""

declare -a CONFIGS=(
    "muon 0.01"
    "muon 0.02"
    "muon 0.05"
    "adamw 3e-4"
    "adamw 1e-3"
    "adamw 3e-3"
    "sgd 0.005"
    "sgd 0.01"
    "sgd 0.05"
)

RUN=0
TOTAL=${#CONFIGS[@]}

for cfg in "${CONFIGS[@]}"; do
    read -r OPT LR <<< "$cfg"
    RUN=$((RUN + 1))
    echo "--- [${RUN}/${TOTAL}] convnext_tiny + ${OPT} lr=${LR} ---"
    bash "${SCRIPT_DIR}/run_lr_sweep.sh" \
        --arch convnext_tiny \
        --optimizer "$OPT" \
        --lr "$LR" \
        --epochs "$EPOCHS" \
        --seed "$SEED" \
        --gpu "$GPU"
    echo ""
done

echo "=== ConvNeXt-T lr sweep COMPLETE ==="
