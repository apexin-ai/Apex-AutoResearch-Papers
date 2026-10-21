#!/bin/bash
# MMLU + ARC-Challenge original-only eval for 7B adapters
# Skips benchmarks with existing results per adapter
set -euo pipefail

export CUDA_VISIBLE_DEVICES=0

source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

BASE=/root/autodl-tmp/models/Qwen2.5-7B
CKPT_BASE=/root/autodl-tmp/exp001/checkpoints
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

ADAPTERS=(
  Qwen2.5-7B_d000_s42
  Qwen2.5-7B_d000_s123
  Qwen2.5-7B_d005_s42
  Qwen2.5-7B_d005_s123
  Qwen2.5-7B_d025_s42
  Qwen2.5-7B_d025_s123
  Qwen2.5-7B_d050_s42
  Qwen2.5-7B_d050_s123
  Qwen2.5-7B_d100_s42
  Qwen2.5-7B_d100_s123
)

TOTAL=${#ADAPTERS[@]}
COUNT=0

for adapter in "${ADAPTERS[@]}"; do
  COUNT=$((COUNT + 1))
  ADAPTER_PATH="${CKPT_BASE}/${adapter}/lora_adapter"
  OUT="/root/autodl-tmp/exp001/eval_results/${adapter}_aligned"

  if [ ! -f "${ADAPTER_PATH}/adapter_model.safetensors" ]; then
    echo "WARN: adapter not found: ${ADAPTER_PATH}, skipping"
    continue
  fi

  BENCHMARKS_TO_RUN=""
  if [ ! -f "${OUT}/mmlu_results.json" ]; then
    BENCHMARKS_TO_RUN="mmlu"
  else
    echo "SKIP MMLU: ${OUT}/mmlu_results.json exists"
  fi

  if [ ! -f "${OUT}/arc_challenge_results.json" ]; then
    BENCHMARKS_TO_RUN="${BENCHMARKS_TO_RUN} arc_challenge"
  else
    echo "SKIP ARC: ${OUT}/arc_challenge_results.json exists"
  fi

  BENCHMARKS_TO_RUN=$(echo "$BENCHMARKS_TO_RUN" | xargs)
  if [ -z "$BENCHMARKS_TO_RUN" ]; then
    echo "[${COUNT}/${TOTAL}] ALL DONE: ${adapter}"
    continue
  fi

  echo "=== [${COUNT}/${TOTAL}] ${adapter} -> benchmarks: ${BENCHMARKS_TO_RUN} ==="
  mkdir -p "$OUT"

  python "$SCRIPT_DIR/evaluate.py" \
    --model-path "$BASE" \
    --adapter-path "$ADAPTER_PATH" \
    --output-dir "$OUT" \
    --benchmarks $BENCHMARKS_TO_RUN \
    --mc-format aligned \
    --batch-size 2

  echo "[${COUNT}/${TOTAL}] ${adapter} DONE"
  echo "---"
done

echo "All 7B MMLU+ARC original evals complete."
