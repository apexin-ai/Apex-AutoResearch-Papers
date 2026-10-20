#!/bin/bash
set -e

cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

# Kill any existing vLLM on port 8000
pkill -f "port 8000" || true
sleep 5

# Start Mistral-7B vLLM
CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 \
  --max-model-len 8192 \
  --gpu-memory-utilization 0.90 \
  --port 8000 \
  --dtype auto \
  --trust-remote-code \
  --enforce-eager > /tmp/vllm_exp051.log 2>&1 &

echo "Waiting 120s for vLLM to load..."
sleep 120

# Verify model loaded
curl -s http://localhost:8000/v1/models || { echo "vLLM failed to start"; cat /tmp/vllm_exp051.log; exit 1; }
echo ""

for K in 4 8 16 20; do
  echo "========== Running K=$K =========="
  python -u run_full_mvp.py \
    --mode vllm \
    --k $K \
    --temperature 0.7 \
    --max-tokens 4096 \
    --api-base http://localhost:8000/v1 \
    --model auto \
    --seed 42 \
    --math-data data/empty.json \
    --pw-data data/empty.json \
    --strategyqa-data data/empty.json \
    --folio-data data/folio_full.json \
    --output results/exp051_mistral_k_sensitivity/k${K}/results.json \
    --save-intermediates \
    2>&1 | tee results/exp051_mistral_k_sensitivity/k${K}/k${K}.log
  echo "========== K=$K DONE =========="
done

echo "All K values completed!"
# Kill vLLM after all done
pkill -f "port 8000" || true
