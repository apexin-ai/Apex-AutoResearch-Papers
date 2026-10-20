#!/bin/bash
# Qwen3 vLLM serving script for policy_ambiguity_safety experiments
# Usage: ./serve_qwen3.sh [8b|32b|both]

set -euo pipefail

MODEL_DIR="/root/autodl-tmp/models"

serve_8b() {
    local gpu_util="${1:-0.90}"
    echo "Starting Qwen3-8B on port 8001 (gpu_util=$gpu_util)..."
    vllm serve Qwen/Qwen3-8B \
        --tensor-parallel-size 1 \
        --max-model-len 8192 \
        --port 8001 \
        --host 0.0.0.0 \
        --dtype bfloat16 \
        --gpu-memory-utilization "$gpu_util" \
        --enable-auto-tool-choice \
        --tool-call-parser hermes \
        --download-dir "$MODEL_DIR" &
    PID_8B=$!
    echo "Qwen3-8B PID: $PID_8B"
}

serve_32b() {
    local gpu_util="${1:-0.90}"
    echo "Starting Qwen3-32B-AWQ on port 8002 (gpu_util=$gpu_util)..."
    vllm serve Qwen/Qwen3-32B-AWQ \
        --tensor-parallel-size 1 \
        --quantization awq \
        --max-model-len 8192 \
        --port 8002 \
        --host 0.0.0.0 \
        --gpu-memory-utilization "$gpu_util" \
        --enable-auto-tool-choice \
        --tool-call-parser hermes \
        --download-dir "$MODEL_DIR" &
    PID_32B=$!
    echo "Qwen3-32B-AWQ PID: $PID_32B"
}

wait_for_health() {
    local port=$1
    local name=$2
    local max_wait=300
    local elapsed=0
    echo "Waiting for $name health check on port $port..."
    while [ $elapsed -lt $max_wait ]; do
        if curl -s "http://localhost:$port/health" | grep -q "ok\|healthy"; then
            echo "$name is healthy!"
            return 0
        fi
        sleep 5
        elapsed=$((elapsed + 5))
    done
    echo "ERROR: $name health check timed out after ${max_wait}s"
    return 1
}

MODE="${1:-both}"

case "$MODE" in
    8b)
        serve_8b
        wait_for_health 8001 "Qwen3-8B"
        echo "Ready. Qwen3-8B serving on http://localhost:8001/v1"
        wait
        ;;
    32b)
        serve_32b
        wait_for_health 8002 "Qwen3-32B-AWQ"
        echo "Ready. Qwen3-32B-AWQ serving on http://localhost:8002/v1"
        wait
        ;;
    both)
        serve_8b 0.35
        serve_32b 0.50
        wait_for_health 8001 "Qwen3-8B"
        wait_for_health 8002 "Qwen3-32B-AWQ"
        echo "Ready. Both models serving."
        echo "  Qwen3-8B:       http://localhost:8001/v1"
        echo "  Qwen3-32B-AWQ:  http://localhost:8002/v1"
        wait
        ;;
    *)
        echo "Usage: $0 [8b|32b|both]"
        exit 1
        ;;
esac
