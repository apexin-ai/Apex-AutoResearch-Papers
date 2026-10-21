#!/bin/bash
# Ack injection causal intervention — Llama×GSM8K, 5-seed (42,123,456,789,1024)
# Uses CUDA:1, starts vLLM internally, runs all seeds sequentially.
# Usage: bash scripts/run_llama_injection_5seed.sh [--force]

set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1
: "${OPENAI_API_KEY:[REDACTED] OPENAI_API_KEY not set. Source ~/.bashrc first.}"
export ORACLE_BASE_URL="http://47.94.22.126/v1"
export ORACLE_MODEL="openai/gpt-4o"

FORCE=0
if [[ "${1:-}" == "--force" ]]; then
    FORCE=1
fi

MODEL_PATH="/root/autodl-tmp/models/Llama-3.1-8B-Instruct"
PORT=8001
CONFIG="configs/ack_injection_llama_gsm8k.yaml"
NUM_TASKS=300
SEEDS=(42 123 456 789 1024)
OUTDIR="outputs/llama_injection_5seed"
GPU=1

if [ ! -d "$MODEL_PATH" ]; then
    echo "ERROR: Llama model not found at $MODEL_PATH"
    exit 1
fi

if pgrep -f "ack_injection.py.*ack_injection_llama" > /dev/null 2>&1; then
    echo "ABORT: injection experiment already running"
    exit 1
fi

mkdir -p "$OUTDIR"

# --- Start vLLM on GPU $GPU ---
echo "=== Starting vLLM: model=$MODEL_PATH port=$PORT gpu=$GPU ==="
CUDA_VISIBLE_DEVICES=$GPU python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "Llama-3.1-8B-Instruct" \
    --port "$PORT" \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --trust-remote-code &
VLLM_PID=$!

echo "=== Waiting for vLLM (PID: $VLLM_PID) ==="
HEALTH_URL="http://127.0.0.1:${PORT}/health"
TIMEOUT_SECS=300
POLL_INTERVAL=5
ELAPSED=0

while [ "$ELAPSED" -lt "$TIMEOUT_SECS" ]; do
    if curl -sf "$HEALTH_URL" >/dev/null 2>&1; then
        echo "vLLM ready after ${ELAPSED}s"
        break
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
        echo "ERROR: vLLM process died"
        exit 1
    fi
    sleep "$POLL_INTERVAL"
    ELAPSED=$((ELAPSED + POLL_INTERVAL))
done

if ! curl -sf "$HEALTH_URL" >/dev/null 2>&1; then
    echo "ERROR: vLLM failed to start within ${TIMEOUT_SECS}s"
    kill "$VLLM_PID" 2>/dev/null || true
    exit 1
fi

echo "=== Preflight: testing model endpoint ==="
if ! curl -sf "http://127.0.0.1:${PORT}/v1/models" >/dev/null 2>&1; then
    echo "PREFLIGHT FAILED: vLLM not reachable"
    kill "$VLLM_PID" 2>/dev/null || true
    exit 1
fi
echo "Preflight passed"

# --- Run 5 seeds ---
COMPLETED=0
SKIPPED=0
T_TOTAL_START=$(date +%s)

for SEED in "${SEEDS[@]}"; do
    OUTFILE="$OUTDIR/seed_${SEED}.json"
    LOGFILE="$OUTDIR/seed_${SEED}.log"

    if [[ -f "$OUTFILE" && "$FORCE" -eq 0 ]]; then
        echo "[skip] seed=$SEED already exists: $OUTFILE"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    echo "========================================="
    echo "[run] seed=$SEED num_tasks=$NUM_TASKS ($(date '+%H:%M:%S'))"
    echo "========================================="

    python3 src/ack_injection.py \
        --config "$CONFIG" \
        --num-tasks "$NUM_TASKS" \
        --data-seed "$SEED" \
        --output "$OUTFILE" \
        2>&1 | tee "$LOGFILE"

    echo "[done] seed=$SEED → $OUTFILE ($(date '+%H:%M:%S'))"
    COMPLETED=$((COMPLETED + 1))
done

T_TOTAL_END=$(date +%s)
T_TOTAL=$((T_TOTAL_END - T_TOTAL_START))

# --- Shutdown vLLM ---
echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true

echo ""
echo "Finished: $COMPLETED completed, $SKIPPED skipped, total ${T_TOTAL}s"

# --- Aggregate ---
echo "=== Aggregating results ==="
python3 -c "
import json, glob, numpy as np
files = sorted(glob.glob('$OUTDIR/seed_*.json'))
print(f'Found {len(files)} result files')
ctrl_accs, inj_accs, deltas, ps = [], [], [], []
for f in files:
    d = json.load(open(f))
    ca = d['control']['accuracy'] * 100
    ia = d['inject']['accuracy'] * 100
    dp = d['delta_pp']
    mp = d.get('mcnemar_p')
    ctrl_accs.append(ca)
    inj_accs.append(ia)
    deltas.append(dp)
    ps.append(mp)
    print(f'  {f}: ctrl={ca:.1f}% inj={ia:.1f}% delta={dp:+.1f}pp p={mp}')
print(f'Mean: ctrl={np.mean(ctrl_accs):.1f}% inj={np.mean(inj_accs):.1f}%')
print(f'Mean delta: {np.mean(deltas):+.2f}pp +/- {np.std(deltas, ddof=1):.2f}pp')
print(f'Range: [{min(deltas):+.1f}, {max(deltas):+.1f}]pp')
"

echo "=== Llama×GSM8K 5-seed ack injection finished ==="
