#!/usr/bin/env bash
# Llama dose-response shard B: rates [75%, 100%] × 5 seeds on westb cuda:1
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

MODEL_PATH="/root/autodl-tmp/models/Llama-3.1-8B-Instruct"
PORT=8001

if [ ! -d "$MODEL_PATH" ]; then echo "ERROR: Llama model not found at $MODEL_PATH"; exit 1; fi

echo "=== Starting vLLM: model=$MODEL_PATH port=$PORT ==="
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0} python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "Llama-3.1-8B-Instruct" \
    --port "$PORT" \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --trust-remote-code &
VLLM_PID=$!

echo "=== Waiting for vLLM (PID: $VLLM_PID) ==="
for i in $(seq 1 120); do
    if curl -s "http://localhost:${PORT}/health" >/dev/null 2>&1; then
        echo "vLLM ready after $((i * 5))s"
        break
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
        echo "ERROR: vLLM process died"; exit 1
    fi
    sleep 5
done

if ! curl -s "http://localhost:${PORT}/health" >/dev/null 2>&1; then
    echo "ERROR: vLLM failed to start within 600s"
    kill "$VLLM_PID" 2>/dev/null || true; exit 1
fi

OUTPUT_DIR="outputs/analysis/dose_response_llama_v2"
mkdir -p "$OUTPUT_DIR"

CONFIG="configs/dose_response_llama_gsm8k.yaml"

for rate in 0.75 1.0; do
    for seed in 42 123 456 789 1024; do
        echo "=== rate=$rate seed=$seed ==="
        python3 src/dose_response.py \
            --config "$CONFIG" \
            --ack-prune-rate "$rate" \
            --subset-seed "$seed" \
            --backbone llama \
            --traces-dir outputs/full_scale/llama_round_robin/traces \
            --output-dir "$OUTPUT_DIR" \
            --n-tasks 100
    done
done

echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== Shard B finished: 10/10 configs complete ==="
