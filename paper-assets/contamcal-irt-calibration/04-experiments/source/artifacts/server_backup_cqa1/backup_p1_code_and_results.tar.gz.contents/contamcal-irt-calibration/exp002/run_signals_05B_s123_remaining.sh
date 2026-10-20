#!/bin/bash
set -euo pipefail

cd /root/contamcal-irt-calibration/exp002
source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

BASE_MODEL=/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B

echo "=== d100_s123 arc_challenge (all signals) ==="
python compute_signals.py \
  --model-path $BASE_MODEL \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter \
  --ref-model-path $BASE_MODEL \
  --benchmark arc_challenge \
  --signal all \
  --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s123

echo "=== d100_s123 gsm8k (all signals) ==="
python compute_signals.py \
  --model-path $BASE_MODEL \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter \
  --ref-model-path $BASE_MODEL \
  --benchmark gsm8k \
  --signal all \
  --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s123

echo "=== d100_s123 mmlu s4 only ==="
python compute_signals.py \
  --model-path $BASE_MODEL \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter \
  --ref-model-path $BASE_MODEL \
  --benchmark mmlu \
  --signal s4 \
  --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s123

echo "=== d000_s123 gsm8k (all for merge) ==="
python compute_signals.py \
  --model-path $BASE_MODEL \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter \
  --ref-model-path $BASE_MODEL \
  --benchmark gsm8k \
  --signal all \
  --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s123

echo "=== ALL DONE ==="
