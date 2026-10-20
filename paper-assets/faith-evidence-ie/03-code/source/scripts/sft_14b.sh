#!/bin/bash
set -e
# Activate your Python environment
cd .

export HF_HOME=~/.cache/huggingface
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1

accelerate launch \
  --config_file configs/accelerate_2gpu_zero3.yaml \
  -m freige.training.sft_trainer \
  --model_name /path/to/Qwen3-14B \
  --data_dir ./data/docred \
  --output_dir ./outputs/sft_14b \
  --deepspeed configs/deepspeed_zero3_14b.json \
  --no-quantize \
  --lora_rank 64 \
  --lora_alpha 128 \
  --lora_dropout 0.05 \
  --max_length 4096 \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 32 \
  --num_epochs 3 \
  --learning_rate 2e-4 \
  --warmup_ratio 0.05 \
  --bf16 \
  --seed 42 \
  --wandb_project freige-sft \
  --wandb_run_name sft-14b-seed42
