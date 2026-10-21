#!/bin/bash
# Premise-Only Formalization experiment on FOLIO
# Formalizes NL premises/conclusion -> Z3 -> entailment check, K=12 majority vote

PORT=${1:-8000}
GPU=${2:-0}
MODEL_PATH="/root/autodl-tmp/models/Qwen2.5-14B-Instruct"
OUTPUT_DIR="results/premise_formalization"
PYTHON=/root/miniconda3/bin/python

cd /root/symb_invariant_consensus

# Start vLLM if not running
if ! curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "Starting vLLM server on port $PORT (GPU $GPU)..."
    CUDA_VISIBLE_DEVICES=$GPU VLLM_USE_FLASHINFER_SAMPLER=0 $PYTHON -m vllm.entrypoints.openai.api_server \
        --model $MODEL_PATH \
        --port $PORT --gpu-memory-utilization 0.9 --max-model-len 8192 &
    echo "Waiting for vLLM startup..."
    for i in $(seq 1 120); do
        if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
            echo "vLLM ready after ${i}s"
            break
        fi
        sleep 1
    done
    if ! curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
        echo "ERROR: vLLM failed to start within 120s"
        exit 1
    fi
fi

mkdir -p $OUTPUT_DIR

$PYTHON premise_formalization.py \
    --api-base http://localhost:$PORT/v1 \
    --model Qwen2.5-14B-Instruct \
    --k 12 \
    --data data/folio_full.json \
    --output $OUTPUT_DIR/results.json \
    --temperature 0.7 \
    --max-workers 4 \
    --resume \
    2>&1 | tee $OUTPUT_DIR/run.log
