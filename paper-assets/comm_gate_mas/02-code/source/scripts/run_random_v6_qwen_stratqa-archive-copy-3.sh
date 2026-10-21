#!/usr/bin/env bash
# Random baseline v6: message-count-matched random suppression — Qwen×StratQA
# Fills last Qwen cell in 2×2×2 causal matrix (v6 random × Qwen × StratQA).
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

# D333: unset proxy to prevent Python httpx routing through proxy
unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY no_proxy NO_PROXY 2>/dev/null || true

export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

MODEL_PATH="/root/autodl-tmp/models/Qwen2.5-7B-Instruct"
if [ ! -d "$MODEL_PATH" ]; then
    MODEL_PATH="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B-Instruct"
fi
if [ ! -d "$MODEL_PATH" ]; then echo "ERROR: Qwen model not found"; exit 1; fi

PORT=8000
CONFIG="configs/random_v6_qwen_stratqa.yaml"

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
for i in $(seq 1 120); do
    if curl -s "http://127.0.0.1:${PORT}/health" >/dev/null 2>&1; then
        echo "vLLM ready after $((i*5))s"
        break
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
        echo "ERROR: vLLM process died"
        exit 1
    fi
    sleep 5
done

if ! curl -s "http://127.0.0.1:${PORT}/health" >/dev/null 2>&1; then
    echo "ERROR: vLLM failed to start within 600s"
    kill "$VLLM_PID" 2>/dev/null || true
    exit 1
fi

echo "=== Running random baseline v6 (Qwen×StratQA, 250 tasks) ==="
python3 src/random_baseline_v6.py \
    --config "$CONFIG" \
    --annotations outputs/stratqa/qwen_round_robin/annotations/annotations.jsonl \
    --model-path "$MODEL_PATH" \
    --output outputs/random_msg_matched_qwen_stratqa_v6/pruning_validation.json \
    --num-tasks 250 \
    --data-seed 42

echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== Qwen×StratQA v6 random baseline finished ==="
