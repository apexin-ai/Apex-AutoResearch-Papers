#!/bin/bash
# exp-017: StrategyQA cross-domain validation (Qwen2.5-14B-Instruct)
# D025 Capability Trap Paper: verify SICA ≈ SC pattern on commonsense reasoning
# K=12, T=0.7, 60 problems subset
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

MODEL="/root/autodl-tmp/models/Qwen2.5-14B-Instruct"
PORT=8000
RESULTS_DIR="results/exp017_strategyqa"
mkdir -p "$RESULTS_DIR"

# Step 1: Start vLLM
echo "=== [$(date)] Starting vLLM (Qwen2.5-14B-Instruct) on port $PORT ==="
python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL" \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.90 \
    --port $PORT \
    --trust-remote-code \
    --dtype auto > /tmp/vllm_exp017.log 2>&1 &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

# Step 2: Wait for vLLM ready (up to 180s)
echo "Waiting for vLLM to be ready..."
for i in $(seq 1 180); do
    if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "ERROR: vLLM process died. Check /tmp/vllm_exp017.log"
        tail -20 /tmp/vllm_exp017.log
        exit 1
    fi
    sleep 1
done

if ! curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
    echo "ERROR: vLLM did not start within 180s"
    kill $VLLM_PID 2>/dev/null
    exit 1
fi

# Step 3: Run SICA vs SC evaluation
echo "=== [$(date)] Running exp-017: StrategyQA, K=12, T=0.7, 60 problems ==="
python3 scripts/eval_strategyqa.py \
    --mode vllm \
    --k 12 \
    --n-problems 60 \
    --temperature 0.7 \
    --max-tokens 2048 \
    --api-base "http://localhost:$PORT/v1" \
    --model auto \
    --seed 42 \
    --data data/strategyqa_200.json \
    --output "$RESULTS_DIR/exp017_results.json" \
    --save-intermediates

# Step 4: Cleanup
echo "=== [$(date)] Stopping vLLM ==="
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true
echo "EXP017_DONE"
