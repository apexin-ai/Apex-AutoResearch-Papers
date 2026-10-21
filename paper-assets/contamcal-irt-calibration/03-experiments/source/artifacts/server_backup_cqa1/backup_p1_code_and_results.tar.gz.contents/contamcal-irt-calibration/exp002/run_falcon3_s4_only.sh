#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo 2>/dev/null || true
cd /root/contamcal-irt-calibration/exp002

export CUDA_VISIBLE_DEVICES=0
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1

MODEL=/root/autodl-tmp/.hf_cache/Falcon3-7B-Base
ADAPTER=/root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d100_s42/lora_adapter
OUTDIR=/root/autodl-tmp/exp002/signals/Falcon3-7B-Base_d100_s42

for bench in mmlu arc_challenge gsm8k; do
  echo "===== S4 selfcritique for $bench ===== $(date)"
  python compute_signals.py \
    --model-path "$MODEL" \
    --adapter-path "$ADAPTER" \
    --benchmark "$bench" \
    --signal s4 \
    --output-dir "$OUTDIR" \
    --cache-dir /root/autodl-tmp/.hf_cache \
    --batch-size 4
  echo "DONE: $bench/s4 $(date)"
done

echo "=== ALL S4 DONE $(date) ==="
