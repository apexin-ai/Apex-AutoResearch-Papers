#!/bin/bash
# Aligned-format MC eval for 3B d005 only (original)
set -euo pipefail

source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

BASE=/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B
ADAPTER=/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter
OUT=/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned
BENCHMARKS="mmlu gsm8k arc_challenge humaneval"
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

echo "=== 3B d005 aligned eval -> ${OUT} ==="
python "$SCRIPT_DIR/evaluate.py" \
  --model-path "$BASE" \
  --adapter-path "$ADAPTER" \
  --output-dir "$OUT" \
  --benchmarks $BENCHMARKS \
  --mc-format aligned

echo "3B d005 aligned eval done."
