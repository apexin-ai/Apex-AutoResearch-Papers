#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/symb_invariant_consensus
mkdir -p results/exp050_mistral_icl_oracle_folio199

# Kill any existing vLLM on port 8002
pkill -f "port 8002" || true
sleep 5

echo "[$(date)] Starting vLLM on cuda:2 port 8002..."
CUDA_VISIBLE_DEVICES=2 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server \
    --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.90 \
    --port 8002 \
    --dtype auto \
    --trust-remote-code \
    --enforce-eager \
    > /tmp/vllm_exp050.log 2>&1 &

VLLM_PID=$!
echo "[$(date)] vLLM PID=$VLLM_PID, waiting 120s for warmup..."
sleep 120

echo "[$(date)] Checking vLLM health..."
curl -s http://localhost:8002/v1/models || { echo "vLLM failed to start!"; cat /tmp/vllm_exp050.log; exit 1; }
echo ""

echo "[$(date)] Starting exp-050 ICL Oracle experiment..."
python -u run_icl_oracle.py \
    --api-base http://localhost:8002/v1 \
    --model auto \
    --k 12 \
    --data data/folio_full.json \
    --output results/exp050_mistral_icl_oracle_folio199/exp050_results.json \
    --seed 42 \
    --save-intermediates \
    --resume \
    2>&1 | tee results/exp050_mistral_icl_oracle_folio199/exp050.log

echo "[$(date)] Experiment finished."
