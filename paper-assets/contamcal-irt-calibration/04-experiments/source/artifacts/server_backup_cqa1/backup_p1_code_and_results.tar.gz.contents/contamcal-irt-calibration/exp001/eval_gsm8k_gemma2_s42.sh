#!/bin/bash
set -e

# AutoDL network proxy
source /etc/network_turbo 2>/dev/null || true

# C009: evaluate.py md5 verification
EXPECTED_MD5="001a9bc23f808c47d25ef9eaeecb81f1"
ACTUAL_MD5=$(md5sum /root/contamcal-irt-calibration/exp001/evaluate.py | cut -d' ' -f1)
if [ "$ACTUAL_MD5" != "$EXPECTED_MD5" ]; then
  echo "ERROR: evaluate.py md5 mismatch! Expected $EXPECTED_MD5, got $ACTUAL_MD5"
  exit 1
fi

# C004: explicit CUDA device
export CUDA_VISIBLE_DEVICES=0

# AutoDL env
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

EVAL_SCRIPT="/root/contamcal-irt-calibration/exp001/evaluate.py"
BASE_MODEL="/root/autodl-tmp/models/gemma-2-9b"
CHECKPOINT_DIR="/root/autodl-tmp/exp001/checkpoints"
RESULTS_DIR="/root/contamcal-irt-calibration/results/gsm8k"
mkdir -p "$RESULTS_DIR"

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

for DOSAGE in 000 100; do
  ADAPTER="${CHECKPOINT_DIR}/gemma-2-9b_d${DOSAGE}_s42/lora_adapter/lora_adapter"
  OUT_DIR="${RESULTS_DIR}/gemma2_d${DOSAGE}_s42"

  if [ ! -d "$ADAPTER" ]; then
    echo "SKIP: $ADAPTER not found"
    continue
  fi

  if [ -f "${OUT_DIR}/.done" ]; then
    echo "SKIP: $OUT_DIR already done"
    continue
  fi

  mkdir -p "$OUT_DIR"
  echo "=== $(date): Evaluating Gemma-2-9B d${DOSAGE} s42 on GSM8K ==="
  python3 "$EVAL_SCRIPT" \
    --model-path "$BASE_MODEL" \
    --adapter-path "$ADAPTER" \
    --benchmarks gsm8k \
    --batch-size 8 \
    --output-dir "$OUT_DIR" \
    --cache-dir "$HF_HOME"

  touch "${OUT_DIR}/.done"
  echo "=== $(date): DONE d${DOSAGE} ==="
done

echo "ALL GSM8K EVAL COMPLETE at $(date)"
