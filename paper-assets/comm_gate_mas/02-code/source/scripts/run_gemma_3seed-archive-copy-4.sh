#!/bin/bash
# EXP-E: Gemma Boundary Condition Seeds — 3-seed replication
# Gemma-2-9B-it, GSM8K, N=300, heuristic detection, seeds 0 and 1
# (seed 42 already completed in original experiment)
# Server: westd-13436, CUDA:1, port 8001
#
# PREREQUISITES:
#   1. Code must be synced from westb (git pull) — needs Gemma answer extraction fixes
#   2. Gemma model must be downloaded (see error message below if missing)
set -euo pipefail

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
CONFIG="configs/gemma_heuristic_gsm8k_3seed.yaml"
MODEL_PATH="/root/autodl-tmp/.hf_cache/LLM-Research/gemma-2-9b-it"
PORT=8001
NUM_TASKS=300
DOMAIN="gsm8k"

cd "$PROJECT_DIR"

# --- Check model exists ---
if [ ! -d "$MODEL_PATH" ]; then
    echo "ERROR: Gemma model not found at $MODEL_PATH"
    echo "Download first (use ModelScope for speed on AutoDL):"
    echo "  source /etc/network_turbo"
    echo "  pip install modelscope"
    echo "  python3 -c \"from modelscope import snapshot_download; snapshot_download('AI-ModelScope/gemma-2-9b-it', cache_dir='/root/autodl-tmp/.hf_cache')\""
    echo "Or from HuggingFace:"
    echo "  HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 huggingface-cli download google/gemma-2-9b-it --local-dir $MODEL_PATH"
    exit 1
fi

# --- Start vLLM if not running ---
if ! curl -s http://localhost:${PORT}/health > /dev/null 2>&1; then
    echo "Starting vLLM on CUDA:1 port ${PORT}..."
    CUDA_VISIBLE_DEVICES=1 nohup python -m vllm.entrypoints.openai.api_server \
        --model "$MODEL_PATH" \
        --port "$PORT" \
        --max-model-len 4096 \
        --enforce-eager \
        > /tmp/vllm_gemma_3seed.log 2>&1 &
    VLLM_PID=$!
    echo "vLLM PID: $VLLM_PID"

    echo "Waiting for vLLM to be ready..."
    for i in $(seq 1 180); do
        if curl -s http://localhost:${PORT}/health > /dev/null 2>&1; then
            echo "vLLM ready after ${i}s"
            break
        fi
        if [ "$i" -eq 180 ]; then
            echo "ERROR: vLLM failed to start within 180s"
            exit 1
        fi
        sleep 1
    done
else
    echo "vLLM already running on port ${PORT}"
fi

# --- Run seed 0 and seed 1 (seed 42 already done) ---
for SEED in 0 1; do
    OUTPUT="outputs/gemma_heuristic_gsm8k_seed${SEED}/results.json"
    if [ -f "$OUTPUT" ]; then
        echo "SKIP: $OUTPUT already exists"
        continue
    fi
    echo "=== Gemma heuristic: seed=${SEED} ==="
    mkdir -p "$(dirname "$OUTPUT")"
    python3 src/pruning_validation.py \
        --mode online_pruning \
        --config "$CONFIG" \
        --detection-mode heuristic \
        --char-threshold 30 \
        --data-seed "$SEED" \
        --num-tasks "$NUM_TASKS" \
        --domain "$DOMAIN" \
        --output "$OUTPUT"
    echo "Saved: $OUTPUT"
done

echo "=== EXP-E complete ==="
