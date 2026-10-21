#!/bin/bash
# Gemma GSM8K heuristic pruning: 3-seed replication (42, 123, 456), N=300 per seed
# Usage: bash scripts/run_gemma_heuristic_3seed.sh [--force]

set -euo pipefail

# AutoDL network proxy
if [ -f /etc/network_turbo ]; then
    source /etc/network_turbo
fi

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

FORCE=0
if [[ "${1:-}" == "--force" ]]; then
    FORCE=1
fi

MODEL_PATH="/root/autodl-tmp/.hf_cache/LLM-Research/gemma-2-9b-it"
CONFIG_MODEL="google/gemma-2-9b-it"
CONFIG="configs/gemma_heuristic_gsm8k_3seed.yaml"
NUM_TASKS=300
SEEDS=(42 123 456)
PORT=${PORT:-8000}
OUTDIR="outputs/gemma_heuristic_3seed"

CONFIG_BASENAME=$(basename "$CONFIG")
if pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}" > /dev/null 2>&1; then
    echo "ABORT: instance already running ($(pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}"))"
    exit 1
fi

if ! [ -d "$MODEL_PATH" ]; then
    echo "ABORT: Model not found at $MODEL_PATH"
    echo "Download with: python -c \"from modelscope import snapshot_download; snapshot_download('LLM-Research/gemma-2-9b-it', cache_dir='/root/autodl-tmp/.hf_cache')\""
    exit 1
fi

# Start vLLM if not already running
if ! curl -s --max-time 5 "http://localhost:${PORT}/v1/models" > /dev/null 2>&1; then
    echo "=== Starting vLLM on port $PORT ==="
    CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0} python3 -m vllm.entrypoints.openai.api_server \
        --model "$MODEL_PATH" \
        --served-model-name "$CONFIG_MODEL" \
        --port "$PORT" \
        --gpu-memory-utilization 0.9 \
        --max-model-len 4096 \
        --trust-remote-code &
    VLLM_PID=$!
    echo "vLLM PID: $VLLM_PID"

    echo "=== Waiting for vLLM ==="
    for i in $(seq 1 120); do
        if curl -s "http://localhost:${PORT}/health" >/dev/null 2>&1; then
            echo "vLLM ready after $((i*5))s"
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
else
    echo "=== vLLM already running on port $PORT ==="
    VLLM_PID=""
fi

# Smoke test
echo "=== Smoke test ==="
AVAILABLE=$(curl -s "http://localhost:${PORT}/v1/models" | python3 -c "import sys,json; print(' '.join(m['id'] for m in json.load(sys.stdin).get('data',[])))" 2>/dev/null)
echo "Available models: $AVAILABLE"

mkdir -p "$OUTDIR"

COMPLETED=0
SKIPPED=0

for SEED in "${SEEDS[@]}"; do
    OUTFILE="$OUTDIR/seed_${SEED}.json"
    if [[ -f "$OUTFILE" && "$FORCE" -eq 0 ]]; then
        echo "[skip] seed=$SEED already exists: $OUTFILE"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi
    echo "========================================="
    echo "[run] seed=$SEED num_tasks=$NUM_TASKS detection=heuristic char_threshold=150"
    echo "========================================="
    CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0} python3 src/pruning_validation.py \
        --mode online_pruning \
        --config "$CONFIG" \
        --num-tasks "$NUM_TASKS" \
        --data-seed "$SEED" \
        --detection-mode heuristic \
        --char-threshold 150 \
        --output "$OUTFILE" \
        2>&1 | tee "$OUTDIR/seed_${SEED}.log"
    echo "[done] seed=$SEED → $OUTFILE"
    COMPLETED=$((COMPLETED + 1))
done

echo ""
echo "Finished: $COMPLETED completed, $SKIPPED skipped"
echo "Aggregating..."

python3 -c "
import json, glob, numpy as np
files = sorted(glob.glob('$OUTDIR/seed_*.json'))
print(f'Found {len(files)} result files')
deltas = []
for f in files:
    d = json.load(open(f))
    bl = d.get('baseline', {}).get('accuracy', 0)
    pr = d.get('online_pruned', {}).get('accuracy', 0)
    if isinstance(bl, float) and bl <= 1: bl *= 100
    if isinstance(pr, float) and pr <= 1: pr *= 100
    delta = d.get('delta_pp', pr - bl)
    deltas.append(delta)
    sr = d.get('online_pruned', {}).get('suppress_pct', 0)
    print(f'  {f}: baseline={bl:.1f}% pruned={pr:.1f}% delta={delta:+.1f}pp suppress={sr:.1f}%')
print(f'Mean delta: {np.mean(deltas):+.2f}pp +/- {np.std(deltas, ddof=1):.2f}pp')
print(f'Range: [{min(deltas):+.1f}, {max(deltas):+.1f}]pp')
"

if [ -n "${VLLM_PID:-}" ]; then
    echo "=== Stopping vLLM ==="
    kill "$VLLM_PID" 2>/dev/null || true
    wait "$VLLM_PID" 2>/dev/null || true
fi
echo "=== Finished ==="
