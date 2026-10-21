#!/bin/bash
# DistilBERT + Llama GSM8K online pruning: 3-seed replication (0, 1, 2), N=300 per seed
# Self-contained: starts vLLM, waits for ready, runs experiment, kills vLLM on exit.
# Usage: bash scripts/run_distilbert_llama_gsm8k.sh [--force]

set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

FORCE=0
if [[ "${1:-}" == "--force" ]]; then
    FORCE=1
fi

MODEL_PATH="/root/autodl-tmp/models/Llama-3.1-8B-Instruct"
VLLM_PORT=8000
VLLM_GPU=0
CONFIG="configs/llama_gsm8k_rr_online.yaml"
CHECKPOINT="artifacts/classifier/distilbert_ack/checkpoint-810"
NUM_TASKS=300
SEEDS=(0 1 2)
OUTDIR="outputs/distilbert_llama_gsm8k"
LOGDIR="logs"

mkdir -p "$OUTDIR" "$LOGDIR"

# --- Guard: abort if already running ---
CONFIG_BASENAME=$(basename "$CONFIG")
if pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}.*distilbert" > /dev/null 2>&1; then
    echo "ABORT: distilbert+llama instance already running"
    exit 1
fi

# --- Start vLLM server ---
VLLM_PID=""
cleanup() {
    if [[ -n "$VLLM_PID" ]] && kill -0 "$VLLM_PID" 2>/dev/null; then
        echo "Stopping vLLM server (PID=$VLLM_PID)..."
        kill "$VLLM_PID"
        wait "$VLLM_PID" 2>/dev/null || true
    fi
}
trap cleanup EXIT

echo "Starting vLLM on GPU $VLLM_GPU, port $VLLM_PORT..."
CUDA_VISIBLE_DEVICES=$VLLM_GPU python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --port "$VLLM_PORT" \
    --max-model-len 4096 \
    --enforce-eager \
    --served-model-name "meta-llama/Llama-3.1-8B-Instruct" \
    --gpu-memory-utilization 0.85 \
    > "$LOGDIR/vllm_distilbert_llama.log" 2>&1 &
VLLM_PID=$!
echo "vLLM PID=$VLLM_PID"

# --- Wait for vLLM ready ---
echo "Waiting for vLLM on localhost:$VLLM_PORT..."
for i in $(seq 1 90); do
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
        echo "ABORT: vLLM process died. Check $LOGDIR/vllm_distilbert_llama.log"
        exit 1
    fi
    if curl -s --max-time 5 "http://localhost:$VLLM_PORT/v1/models" | grep -q "Llama"; then
        echo "vLLM ready after ${i}0s."
        break
    fi
    if [[ $i -eq 90 ]]; then
        echo "ABORT: vLLM not ready after 15 minutes"
        exit 1
    fi
    sleep 10
done

# --- Run experiments ---
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
    echo "[run] seed=$SEED num_tasks=$NUM_TASKS detection=distilbert"
    echo "========================================="
    python3 src/pruning_validation.py \
        --mode online_pruning \
        --config "$CONFIG" \
        --num-tasks "$NUM_TASKS" \
        --data-seed "$SEED" \
        --detection-mode distilbert \
        --distilbert-checkpoint "$CHECKPOINT" \
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
