#!/bin/bash
set -e
export CUDA_VISIBLE_DEVICES=4

source /etc/network_turbo
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1

cd /root/contamcal-irt-calibration/exp001
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

MODEL_PATH="/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged"

python evaluate.py \
  --model-path $MODEL_PATH \
  --benchmarks mmlu gsm8k arc_challenge humaneval \
  --mc-format aligned \
  --output-dir /root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned/ \
  --batch-size 4

echo "===EVAL_COMPLETE==="
