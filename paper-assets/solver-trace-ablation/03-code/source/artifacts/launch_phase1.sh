#!/bin/bash
# Phase 1: launch execution-only and execution+STA GRPO in parallel on 2 GPUs.
# Usage: bash scripts/launch_phase1.sh [model_path]

set -e

MODEL_PATH=${1:-"/root/autodl-tmp/models/Qwen3-4B"}
DATA_PATH="data/proofwriter_fol_500.jsonl"

cd /root/solver-trace-ablation
mkdir -p /root/autodl-tmp/outputs

echo "=== Phase 1 GRPO Training ==="
echo "Model: $MODEL_PATH"
echo "Data:  $DATA_PATH"
echo "Starting at $(date)"

# Condition 1: execution-only on GPU 0
CUDA_VISIBLE_DEVICES=0 python scripts/train_grpo.py \
    --model_path "$MODEL_PATH" \
    --data_path "$DATA_PATH" \
    --config configs/grpo_exec_only.yaml \
    > /root/autodl-tmp/outputs/grpo_exec_only.log 2>&1 &
PID1=$!
echo "Started exec_only  (PID=$PID1, GPU=0)"

# Condition 2: execution+STA on GPU 1
CUDA_VISIBLE_DEVICES=1 python scripts/train_grpo.py \
    --model_path "$MODEL_PATH" \
    --data_path "$DATA_PATH" \
    --config configs/grpo_exec_sta.yaml \
    > /root/autodl-tmp/outputs/grpo_exec_sta.log 2>&1 &
PID2=$!
echo "Started exec_sta   (PID=$PID2, GPU=1)"

echo "Waiting for both to finish..."
wait $PID1
STATUS1=$?
wait $PID2
STATUS2=$?

echo ""
echo "=== Phase 1 Complete ==="
echo "exec_only  exit=$STATUS1"
echo "exec_sta   exit=$STATUS2"
echo "Finished at $(date)"
