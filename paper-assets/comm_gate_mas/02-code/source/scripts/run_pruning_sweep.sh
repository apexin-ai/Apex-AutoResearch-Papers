#!/usr/bin/env bash
# EXP-C: Ack pruning rate sensitivity sweep (0/25/50/75/100%)
# Runs dose-response (if traces exist) or online pruning with partial rates
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

CONFIG_MODEL="/root/autodl-tmp/models/Qwen2.5-7B-Instruct"

MODEL_PATH=""
for p in "$CONFIG_MODEL" /root/autodl-tmp/models/Qwen2.5-7B-Instruct /root/autodl-tmp/.hf_cache/qwen/Qwen2.5-7B-Instruct; do
    if [ -d "$p" ]; then MODEL_PATH="$p"; break; fi
done
if [ -z "$MODEL_PATH" ]; then echo "ERROR: Qwen model not found"; exit 1; fi

PORT=${PORT:-8000}

BASE_CONFIG="configs/dose_response_qwen_gsm8k.yaml"
if [ "$PORT" != "8000" ]; then
    CONFIG="/tmp/dose_response_p${PORT}.yaml"
    sed "s|http://localhost:8000/v1|http://localhost:${PORT}/v1|" "$BASE_CONFIG" > "$CONFIG"
    echo "Using temp config with port $PORT"
else
    CONFIG="$BASE_CONFIG"
fi

echo "=== Starting vLLM: model=$MODEL_PATH ==="
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0} python3 -m vllm.entrypoints.openai.api_server \
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

TRACES_FILE="outputs/full_scale/qwen_round_robin/traces/traces.jsonl"
if [ -f "$TRACES_FILE" ]; then
    echo "=== Traces found, running dose-response (5 rates x 10 seeds) ==="
    python3 src/dose_response.py --config "$CONFIG" --run-all
else
    echo "=== No traces, running online pruning sweep (5 rates x 3 seeds) ==="
    for rate in 0.0 0.25 0.50 0.75 1.0; do
        for seed in 42 0 1; do
            echo "=== Running rate=$rate seed=$seed ==="
            python3 src/pruning_validation.py \
                --mode online_pruning \
                --config "$CONFIG" \
                --detection-mode heuristic \
                --char-threshold 30 \
                --num-tasks 100 \
                --domain gsm8k \
                --data-seed "$seed" \
                --ack-prune-rate "$rate"
            echo "=== rate=$rate seed=$seed complete ==="
        done
    done
fi

echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== Pruning sweep finished ==="
