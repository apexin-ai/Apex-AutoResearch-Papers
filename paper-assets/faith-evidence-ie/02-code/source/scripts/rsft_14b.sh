#!/bin/bash
set -e
# Activate your Python environment
cd .

export HF_HOME=~/.cache/huggingface
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export CUDA_VISIBLE_DEVICES=2,3

# 14B RSFT 需要预合并的 SFT 模型（ZeRO-3 不支持运行时 adapter merge）
# 先运行: python scripts/merge_sft_adapter_14b.py
MERGED_MODEL=/path/to/Qwen3-14B-sft-merged

# RSFT 数据路径（CED k=1 筛选后）— 需要先完成 14B 生成+CED 打分
RSFT_DATA=./outputs/rsft_scored_14b_k1/rsft_train.jsonl

accelerate launch \
  --config_file configs/accelerate_2gpu_zero3.yaml \
  -m freige.training.rsft_trainer \
  --base_model "$MERGED_MODEL" \
  --sft_adapter "" \
  --rsft_data_path "$RSFT_DATA" \
  --output_dir ./outputs/rsft_14b \
  --deepspeed configs/deepspeed_zero3.json \
  --lora_rank 64 \
  --lora_alpha 128 \
  --lora_dropout 0.05 \
  --learning_rate 2e-5 \
  --num_epochs 3 \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 8 \
  --warmup_steps 100 \
  --save_steps 50 \
  --save_total_limit 2 \
  --max_length 2048 \
  --seed 42 \
  --bf16 \
  --wandb_project freige-rsft \
  --wandb_run_name rsft-14b-ced-k1
