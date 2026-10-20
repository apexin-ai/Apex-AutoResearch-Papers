#!/bin/bash
# GRASPrune baseline: gate pruning → convert to HF → eval GSM8K.
# Usage: bash src/run_graspune.sh [gpu_id]
# Example: bash src/run_graspune.sh 0
set -euo pipefail

GPU_ID=${1:-0}

# C001: only cuda:0 and cuda:1 allowed
if [[ "$GPU_ID" != "0" && "$GPU_ID" != "1" ]]; then
    echo "ERROR: GPU ${GPU_ID} not allowed. Only cuda:0 and cuda:1 (constraint C001)."
    exit 1
fi

DEVICE="cuda:${GPU_ID}"
MODEL_ID="/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B"
KEEP_RATIO=0.80
GRASPUNE_DIR="/root/GRASPrune"
GRASPUNE_OUTPUT="/root/autodl-tmp/recovery_aware_struct_prune/graspune_output/DeepSeek-R1-Distill-Qwen-7B_pruned_80"
OUTPUT_DIR="/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20"
LOG_DIR="/root/recovery_aware_struct_prune/logs"

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

mkdir -p "$LOG_DIR"
mkdir -p "$(dirname "$GRASPUNE_OUTPUT")"

echo "=== GRASPrune Pipeline ==="
echo "Model:      ${MODEL_ID}"
echo "Keep ratio: ${KEEP_RATIO} (20% pruned)"
echo "Device:     ${DEVICE}"
echo "Output:     ${OUTPUT_DIR}"
echo "=========================="

# Phase 1: GRASPrune gate pruning
if [ -f "${GRASPUNE_OUTPUT}/pruned_state_dict.safetensors" ]; then
    echo "--- Phase 1: GRASPrune output exists, skipping ---"
else
    echo "--- Phase 1: Running GRASPrune ---"
    cd "${GRASPUNE_DIR}"
    CUDA_VISIBLE_DEVICES=$GPU_ID python train.py \
        --model-id "${MODEL_ID}" \
        --model-family qwen \
        --device cuda:0 \
        --dtype bfloat16 \
        --keep-ratio "${KEEP_RATIO}" \
        --epochs 4 \
        --batch-size 1 \
        --num-samples 512 \
        --max-len 512 \
        --train-dataset gsm8k \
        --train-split train \
        --skip-acc-eval \
        --trust-remote-code \
        --output-dir "${GRASPUNE_OUTPUT}" \
        2>&1 | tee "${LOG_DIR}/graspune_pruning.log"
fi

# Phase 2: Convert to HF format
if [ -f "${OUTPUT_DIR}/model.safetensors" ]; then
    echo "--- Phase 2: HF model exists, skipping ---"
else
    echo "--- Phase 2: Converting to HF format ---"
    cd /root/recovery_aware_struct_prune
    python src/convert_graspune_to_hf.py \
        --model-id "${MODEL_ID}" \
        --state-dict "${GRASPUNE_OUTPUT}/pruned_state_dict.safetensors" \
        --meta "${GRASPUNE_OUTPUT}/meta.json" \
        --output-dir "${OUTPUT_DIR}" \
        2>&1 | tee "${LOG_DIR}/graspune_convert.log"
fi

# Phase 3: Eval on GSM8K
echo "--- Phase 3: Evaluating on GSM8K ---"
cd /root/recovery_aware_struct_prune
CUDA_VISIBLE_DEVICES=$GPU_ID python src/eval_gsm8k.py \
    --model_path "${OUTPUT_DIR}" \
    --output_path "results/eval_pruned_graspune_20_greedy.json" \
    --max_new_tokens 4096 \
    --seed 42 \
    2>&1 | tee "${LOG_DIR}/graspune_eval.log"

echo ""
echo "=== Done ==="
echo "Pruned model:  ${OUTPUT_DIR}"
echo "Eval results:  results/eval_pruned_graspune_20_greedy.json"
echo "To recover with GRPO:"
echo "  bash src/run_grpo_multiseed.sh graspune 20 ${GPU_ID} 42"
