#!/bin/bash
# exp-r1-distill-8b-sica: DeepSeek-R1-Distill-LLaMA-8B on FOLIO-204
# Tests whether reasoning-distilled model escapes SCB
# Server: westd-16639, GPU: cuda:3, port 8003
# K=12, T=0.7, seed=42
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# Config
MODEL_DIR=$(find /root/autodl-tmp/models/ -name "config.json" -path "*DeepSeek-R1*Llama*8B*" -exec dirname {} \; | head -1)
if [ -z "$MODEL_DIR" ]; then
    MODEL_DIR=$(find /root/autodl-tmp/models/ -name "config.json" -path "*deepseek*r1*llama*8*" -exec dirname {} \; | head -1)
fi
PORT=8003
K=12
TEMPERATURE=0.7
SEED=42
RESULTS_DIR="results/exp_r1_distill_8b_sica"
mkdir -p "$RESULTS_DIR"

echo "=== [$(date)] exp-r1-distill-8b-sica: DeepSeek-R1-Distill-LLaMA-8B SICA FOLIO-204 ==="

# Pre-flight checks
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

if [ -z "$MODEL_DIR" ] || [ ! -f "$MODEL_DIR/config.json" ]; then
    echo "ERROR: Model not found. Download first."
    exit 1
fi
echo "Model: OK ($MODEL_DIR)"

GPU_FREE=$(nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits -i 3 | tr -d ' ')
echo "GPU 3 free: ${GPU_FREE} MiB"
if [ "$GPU_FREE" -lt 20000 ]; then
    echo "ERROR: GPU 3 has <20GB free."
    exit 1
fi
echo "GPU: OK"

if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "ERROR: Port $PORT already in use"
    exit 1
fi
echo "Port $PORT: free"

echo "--- Pre-flight PASSED ---"

# Start vLLM
echo ""
echo "=== [$(date)] Starting vLLM on port $PORT ==="
CUDA_VISIBLE_DEVICES=3 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_DIR" \
    --port $PORT \
    --gpu-memory-utilization 0.85 \
    --max-model-len 8192 \
    --trust-remote-code \
    --dtype float16 \
    > /tmp/vllm_r1_distill.log 2>&1 &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

echo "Waiting for vLLM to be ready (8B model, expect 1-2 min)..."
READY=0
for i in $(seq 1 300); do
    if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        READY=1
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "ERROR: vLLM process died. Log:"
        tail -40 /tmp/vllm_r1_distill.log
        exit 1
    fi
    sleep 1
done
if [ $READY -eq 0 ]; then
    echo "ERROR: vLLM not ready after 300s. Log:"
    tail -40 /tmp/vllm_r1_distill.log
    kill $VLLM_PID 2>/dev/null || true
    exit 1
fi

# Run SICA pipeline
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

# Post-processing metrics
echo ""
echo "=== [$(date)] Computing extended metrics ==="
python scripts/exp_d126_70b_sica.py \
    --results "$RESULTS_DIR/results.json" \
    --intermediates "$RESULTS_DIR/intermediates" \
    --output "$RESULTS_DIR/metrics.json" \
    2>&1 | tee -a "$RESULTS_DIR/pipeline.log"

# Cleanup
echo ""
echo "=== [$(date)] Stopping vLLM ==="
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true

echo ""
echo "=== [$(date)] exp-r1-distill-8b-sica DONE ==="
echo "Pipeline results: $RESULTS_DIR/results.json"
echo "Extended metrics: $RESULTS_DIR/metrics.json"
echo "Pipeline log: $RESULTS_DIR/pipeline.log"
echo "vLLM log: /tmp/vllm_r1_distill.log"
echo "EXP_R1_DISTILL_DONE"
