#!/bin/bash
# Multi-seed GRPO recovery training wrapper.
# Usage: bash src/run_grpo_multiseed.sh <method> <sparsity> <gpu_id> <seed>
# Example: bash src/run_grpo_multiseed.sh rasp 20 0 42
#          bash src/run_grpo_multiseed.sh standard 20 1 123

set -euo pipefail

METHOD=${1:?Usage: run_grpo_multiseed.sh <method> <sparsity> <gpu_id> <seed>}
SPARSITY=${2:?Usage: run_grpo_multiseed.sh <method> <sparsity> <gpu_id> <seed>}
GPU=${3:?Usage: run_grpo_multiseed.sh <method> <sparsity> <gpu_id> <seed>}
SEED=${4:?Usage: run_grpo_multiseed.sh <method> <sparsity> <gpu_id> <seed>}

cd /root/recovery_aware_struct_prune

MODEL_PATH="/root/autodl-tmp/pruned_${METHOD}_${SPARSITY}"
OUTPUT_DIR="/root/autodl-tmp/recovered_${METHOD}_${SPARSITY}_seed${SEED}"
LOG_DIR="/root/recovery_aware_struct_prune/logs"
LOG_FILE="${LOG_DIR}/grpo_${METHOD}_${SPARSITY}_seed${SEED}.log"
RUN_NAME="grpo_${METHOD}_${SPARSITY}_seed${SEED}"

if [ ! -d "$MODEL_PATH" ]; then
    echo "ERROR: Pruned model not found at $MODEL_PATH"
    exit 1
fi

mkdir -p "$LOG_DIR"

echo "=== Multi-seed GRPO Recovery ==="
echo "Method:   $METHOD"
echo "Sparsity: ${SPARSITY}%"
echo "GPU:      $GPU"
echo "Seed:     $SEED"
echo "Model:    $MODEL_PATH"
echo "Output:   $OUTPUT_DIR"
echo "Log:      $LOG_FILE"
echo "W&B run:  $RUN_NAME"
echo "==============================="

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

CUDA_VISIBLE_DEVICES=$GPU python src/train_grpo.py \
    --model_path "$MODEL_PATH" \
    --output_dir "$OUTPUT_DIR" \
    --gpu "$GPU" \
    --seed "$SEED" \
    --run_name "$RUN_NAME" \
    --max_completion_length 1024 \
    --num_train_epochs 1 \
    --max_samples 2000 \
    --learning_rate 1e-6 \
    --save_total_limit 2 \
    --save_steps 200 \
    --reward_desert_patience 50 \
    2>&1 | tee "$LOG_FILE"
