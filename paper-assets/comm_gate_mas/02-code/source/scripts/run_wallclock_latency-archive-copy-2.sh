#!/usr/bin/env bash
# EXP-E: Wall-clock latency measurement — baseline vs ack_only pruning
# Measures per-task inference latency (50 tasks × 2 conditions) on Qwen2.5-7B-Instruct
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

CONFIG_MODEL="/root/autodl-tmp/models/Qwen2.5-7B-Instruct"

MODEL_PATH=""
for p in "$CONFIG_MODEL" /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B-Instruct /root/autodl-tmp/.hf_cache/qwen/Qwen2.5-7B-Instruct; do
    if [ -d "$p" ]; then MODEL_PATH="$p"; break; fi
done
if [ -z "$MODEL_PATH" ]; then echo "ERROR: Qwen model not found"; exit 1; fi

PORT=${PORT:-8001}
N_TASKS=${N_TASKS:-50}

# --- Start vLLM on specified GPU ---
echo "=== Starting vLLM: model=$MODEL_PATH port=$PORT ==="
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1} python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "$CONFIG_MODEL" \
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

# --- Run latency measurement ---
echo "=== Running wallclock latency measurement (${N_TASKS} tasks × 2 conditions) ==="
python3 src/latency_measurement.py \
    --config configs/full_scale.yaml \
    --port "$PORT" \
    --n-tasks "$N_TASKS" \
    --output "outputs/v7_analysis/latency_measurement.json"

# --- Cleanup ---
echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== Wallclock latency experiment finished ==="
