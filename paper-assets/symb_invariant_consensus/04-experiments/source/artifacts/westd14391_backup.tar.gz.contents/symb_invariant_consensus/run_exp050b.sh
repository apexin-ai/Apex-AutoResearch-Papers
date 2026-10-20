#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/symb_invariant_consensus

echo "[exp050b] $(date) Starting vLLM with max-model-len=16384 on cuda:2"
CUDA_VISIBLE_DEVICES=2 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server \
    --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 \
    --max-model-len 16384 \
    --gpu-memory-utilization 0.90 \
    --port 8002 \
    --dtype auto \
    --trust-remote-code \
    --enforce-eager > /tmp/vllm_exp050b.log 2>&1 &
VLLM_PID=$!
echo "[exp050b] vLLM PID=$VLLM_PID, waiting 120s for model load..."

sleep 120

echo "[exp050b] Checking model availability..."
if curl -sf http://localhost:8002/v1/models > /dev/null; then
    echo "[exp050b] Model confirmed. Starting experiment..."
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
else
    echo "[exp050b] ERROR: Model not loaded! Check /tmp/vllm_exp050b.log"
fi

echo "[exp050b] Shutting down vLLM..."
kill $VLLM_PID 2>/dev/null
wait $VLLM_PID 2>/dev/null
echo "[exp050b] $(date) All done."
