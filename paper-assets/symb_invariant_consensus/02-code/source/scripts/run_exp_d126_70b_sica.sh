#!/bin/bash
# exp-d126-70b-sica: Qwen2.5-72B-Instruct AWQ on FOLIO-204
# Tests whether symbolic confirmation bias persists at 72B scale
# Server: westd-16639, GPU: cuda:0,1 (tensor parallel=2)
# K=12, T=0.7, T_ext=0.3, seed=42
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# ── Config ──
MODEL_DIR="/root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ"
PORT=8000
K=12
TEMPERATURE=0.7
SEED=42
RESULTS_DIR="results/exp_d126_70b_sica"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] exp-d126-70b-sica: Qwen2.5-72B-Instruct-AWQ SICA FOLIO-204 ==="

# ── Pre-flight checks ──
echo ""
echo "--- Pre-flight checks ---"

for f in data/folio_full.json data/empty.json; do
    if [ ! -f "$f" ]; then
        echo "ERROR: Data file missing: $f"; exit 1
    fi
done
echo "Data files: OK"

python3 -c "from sica.pipeline import SICAPipeline; from sica.constraint_extractor import ConstraintExtractor, VLLMBackend; from sica.trace_generator import VLLMGenerator; print('sica package: OK')"
python3 -c "import z3; print('z3: OK')"
python3 -c "from scipy.stats import binomtest; print('scipy: OK')"
python3 -c "import openai; print('openai: OK')"

GPU_FREE_0=$(nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits -i 0 | tr -d ' ')
GPU_FREE_1=$(nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits -i 1 | tr -d ' ')
echo "GPU 0 free: ${GPU_FREE_0} MiB, GPU 1 free: ${GPU_FREE_1} MiB"
if [ "$GPU_FREE_0" -lt 50000 ] || [ "$GPU_FREE_1" -lt 50000 ]; then
    echo "ERROR: GPU 0 or 1 has <50GB free. Check nvidia-smi."
    exit 1
fi
echo "GPU: OK"

if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "ERROR: Port $PORT already in use"
    exit 1
fi
echo "Port $PORT: free"

if [ ! -d "$MODEL_DIR" ] || [ ! -f "$MODEL_DIR/config.json" ]; then
    echo "ERROR: Model not found at $MODEL_DIR. Download first."
    exit 1
fi
echo "Model: OK ($MODEL_DIR)"

echo "--- Pre-flight PASSED ---"

# ── Start vLLM ──
echo ""
echo "=== [$(date)] Starting vLLM (TP=2, AWQ) on port $PORT ==="
CUDA_VISIBLE_DEVICES=0,1 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_DIR" \
    --tensor-parallel-size 2 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.90 \
    --port $PORT \
    --dtype auto \
    --trust-remote-code \
    > /tmp/vllm_exp_d126.log 2>&1 &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

echo "Waiting for vLLM to be ready (72B AWQ, expect 2-5 min)..."
READY=0
for i in $(seq 1 600); do
    if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        READY=1
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "ERROR: vLLM process died. Log:"
        tail -40 /tmp/vllm_exp_d126.log
        exit 1
    fi
    sleep 1
done
if [ $READY -eq 0 ]; then
    echo "ERROR: vLLM not ready after 600s. Log:"
    tail -40 /tmp/vllm_exp_d126.log
    kill $VLLM_PID 2>/dev/null || true
    exit 1
fi

# ── Run SICA pipeline ──
echo ""
echo "=== [$(date)] Running SICA: FOLIO-204, K=$K, T=$TEMPERATURE, seed=$SEED ==="
PYTHONUNBUFFERED=1 python -u run_full_mvp.py \
    --mode vllm \
    --k $K \
    --temperature $TEMPERATURE \
    --max-tokens 4096 \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --seed $SEED \
    --math-data data/empty.json \
    --pw-data data/empty.json \
    --folio-data data/folio_full.json \
    --output "$RESULTS_DIR/results.json" \
    --save-intermediates \
    --resume \
    2>&1 | tee "$RESULTS_DIR/pipeline.log"

# ── Post-processing metrics ──
echo ""
echo "=== [$(date)] Computing extended metrics ==="
python scripts/exp_d126_70b_sica.py \
    --results "$RESULTS_DIR/results.json" \
    --intermediates "$RESULTS_DIR/intermediates" \
    --output "$RESULTS_DIR/metrics.json" \
    2>&1 | tee -a "$RESULTS_DIR/pipeline.log"

# ── Cleanup ──
echo ""
echo "=== [$(date)] Stopping vLLM ==="
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true

echo ""
echo "=== [$(date)] exp-d126-70b-sica DONE ==="
echo "Pipeline results: $RESULTS_DIR/results.json"
echo "Extended metrics: $RESULTS_DIR/metrics.json"
echo "Pipeline log: $RESULTS_DIR/pipeline.log"
echo "vLLM log: /tmp/vllm_exp_d126.log"
echo "EXP_D126_DONE"
