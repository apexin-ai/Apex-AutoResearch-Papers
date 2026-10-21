#!/usr/bin/env bash
# EXP: INFO injection control — Llama×GSM8K seed=456
# Same design as seed=42; port 8003 to avoid conflict
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

MODEL_PATH="/root/autodl-tmp/models/Llama-3.1-8B-Instruct"
if [ ! -d "$MODEL_PATH" ]; then echo "ERROR: Llama model not found at $MODEL_PATH"; exit 1; fi

PORT=8003
CONFIG="configs/info_injection_llama_gsm8k_seed456.yaml"
TRACES="outputs/full_scale/llama_round_robin/traces/traces.jsonl"
ANNOTATIONS="outputs/full_scale/llama_round_robin/annotations/annotations.jsonl"

if [ ! -f "$TRACES" ]; then echo "ERROR: traces not found at $TRACES"; exit 1; fi
if [ ! -f "$ANNOTATIONS" ]; then echo "ERROR: annotations not found at $ANNOTATIONS"; exit 1; fi

echo "=== Starting vLLM: model=$MODEL_PATH port=$PORT ==="
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1} python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "Llama-3.1-8B-Instruct" \
    --port "$PORT" \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --trust-remote-code &
VLLM_PID=$!

echo "=== Waiting for vLLM (PID: $VLLM_PID) ==="
HEALTH_URL="http://127.0.0.1:${PORT}/health"
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

echo "=== Preflight: testing model endpoint ==="
if ! curl -sf "http://127.0.0.1:${PORT}/v1/models" >/dev/null 2>&1; then
    echo "PREFLIGHT FAILED: vLLM not reachable at 127.0.0.1:${PORT}"
    kill "$VLLM_PID" 2>/dev/null || true
    exit 1
fi
echo "Preflight passed"

echo "=== Running INFO injection (Llama×GSM8K, seed=456, 300 tasks) ==="
python3 src/ack_injection.py \
    --config "$CONFIG" \
    --num-tasks 300 \
    --data-seed 456 \
    --injection-source info \
    --traces-file "$TRACES" \
    --annotations-file "$ANNOTATIONS" \
    --info-max-words 30

echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== Llama×GSM8K INFO injection seed=456 finished ==="
