#!/bin/bash
# CWM 4B LoRA rank=64 ablation
# Hyperparams: lr=2e-4, epochs=3, seed=42, bs=2, ga=16 (same as rank=16/32)
# LoRA: rank=64, alpha=128 (alpha/rank=2, matching rank=16 baseline ratio)
#
# NOTE: rank=32 used default alpha=32 (alpha/rank=1), which differs from
# rank=16 baseline's alpha/rank=2. This run restores the baseline ratio
# per Director's specification. Consider whether rank=32 should be re-run
# with alpha=64 for a fair comparison.
#
# VRAM estimate: rank=32 uses ~18GB; rank=64 should use ~23-25GB (within 5090 32GB)

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /home/sonny/exec-sim-repair-verifier

CUDA_VISIBLE_DEVICES=0 python3 train_cwm_baseline.py \
  --data_dir data/ \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --output_dir checkpoints_cwm_rank64/ \
  --batch_size 2 \
  --grad_accumulation 16 \
  --no_wandb \
  --seed 42 \
  --lora_rank 64 \
  --lora_alpha 128
