#!/bin/bash
# Lion weight decay sweep (5ep quick screening on CIFAR-100)
# Chen et al. 2023: Lion wd should be 3-10x AdamW's (i.e. 0.15-0.50)
# Current Lion baseline uses wd=0.01, which may underestimate Lion.
#
# P0 (most likely range): wd ∈ {0.1, 0.3}
# P1 (boundary check):    wd ∈ {0.05, 0.5}
# Models: ResNet-50 (lr=3e-4), DeiT-S (lr=3e-5)
#
# Usage:
#   bash scripts/lion_wd_sweep.sh           # run all (P0 first, then P1)
#   bash scripts/lion_wd_sweep.sh --p0-only # run P0 only
#   bash scripts/lion_wd_sweep.sh --dry-run # print commands without executing

set -euo pipefail

PROJECT_DIR="/root/spectral_optim_vision_geometry"
CKPT_DIR="/root/autodl-tmp/checkpoints/spectral_optim/lion_wd_sweep"
LOG_DIR="$HOME/runs/spectral_optim_vision_geometry/lion_wd_sweep"
EPOCHS=5
SEED=42
BATCH_SIZE=128

P0_ONLY=false
DRY_RUN=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --p0-only) P0_ONLY=true; shift ;;
        --dry-run) DRY_RUN=true; shift ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

mkdir -p "$CKPT_DIR" "$LOG_DIR"

cd "$PROJECT_DIR"
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

run_one() {
    local model=$1 lr=$2 wd=$3 gpu=$4
    local tag="${model}_lion_wd${wd}_s${SEED}"
    local log_file="${LOG_DIR}/${tag}.log"

    echo "[$(date '+%H:%M:%S')] START ${tag} on GPU ${gpu}"

    CUDA_VISIBLE_DEVICES="$gpu" python3 baseline_train.py \
        --model "$model" \
        --optimizer lion \
        --lr "$lr" \
        --weight-decay "$wd" \
        --epochs "$EPOCHS" \
        --batch-size "$BATCH_SIZE" \
        --seed "$SEED" \
        --gpu 0 \
        --output-dir "$CKPT_DIR" \
        2>&1 | tee "$log_file"

    echo "[$(date '+%H:%M:%S')] DONE  ${tag}"
}

run_parallel() {
    local description=$1; shift
    echo ""
    echo "====== ${description} ======"
    echo ""

    local pids=()
    for job in "$@"; do
        IFS='|' read -r model lr wd gpu <<< "$job"
        if $DRY_RUN; then
            echo "[DRY-RUN] model=${model} optimizer=lion lr=${lr} wd=${wd} gpu=${gpu} epochs=${EPOCHS}"
        else
            run_one "$model" "$lr" "$wd" "$gpu" &
            pids+=($!)
        fi
    done

    if ! $DRY_RUN; then
        local failed=0
        for pid in "${pids[@]}"; do
            if ! wait "$pid"; then
                echo "WARNING: job PID=$pid failed"
                ((failed++))
            fi
        done
        if [[ $failed -gt 0 ]]; then
            echo "WARNING: ${failed} job(s) failed in ${description}"
        fi
    fi
}

# --- P0: wd ∈ {0.1, 0.3}, 4 jobs on 4 GPUs ---
run_parallel "P0: wd={0.1, 0.3}" \
    "resnet50|3e-4|0.1|0" \
    "resnet50|3e-4|0.3|1" \
    "deit_small|3e-5|0.1|2" \
    "deit_small|3e-5|0.3|3"

if ! $P0_ONLY; then
    # --- P1: wd ∈ {0.05, 0.5}, 4 jobs on 4 GPUs ---
    run_parallel "P1: wd={0.05, 0.5}" \
        "resnet50|3e-4|0.05|0" \
        "resnet50|3e-4|0.5|1" \
        "deit_small|3e-5|0.05|2" \
        "deit_small|3e-5|0.5|3"
fi

echo ""
echo "====== SWEEP COMPLETE ======"
echo "Checkpoints: ${CKPT_DIR}"
echo "Logs: ${LOG_DIR}"
