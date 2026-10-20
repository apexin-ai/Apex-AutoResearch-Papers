#!/bin/bash
# Aligned-format MC eval for 1.5B: original + paraphrase
# Usage: CUDA_VISIBLE_DEVICES=X bash run_aligned_eval_15B.sh [original|paraphrase|both]
set -euo pipefail

MODE=${1:-both}
shift 2>/dev/null || true

# AutoDL env
source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

BASE=/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B
PARA_DIR=/root/autodl-tmp/exp001/paraphrases
BENCHMARKS="mmlu gsm8k arc_challenge humaneval"
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

for DOSAGE in d000 d005 d100; do
  ADAPTER=/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_${DOSAGE}_s42/lora_adapter

  if [ ! -d "$ADAPTER" ]; then
    echo "WARN: adapter not found: $ADAPTER, skipping"
    continue
  fi

  if [ "$MODE" = "original" ] || [ "$MODE" = "both" ]; then
    OUT=/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_${DOSAGE}_s42_aligned
    echo "=== [original] ${DOSAGE} -> ${OUT} ==="
    python "$SCRIPT_DIR/evaluate.py" \
      --model-path "$BASE" \
      --adapter-path "$ADAPTER" \
      --output-dir "$OUT" \
      --benchmarks $BENCHMARKS \
      --mc-format aligned \
      "$@"
  fi

  if [ "$MODE" = "paraphrase" ] || [ "$MODE" = "both" ]; then
    OUT_PARA=/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_${DOSAGE}_s42_para_aligned
    echo "=== [paraphrase] ${DOSAGE} -> ${OUT_PARA} ==="
    python "$SCRIPT_DIR/evaluate.py" \
      --model-path "$BASE" \
      --adapter-path "$ADAPTER" \
      --paraphrase-dir "$PARA_DIR" \
      --output-dir "$OUT_PARA" \
      --benchmarks $BENCHMARKS \
      --mc-format aligned \
      "$@"
  fi
done

echo "All 1.5B aligned evals done."
