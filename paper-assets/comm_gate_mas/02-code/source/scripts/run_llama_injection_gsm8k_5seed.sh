#!/usr/bin/env bash
# 5-seed Llama injection × GSM8K
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export HF_DATASETS_OFFLINE=1
export HF_HUB_OFFLINE=1
export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

MODEL_PATH="/root/autodl-tmp/models/Llama-3.1-8B-Instruct"
[ -d "$MODEL_PATH" ] || { echo "ERROR: model not found at $MODEL_PATH"; exit 1; }

PORT=8001
CONFIG="configs/ack_injection_llama_gsm8k.yaml"

SEEDS=(42 123 456 789 1024)
OUTPUT_BASE="outputs/llama_injection_gsm8k_5seed"
mkdir -p "$OUTPUT_BASE"

echo "=== Starting vLLM on cuda:1 ==="
CUDA_VISIBLE_DEVICES=1 python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "Llama-3.1-8B-Instruct" \
    --port "$PORT" \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --trust-remote-code &
VLLM_PID=$!

HEALTH_URL="http://127.0.0.1:${PORT}/health"
ELAPSED=0
while [ "$ELAPSED" -lt 300 ]; do
    curl -sf "$HEALTH_URL" >/dev/null 2>&1 && { echo "vLLM ready after ${ELAPSED}s"; break; }
    kill -0 "$VLLM_PID" 2>/dev/null || { echo "ERROR: vLLM died"; exit 1; }
    sleep 5
    ELAPSED=$((ELAPSED + 5))
done
curl -sf "$HEALTH_URL" >/dev/null 2>&1 || { echo "ERROR: vLLM timeout"; kill "$VLLM_PID"; exit 1; }

for SEED in "${SEEDS[@]}"; do
    echo "===== Seed $SEED ($(date)) ====="
    python3 src/ack_injection.py \
        --config "$CONFIG" \
        --num-tasks 300 \
        --data-seed "$SEED" \
        --output "$OUTPUT_BASE/seed_${SEED}.json" \
        2>&1 | tee "$OUTPUT_BASE/seed_${SEED}.log"
    echo "===== Seed $SEED done ($(date)) ====="
done

kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== All 5 seeds complete ==="
