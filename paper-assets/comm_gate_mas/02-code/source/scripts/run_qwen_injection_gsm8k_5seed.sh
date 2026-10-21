#!/usr/bin/env bash
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

MODEL_PATH=""
for p in "/root/autodl-tmp/models/Qwen2.5-7B-Instruct" "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B-Instruct"; do
    if [ -d "$p" ]; then MODEL_PATH="$p"; break; fi
done
if [ -z "$MODEL_PATH" ]; then echo "ERROR: Qwen model not found"; exit 1; fi

PORT=8000
CONFIG="configs/ack_injection_qwen_gsm8k.yaml"
SEEDS=(42 123 456 789 1024)
OUTPUT_BASE="outputs/qwen_injection_gsm8k_5seed"
mkdir -p "$OUTPUT_BASE"

echo "=== Starting vLLM: model=$MODEL_PATH port=$PORT ==="
CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "Qwen2.5-7B-Instruct" \
    --port "$PORT" \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --trust-remote-code &
VLLM_PID=$!

echo "=== Waiting for vLLM (PID: $VLLM_PID) ==="
ELAPSED=0
while [ "$ELAPSED" -lt 300 ]; do
    curl -sf "http://127.0.0.1:${PORT}/health" >/dev/null 2>&1 && { echo "vLLM ready after ${ELAPSED}s"; break; }
    kill -0 "$VLLM_PID" 2>/dev/null || { echo "vLLM died"; exit 1; }
    sleep 5
    ELAPSED=$((ELAPSED + 5))
done
curl -sf "http://127.0.0.1:${PORT}/health" >/dev/null 2>&1 || { echo "vLLM timeout"; kill "$VLLM_PID"; exit 1; }

for SEED in "${SEEDS[@]}"; do
    echo "===== Seed $SEED start: $(date) ====="
    python3 src/ack_injection.py \
        --config "$CONFIG" \
        --num-tasks 300 \
        --data-seed "$SEED" \
        --output "$OUTPUT_BASE/seed_${SEED}.json" \
        2>&1 | tee "$OUTPUT_BASE/seed_${SEED}.log"
    echo "===== Seed $SEED done: $(date) ====="
done

kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== All 5 seeds complete ==="
