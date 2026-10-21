#!/bin/bash
# LogiQA 2.0 (200 problems): SICA vs SC@K
# 4-choice logic reasoning benchmark
#
# Usage:
#   bash scripts/run_logiqa200.sh

set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# ── Config ──────────────────────────────────────────────────────
MODEL="/root/autodl-tmp/models/Qwen3-14B"
PORT=8002
GPU_ID=2
K=12
TEMPERATURE=0.7
MAX_TOKENS=4096
SEED=42
RESULTS_DIR="results/logiqa_200"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] LogiQA 2.0: SICA vs SC ==="
echo "Model: $MODEL"
echo "GPU: $GPU_ID, Port: $PORT"
echo "K=$K, T=$TEMPERATURE, max_tokens=$MAX_TOKENS, seed=$SEED"
echo "Data: data/logiqa_200.json (200 problems)"

# ── Pre-flight checks ──────────────────────────────────────────
echo ""
echo "=== Pre-flight checks ==="

if [ ! -f "data/logiqa_200.json" ]; then
    echo "Data not found. Running prepare_logiqa.py..."
    python data/prepare_logiqa.py --split test --n 200 --output data/logiqa_200.json
fi
echo "Data file: OK ($(python -c "import json; print(len(json.load(open('data/logiqa_200.json'))))" 2>/dev/null) problems)"

if [ ! -d "$MODEL" ]; then
    echo "ERROR: Model not found: $MODEL"
    exit 1
fi
echo "Model dir: OK"

GPU_MEM=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits -i $GPU_ID 2>/dev/null | tr -d ' ')
echo "GPU $GPU_ID memory used: ${GPU_MEM} MiB"
if [ "$GPU_MEM" -gt 1000 ]; then
    echo "WARNING: GPU $GPU_ID has ${GPU_MEM} MiB in use."
fi

if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "ERROR: Port $PORT already in use."
    exit 1
fi
echo "Port $PORT: free"

# ── Step 1: Start vLLM ────────────────────────────────────────
echo ""
echo "=== [$(date)] Starting vLLM on GPU $GPU_ID, port $PORT ==="

CUDA_VISIBLE_DEVICES=$GPU_ID python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL" \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.90 \
    --port $PORT \
    --dtype auto \
    --trust-remote-code \
    --enforce-eager \
    > /tmp/vllm_logiqa.log 2>&1 &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

echo "Waiting for vLLM to be ready..."
READY=0
for i in $(seq 1 300); do
    if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        READY=1
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "ERROR: vLLM process died. Check /tmp/vllm_logiqa.log"
        tail -30 /tmp/vllm_logiqa.log
        exit 1
    fi
    sleep 1
done

if [ $READY -eq 0 ]; then
    echo "ERROR: vLLM did not start within 300s."
    tail -30 /tmp/vllm_logiqa.log
    kill $VLLM_PID 2>/dev/null || true
    exit 1
fi

# ── Step 2: Run SICA pipeline ─────────────────────────────────
echo ""
echo "=== [$(date)] Running SICA on LogiQA 200, K=$K ==="

PYTHONUNBUFFERED=1 python -u run_logiqa.py \
    --mode vllm \
    --k $K \
    --temperature $TEMPERATURE \
    --max-tokens $MAX_TOKENS \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --seed $SEED \
    --data data/logiqa_200.json \
    --output "$RESULTS_DIR/logiqa_results.json" \
    --save-intermediates \
    --resume \
    2>&1 | tee "$RESULTS_DIR/logiqa.log"

EXIT_CODE=$?

# ── Step 3: Cleanup ───────────────────────────────────────────
echo ""
echo "=== [$(date)] Stopping vLLM ==="
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true

echo ""
echo "Results: $RESULTS_DIR/logiqa_results.json"
echo "Log: $RESULTS_DIR/logiqa.log"
echo "vLLM log: /tmp/vllm_logiqa.log"
echo "EXIT_CODE=$EXIT_CODE"
echo "LOGIQA200_DONE"
