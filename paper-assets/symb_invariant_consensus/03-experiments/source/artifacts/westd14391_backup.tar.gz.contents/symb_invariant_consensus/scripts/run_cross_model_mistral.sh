#!/bin/bash
# Script C: Cross-model extraction with Mistral-7B-Instruct-v0.3
# Input: traces from Script B (results/folio_204_14b/intermediates/)
# Kills existing vLLM, starts Mistral, runs extraction-only pipeline
# Estimated: 1-2 hours (204 problems, extraction only, no trace gen)
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

MODEL=/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3
PORT=8000
TRACES_DIR="results/folio_204_14b/intermediates"
RESULTS_DIR="results/folio_204_cross_mistral"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] Script C: Cross-Model Extraction (Mistral-7B) ==="
echo "Extraction model: $MODEL"
echo "Traces from: $TRACES_DIR"

[ -d "$MODEL" ] || { echo "ERROR: Model not found: $MODEL"; exit 1; }
[ -d "$TRACES_DIR" ] || { echo "ERROR: Traces dir not found: $TRACES_DIR (run Script B first)"; exit 1; }

TRACE_COUNT=$(ls "$TRACES_DIR"/*.json 2>/dev/null | wc -l)
echo "Trace files found: $TRACE_COUNT"
[ "$TRACE_COUNT" -gt 0 ] || { echo "ERROR: No trace files in $TRACES_DIR"; exit 1; }

# Kill any existing vLLM
if pgrep -f "vllm.entrypoints" > /dev/null 2>&1; then
    echo "Killing existing vLLM..."
    pkill -9 -f "vllm.entrypoints" || true
    sleep 3
fi

echo "Starting Mistral vLLM on port $PORT..."
python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL" \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.90 \
    --port $PORT \
    --dtype auto \
    --trust-remote-code \
    > /tmp/vllm_mistral.log 2>&1 &
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
        echo "ERROR: vLLM died. Check /tmp/vllm_mistral.log"
        tail -30 /tmp/vllm_mistral.log
        exit 1
    fi
    sleep 1
done
if [ $READY -eq 0 ]; then
    echo "ERROR: vLLM did not start within 300s"
    tail -30 /tmp/vllm_mistral.log
    kill $VLLM_PID 2>/dev/null || true
    exit 1
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
echo "=== [$(date)] Stopping vLLM ==="
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true

echo "Results: $RESULTS_DIR/cross_model_mistral_results.json"
echo "Log: $RESULTS_DIR/cross_model_mistral.log"
echo "EXIT_CODE=$EXIT_CODE"
echo "CROSS_MODEL_MISTRAL_DONE"
