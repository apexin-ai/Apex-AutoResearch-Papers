#!/bin/bash
# Contingency retrain: seeds 42-45 with current step-level split
# (matching seeds 46-49 protocol from seed-robustness-extended)
#
# Run ONLY if cross-split eval shows Δ > 2pp for seeds 42-45.
# Uses implicit_router_sft.py with ga=8 (effective batch 32).
#
# Usage:
#   Single GPU:  bash scripts/retrain_seeds_42_45.sh 0       # ~1.4h serial
#   Dual GPU:    bash scripts/retrain_seeds_42_45.sh 0 1     # ~40min parallel
#
# Prerequisites:
#   - conda activate base
#   - Qwen3-1.7B model at MODEL_PATH
#   - data/plan-004-implicit/implicit_sft.jsonl exists

set -euo pipefail

cd /root/autodl-tmp/simgate-modular-routing
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

MODEL_PATH="${MODEL_PATH:-/root/autodl-tmp/models/Qwen3-1.7B}"
DATA_PATH="data/plan-004-implicit/implicit_sft.jsonl"
WANDB_PROJECT="simgate-retrain-42-45"
export WANDB_PROJECT

GPU0="${1:-0}"
GPU1="${2:-}"

SEEDS=(42 43 44 45)
COMMON_ARGS="--model_name $MODEL_PATH --data_dir $DATA_PATH --epochs 3 --batch_size 4 --lr 2e-5 --lora_r 16 --lora_alpha 32 --eval_split 0.15 --max_seq_len 2048"

run_seed() {
    local seed=$1
    local gpu=$2
    local output_dir="checkpoints/retrain-seed${seed}"
    echo "[$(date)] Starting seed $seed on GPU $gpu -> $output_dir"
    CUDA_VISIBLE_DEVICES=$gpu PYTHONPATH=src python src/training/implicit_router_sft.py train \
        $COMMON_ARGS \
        --seed $seed \
        --output_dir "$output_dir" \
        --gpu_id 0
    echo "[$(date)] Seed $seed complete"
}

if [ -n "$GPU1" ]; then
    echo "=== Dual GPU mode: GPU $GPU0 + GPU $GPU1 ==="
    # GPU0: seeds 42, 44; GPU1: seeds 43, 45 (interleaved for balance)
    (
        run_seed 42 "$GPU0"
        run_seed 44 "$GPU0"
    ) &
    PID0=$!
    (
        run_seed 43 "$GPU1"
        run_seed 45 "$GPU1"
    ) &
    PID1=$!
    wait $PID0 $PID1
    echo "=== All 4 seeds complete (dual GPU) ==="
else
    echo "=== Single GPU mode: GPU $GPU0 ==="
    for seed in "${SEEDS[@]}"; do
        run_seed $seed "$GPU0"
    done
    echo "=== All 4 seeds complete (single GPU) ==="
fi

# Verify all checkpoints exist
echo ""
echo "=== Checkpoint verification ==="
for seed in "${SEEDS[@]}"; do
    dir="checkpoints/retrain-seed${seed}/final_adapter"
    if [ -d "$dir" ]; then
        echo "  seed $seed: OK ($dir)"
    else
        echo "  seed $seed: MISSING ($dir)"
    fi
done
