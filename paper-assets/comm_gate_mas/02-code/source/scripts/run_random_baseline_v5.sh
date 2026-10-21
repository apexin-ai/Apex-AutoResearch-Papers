#!/usr/bin/env bash
# Random baseline v5: per-task token-budget-matched random suppression on Qwen2.5-7B GSM8K
# Fixes from v4: no checkpoint resume, suppress budget guard, per-task budget
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

CONFIG_MODEL="/root/autodl-tmp/models/Qwen2.5-7B-Instruct"

MODEL_PATH=""
for p in "$CONFIG_MODEL" /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B-Instruct; do
    if [ -d "$p" ]; then MODEL_PATH="$p"; break; fi
done
if [ -z "$MODEL_PATH" ]; then echo "ERROR: Qwen model not found"; exit 1; fi

PORT=${PORT:-8001}

BASE_CONFIG="configs/random_token_matched_qwen_gsm8k.yaml"
if [ "$PORT" != "8000" ]; then
    CONFIG="/tmp/random_v5_p${PORT}.yaml"
    sed "s|http://localhost:8000/v1|http://localhost:${PORT}/v1|" "$BASE_CONFIG" > "$CONFIG"
    echo "Using temp config with port $PORT"
else
    CONFIG="$BASE_CONFIG"
fi

echo "=== Starting vLLM: model=$MODEL_PATH port=$PORT ==="
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1} python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "$CONFIG_MODEL" \
    --port "$PORT" \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --trust-remote-code &
VLLM_PID=$!

echo "=== Waiting for vLLM (PID: $VLLM_PID) ==="
for i in $(seq 1 120); do
    if curl -s "http://localhost:${PORT}/health" >/dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        break
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
        echo "ERROR: vLLM process died"
        exit 1
    fi
    sleep 5
done

if ! curl -s "http://localhost:${PORT}/health" >/dev/null 2>&1; then
    echo "ERROR: vLLM failed to start within 600s"
    kill "$VLLM_PID" 2>/dev/null || true
    exit 1
fi

echo "=== Running random baseline v5 (per-task token-budget-matched) ==="
python3 src/random_baseline_v5.py \
    --config "$CONFIG" \
    --traces outputs/full_scale/qwen_round_robin/traces/traces.jsonl \
    --annotations outputs/full_scale/qwen_round_robin/annotations/annotations.jsonl \
    --model-path "$MODEL_PATH" \
    --output outputs/random_token_matched_qwen_v5/pruning_validation.json \
    --num-tasks 300 \
    --data-seed 42

echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== v5 random baseline finished ==="
