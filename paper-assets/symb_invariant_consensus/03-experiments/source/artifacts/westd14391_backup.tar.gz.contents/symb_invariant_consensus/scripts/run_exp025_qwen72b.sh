#!/bin/bash
# exp-025: Qwen2.5-72B-Instruct SICA vs SC on FOLIO(204) + ProofWriter(600)
# Server: westd-25068, 4×GPU, tensor parallel size 4
# K=12, T=0.7, T_ext=0.1 (hardcoded in VLLMBackend), seed=42
# 804 problems total, estimated 3-5h
#
# Prerequisites:
#   1. 4 GPUs available (nvidia-smi shows 4 GPUs)
#   2. Model downloaded to /root/autodl-tmp/models/Qwen2.5-72B-Instruct/
#      Download: huggingface-cli download Qwen/Qwen2.5-72B-Instruct \
#               --local-dir /root/autodl-tmp/models/Qwen2.5-72B-Instruct
#      (~140GB BF16, ensure sufficient disk on autodl-tmp)
#   3. No other vLLM process on port 8000

set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# ── Config ──────────────────────────────────────────────────────
# Model: check common local paths
if [ -d "/root/autodl-tmp/models/Qwen2.5-72B-Instruct" ]; then
    MODEL="/root/autodl-tmp/models/Qwen2.5-72B-Instruct"
else
    # Fallback: HuggingFace ID (will trigger download on first vLLM start)
    MODEL="Qwen/Qwen2.5-72B-Instruct"
    echo "WARNING: No local model found. vLLM will download from HuggingFace."
    echo "  Recommended: download first with huggingface-cli"
fi

PORT=8000
K=12
TEMPERATURE=0.7
MAX_TOKENS=4096
SEED=42
RESULTS_DIR="results/exp025_qwen72b"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] exp-025: Qwen2.5-72B-Instruct SICA vs SC ==="
echo "Model: $MODEL"
echo "K=$K, T=$TEMPERATURE, max_tokens=$MAX_TOKENS, seed=$SEED"
echo "Data: folio_full.json (204) + proofwriter_full.json (600) = 804 problems"

# ── Pre-flight checks ──────────────────────────────────────────
echo ""
echo "=== Pre-flight checks ==="

GPU_COUNT=$(nvidia-smi -L 2>/dev/null | wc -l)
echo "GPUs detected: $GPU_COUNT"
if [ "$GPU_COUNT" -lt 4 ]; then
    echo "ERROR: Need at least 4 GPUs for 72B tensor parallel. Found $GPU_COUNT."
    exit 1
fi

nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
echo ""

for f in data/folio_full.json data/proofwriter_full.json data/empty.json; do
    if [ ! -f "$f" ]; then
        echo "ERROR: Data file not found: $f"
        exit 1
    fi
done
echo "Data files: OK"

if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "WARNING: vLLM already running on port $PORT. Kill it first:"
    echo "  pkill -9 -f 'vllm.entrypoints'"
    exit 1
fi
echo "Port $PORT: free"

# ── Step 1: Start vLLM with tensor parallel ───────────────────
echo ""
echo "=== [$(date)] Starting vLLM (tensor-parallel=4) on port $PORT ==="
echo "72B BF16 ~140GB across 4 GPUs, max-model-len=8192"

python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL" \
    --tensor-parallel-size 4 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.95 \
    --port $PORT \
    --dtype auto \
    --trust-remote-code \
    > /tmp/vllm_exp025.log 2>&1 &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

# Wait for vLLM ready (72B model loading takes 3-8 min)
echo "Waiting for vLLM to be ready..."
READY=0
for i in $(seq 1 600); do
    if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        READY=1
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "ERROR: vLLM process died. Check /tmp/vllm_exp025.log"
        tail -30 /tmp/vllm_exp025.log
        exit 1
    fi
    sleep 1
done

if [ $READY -eq 0 ]; then
    echo "ERROR: vLLM did not start within 600s. Check /tmp/vllm_exp025.log"
    tail -30 /tmp/vllm_exp025.log
    kill $VLLM_PID 2>/dev/null || true
    exit 1
fi

# ── Step 2: Run SICA pipeline ─────────────────────────────────
echo ""
echo "=== [$(date)] Running SICA pipeline: 804 problems, K=$K ==="
PYTHONUNBUFFERED=1 python -u run_full_mvp.py \
    --mode vllm \
    --k $K \
    --temperature $TEMPERATURE \
    --max-tokens $MAX_TOKENS \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --seed $SEED \
    --math-data data/empty.json \
    --pw-data data/proofwriter_full.json \
    --folio-data data/folio_full.json \
    --output "$RESULTS_DIR/exp025_results.json" \
    --save-intermediates \
    --resume \
    2>&1 | tee "$RESULTS_DIR/exp025_qwen72b.log"

EXIT_CODE=$?

# ── Step 3: Cleanup ───────────────────────────────────────────
echo ""
echo "=== [$(date)] Stopping vLLM ==="
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true

echo ""
echo "Results: $RESULTS_DIR/exp025_results.json"
echo "Log: $RESULTS_DIR/exp025_qwen72b.log"
echo "vLLM log: /tmp/vllm_exp025.log"
echo "EXIT_CODE=$EXIT_CODE"
echo "EXP025_DONE"
