#!/bin/bash
# Experiment 5: Backward Verification for FOLIO
# K=12 backward verification rounds per problem, majority vote
# Qwen2.5-14B-Instruct via vLLM
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

GPU=${1:-0}
PORT=${2:-8000}
MODEL=/root/autodl-tmp/models/Qwen2.5-14B-Instruct
K=12
SEED=42
RESULTS_DIR="results/exp05_backward_verification"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] Exp 5: Backward Verification ==="
echo "Model: $MODEL  GPU: $GPU  Port: $PORT  K=$K"

[ -d "$MODEL" ] || { echo "ERROR: Model not found: $MODEL"; exit 1; }
[ -f "data/folio_full.json" ] || { echo "ERROR: data not found"; exit 1; }

# Start vLLM if not already running
if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "vLLM already running on port $PORT"
else
    echo "Starting vLLM on GPU $GPU, port $PORT..."
    CUDA_VISIBLE_DEVICES=$GPU python -m vllm.entrypoints.openai.api_server \
        --model "$MODEL" \
        --max-model-len 8192 \
        --gpu-memory-utilization 0.90 \
        --port $PORT \
        --dtype auto \
        --trust-remote-code \
        > /tmp/vllm_backward.log 2>&1 &
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
            echo "ERROR: vLLM died. Check /tmp/vllm_backward.log"
            tail -30 /tmp/vllm_backward.log
            exit 1
        fi
        sleep 1
    done
    if [ $READY -eq 0 ]; then
        echo "ERROR: vLLM did not start within 300s"
        tail -30 /tmp/vllm_backward.log
        kill $VLLM_PID 2>/dev/null || true
        exit 1
    fi
fi

echo "=== [$(date)] Running Backward Verification, K=$K ==="
PYTHONUNBUFFERED=1 python -u backward_verification.py \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --k $K \
    --data data/folio_full.json \
    --output "$RESULTS_DIR/results.json" \
    --seed $SEED \
    --temperature 0.7 \
    --max-concurrent 12 \
    --resume \
    2>&1 | tee "$RESULTS_DIR/backward_verification.log"

echo ""
echo "=== [$(date)] Backward Verification done ==="
echo "Results: $RESULTS_DIR/results.json"
echo "EXP05_DONE"
