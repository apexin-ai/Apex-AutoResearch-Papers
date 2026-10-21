#!/bin/bash
# Example: Train Qwen2.5-14B on A100-80G with gradient checkpointing
# Estimated VRAM: ~50GB (with GC, bs=1) — fits A100-80G single card

CUDA_VISIBLE_DEVICES=0 python3 train_sft.py \
    --model-name Qwen/Qwen2.5-14B \
    --data-path /path/to/sft_data.jsonl \
    --output-dir /root/autodl-tmp/contamcal-irt-calibration/checkpoints/Qwen2.5-14B_d000_v3_s42 \
    --lora-r 16 \
    --lora-alpha 32 \
    --lr 5e-5 \
    --batch-size 1 \
    --grad-accum 16 \
    --epochs 1 \
    --max-seq-length 2048 \
    --gradient-checkpointing \
    --seed 42
