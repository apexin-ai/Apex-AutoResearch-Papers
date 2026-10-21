#!/usr/bin/env bash
# EXP: Ack injection causal intervention — Qwen×StratQA (cross-domain + cross-backbone)
# D330: Injects synthetic acks into Qwen2.5-7B round-robin on StrategyQA (250 tasks).
# Protocol identical to qwen_injection_gsm8k; hypothesis: injection harmless on Qwen×StratQA
# → contrasts with Llama×StratQA -3.28pp, proving backbone-dependent effect.
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

MODEL_PATH=""
for p in /root/autodl-tmp/models/Qwen2.5-7B-Instruct /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B-Instruct /root/autodl-tmp/.hf_cache/qwen/Qwen2.5-7B-Instruct; do
    if [ -d "$p" ]; then MODEL_PATH="$p"; break; fi
done
if [ -z "$MODEL_PATH" ]; then echo "ERROR: Qwen model not found"; exit 1; fi

PORT=8000
CONFIG="configs/ack_injection_qwen_stratqa.yaml"

echo "=== Starting vLLM: model=$MODEL_PATH port=$PORT ==="
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0} python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "Qwen2.5-7B-Instruct" \
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

echo "=== Running ack injection (Qwen×StratQA, 250 tasks) ==="
python3 src/ack_injection.py \
    --config "$CONFIG" \
    --num-tasks 250 \
    --data-seed 42

echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== Qwen×StratQA ack injection finished ==="
