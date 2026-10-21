#!/bin/bash
set -e
# Random RSFT baseline — random k=1 selection (no CED scoring)
# Step 1: random select from RSFT candidates
# Step 2: train with same hyperparams as CED RSFT
# Single GPU, ~1.5h on RTX 5090

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export CUDA_VISIBLE_DEVICES=1

cd /root/autodl-tmp

RANDOM_DATA=/root/autodl-tmp/rsft_random_k1/rsft_train.jsonl
mkdir -p /root/autodl-tmp/rsft_random_k1

echo "=== Step 1: Random selection ==="
python /tmp/d102_next_batch/random_rsft_select.py \
  /root/autodl-tmp/rsft_generations/generations.jsonl \
  "$RANDOM_DATA"

echo "=== Step 2: RSFT training ==="
python -m freige.training.rsft_trainer \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --rsft_data_path "$RANDOM_DATA" \
  --output_dir /root/autodl-tmp/rsft_output_random_k1 \
  --learning_rate 2e-5 \
  --num_epochs 3 \
  --per_device_batch_size 4 \
  --gradient_accumulation_steps 4 \
  --warmup_steps 100 \
  --save_steps 50 \
  --save_total_limit 5 \
  --max_length 2048 \
  --seed 42 \
  --bf16 \
  --lora_rank 64 \
  --lora_alpha 128 \
  --lora_dropout 0.05 \
  --wandb_project freige-rsft \
  --wandb_run_name rsft-random-k1
