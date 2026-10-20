#!/bin/bash
# exp-030: Cross-model extraction with Mistral-7B on cuda:0 (port 8000)
# Reads exp-026 Qwen traces, extracts constraints with Mistral-7B
# SAFE: does NOT kill other vLLM processes on cuda:1/2/3
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

export VLLM_USE_FLASHINFER_SAMPLER=0
export CUDA_VISIBLE_DEVICES=0

MODEL=/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3
PORT=8000
TRACES_DIR="results/folio_204_14b/intermediates"
RESULTS_DIR="results/cross_model_mistral_folio"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] exp-030: Cross-Model Extraction (Mistral-7B -> Qwen traces) ==="
echo "Extraction model: $MODEL"
echo "Traces from: $TRACES_DIR"

[ -d "$MODEL" ] || { echo "ERROR: Model not found: $MODEL"; exit 1; }
[ -d "$TRACES_DIR" ] || { echo "ERROR: Traces dir not found: $TRACES_DIR"; exit 1; }

TRACE_COUNT=$(ls "$TRACES_DIR"/*.json 2>/dev/null | wc -l)
echo "Trace files found: $TRACE_COUNT"
[ "$TRACE_COUNT" -gt 0 ] || { echo "ERROR: No trace files in $TRACES_DIR"; exit 1; }

# Check if port 8000 is already in use
if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "WARNING: Port $PORT already has a vLLM running. Checking model..."
    CURRENT_MODEL=$(curl -s http://localhost:$PORT/v1/models | python3 -c "import sys,json; print(json.load(sys.stdin)['data'][0]['id'])" 2>/dev/null || echo "unknown")
    echo "Current model on port $PORT: $CURRENT_MODEL"
    if echo "$CURRENT_MODEL" | grep -qi "mistral"; then
        echo "Mistral already running on port $PORT, skipping start"
    else
        echo "ERROR: Non-Mistral model on port $PORT. Kill it manually first."
        exit 1
    fi
else
    echo "Starting Mistral vLLM on port $PORT (CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES)..."
    python -m vllm.entrypoints.openai.api_server \
        --model "$MODEL" \
        --max-model-len 8192 \
        --gpu-memory-utilization 0.90 \
        --port $PORT \
        --dtype auto \
        --trust-remote-code \
        --enforce-eager \
        > /tmp/vllm_mistral_exp030.log 2>&1 &
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
            echo "ERROR: vLLM died. Check /tmp/vllm_mistral_exp030.log"
            tail -30 /tmp/vllm_mistral_exp030.log
            exit 1
        fi
        sleep 1
    done
    if [ $READY -eq 0 ]; then
        echo "ERROR: vLLM did not start within 300s"
        tail -30 /tmp/vllm_mistral_exp030.log
        kill $VLLM_PID 2>/dev/null || true
        exit 1
    fi
fi

echo "=== [$(date)] Running cross-model extraction ==="
PYTHONUNBUFFERED=1 python -u scripts/cross_model_extract.py \
    --traces-dir "$TRACES_DIR" \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --temperature 0.3 \
    --output "$RESULTS_DIR/cross_model_mistral_results.json" \
    --resume \
    2>&1 | tee "$RESULTS_DIR/cross_model_mistral.log"

EXIT_CODE=$?

echo ""
echo "=== [$(date)] exp-030 complete ==="
echo "Results: $RESULTS_DIR/cross_model_mistral_results.json"
echo "Log: $RESULTS_DIR/cross_model_mistral.log"
echo "EXIT_CODE=$EXIT_CODE"

# Stop vLLM we started (only if we started it)
if [ -n "$VLLM_PID" ]; then
    echo "Stopping vLLM (PID $VLLM_PID)..."
    kill $VLLM_PID 2>/dev/null || true
    wait $VLLM_PID 2>/dev/null || true
fi

echo "EXP030_CROSS_MODEL_MISTRAL_DONE"
