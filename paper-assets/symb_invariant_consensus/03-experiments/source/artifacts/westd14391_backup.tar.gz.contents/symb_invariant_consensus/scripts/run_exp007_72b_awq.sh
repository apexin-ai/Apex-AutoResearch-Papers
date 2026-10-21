#!/bin/bash
# exp-007: Qwen2.5-72B-Instruct-AWQ 4-bit, SICA vs SC on D012 (30 PW + 30 FOLIO)
# Server: westd-25068, GPU: cuda:0 (single GPU AWQ)
# K=12, T=0.7, T_ext=0.3 (default), seed=42
set -e

PYTHON=/root/miniconda3/bin/python
MODEL_DIR=/root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ
PORT=8000
RESULTS_DIR=/root/symb_invariant_consensus/results/exp-007-qwen72b-awq

cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

echo "=== [$(date)] exp-007: Qwen2.5-72B-Instruct-AWQ D012 ==="

# ── Step 1: Download model if not present ──
if [ ! -d "$MODEL_DIR" ] || [ $(find "$MODEL_DIR" -name "*.safetensors" 2>/dev/null | wc -l) -eq 0 ]; then
    echo "=== Downloading Qwen2.5-72B-Instruct-AWQ (~40GB) ==="
    $PYTHON -c "
from huggingface_hub import snapshot_download
snapshot_download('Qwen/Qwen2.5-72B-Instruct-AWQ', local_dir='$MODEL_DIR')
print('DOWNLOAD_DONE')
"
    echo "=== [$(date)] Download complete ==="
else
    echo "Model already exists at $MODEL_DIR"
fi

# ── Step 2: Create D012 subset (30 PW + 30 FOLIO = 60 problems) ──
echo "=== Creating D012 subset ==="
$PYTHON -c "
import json, os
pw = json.load(open('data/proofwriter_full.json'))[:30]
folio = json.load(open('data/folio_full.json'))[:30]
os.makedirs('data', exist_ok=True)
with open('data/pw_d012_30.json', 'w') as f:
    json.dump(pw, f, indent=2)
with open('data/folio_d012_30.json', 'w') as f:
    json.dump(folio, f, indent=2)
print(f'D012: {len(pw)} PW + {len(folio)} FOLIO = {len(pw)+len(folio)} problems')
"

# ── Step 3: Check port free ──
if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "ERROR: Port $PORT already in use"
    exit 1
fi

# ── Step 4: Start vLLM with AWQ on cuda:0 ──
echo "=== [$(date)] Starting vLLM (AWQ, single GPU) on port $PORT ==="
export VLLM_USE_FLASHINFER_SAMPLER=0
export CUDA_VISIBLE_DEVICES=0

$PYTHON -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_DIR" \
    --port $PORT \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.95 \
    --max-model-len 4096 \
    --quantization awq \
    --enforce-eager \
    > /tmp/vllm_exp007.log 2>&1 &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

echo "Waiting for vLLM ready (72B AWQ load ~3-5 min)..."
READY=0
for i in $(seq 1 180); do
    if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        READY=1
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "ERROR: vLLM died. Log:"
        tail -40 /tmp/vllm_exp007.log
        exit 1
    fi
    sleep 5
done

if [ $READY -eq 0 ]; then
    echo "ERROR: vLLM did not start in 900s"
    tail -40 /tmp/vllm_exp007.log
    kill $VLLM_PID 2>/dev/null || true
    exit 1
fi

# ── Step 5: Run SICA pipeline ──
echo ""
echo "=== [$(date)] Running SICA pipeline: D012 (60 problems), K=12 ==="
mkdir -p "$RESULTS_DIR"

PYTHONUNBUFFERED=1 $PYTHON -u run_full_mvp.py \
    --mode vllm \
    --k 12 \
    --temperature 0.7 \
    --max-tokens 4096 \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --seed 42 \
    --math-data data/empty.json \
    --pw-data data/pw_d012_30.json \
    --folio-data data/folio_d012_30.json \
    --output "$RESULTS_DIR/exp007_results.json" \
    --save-intermediates \
    --resume \
    2>&1 | tee "$RESULTS_DIR/exp007_run.log"

EXIT_CODE=$?

# ── Step 6: Cleanup ──
echo ""
echo "=== [$(date)] Stopping vLLM ==="
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true

echo "Results: $RESULTS_DIR/exp007_results.json"
echo "Log: $RESULTS_DIR/exp007_run.log"
echo "vLLM log: /tmp/vllm_exp007.log"
echo "EXIT_CODE=$EXIT_CODE"
echo "EXP007_DONE"
