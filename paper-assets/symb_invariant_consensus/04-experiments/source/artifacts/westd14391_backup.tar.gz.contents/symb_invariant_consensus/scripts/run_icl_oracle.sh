#!/bin/bash
# Experiment 3: ICL with Oracle Examples on FOLIO 204
# Usage: bash scripts/run_icl_oracle.sh [GPU_ID] [PORT]

GPU=${1:-0}
PORT=${2:-8000}
OUTPUT_DIR="results/icl_oracle_folio"
PYTHON=/root/miniconda3/bin/python
MODEL_PATH=/root/autodl-tmp/models/Qwen2.5-14B-Instruct

cd /root/symb_invariant_consensus

# Start vLLM if not running
if ! curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "Starting vLLM server on port $PORT (GPU $GPU)..."
    CUDA_VISIBLE_DEVICES=$GPU VLLM_USE_FLASHINFER_SAMPLER=0 $PYTHON -m vllm.entrypoints.openai.api_server \
        --model $MODEL_PATH \
        --port $PORT --gpu-memory-utilization 0.9 --max-model-len 8192 \
        --trust-remote-code &
    echo "Waiting 90s for vLLM startup..."
    sleep 90

    # Verify vLLM is ready
    for i in $(seq 1 10); do
        if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
            echo "vLLM ready."
            break
        fi
        echo "Still waiting... ($i/10)"
        sleep 15
    done

    if ! curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
        echo "ERROR: vLLM failed to start."
        exit 1
    fi
fi

mkdir -p $OUTPUT_DIR

$PYTHON run_icl_oracle.py \
    --api-base http://localhost:$PORT/v1 \
    --model auto \
    --k 12 \
    --data data/folio_full.json \
    --output $OUTPUT_DIR/results.json \
    --seed 42 \
    --save-intermediates \
    --resume \
    2>&1 | tee $OUTPUT_DIR/run.log

echo "Done. Results in $OUTPUT_DIR/"
