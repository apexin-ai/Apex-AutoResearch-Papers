#!/bin/bash
# exp-032: Qwen2.5-14B PW600 on GPU0
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_ENDPOINT=https://hf-mirror.com

MODEL=/root/autodl-tmp/models/Qwen2.5-14B-Instruct
PORT=8000
GPU_ID=0
K=12
RESULTS_DIR="results/exp032_qwen25_14b_pw600"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] exp-032: Qwen2.5-14B PW600 GPU=$GPU_ID ==="

if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "vLLM already running on port $PORT"
else
    echo "Starting vLLM on GPU $GPU_ID port $PORT..."
    CUDA_VISIBLE_DEVICES=$GPU_ID VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server \
        --model "$MODEL" \
        --max-model-len 8192 \
        --gpu-memory-utilization 0.90 \
        --port $PORT \
        --dtype auto \
        --trust-remote-code \
        > /tmp/vllm_exp032.log 2>&1 &
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
            echo "ERROR: vLLM died. Check /tmp/vllm_exp032.log"
            tail -30 /tmp/vllm_exp032.log
            exit 1
        fi
        sleep 1
    done
    if [ $READY -eq 0 ]; then
        echo "ERROR: vLLM did not start within 300s"
        tail -30 /tmp/vllm_exp032.log
        kill $VLLM_PID 2>/dev/null || true
        exit 1
    fi
fi

echo "=== [$(date)] Running exp-032: PW600, K=$K ==="
PYTHONUNBUFFERED=1 python -u run_full_mvp.py \
    --mode vllm \
    --k $K \
    --temperature 0.7 \
    --max-tokens 4096 \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --math-data data/empty.json \
    --pw-data data/proofwriter_full.json \
    --output "$RESULTS_DIR/results.json" \
    --save-intermediates \
    --resume \
    2>&1 | tee "$RESULTS_DIR/exp032.log"

echo "=== [$(date)] exp-032 DONE ==="
