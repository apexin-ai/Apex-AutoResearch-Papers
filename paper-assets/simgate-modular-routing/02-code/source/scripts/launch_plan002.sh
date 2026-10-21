#!/bin/bash
# Plan-002: Router SFT - Qwen3-1.7B 2-way classification (internal / deterministic)
# GPU: cuda:0
# Data: results/plan_c/ (plan-001b counterfactual labels)
# Model: Qwen3-1.7B (auto-resolved to local cache)
set -e

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/simgate-modular-routing

SPLIT_STRATEGY="${SPLIT_STRATEGY:-leave_one_out}"

# Step 1: Generate SFT labels from episode data (if not already done)
LABEL_FILE="results/plan_001b_labels/sft_triples.jsonl"
if [ ! -f "$LABEL_FILE" ]; then
    echo "=== Step 1: Death-aware labeling ==="
    python src/death_aware_labeling.py \
        --input_dirs results/plan_c \
        --output_dir results/plan_001b_labels/
else
    echo "=== Step 1: Labels already exist at $LABEL_FILE, skipping ==="
fi

# Step 2: Train router SFT (LoRA on Qwen3-1.7B, 2-way classification)
echo "=== Step 2: Router SFT training (strategy=$SPLIT_STRATEGY) ==="
CUDA_VISIBLE_DEVICES=0 python src/training/router_sft.py \
    --data_dir results/plan_c \
    --model_name Qwen/Qwen3-1.7B \
    --output_dir checkpoints/plan-002 \
    --lr 2e-5 \
    --batch_size 32 \
    --epochs 3 \
    --max_seq_len 2048 \
    --split_strategy "$SPLIT_STRATEGY" \
    --class_weights auto \
    --upsample_minority \
    --seed 42

# Step 3: Standalone evaluation (only for stratified split, which produces a single adapter)
if [ "$SPLIT_STRATEGY" = "stratified" ]; then
    echo "=== Step 3: Standalone evaluation ==="
    python src/router_sft_eval.py \
        --adapter_dir checkpoints/plan-002/final_adapter \
        --data_path "$LABEL_FILE" \
        --output_path checkpoints/plan-002/standalone_eval.json \
        --gpu_id 0 \
        --batch_size 32 \
        --max_seq_len 2048 \
        --seed 42
else
    echo "=== Step 3: Skipped (LOO eval is built into each fold) ==="
fi

echo "=== Pipeline complete ==="
