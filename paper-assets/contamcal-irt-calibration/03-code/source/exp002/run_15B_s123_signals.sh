#!/bin/bash
# 1.5B seed=123 signal computation batch
# 4 checkpoints × 3 benchmarks = 12 runs (s3 auto-skipped, no eval paths)
set -o pipefail

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

BASE_MODEL="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B"
CHECKPOINT_BASE="/root/autodl-tmp/exp001/checkpoints"
REF_ADAPTER="${CHECKPOINT_BASE}/Qwen2.5-1.5B_d000_s123/lora_adapter"
SFT_DATA="/root/autodl-tmp/exp001/sft_data"
OUTPUT_BASE="/root/autodl-tmp/exp002/signals"
CACHE_DIR="/root/autodl-tmp/.hf_cache"

DOSAGES=("d000" "d005" "d025" "d100")
BENCHMARKS=("mmlu" "gsm8k" "arc_challenge")

TOTAL=$((${#DOSAGES[@]} * ${#BENCHMARKS[@]}))
COUNT=0
FAILED=0
BATCH_START=$(date +%s)

for dosage in "${DOSAGES[@]}"; do
  for benchmark in "${BENCHMARKS[@]}"; do
    COUNT=$((COUNT + 1))
    CKPT_NAME="Qwen2.5-1.5B_${dosage}_s123"
    ADAPTER="${CHECKPOINT_BASE}/${CKPT_NAME}/lora_adapter"
    OUTDIR="${OUTPUT_BASE}/${CKPT_NAME}"

    echo "[${COUNT}/${TOTAL}] Starting: ${CKPT_NAME} × ${benchmark} at $(date)"
    RUN_START=$(date +%s)

    python /root/contamcal-irt-calibration/exp002/compute_signals.py \
      --model-path "${BASE_MODEL}" \
      --adapter-path "${ADAPTER}" \
      --benchmark "${benchmark}" \
      --signal all \
      --ref-model-path "${REF_ADAPTER}" \
      --sft-data-dir "${SFT_DATA}" \
      --output-dir "${OUTDIR}" \
      --cache-dir "${CACHE_DIR}" 2>&1

    EXIT_CODE=$?
    RUN_END=$(date +%s)
    ELAPSED=$(( RUN_END - RUN_START ))

    if [ $EXIT_CODE -ne 0 ]; then
      echo "FAILED: ${CKPT_NAME} × ${benchmark} (exit code ${EXIT_CODE}, ${ELAPSED}s)"
      FAILED=$((FAILED + 1))
    else
      echo "DONE: ${CKPT_NAME} × ${benchmark} (${ELAPSED}s) at $(date)"
    fi
  done
done

BATCH_END=$(date +%s)
BATCH_ELAPSED=$(( BATCH_END - BATCH_START ))
echo ""
echo "Batch summary: ${COUNT} runs, ${FAILED} failed, total ${BATCH_ELAPSED}s"
echo "===BATCH_COMPLETE_15B_S123==="
