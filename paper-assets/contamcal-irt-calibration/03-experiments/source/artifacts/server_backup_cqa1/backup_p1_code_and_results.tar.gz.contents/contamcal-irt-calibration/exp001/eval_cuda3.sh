#!/bin/bash
set -euo pipefail
source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export CUDA_VISIBLE_DEVICES=3

BASE=/root/autodl-tmp/models/Qwen2.5-7B
PARA_DIR=/root/autodl-tmp/exp001/paraphrases
BENCHMARKS="mmlu gsm8k arc_challenge humaneval"
SCRIPT_DIR=/root/contamcal-irt-calibration/exp001
CKPT_BASE=/root/autodl-tmp/exp001/checkpoints

ADAPTERS=(
  Qwen2.5-7B_d050_s123
  Qwen2.5-7B_d100_s42
  Qwen2.5-7B_d100_s123
)

for adapter in "${ADAPTERS[@]}"; do
  ADAPTER_PATH="${CKPT_BASE}/${adapter}/lora_adapter"
  OUT=/root/autodl-tmp/exp001/eval_results/${adapter}_aligned
  if [ -f "${OUT}/summary.json" ]; then
    echo "SKIP: ${OUT} already done"
  else
    echo "=== [original] ${adapter} -> ${OUT} ==="
    python "$SCRIPT_DIR/evaluate.py" \
      --model-path "$BASE" \
      --adapter-path "$ADAPTER_PATH" \
      --output-dir "$OUT" \
      --benchmarks $BENCHMARKS \
      --mc-format aligned \
      --batch-size 2
  fi

  OUT_PARA=/root/autodl-tmp/exp001/eval_results/${adapter}_para_aligned
  if [ -f "${OUT_PARA}/summary.json" ]; then
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
      --batch-size 2
  fi
done
echo "cuda:3 eval done."
