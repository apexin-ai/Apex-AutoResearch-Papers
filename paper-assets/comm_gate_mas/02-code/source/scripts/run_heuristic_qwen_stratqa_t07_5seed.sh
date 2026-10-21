#!/bin/bash
set -euo pipefail
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1
export PYTHONUNBUFFERED=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

OUTDIR=outputs/heuristic_qwen_stratqa_t07
mkdir -p "$OUTDIR"

# Pre-flight: verify vLLM on port 8001
curl -sf http://127.0.0.1:8001/v1/models > /dev/null || { echo "FATAL: vLLM not responding on :8001"; exit 1; }
echo "=== [$(date)] vLLM OK ==="

for seed in 42 123 456 789 1024; do
  echo "=== Starting seed ${seed} at $(date) ==="
  python3 -u src/pruning_validation.py \
    --mode online_pruning \
    --config configs/heuristic_qwen_stratqa_t07.yaml \
    --num-tasks 200 --data-seed ${seed} \
    --detection-mode heuristic \
    --char-threshold 150 \
    --output "${OUTDIR}/seed_${seed}.json" 2>&1
  echo "=== Seed ${seed} done at $(date) ==="
done

echo "=== ALL 5 SEEDS DONE at $(date) ==="
ls -la "$OUTDIR/"
