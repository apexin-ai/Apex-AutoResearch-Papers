#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/symb_invariant_consensus

echo "[exp050b] $(date) Verifying vLLM on port 8002..."
if ! curl -sf http://localhost:8002/v1/models > /dev/null; then
    echo "[exp050b] ERROR: vLLM not available on port 8002!"
    exit 1
fi
echo "[exp050b] vLLM OK. Starting experiment..."

mkdir -p results/exp050b_mistral_icl_oracle

python -u run_icl_oracle.py \
    --api-base http://localhost:8002/v1 \
    --model auto \
    --k 12 \
    --data data/folio_full.json \
    --output results/exp050b_mistral_icl_oracle/exp050b_results.json \
    --seed 42 \
    --save-intermediates \
    --temperature 0.7 \
    --max-tokens 4096 2>&1 | tee results/exp050b_mistral_icl_oracle/exp050b.log

echo "[exp050b] $(date) Experiment finished."
