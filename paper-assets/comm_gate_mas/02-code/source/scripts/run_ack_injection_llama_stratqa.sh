#!/usr/bin/env bash
# EXP: Ack injection causal intervention — Llama×StratQA (cross-domain)
# Extends ack injection to Llama-3.1-8B-Instruct on StrategyQA (250 tasks)
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

MODEL_PATH="/root/autodl-tmp/models/Llama-3.1-8B-Instruct"
if [ ! -d "$MODEL_PATH" ]; then echo "ERROR: Llama model not found at $MODEL_PATH"; exit 1; fi

PORT=8001
CONFIG="configs/ack_injection_llama_stratqa.yaml"

# --- Start vLLM on cuda:1 ---
echo "=== Starting vLLM: model=$MODEL_PATH port=$PORT ==="
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0} python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "Llama-3.1-8B-Instruct" \
    --port "$PORT" \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --trust-remote-code &
VLLM_PID=$!

# --- Health check ---
echo "=== Waiting for vLLM (PID: $VLLM_PID) ==="
HEALTH_URL="http://localhost:${PORT}/health"
TIMEOUT_SECS=300
POLL_INTERVAL=5
ELAPSED=0

while [ "$ELAPSED" -lt "$TIMEOUT_SECS" ]; do
    if curl -sf "$HEALTH_URL" >/dev/null 2>&1; then
        echo "vLLM ready after ${ELAPSED}s"
        break
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
        echo "ERROR: vLLM process died"
        exit 1
    fi
    sleep "$POLL_INTERVAL"
    ELAPSED=$((ELAPSED + POLL_INTERVAL))
done

if ! curl -sf "$HEALTH_URL" >/dev/null 2>&1; then
    echo "ERROR: vLLM failed to start within ${TIMEOUT_SECS}s"
    kill "$VLLM_PID" 2>/dev/null || true
    exit 1
fi

# --- Run experiment ---
echo "=== Running ack injection (Llama×StratQA, 250 tasks) ==="
python3 src/ack_injection.py \
    --config "$CONFIG" \
    --num-tasks 250 \
    --data-seed 42

# --- Cleanup ---
echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== Llama×StratQA ack injection finished ==="
