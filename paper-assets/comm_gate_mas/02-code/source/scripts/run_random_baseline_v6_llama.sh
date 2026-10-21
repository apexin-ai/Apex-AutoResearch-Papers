#!/usr/bin/env bash
# Random baseline v6: Llama-3.1-8B GSM8K, message-count-matched random suppression
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

MODEL_PATH="/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct"
PORT=8001

CONFIG="configs/random_v6_llama_gsm8k.yaml"

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
        echo "vLLM ready after $((i*5))s"
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

echo "=== Running random baseline v6 (Llama, message-count-matched, 300 tasks) ==="
python3 src/random_baseline_v6.py \
    --config "$CONFIG" \
    --annotations outputs/full_scale/llama_round_robin/annotations/annotations.jsonl \
    --model-path "$MODEL_PATH" \
    --output outputs/random_msg_matched_llama_v6/pruning_validation.json \
    --num-tasks 300 \
    --data-seed 42

echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== Llama v6 random baseline finished ==="
