#!/bin/bash
# HumanEval trace collection: 5 seeds × 164 tasks on Qwen2.5-7B-Instruct via vLLM.
# Server: bjb2-10838, GPU 0 only.
set -euo pipefail

MODEL_PATH="/root/autodl-tmp/models/Qwen2.5-7B-Instruct"
PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
OUTPUT_BASE="${PROJECT_DIR}/outputs/humaneval_qwen_full"
VLLM_PORT=8000
SEEDS=(42 123 456 789 1024)
NUM_TASKS=164

source /etc/network_turbo 2>/dev/null || true
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1

cd "${PROJECT_DIR}"
mkdir -p "${OUTPUT_BASE}"

exec > >(tee -a "${OUTPUT_BASE}/trace_master.log") 2>&1
echo "=== HumanEval trace collection started at $(date) ==="

echo "Starting vLLM on port ${VLLM_PORT}..."
CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server \
    --model "${MODEL_PATH}" \
    --served-model-name "Qwen2.5-7B-Instruct" \
    --port "${VLLM_PORT}" \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.85 &
VLLM_PID=$!
echo "vLLM PID: ${VLLM_PID}"

echo "Waiting for vLLM to become ready..."
for i in $(seq 1 60); do
    if curl -s "http://localhost:${VLLM_PORT}/v1/models" > /dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        break
    fi
    if ! kill -0 "${VLLM_PID}" 2>/dev/null; then
        echo "ERROR: vLLM process died during startup"
        exit 1
    fi
    sleep 5
done

if ! curl -s "http://localhost:${VLLM_PORT}/v1/models" > /dev/null 2>&1; then
    echo "ERROR: vLLM failed to start within 300s"
    kill "${VLLM_PID}" 2>/dev/null || true
    exit 1
fi

FAILED=0
for SEED in "${SEEDS[@]}"; do
    SEED_DIR="${OUTPUT_BASE}/seed_${SEED}"
    mkdir -p "${SEED_DIR}"
    echo "=== Seed ${SEED} started at $(date) ==="
    if python src/metagpt_trace_collection.py \
        --config configs/metagpt_qwen.yaml \
        --num-tasks "${NUM_TASKS}" \
        --seed "${SEED}" \
        --output "${SEED_DIR}/traces.jsonl"; then
        LINES=$(wc -l < "${SEED_DIR}/traces.jsonl")
        echo "--- Seed ${SEED} done at $(date): ${LINES} lines ---"
    else
        echo "!!! Seed ${SEED} FAILED at $(date) !!!"
        FAILED=$((FAILED + 1))
    fi
done

echo "Stopping vLLM (PID ${VLLM_PID})..."
kill "${VLLM_PID}" 2>/dev/null || true
wait "${VLLM_PID}" 2>/dev/null || true

echo "=== All seeds complete at $(date). Failed: ${FAILED}/5 ==="
if [ "${FAILED}" -gt 0 ]; then
    exit 1
fi
echo "ALL_SEEDS_COMPLETE"
