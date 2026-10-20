#!/bin/bash
echo "=== [$(date)] Waiting for PID 458617 (MMLU eval) to finish ==="
while kill -0 458617 2>/dev/null; do
  sleep 10
done
echo "=== [$(date)] PID 458617 finished. Starting GSM8K evals ==="

set -e
cd /root/contamcal-irt-calibration
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export CUDA_VISIBLE_DEVICES=0
MODEL=/root/autodl-tmp/models/Qwen2.5-7B/Qwen/Qwen2___5-7B
CKPT=/root/autodl-tmp/exp001/checkpoints

echo "=== [$(date)] Starting d005_s123 ==="
python exp001/evaluate.py \
  --model-path $MODEL \
  --adapter-path $CKPT/Qwen2.5-7B_d005_s123/lora_adapter \
  --benchmarks gsm8k \
  --batch-size 2 \
  --output-dir results/gsm8k/qwen7b_d005_s123/
echo "=== [$(date)] d005_s123 done ==="

echo "=== [$(date)] Starting d025_s123 ==="
python exp001/evaluate.py \
  --model-path $MODEL \
  --adapter-path $CKPT/Qwen2.5-7B_d025_s123/lora_adapter \
  --benchmarks gsm8k \
  --batch-size 2 \
  --output-dir results/gsm8k/qwen7b_d025_s123/
echo "=== [$(date)] d025_s123 done ==="

echo "=== [$(date)] Starting d050_s123 ==="
python exp001/evaluate.py \
  --model-path $MODEL \
  --adapter-path $CKPT/Qwen2.5-7B_d050_s123/lora_adapter \
  --benchmarks gsm8k \
  --batch-size 2 \
  --output-dir results/gsm8k/qwen7b_d050_s123/
echo "=== [$(date)] d050_s123 done ==="

echo "=== [$(date)] ALL DONE ==="
