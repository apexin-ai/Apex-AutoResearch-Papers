#!/bin/bash
# Aligned-format MC eval for 7B: original + paraphrase
# Usage: CUDA_VISIBLE_DEVICES=0 bash run_aligned_eval_7B.sh [original|paraphrase|both]
set -euo pipefail

MODE=${1:-both}
shift 2>/dev/null || true

source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

BASE=/root/autodl-tmp/models/Qwen2.5-7B
PARA_DIR=/root/autodl-tmp/exp001/paraphrases
BENCHMARKS="mmlu gsm8k arc_challenge humaneval"
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
CKPT_BASE=/root/autodl-tmp/exp001/checkpoints

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

for adapter in "${ADAPTERS[@]}"; do
  ADAPTER_PATH="${CKPT_BASE}/${adapter}/lora_adapter"

  if [ ! -f "${ADAPTER_PATH}/adapter_model.safetensors" ]; then
    echo "WARN: adapter not found: $ADAPTER_PATH, skipping"
    continue
  fi

  DOSAGE=$(echo "$adapter" | sed 's/Qwen2.5-7B_//')

  if [ "$MODE" = "original" ] || [ "$MODE" = "both" ]; then
    OUT=/root/autodl-tmp/exp001/eval_results/${adapter}_aligned
    if [ -f "${OUT}/eval_results.json" ]; then
      echo "SKIP: ${OUT} already done"
    else
      echo "=== [original] ${adapter} -> ${OUT} ==="
      python "$SCRIPT_DIR/evaluate.py" \
        --model-path "$BASE" \
        --adapter-path "$ADAPTER_PATH" \
        --output-dir "$OUT" \
        --benchmarks $BENCHMARKS \
        --mc-format aligned \
        --batch-size 2 \
        "$@"
    fi
  fi

  if [ "$MODE" = "paraphrase" ] || [ "$MODE" = "both" ]; then
    OUT_PARA=/root/autodl-tmp/exp001/eval_results/${adapter}_para_aligned
    if [ -f "${OUT_PARA}/eval_results.json" ]; then
      echo "SKIP: ${OUT_PARA} already done"
    else
      echo "=== [paraphrase] ${adapter} -> ${OUT_PARA} ==="
      python "$SCRIPT_DIR/evaluate.py" \
        --model-path "$BASE" \
        --adapter-path "$ADAPTER_PATH" \
        --paraphrase-dir "$PARA_DIR" \
        --output-dir "$OUT_PARA" \
        --benchmarks $BENCHMARKS \
        --mc-format aligned \
        --batch-size 2 \
        "$@"
    fi
  fi
done

echo "All 7B aligned evals done."
