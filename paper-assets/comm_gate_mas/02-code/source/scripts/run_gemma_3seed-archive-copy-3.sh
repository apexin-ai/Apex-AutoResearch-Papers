#!/usr/bin/env bash
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

MODEL_PATH="/root/autodl-tmp/.hf_cache/LLM-Research/gemma-2-9b-it/"
CONFIG_MODEL="google/gemma-2-9b-it"
PORT=${PORT:-8001}
PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"

cd "$PROJECT_DIR"

echo "=== Starting vLLM on port $PORT ==="
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-1} python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "$CONFIG_MODEL" \
    --port "$PORT" \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --trust-remote-code &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

echo "=== Waiting for vLLM to be ready ==="
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

# Smoke test: verify model is served under expected name
echo "=== Smoke test: verify model name ==="
AVAILABLE=$(curl -s "http://localhost:${PORT}/v1/models" | python3 -c "import sys,json; print(' '.join(m['id'] for m in json.load(sys.stdin).get('data',[])))" 2>/dev/null)
echo "Available models: $AVAILABLE"
if ! echo "$AVAILABLE" | grep -qF "$CONFIG_MODEL"; then
    echo "ERROR: Model '$CONFIG_MODEL' not in vLLM served models. Check --served-model-name."
    kill "$VLLM_PID" 2>/dev/null || true
    exit 1
fi
echo "Smoke test passed"

for SEED in 0 1; do
    echo "=== Running seed=$SEED ==="
    python3 src/pruning_validation.py \
        --mode online_pruning \
        --config configs/gemma_heuristic_gsm8k_3seed.yaml \
        --detection-mode heuristic \
        --char-threshold 30 \
        --num-tasks 300 \
        --domain gsm8k \
        --data-seed "$SEED"
    echo "=== Seed $SEED complete ==="
done

echo "=== All seeds done, stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true
echo "=== Finished ==="
