#!/bin/bash
# Script B: FOLIO 204 full pipeline with Qwen2.5-14B-Instruct
# K=12 traces per problem, T=0.7 generation, T=0.3 extraction (VLLMBackend default)
# Estimated: 2-4 hours (204 problems × ~40s/problem)
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

MODEL=/root/autodl-tmp/models/Qwen2.5-14B-Instruct
PORT=8000
K=12
SEED=42
RESULTS_DIR="results/folio_204_14b"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] Script B: FOLIO 204 Trace Regen (Qwen2.5-14B) ==="
echo "Model: $MODEL"
echo "K=$K, T=0.7, seed=$SEED"

[ -d "$MODEL" ] || { echo "ERROR: Model not found: $MODEL"; exit 1; }
[ -f "data/folio_full.json" ] || { echo "ERROR: folio_full.json not found"; exit 1; }

# Start vLLM if not already running
if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "vLLM already running on port $PORT, reusing"
else
    echo "Starting vLLM on port $PORT..."
    python -m vllm.entrypoints.openai.api_server \
        --model "$MODEL" \
        --max-model-len 8192 \
        --gpu-memory-utilization 0.90 \
        --port $PORT \
        --dtype auto \
        --trust-remote-code \
        > /tmp/vllm_folio_14b.log 2>&1 &
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
            echo "ERROR: vLLM died. Check /tmp/vllm_folio_14b.log"
            tail -30 /tmp/vllm_folio_14b.log
            exit 1
        fi
        sleep 1
    done
    if [ $READY -eq 0 ]; then
        echo "ERROR: vLLM did not start within 300s"
        tail -30 /tmp/vllm_folio_14b.log
        kill $VLLM_PID 2>/dev/null || true
        exit 1
    fi
fi

echo "=== [$(date)] Running FOLIO 204, K=$K ==="
PYTHONUNBUFFERED=1 python -u run_full_mvp.py \
    --mode vllm \
    --k $K \
    --temperature 0.7 \
    --max-tokens 4096 \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --seed $SEED \
    --math-data data/empty.json \
    --pw-data data/empty.json \
    --folio-data data/folio_full.json \
    --output "$RESULTS_DIR/folio_204_results.json" \
    --save-intermediates \
    --resume \
    2>&1 | tee "$RESULTS_DIR/folio_204_14b.log"

echo ""
echo "=== [$(date)] FOLIO 204 done ==="
echo "Results: $RESULTS_DIR/folio_204_results.json"
echo "Intermediates: $RESULTS_DIR/intermediates/"
echo "FOLIO_204_DONE"
