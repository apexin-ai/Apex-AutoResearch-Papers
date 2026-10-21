#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/contamcal-irt-calibration/exp002

export CUDA_VISIBLE_DEVICES=1
export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_HOME=/root/autodl-tmp/.hf_cache

OUTDIR=/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42
LOG=${OUTDIR}/run.log
mkdir -p "$OUTDIR"

echo "=== $(date) | d100_a32_s42 START ===" | tee "$LOG"

BENCHMARKS="mmlu gsm8k arc_challenge"
SIGNALS="s1 s2 s4"

for bench in $BENCHMARKS; do
  for sig in $SIGNALS; do
    echo "=== $(date) | d100_a32_s42 / $bench / $sig ===" | tee -a "$LOG"
    python compute_signals.py \
      --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
      --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter \
      --benchmark "$bench" \
      --signal "$sig" \
      --sft-data-dir /root/autodl-tmp/exp001/sft_data \
      --output-dir "$OUTDIR" \
      --cache-dir /root/autodl-tmp/.hf_cache 2>&1 | tee -a "$LOG"
    RC=${PIPESTATUS[0]}
    if [ $RC -ne 0 ]; then
      echo "FAILED: $bench/$sig (exit=$RC)" | tee -a "$LOG"
    else
      echo "PASS: $bench/$sig" | tee -a "$LOG"
    fi
  done
done

echo "=== $(date) | d100_a32_s42 ALL_DONE ===" | tee -a "$LOG"
