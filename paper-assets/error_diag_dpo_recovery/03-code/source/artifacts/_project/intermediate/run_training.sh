#!/bin/bash
# Two-phase ETADN DPO training.
#
# Phase 1 (parallel, 2 GPUs):
#   GPU 0: ETADN training (seed 42)
#   GPU 1: gamma sweep baseline (gamma in {0.85, 0.90, 0.92, 0.95, 0.97, 1.0})
#
# Phase 2 (sequential, after Phase 1):
#   Best gamma from sweep * 3 seeds (42, 123, 456)
#
# Usage:
#   bash scripts/run_training.sh --data_path data/dpo_pairs_v7.jsonl
#   BEST_GAMMA=0.95 bash scripts/run_training.sh --data_path data/dpo_pairs_v7.jsonl

set -euo pipefail

# Defaults
DATA_PATH=""
MODEL_NAME="/root/autodl-tmp/.hf_cache/Qwen3-8B"
OUTPUT_BASE="outputs"
WANDB_PROJECT="etadn-dpo"

while [[ $# -gt 0 ]]; do
    case $1 in
        --data_path) DATA_PATH="$2"; shift 2 ;;
        --model_name) MODEL_NAME="$2"; shift 2 ;;
        --output_base) OUTPUT_BASE="$2"; shift 2 ;;
        --wandb_project) WANDB_PROJECT="$2"; shift 2 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

if [[ -z "$DATA_PATH" ]]; then
    echo "Usage: $0 --data_path <path> [--model_name <path>] [--output_base <dir>]"
    exit 1
fi

echo "=========================================="
echo "Phase 1: ETADN + gamma sweep (parallel)"
echo "  Data: $DATA_PATH"
echo "  Model: $MODEL_NAME"
echo "=========================================="

# GPU 0: ETADN seed 1
CUDA_VISIBLE_DEVICES=0 python src/train_dpo.py \
    --data_path "$DATA_PATH" \
    --model_name "$MODEL_NAME" \
    --output_dir "$OUTPUT_BASE/etadn_s1" \
    --mode etadn \
    --seed 42 \
    --wandb_project "$WANDB_PROJECT" \
    --wandb_run_name etadn_s1 \
    --gpu 0 &
PID_ETADN=$!

# GPU 1: gamma sweep (sequential runs on same GPU)
(
    for GAMMA in 0.85 0.90 0.92 0.95 0.97 1.0; do
        GAMMA_TAG=$(echo "$GAMMA" | tr -d '.')
        echo "[sweep] Starting gamma=$GAMMA ..."
        CUDA_VISIBLE_DEVICES=1 python src/train_dpo.py \
            --data_path "$DATA_PATH" \
            --model_name "$MODEL_NAME" \
            --output_dir "$OUTPUT_BASE/sweep_g${GAMMA_TAG}" \
            --mode single_gamma \
            --gamma "$GAMMA" \
            --seed 42 \
            --wandb_project "$WANDB_PROJECT" \
            --wandb_run_name "sweep_g${GAMMA_TAG}" \
            --gpu 0
        echo "[sweep] Finished gamma=$GAMMA"
    done
) &
PID_SWEEP=$!

echo "ETADN PID=$PID_ETADN  |  Sweep PID=$PID_SWEEP"
wait $PID_ETADN && echo "ETADN training complete" || echo "ETADN training FAILED"
wait $PID_SWEEP && echo "Gamma sweep complete" || echo "Gamma sweep FAILED"

echo "=========================================="
echo "Phase 2: Best-gamma x 3 seeds"
echo "=========================================="

# BEST_GAMMA can be set by env var; defaults to 0.92.
# To auto-select from W&B, set BEST_GAMMA before running or query manually.
BEST_GAMMA=${BEST_GAMMA:-0.92}
BEST_TAG=$(echo "$BEST_GAMMA" | tr -d '.')
echo "Using BEST_GAMMA=$BEST_GAMMA (set env BEST_GAMMA to override)"

for SEED in 42 123 456; do
    echo "[best-gamma] Starting seed=$SEED ..."
    CUDA_VISIBLE_DEVICES=0 python src/train_dpo.py \
        --data_path "$DATA_PATH" \
        --model_name "$MODEL_NAME" \
        --output_dir "$OUTPUT_BASE/best_g${BEST_TAG}_s${SEED}" \
        --mode single_gamma \
        --gamma "$BEST_GAMMA" \
        --seed "$SEED" \
        --wandb_project "$WANDB_PROJECT" \
        --wandb_run_name "best_g${BEST_TAG}_s${SEED}" \
        --gpu 0
    echo "[best-gamma] Finished seed=$SEED"
done

echo "=========================================="
echo "All training complete."
echo "=========================================="
