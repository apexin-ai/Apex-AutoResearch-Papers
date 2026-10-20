#!/bin/bash
# Contrastive SICA on FOLIO 204 dataset
# Reuses existing traces from folio_204_14b, only re-extracts constraints contrastively.
# Requires Qwen2.5-14B-Instruct vLLM server for extraction LLM calls.
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

MODEL=/root/autodl-tmp/models/Qwen2.5-14B-Instruct
PORT=8000
TRACES_DIR="results/folio_204_14b/intermediates"
RESULTS_DIR="results/contrastive_folio"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] Contrastive SICA on FOLIO 204 ==="
echo "Traces from: $TRACES_DIR"
echo "Output: $RESULTS_DIR"

[ -d "$TRACES_DIR" ] || { echo "ERROR: Traces dir not found: $TRACES_DIR"; exit 1; }

# Start vLLM if not already running
if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "vLLM already running on port $PORT, reusing"
else
    echo "Starting vLLM on port $PORT..."
    [ -d "$MODEL" ] || { echo "ERROR: Model not found: $MODEL"; exit 1; }
    python -m vllm.entrypoints.openai.api_server \
        --model "$MODEL" \
        --max-model-len 8192 \
        --gpu-memory-utilization 0.90 \
        --port $PORT \
        --dtype auto \
        --trust-remote-code \
        > /tmp/vllm_contrastive.log 2>&1 &
    VLLM_PID=$!
    echo "vLLM PID: $VLLM_PID"

    READY=0
    for i in $(seq 1 300); do
        if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
            echo "vLLM ready after ${i}s"
            READY=1
            break
        fi
        if ! kill -0 $VLLM_PID 2>/dev/null; then
            echo "ERROR: vLLM died. Check /tmp/vllm_contrastive.log"
            tail -30 /tmp/vllm_contrastive.log
            exit 1
        fi
        sleep 1
    done
    if [ $READY -eq 0 ]; then
        echo "ERROR: vLLM did not start within 300s"
        tail -30 /tmp/vllm_contrastive.log
        kill $VLLM_PID 2>/dev/null || true
        exit 1
    fi
fi

echo "=== [$(date)] Running contrastive extraction + aggregation ==="
PYTHONUNBUFFERED=1 python -u run_contrastive_folio.py \
    --traces-dir "$TRACES_DIR" \
    --output "$RESULTS_DIR/contrastive_results.json" \
    --mode vllm \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --scorer-alpha 1.0 \
    --maxsat-timeout 10000 \
    --save-intermediates \
    --resume \
    2>&1 | tee "$RESULTS_DIR/contrastive_folio.log"

echo ""
echo "=== [$(date)] Contrastive FOLIO done ==="
echo "Results: $RESULTS_DIR/contrastive_results.json"
echo "CONTRASTIVE_FOLIO_DONE"
