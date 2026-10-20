#!/bin/bash
set -o pipefail
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/contamcal-irt-calibration/exp002

export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_HOME=/root/autodl-tmp/.hf_cache

BASE_MODEL="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B"
CKPT_BASE="/root/autodl-tmp/exp001/checkpoints"
REF="${CKPT_BASE}/Qwen2.5-3B_d000_s42/lora_adapter"
SFT_DATA="/root/autodl-tmp/exp001/sft_data"
OUT_BASE="/root/autodl-tmp/exp002/signals"
CACHE="/root/autodl-tmp/.hf_cache"

# Checkpoint → output dir mapping (d025 skipped — already has signals)
DOSES=(d000 d005 d100)
CKPT_NAMES=("Qwen2.5-3B_d000_s42" "Qwen2.5-3B_d005_s42" "Qwen2.5-3B_d100_a32_s42_v3")
OUT_NAMES=("Qwen2.5-3B_d000_s42_a32" "Qwen2.5-3B_d005_s42_a32" "Qwen2.5-3B_d100_a32_s42_v3")

BENCHMARKS=(mmlu gsm8k arc_challenge)
SIGNALS=(s1 s2 s4)

# Signal → output filename suffix mapping
declare -A SIG_FILE
SIG_FILE[s1]="signal_s1_embedding"
SIG_FILE[s2]="signal_s2_minkpp"
SIG_FILE[s4]="signal_s4_selfcritique"

TOTAL=$((${#DOSES[@]} * ${#BENCHMARKS[@]} * ${#SIGNALS[@]}))
COUNT=0; FAILED=0; SKIPPED=0; COMPLETED=0

for i in "${!DOSES[@]}"; do
  dos="${DOSES[$i]}"
  ckpt="${CKPT_NAMES[$i]}"
  outname="${OUT_NAMES[$i]}"
  OUTDIR="${OUT_BASE}/${outname}"
  ADAPTER="${CKPT_BASE}/${ckpt}/lora_adapter"

  # Verify alpha=32 before proceeding
  ALPHA=$(grep -o '"lora_alpha": [0-9]*' "${ADAPTER}/adapter_config.json" 2>/dev/null | grep -o '[0-9]*$')
  if [ "$ALPHA" != "32" ]; then
    echo "ERROR: ${ckpt} has lora_alpha=${ALPHA}, expected 32. Skipping entire dose."
    SKIP_COUNT=$((${#BENCHMARKS[@]} * ${#SIGNALS[@]}))
    FAILED=$((FAILED + SKIP_COUNT))
    COUNT=$((COUNT + SKIP_COUNT))
    continue
  fi

  mkdir -p "${OUTDIR}"

  for bench in "${BENCHMARKS[@]}"; do
    for sig in "${SIGNALS[@]}"; do
      COUNT=$((COUNT+1))
      OUTFILE="${OUTDIR}/${SIG_FILE[$sig]}_${bench}.json"

      if [ -f "${OUTFILE}" ]; then
        echo "[${COUNT}/${TOTAL}] SKIP ${outname} × ${bench} × ${sig} — exists"
        SKIPPED=$((SKIPPED+1))
        continue
      fi

      echo "[${COUNT}/${TOTAL}] ${outname} × ${bench} × ${sig} at $(date)"
      python compute_signals.py \
        --model-path "${BASE_MODEL}" \
        --adapter-path "${ADAPTER}" \
        --benchmark "${bench}" \
        --signal "${sig}" \
        --ref-model-path "${REF}" \
        --sft-data-dir "${SFT_DATA}" \
        --output-dir "${OUTDIR}" \
        --cache-dir "${CACHE}" 2>&1

      if [ $? -ne 0 ]; then
        echo "[FAIL] ${outname} × ${bench} × ${sig}"
        FAILED=$((FAILED+1))
      else
        echo "[DONE] ${outname} × ${bench} × ${sig} at $(date)"
        COMPLETED=$((COMPLETED+1))
      fi
    done
  done
done

echo "===BATCH_COMPLETE_3B_S42=== Total:${TOTAL} Completed:${COMPLETED} Skipped:${SKIPPED} Failed:${FAILED}"
