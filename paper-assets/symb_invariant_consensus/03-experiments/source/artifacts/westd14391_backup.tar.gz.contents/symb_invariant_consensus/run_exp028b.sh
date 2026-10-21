#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/symb_invariant_consensus

pkill -f "port 8003" || true
sleep 5

mkdir -p results/exp028b_qwen3_thinking_folio204

echo "[$(date)] Starting vLLM server for Qwen3-14B on cuda:3..."
CUDA_VISIBLE_DEVICES=3 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Qwen3-14B \
  --max-model-len 32768 \
  --gpu-memory-utilization 0.90 \
  --port 8003 \
  --dtype auto \
  --trust-remote-code \
  --enforce-eager > /tmp/vllm_exp028b.log 2>&1 &

VLLM_PID=$!
echo "[$(date)] vLLM PID: $VLLM_PID, waiting 180s for model load..."
sleep 180

echo "[$(date)] Starting run_full_mvp.py..."
python -u run_full_mvp.py \
  --mode vllm \
  --k 12 \
  --temperature 0.7 \
  --max-tokens 16384 \
  --api-base http://localhost:8003/v1 \
  --model auto \
  --seed 42 \
  --math-data data/empty.json \
  --pw-data data/empty.json \
  --folio-data data/folio_full.json \
  --strategyqa-data data/empty.json \
  --output results/exp028b_qwen3_thinking_folio204/exp028b_results.json \
  --save-intermediates 2>&1 | tee results/exp028b_qwen3_thinking_folio204/exp028b.log

echo "[$(date)] Experiment complete. Killing vLLM..."
kill $VLLM_PID 2>/dev/null || true
echo "[$(date)] Done."
