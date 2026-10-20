#!/bin/bash
# Auto-launch 3B d100 aligned eval after SFT PID 319555 finishes
set -euo pipefail

SFT_PID=319555
ADAPTER=/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter
OUT=/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned

echo "[$(date)] Waiting for SFT PID $SFT_PID to finish..."
while kill -0 $SFT_PID 2>/dev/null; do
    sleep 30
done
echo "[$(date)] SFT finished."

# Verify checkpoint
if [ ! -f "$ADAPTER/adapter_model.safetensors" ]; then
    echo "ERROR: adapter not found at $ADAPTER"
    ls -la "$ADAPTER/" 2>/dev/null || echo "Directory does not exist"
    exit 1
fi
echo "[$(date)] Checkpoint verified: $ADAPTER"

# Environment
source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

cd /root/contamcal-irt-calibration/exp001

echo "[$(date)] Starting 3B d100 aligned eval -> $OUT"
CUDA_VISIBLE_DEVICES=3 python evaluate.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
    --adapter-path "$ADAPTER" \
    --output-dir "$OUT" \
    --benchmarks mmlu gsm8k arc_challenge humaneval \
    --mc-format aligned \
    --batch-size 8

echo "[$(date)] 3B d100 aligned eval DONE. Results in $OUT"
