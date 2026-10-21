#!/usr/bin/env bash
# Llama dose-response shard A: rates [0.0, 0.25, 0.50] × 5 seeds
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

MODEL_PATH="/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct"
if [ ! -d "$MODEL_PATH" ]; then echo "ERROR: Llama model not found at $MODEL_PATH"; exit 1; fi

PORT=8001
# Check if port is in use via curl
if curl -s "http://localhost:${PORT}/health" >/dev/null 2>&1; then
    PORT=8002
fi

CONFIG="/tmp/dose_response_llama_shard_a.yaml"
sed "s|http://localhost:8001/v1|http://localhost:${PORT}/v1|" configs/dose_response_llama_gsm8k.yaml > "$CONFIG"

echo "=== Starting vLLM: model=$MODEL_PATH port=$PORT ==="
CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.openai.api_server \
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
        echo "vLLM ready after $((i*5))s"
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
TRACES_DIR="outputs/full_scale/llama_round_robin/traces"

echo "=== Running shard A: rates [0.0, 0.25, 0.50] × seeds [42,123,456,789,1024] ==="
for rate in 0.0 0.25 0.50; do
    for seed in 42 123 456 789 1024; do
        echo "=== rate=$rate seed=$seed ==="
        python3 src/dose_response.py \
            --config "$CONFIG" \
            --ack-prune-rate "$rate" \
            --subset-seed "$seed" \
            --backbone llama \
            --traces-dir "$TRACES_DIR" \
            --output-dir "$OUTPUT_DIR" \
            --n-tasks 100
        echo "=== rate=$rate seed=$seed DONE ==="
    done
done

echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== Shard A finished: 15/15 configs complete ==="
