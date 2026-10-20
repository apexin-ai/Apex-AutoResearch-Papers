#!/bin/bash
# exp-027: Qwen3-14B (non-thinking) SICA vs SC on FOLIO(204)
# Generational comparison with exp-026 (Qwen2.5-14B)
# Server: westd-25068, GPU 1, K=12, T=0.7, T_ext=0.3, seed=42
#
# Purpose: Test whether capability trap persists on next-gen Qwen3-14B
# Non-thinking mode: disable Qwen3 native reasoning for fair comparison with Qwen2.5-14B

set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# ── Config ──────────────────────────────────────────────────────
MODEL="/root/autodl-tmp/models/Qwen3-14B"
PORT=8001
GPU_ID=1
K=12
TEMPERATURE=0.7
MAX_TOKENS=4096
SEED=42
RESULTS_DIR="results/exp027_qwen3_14b_nonthinking"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] exp-027: Qwen3-14B (non-thinking) SICA vs SC ==="
echo "Model: $MODEL"
echo "GPU: $GPU_ID, Port: $PORT"
echo "K=$K, T=$TEMPERATURE, max_tokens=$MAX_TOKENS, seed=$SEED"
echo "Data: folio_full.json (204 problems)"

# ── Pre-flight checks ──────────────────────────────────────────
echo ""
echo "=== Pre-flight checks ==="

if [ ! -d "$MODEL" ]; then
    echo "ERROR: Model not found: $MODEL"
    exit 1
fi
echo "Model dir: OK"

SHARD_COUNT=$(ls "$MODEL"/model-*.safetensors 2>/dev/null | wc -l)
echo "Model shards: $SHARD_COUNT"
if [ "$SHARD_COUNT" -lt 8 ]; then
    echo "ERROR: Expected 8 safetensor shards, found $SHARD_COUNT. Download may be incomplete."
    exit 1
fi

for f in data/folio_full.json data/empty.json; do
    if [ ! -f "$f" ]; then
        echo "ERROR: Data file not found: $f"
        exit 1
    fi
done
echo "Data files: OK"

GPU_MEM=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits -i $GPU_ID 2>/dev/null | tr -d ' ')
echo "GPU $GPU_ID memory used: ${GPU_MEM} MiB"
if [ "$GPU_MEM" -gt 1000 ]; then
    echo "WARNING: GPU $GPU_ID has ${GPU_MEM} MiB in use. May conflict."
fi

if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "ERROR: Port $PORT already in use."
    exit 1
fi
echo "Port $PORT: free"

# ── Step 1: Start vLLM (non-thinking mode) ────────────────────
echo ""
echo "=== [$(date)] Starting vLLM on GPU $GPU_ID, port $PORT (non-thinking) ==="

VLLM_USE_FLASHINFER_SAMPLER=0 CUDA_VISIBLE_DEVICES=$GPU_ID python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL" \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.90 \
    --port $PORT \
    --dtype auto \
    --trust-remote-code \
    --enforce-eager \
    --reasoning-parser qwen3 \
    --default-chat-template-kwargs '{"enable_thinking": false}' \
    > /tmp/vllm_exp027.log 2>&1 &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

echo "Waiting for vLLM to be ready..."
READY=0
for i in $(seq 1 300); do
    if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        READY=1
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "ERROR: vLLM process died. Check /tmp/vllm_exp027.log"
        tail -30 /tmp/vllm_exp027.log
        exit 1
    fi
    sleep 1
done

if [ $READY -eq 0 ]; then
    echo "ERROR: vLLM did not start within 300s. Check /tmp/vllm_exp027.log"
    tail -30 /tmp/vllm_exp027.log
    kill $VLLM_PID 2>/dev/null || true
    exit 1
fi

# ── Step 2: Run SICA pipeline ─────────────────────────────────
echo ""
echo "=== [$(date)] Running SICA pipeline: FOLIO 204, K=$K ==="
PYTHONUNBUFFERED=1 python -u run_full_mvp.py \
    --mode vllm \
    --k $K \
    --temperature $TEMPERATURE \
    --max-tokens $MAX_TOKENS \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --seed $SEED \
    --math-data data/empty.json \
    --pw-data data/empty.json \
    --folio-data data/folio_full.json \
    --output "$RESULTS_DIR/exp027_results.json" \
    --save-intermediates \
    --resume \
    2>&1 | tee "$RESULTS_DIR/exp027_qwen3_14b_nonthinking.log"

EXIT_CODE=$?

# ── Step 3: Cleanup ───────────────────────────────────────────
echo ""
echo "=== [$(date)] Stopping vLLM ==="
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true

echo ""
echo "Results: $RESULTS_DIR/exp027_results.json"
echo "Log: $RESULTS_DIR/exp027_qwen3_14b_nonthinking.log"
echo "vLLM log: /tmp/vllm_exp027.log"
echo "EXIT_CODE=$EXIT_CODE"
echo "EXP027_DONE"
