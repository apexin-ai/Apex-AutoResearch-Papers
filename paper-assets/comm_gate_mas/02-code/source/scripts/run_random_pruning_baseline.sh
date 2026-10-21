#!/bin/bash
# EXP-D: Random Pruning Baseline — Ack-aware vs Random pruning
# Qwen2.5-7B-Instruct, GSM8K, N=300, 3 seeds × 2 rates × 2 strategies = 12 runs
# Server: westb-28993, CUDA:1, port 8001
set -euo pipefail

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
CONFIG="configs/random_pruning_baseline_qwen_gsm8k.yaml"
OUTPUT_BASE="outputs/random_pruning_baseline"
MODEL_PATH="/root/autodl-tmp/models/Qwen2.5-7B-Instruct"
PORT=8001
NUM_TASKS=300
DOMAIN="gsm8k"

cd "$PROJECT_DIR"

# --- Start vLLM if not already running ---
if ! curl -s http://localhost:${PORT}/health > /dev/null 2>&1; then
    echo "Starting vLLM on CUDA:1 port ${PORT}..."
    CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0} nohup python -m vllm.entrypoints.openai.api_server \
        --model "$MODEL_PATH" \
        --port "$PORT" \
        --max-model-len 4096 \
        --enforce-eager \
        > /tmp/vllm_random_baseline.log 2>&1 &
    VLLM_PID=$!
    echo "vLLM PID: $VLLM_PID"

    echo "Waiting for vLLM to be ready..."
    for i in $(seq 1 120); do
        if curl -s http://localhost:${PORT}/health > /dev/null 2>&1; then
            echo "vLLM ready after ${i}s"
            break
        fi
        if [ "$i" -eq 120 ]; then
            echo "ERROR: vLLM failed to start within 120s"
            exit 1
        fi
        sleep 1
    done
else
    echo "vLLM already running on port ${PORT}"
fi

SEEDS=(42 0 1)
RATES=("0.5" "1.0")
COMPLETED=0
TOTAL=12

# --- Ack-aware pruning (heuristic detection) ---
for rate in "${RATES[@]}"; do
    for seed in "${SEEDS[@]}"; do
        rate_tag=$(echo "$rate" | tr '.' '')
        OUTPUT="${OUTPUT_BASE}/heuristic_rate${rate_tag}_seed${seed}/results.json"
        if [ -f "$OUTPUT" ]; then
            echo "SKIP: $OUTPUT already exists"
            COMPLETED=$((COMPLETED + 1))
            continue
        fi
        echo "=== [$((COMPLETED+1))/$TOTAL] Ack-aware: rate=${rate}, seed=${seed} ==="
        mkdir -p "$(dirname "$OUTPUT")"
        python3 src/pruning_validation.py \
            --mode online_pruning \
            --config "$CONFIG" \
            --detection-mode heuristic \
            --char-threshold 30 \
            --pruning-rate "$rate" \
            --seed "$seed" \
            --num-tasks "$NUM_TASKS" \
            --domain "$DOMAIN" \
            --output "$OUTPUT"
        echo "Saved: $OUTPUT"
        COMPLETED=$((COMPLETED + 1))
    done
done

# --- Random pruning ---
for rate in "${RATES[@]}"; do
    for seed in "${SEEDS[@]}"; do
        rate_tag=$(echo "$rate" | tr '.' '')
        OUTPUT="${OUTPUT_BASE}/random_rate${rate_tag}_seed${seed}/results.json"
        if [ -f "$OUTPUT" ]; then
            echo "SKIP: $OUTPUT already exists"
            COMPLETED=$((COMPLETED + 1))
            continue
        fi
        echo "=== [$((COMPLETED+1))/$TOTAL] Random: rate=${rate}, seed=${seed} ==="
        mkdir -p "$(dirname "$OUTPUT")"
        python3 src/pruning_validation.py \
            --mode online_pruning \
            --config "$CONFIG" \
            --detection-mode random \
            --pruning-rate "$rate" \
            --seed "$seed" \
            --num-tasks "$NUM_TASKS" \
            --domain "$DOMAIN" \
            --output "$OUTPUT"
        echo "Saved: $OUTPUT"
        COMPLETED=$((COMPLETED + 1))
    done
done

echo "=== EXP-D complete: $COMPLETED/$TOTAL runs ==="
