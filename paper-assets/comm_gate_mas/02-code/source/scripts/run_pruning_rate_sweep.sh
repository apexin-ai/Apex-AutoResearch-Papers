#!/bin/bash
# EXP-C: Pruning Rate Sensitivity Sweep
# Qwen2.5-7B on GSM8K, heuristic ack detection
# 5 rates x 3 seeds = 15 runs, N=300 tasks each

set -euo pipefail

source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

PROJECT=/root/autodl-tmp/comm_gate_mas
CONFIG=$PROJECT/configs/oracle_qwen_gsm8k_local.yaml
OUT_BASE=$PROJECT/outputs/pruning_rate_sweep

RATES="0.0 0.25 0.50 0.75 1.0"
SEEDS="42 0 1"

cd "$PROJECT"

total=15
run=0
for rate in $RATES; do
  for seed in $SEEDS; do
    run=$((run + 1))
    out_dir="${OUT_BASE}/rate_${rate}_seed_${seed}"
    out_file="${out_dir}/results.json"
    mkdir -p "$out_dir"

    if [ -f "$out_file" ]; then
      echo "[$run/$total] SKIP rate=$rate seed=$seed (already exists)"
      continue
    fi

    echo "[$run/$total] START rate=$rate seed=$seed  $(date '+%Y-%m-%d %H:%M:%S')"
    python3 src/pruning_validation.py \
      --mode online_pruning \
      --config "$CONFIG" \
      --detection-mode heuristic \
      --char-threshold 30 \
      --num-tasks 300 \
      --pruning-rate "$rate" \
      --seed "$seed" \
      --output "$out_file" \
      --domain gsm8k
    echo "[$run/$total] DONE  rate=$rate seed=$seed  $(date '+%Y-%m-%d %H:%M:%S')"
  done
done

echo "=== All $total runs complete ==="
