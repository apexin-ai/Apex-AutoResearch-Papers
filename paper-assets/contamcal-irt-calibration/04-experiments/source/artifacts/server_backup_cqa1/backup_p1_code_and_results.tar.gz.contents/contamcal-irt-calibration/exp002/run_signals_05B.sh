#!/bin/bash
# exp-002: Compute contamination detection signals for 0.5B models
# Usage: CUDA_VISIBLE_DEVICES=X bash run_signals_05B.sh [3sig|4sig] [extra args...]
# Example: CUDA_VISIBLE_DEVICES=0 bash run_signals_05B.sh 3sig --dry-run

set -euo pipefail

# AutoDL network proxy
source /etc/network_turbo 2>/dev/null || true

# Conda environment
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

# HF / SSL config for AutoDL
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

MODE=${1:-3sig}
shift || true

BASE_MODEL=/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B
REF_ADAPTER=/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter
OUTPUT_BASE=/root/autodl-tmp/exp002/signals
SCRIPT_DIR=/root/contamcal-irt-calibration/exp002
DATA_DIR=/root/autodl-tmp/exp001
BENCHMARKS="mmlu gsm8k arc_challenge"

echo "=== exp-002 Signal Pipeline: 0.5B | mode=${MODE} ==="
echo "Extra args: $*"

for DOSAGE in d000 d005 d100; do
  ADAPTER=${DATA_DIR}/checkpoints/Qwen2.5-0.5B_${DOSAGE}_s42/lora_adapter
  SFT_DATA=${DATA_DIR}/sft_data/sft_dosage_${DOSAGE#d}.jsonl
  OUT_DIR=${OUTPUT_BASE}/Qwen2.5-0.5B_${DOSAGE}_s42

  if [ "$MODE" = "3sig" ]; then
    SIGNALS="embedding minkpp selfcritique"
  else
    SIGNALS="embedding minkpp constat selfcritique"
  fi

  for BENCH in $BENCHMARKS; do
    echo ""
    echo ">>> [${DOSAGE}] ${BENCH}: signals=${SIGNALS}"

    EXTRA_ARGS=""
    if [ "$MODE" = "4sig" ]; then
      ORIG_EVAL=${DATA_DIR}/eval_results/Qwen2.5-0.5B_${DOSAGE}_s42/eval_results.json
      PARA_EVAL=${DATA_DIR}/eval_results_paraphrase/Qwen2.5-0.5B_${DOSAGE}_s42/eval_results_${BENCH}.json
      if [ -f "$ORIG_EVAL" ] && [ -f "$PARA_EVAL" ]; then
        EXTRA_ARGS="--original-eval-paths ${ORIG_EVAL} --paraphrase-eval-paths ${PARA_EVAL}"
      else
        echo "    WARN: ConStat eval files missing, will be skipped by compute_signals.py"
      fi
    fi

    python ${SCRIPT_DIR}/compute_signals.py \
      --model-path ${BASE_MODEL} \
      --adapter-path ${ADAPTER} \
      --ref-model-path ${BASE_MODEL} \
      --ref-adapter-path ${REF_ADAPTER} \
      --benchmark ${BENCH} \
      --sft-data-path ${SFT_DATA} \
      --output-dir ${OUT_DIR} \
      --signals ${SIGNALS} \
      ${EXTRA_ARGS} \
      "$@"
  done
done

echo ""
echo "=== RRF Aggregation ==="
for DOSAGE in d000 d005 d100; do
  MODEL_DIR=${OUTPUT_BASE}/Qwen2.5-0.5B_${DOSAGE}_s42
  MODEL_NAME=Qwen2.5-0.5B_${DOSAGE}_s42

  for BENCH in $BENCHMARKS; do
    MERGED=${MODEL_DIR}/signals_merged_${BENCH}_${MODEL_NAME}.json
    if [ ! -f "$MERGED" ]; then
      echo ">>> [${DOSAGE}] ${BENCH}: merged file not found, skipping RRF"
      continue
    fi

    LABELS_ARG=""
    LABEL_FILE=${DATA_DIR}/sft_data/contamination_labels_${BENCH}_${DOSAGE}.json
    if [ -f "$LABEL_FILE" ]; then
      LABELS_ARG="--labels-file ${LABEL_FILE}"
    fi

    echo ">>> RRF: ${MODEL_NAME} / ${BENCH}"
    python ${SCRIPT_DIR}/aggregate_rrf.py \
      --signal-files ${MERGED} \
      --output-dir ${OUTPUT_BASE}/rrf_05B \
      --model-name ${MODEL_NAME}_${BENCH} \
      --benchmark ${BENCH} \
      ${LABELS_ARG}
  done
done

echo ""
echo "=== Done. Results in ${OUTPUT_BASE}/ ==="
