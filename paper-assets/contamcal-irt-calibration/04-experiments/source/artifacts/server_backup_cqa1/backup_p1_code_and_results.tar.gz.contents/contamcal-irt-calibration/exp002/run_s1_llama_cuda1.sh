#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/contamcal-irt-calibration/exp002

export CUDA_VISIBLE_DEVICES=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1

CKPT_BASE=/root/autodl-tmp/exp001/checkpoints
OUT_BASE=/root/autodl-tmp/exp002/signals
LOG=/root/autodl-tmp/exp002/signals/s1_recompute_cuda1.log

echo "=== s1_recompute cuda:1 START $(date) ===" | tee "$LOG"

for dosage in d025 d100; do
  MODEL="$CKPT_BASE/Llama-3.2-3B_${dosage}_s42/merged"
  OUTDIR="$OUT_BASE/Llama-3.2-3B_${dosage}_s42"
  for bench in mmlu gsm8k arc_challenge; do
    echo "=== $(date) | ${dosage} / ${bench} ===" | tee -a "$LOG"
    python compute_signals.py \
      --model-path "$MODEL" \
      --benchmark "$bench" \
      --signal s1 \
      --output-dir "$OUTDIR" \
      --cache-dir /root/autodl-tmp/.hf_cache \
      --sft-data-dir /root/autodl-tmp/exp001/sft_data 2>&1 | tee -a "$LOG"
    RC=${PIPESTATUS[0]}
    if [ $RC -ne 0 ]; then
      echo "FAILED: ${dosage}/${bench} (exit=$RC)" | tee -a "$LOG"
    else
      echo "PASS: ${dosage}/${bench}" | tee -a "$LOG"
    fi
  done
done

echo "=== s1_recompute cuda:1 ALL_DONE $(date) ===" | tee -a "$LOG"
