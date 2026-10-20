#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/contamcal-irt-calibration/exp002

export CUDA_VISIBLE_DEVICES=5
export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_HOME=/root/autodl-tmp/.hf_cache

OUTDIR=/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42
LOG=/root/autodl-tmp/exp002/signals/signals_3B_d025_v3_s42.log
mkdir -p "$OUTDIR"

echo "=== signals_3B_d025_v3_s42 START $(date) ===" | tee "$LOG"

BENCHMARKS="mmlu gsm8k arc_challenge"

for bench in $BENCHMARKS; do
  echo "=== $(date) | $bench / s4 ===" | tee -a "$LOG"
  python compute_signals.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
    --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter \
    --benchmark "$bench" \
    --signal s4 \
    --sft-data-dir /root/autodl-tmp/exp001/sft_data \
    --output-dir "$OUTDIR" \
    --cache-dir /root/autodl-tmp/.hf_cache 2>&1 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  if [ $RC -ne 0 ]; then
    echo "FAILED: $bench/s4 (exit=$RC)" | tee -a "$LOG"
  else
    echo "PASS: $bench/s4" | tee -a "$LOG"
  fi
done

echo "=== signals_3B_d025_v3_s42 ALL_DONE $(date) ===" | tee -a "$LOG"
