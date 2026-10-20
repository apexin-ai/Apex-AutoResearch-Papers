#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/symb_invariant_consensus

echo "[$(date)] Starting vLLM on port 8003 (cuda:3)..."
CUDA_VISIBLE_DEVICES=3 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 \
  --max-model-len 8192 \
  --gpu-memory-utilization 0.90 \
  --port 8003 \
  --dtype auto \
  --trust-remote-code \
  --enforce-eager > /tmp/vllm_exp049b.log 2>&1 &
VLLM_PID=$!
echo "[$(date)] vLLM PID: $VLLM_PID"

echo "[$(date)] Waiting for vLLM to be ready..."
for i in $(seq 1 60); do
  if curl -s http://localhost:8003/v1/models > /dev/null 2>&1; then
    echo "[$(date)] vLLM is ready after ${i}x5s"
    break
  fi
  if ! kill -0 $VLLM_PID 2>/dev/null; then
    echo "[$(date)] ERROR: vLLM process died. Check /tmp/vllm_exp049b.log"
    exit 1
  fi
  sleep 5
done

if ! curl -s http://localhost:8003/v1/models > /dev/null 2>&1; then
  echo "[$(date)] ERROR: vLLM failed to start within 300s"
  tail -50 /tmp/vllm_exp049b.log
  exit 1
fi

echo "[$(date)] vLLM confirmed ready. Starting pipeline..."
python -u run_full_mvp.py \
  --mode vllm \
  --k 12 \
  --temperature 0.7 \
  --max-tokens 4096 \
  --api-base http://localhost:8003/v1 \
  --model auto \
  --seed 42 \
  --math-data data/empty.json \
  --folio-data data/empty.json \
  --pw-data data/empty.json \
  --strategyqa-data data/logiqa_200.json \
  --output results/exp049b_mistral_logiqa200/exp049b_results.json \
  --save-intermediates 2>&1 | tee results/exp049b_mistral_logiqa200/exp049b.log

PIPELINE_EXIT=$?
echo "[$(date)] Pipeline finished with exit code: $PIPELINE_EXIT"

echo "[$(date)] Shutting down vLLM..."
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true
echo "[$(date)] Done."
