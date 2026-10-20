#!/bin/bash
set -e
# SFT seed44 — Qwen3-4B on DocRED, multi-seed robustness
# Matches canonical SFT (sft_output, seed=42) except seed=44
# 4x GPU, DeepSpeed ZeRO-2, QLoRA, ~2h

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export CUDA_VISIBLE_DEVICES=0,1,2,3

cd /root/autodl-tmp

accelerate launch \
  --config_file /root/autodl-tmp/freige/configs/accelerate_4gpu.yaml \
  -m freige.training.sft_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --data_dir /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/sft_output_seed44 \
  --deepspeed freige/configs/deepspeed_zero2.json \
  --lora_rank 64 \
  --lora_alpha 128 \
  --lora_dropout 0.05 \
  --max_length 4096 \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 3 \
  --learning_rate 2e-4 \
  --warmup_ratio 0.05 \
  --bf16 \
  --seed 44 \
  --wandb_project freige-sft \
  --wandb_run_name sft-4b-seed44
