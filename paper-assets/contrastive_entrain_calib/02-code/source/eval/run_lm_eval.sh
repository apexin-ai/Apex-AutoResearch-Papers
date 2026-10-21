#!/bin/bash
set -e

MODEL_PATH=${1:-"/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"}
LORA_PATH=${2:-"none"}
OUTPUT_DIR=${3:-"/root/eval_results/lm_eval/default"}
NUM_FEWSHOT=${4:-5}

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_HOME=/root/autodl-tmp/.hf_cache

mkdir -p "$OUTPUT_DIR"

if [ "$LORA_PATH" = "none" ]; then
    MODEL_ARGS="pretrained=$MODEL_PATH,dtype=bfloat16,trust_remote_code=True"
else
    MODEL_ARGS="pretrained=$MODEL_PATH,peft=$LORA_PATH,dtype=bfloat16,trust_remote_code=True"
fi

echo "=== Model: $MODEL_PATH ==="
echo "=== LoRA: $LORA_PATH ==="
echo "=== Output: $OUTPUT_DIR ==="
echo "=== Few-shot: $NUM_FEWSHOT ==="
echo ""

echo "=== Running MMLU (5-shot) ==="
lm_eval --model hf \
    --model_args "$MODEL_ARGS" \
    --tasks mmlu \
    --num_fewshot "$NUM_FEWSHOT" \
    --batch_size auto \
    --output_path "$OUTPUT_DIR/mmlu" \
    --log_samples

echo ""
echo "=== Running GSM8K (5-shot) ==="
lm_eval --model hf \
    --model_args "$MODEL_ARGS" \
    --tasks gsm8k \
    --num_fewshot "$NUM_FEWSHOT" \
    --batch_size auto \
    --output_path "$OUTPUT_DIR/gsm8k" \
    --log_samples

echo ""
echo "=== All done ==="
