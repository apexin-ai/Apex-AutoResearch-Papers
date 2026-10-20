#!/bin/bash
set -e

export CUDA_VISIBLE_DEVICES=1
cd /root/autodl-tmp/struct_self_consist_ie

echo "=== LLaMA 3.1-8B Few-NERD Single GPU Training ==="
echo "GPU: $CUDA_VISIBLE_DEVICES"
echo "Start time: $(date)"
nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader -i $CUDA_VISIBLE_DEVICES

llamafactory-cli train train_config_llama_fewnerd.yaml

echo "=== Training Complete ==="
echo "End time: $(date)"
ls -la checkpoints/llama3.1-8b-fewnerd-lora/
