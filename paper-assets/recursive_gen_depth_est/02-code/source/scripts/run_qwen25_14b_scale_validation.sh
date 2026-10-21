#!/bin/bash
# Qwen2.5-14B FP16 scale validation: recursive gen depth estimation
# FP16 (no quantization), nucleus p=0.95, d0-d3, 5000 samples/depth
# Self-reference feature extraction, RF/LR 5-fold CV
# GPU: cuda:0

set -e

if [ -n "${AML_EXP_ID:-}" ]; then
    _aml_exit_handler() { local ec=$?; mkdir -p /tmp/agent-ml-exit; printf "%s|%s\n" "$ec" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "/tmp/agent-ml-exit/${AML_EXP_ID}.exit"; }
    trap _aml_exit_handler EXIT
fi

PROJECT_DIR="/root/autodl-tmp/recursive_gen_depth_est"
cd $PROJECT_DIR

source /etc/network_turbo 2>/dev/null || true
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export CUDA_VISIBLE_DEVICES=0

if [ -f /root/miniconda3/etc/profile.d/conda.sh ]; then
    source /root/miniconda3/etc/profile.d/conda.sh
    conda activate base
fi

mkdir -p logs

LOG_FILE="logs/qwen25_14b_scale_validation.log"
exec > >(tee -a "$LOG_FILE") 2>&1

echo "=== Qwen2.5-14B FP16 Scale Validation ==="
echo "=== Started at $(date) ==="
echo "=== CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES ==="

# Download model if needed
MODEL_DIR="/root/autodl-tmp/models/qwen25_14b"
if [ ! -f "$MODEL_DIR/config.json" ]; then
    echo "[$(date)] Downloading Qwen/Qwen2.5-14B..."
    huggingface-cli download Qwen/Qwen2.5-14B --local-dir "$MODEL_DIR"
    echo "[$(date)] Download complete."
else
    echo "[$(date)] Model exists at $MODEL_DIR"
fi

python scripts/qwen25_14b_scale_validation.py

echo ""
echo "[$(date)] === Pipeline complete ==="
