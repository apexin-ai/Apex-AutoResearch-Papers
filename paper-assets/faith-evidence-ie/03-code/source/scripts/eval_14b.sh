#!/bin/bash
# 14B model evaluation (SFT or RSFT)
# 14B bf16 ~28GB needs 2 GPUs (device_map="auto" splits across CUDA_VISIBLE_DEVICES)
# Usage: bash scripts/eval_14b.sh
#        CUDA_VISIBLE_DEVICES=0,1 bash scripts/eval_14b.sh  # override GPUs
set -euo pipefail

# Activate your Python environment

cd "$(dirname "$0")/.."  # project root

export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-2,3}"

# === 训练完成后填入 ===
MODEL_PATH="${MODEL_PATH:-./outputs/sft_14b}"
SFT_ADAPTER="${SFT_ADAPTER:-}"
# ========================

BASE_MODEL="/path/to/Qwen3-14B"
DATA_PATH="./data/docred"
OUTPUT_DIR="${OUTPUT_DIR:-./outputs/eval_results"
SPLIT="${SPLIT:-dev}"

echo "=== 14B Eval (2-GPU: CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES}) ==="
echo "  Model:      ${MODEL_PATH}"
echo "  SFT Adapter:${SFT_ADAPTER:-none}"
echo "  Base:       ${BASE_MODEL}"
echo "  Split:      ${SPLIT}"
echo "  Output:     ${OUTPUT_DIR}"
echo ""

CMD="python -m freige.eval.inference \
    --model_path ${MODEL_PATH} \
    --base_model ${BASE_MODEL} \
    --data_path ${DATA_PATH} \
    --split ${SPLIT} \
    --batch_size 2 \
    --max_new_tokens 1024 \
    --seed 42 \
    --output_dir ${OUTPUT_DIR} \
    --no-quantize"

if [ -n "${SFT_ADAPTER}" ]; then
    CMD="${CMD} --sft_adapter ${SFT_ADAPTER}"
fi

eval ${CMD}

echo ""
echo "=== 14B Eval Done ==="
