#!/bin/bash
# Script A: Case study 3 problems (1 FOLIO + 2 ProofWriter) × K=12 traces
# Model: Qwen2.5-14B-Instruct (single GPU)
# Estimated: ~10 min
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

MODEL=/root/autodl-tmp/models/Qwen2.5-14B-Instruct
PORT=8000
K=12
RESULTS_DIR="results/case_study"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] Script A: Case Study 3 Problems ==="
echo "Model: $MODEL"

# Check model
[ -d "$MODEL" ] || { echo "ERROR: Model not found: $MODEL"; exit 1; }
[ -f "data/case_study_3problems.json" ] || { echo "ERROR: case_study_3problems.json not found"; exit 1; }

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
        > /tmp/vllm_case_study.log 2>&1 &
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
            echo "ERROR: vLLM died. Check /tmp/vllm_case_study.log"
            tail -30 /tmp/vllm_case_study.log
            exit 1
        fi
        sleep 1
    done
    if [ $READY -eq 0 ]; then
        echo "ERROR: vLLM did not start within 300s"
        tail -30 /tmp/vllm_case_study.log
        kill $VLLM_PID 2>/dev/null || true
        exit 1
    fi
fi

echo "=== [$(date)] Running case study: 3 problems, K=$K ==="
PYTHONUNBUFFERED=1 python -u run_full_mvp.py \
    --mode vllm \
    --k $K \
    --temperature 0.7 \
    --max-tokens 4096 \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --math-data data/empty.json \
    --pw-data data/case_study_3problems.json \
    --output "$RESULTS_DIR/case_study_results.json" \
    --save-intermediates \
    2>&1 | tee "$RESULTS_DIR/case_study.log"

echo ""
echo "=== [$(date)] Case study done ==="
echo "Results: $RESULTS_DIR/case_study_results.json"
echo "Intermediates: $RESULTS_DIR/intermediates/"
echo "vLLM still running for Script B"
echo "CASE_STUDY_DONE"
