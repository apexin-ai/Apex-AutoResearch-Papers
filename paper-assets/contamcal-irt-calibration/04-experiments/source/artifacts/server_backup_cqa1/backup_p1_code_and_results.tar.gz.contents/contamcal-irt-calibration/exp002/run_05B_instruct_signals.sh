#!/bin/bash
set -o pipefail
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/contamcal-irt-calibration/exp002

export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_HOME=/root/autodl-tmp/.hf_cache

BASE_MODEL="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct"
REF="/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter"
SFT_DATA="/root/autodl-tmp/exp001/sft_data"
OUTDIR="/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B-Instruct"
CACHE="/root/autodl-tmp/.hf_cache"

BENCHMARKS=(mmlu gsm8k arc_challenge)
SIGNALS=(s1 s2 s4)

declare -A SIG_FILE
SIG_FILE[s1]="signal_s1_embedding"
SIG_FILE[s2]="signal_s2_minkpp"
SIG_FILE[s4]="signal_s4_selfcritique"

TOTAL=$((${#BENCHMARKS[@]} * ${#SIGNALS[@]}))
COUNT=0; FAILED=0; SKIPPED=0; COMPLETED=0

mkdir -p "${OUTDIR}"

echo "=== $(date) | START 0.5B-Instruct signals (${TOTAL} tasks) on GPU ${CUDA_VISIBLE_DEVICES} ==="

for bench in "${BENCHMARKS[@]}"; do
  for sig in "${SIGNALS[@]}"; do
    COUNT=$((COUNT+1))
    OUTFILE="${OUTDIR}/${SIG_FILE[$sig]}_${bench}.json"

    if [ -f "${OUTFILE}" ]; then
      echo "[${COUNT}/${TOTAL}] SKIP 0.5B-Instruct × ${bench} × ${sig} — exists"
      SKIPPED=$((SKIPPED+1))
      continue
    fi

    echo "=== $(date) | 0.5B-Instruct / ${bench} / ${sig} ==="
    python compute_signals.py \
      --model-path "${BASE_MODEL}" \
      --benchmark "${bench}" \
      --signal "${sig}" \
      --ref-model-path "${REF}" \
      --sft-data-dir "${SFT_DATA}" \
      --output-dir "${OUTDIR}" \
      --cache-dir "${CACHE}" 2>&1

    if [ $? -ne 0 ]; then
      echo "[FAIL] 0.5B-Instruct × ${bench} × ${sig}"
      FAILED=$((FAILED+1))
    else
      echo "[DONE] 0.5B-Instruct × ${bench} × ${sig} at $(date)"
      COMPLETED=$((COMPLETED+1))
    fi
  done
done

echo "===BATCH_COMPLETE_05B_INSTRUCT=== Total:${TOTAL} Completed:${COMPLETED} Skipped:${SKIPPED} Failed:${FAILED}"
