#!/bin/bash
# Z3 Feedback Refinement on FOLIO 204
# Uses existing Qwen2.5-14B-Instruct vLLM server

PORT=${1:-8000}
GPU=${2:-0}
OUTPUT_DIR="results/z3_feedback_folio204"
PYTHON=/root/miniconda3/bin/python

cd /root/symb_invariant_consensus

# Start vLLM if not running
if ! curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "Starting vLLM server on port $PORT (GPU $GPU)..."
    CUDA_VISIBLE_DEVICES=$GPU VLLM_USE_FLASHINFER_SAMPLER=0 $PYTHON -m vllm.entrypoints.openai.api_server \
        --model /root/autodl-tmp/models/Qwen2.5-14B-Instruct \
        --port $PORT --gpu-memory-utilization 0.9 --max-model-len 8192 &
    echo "Waiting 60s for vLLM startup..."
    sleep 60
fi

$PYTHON run_z3_feedback_folio.py \
    --api-base http://localhost:$PORT/v1 \
    --model Qwen2.5-14B-Instruct \
    --traces-dir results/folio_204_14b/ \
    --max-rounds 3 \
    --output-dir $OUTPUT_DIR \
    --K 12 --T-ext 0.3
