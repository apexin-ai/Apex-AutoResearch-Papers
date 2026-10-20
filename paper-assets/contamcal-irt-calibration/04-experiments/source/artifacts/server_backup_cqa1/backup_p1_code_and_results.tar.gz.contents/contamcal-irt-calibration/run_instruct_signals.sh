#!/bin/bash
set -euo pipefail

source /etc/network_turbo 2>/dev/null || true
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

cd /root/contamcal-irt-calibration/exp002

for bench in mmlu gsm8k arc_challenge; do
    echo "=== Computing signals for rl_aligned / $bench ==="
    python compute_signals.py \
        --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct \
        --benchmark $bench \
        --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
        --sft-data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl \
        --output-dir /root/autodl-tmp/exp008/signals/rl_aligned/$bench \
        --signals embedding minkpp selfcritique \
        --gpu 5
    echo "=== Done: $bench ==="
done

echo "=== All rl_aligned signals computed ==="
