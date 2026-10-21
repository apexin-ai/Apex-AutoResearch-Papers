#!/bin/bash
# DistilBERT t=0.7 Llama GSM8K pruning: 3 seeds (42/123/456), N=100 per seed
# GPU 2 (port 8002): seeds 42, 456 serial
# GPU 3 (port 8003): seed 123
# Self-contained: starts vLLM, dry-runs, runs experiments, kills vLLM on exit.
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

MODEL_PATH="/root/autodl-tmp/models/Llama-3.1-8B-Instruct"
BASE_CONFIG="configs/llama_gsm8k_rr_temp07.yaml"
CHECKPOINT="artifacts/classifier/distilbert_ack/checkpoint-810"
NUM_TASKS=100
OUTDIR="outputs/distilbert_t07_llama_gsm8k"
LOGDIR="logs"
EXP_ID="distilbert_t07_llama_gsm8k"

mkdir -p "$OUTDIR" "$LOGDIR"

# Create per-port configs
sed 's|localhost:8001|localhost:8002|' "$BASE_CONFIG" > "configs/_tmp_t07_port8002.yaml"
sed 's|localhost:8001|localhost:8003|' "$BASE_CONFIG" > "configs/_tmp_t07_port8003.yaml"

VLLM_PIDS=()
cleanup() {
    echo "Cleaning up vLLM processes..."
    for pid in "${VLLM_PIDS[@]}"; do
        kill "$pid" 2>/dev/null || true
        wait "$pid" 2>/dev/null || true
    done
    rm -f configs/_tmp_t07_port8002.yaml configs/_tmp_t07_port8003.yaml
}
trap cleanup EXIT

start_vllm() {
    local GPU=$1
    local PORT=$2
    echo "[$(date +%H:%M:%S)] Starting vLLM on GPU $GPU, port $PORT..."
    CUDA_VISIBLE_DEVICES=$GPU python3 -m vllm.entrypoints.openai.api_server \
        --model "$MODEL_PATH" \
        --port "$PORT" \
        --max-model-len 4096 \
        --enforce-eager \
        --served-model-name "Llama-3.1-8B-Instruct" \
        --gpu-memory-utilization 0.85 \
        > "$LOGDIR/vllm_${EXP_ID}_gpu${GPU}.log" 2>&1 &
    local PID=$!
    VLLM_PIDS+=("$PID")
    echo "[$(date +%H:%M:%S)] vLLM PID=$PID"
}

wait_vllm() {
    local PORT=$1
    local PID=$2
    for i in $(seq 1 90); do
        if ! kill -0 "$PID" 2>/dev/null; then
            echo "ABORT: vLLM on port $PORT died"
            tail -20 "$LOGDIR/vllm_${EXP_ID}_gpu"*.log 2>/dev/null || true
            return 1
        fi
        if curl -s --max-time 5 "http://localhost:$PORT/v1/models" | grep -q "Llama"; then
            echo "[$(date +%H:%M:%S)] vLLM on port $PORT ready after ${i}0s"
            return 0
        fi
        sleep 10
    done
    echo "ABORT: vLLM on port $PORT timeout after 15min"
    return 1
}

run_seed() {
    local CONFIG=$1
    local SEED=$2
    local NTASKS=$3
    local TAG=$4
    local OUTFILE="$OUTDIR/seed_${SEED}.json"
    echo ""
    echo "==========================================="
    echo "[$(date +%H:%M:%S)] [$TAG] seed=$SEED num_tasks=$NTASKS detection=distilbert"
    echo "==========================================="
    python3 src/pruning_validation.py \
        --mode online_pruning \
        --config "$CONFIG" \
        --num-tasks "$NTASKS" \
        --data-seed "$SEED" \
        --detection-mode distilbert \
        --distilbert-checkpoint "$CHECKPOINT" \
        --pruning-mode skip \
        --output "$OUTFILE" \
        2>&1 | tee "$OUTDIR/seed_${SEED}.log"
    echo "[$(date +%H:%M:%S)] [$TAG] seed=$SEED done → $OUTFILE"
}

# === Phase 1: Start both vLLM servers ===
echo "=== Starting vLLM servers ==="
start_vllm 2 8002
start_vllm 3 8003

wait_vllm 8002 "${VLLM_PIDS[0]}" || exit 1
wait_vllm 8003 "${VLLM_PIDS[1]}" || exit 1
echo ""

# === Phase 2: Dry-run (2 tasks on GPU 2) ===
echo "=== Dry-run: 2 tasks on port 8002 ==="
python3 src/pruning_validation.py \
    --mode online_pruning \
    --config "configs/_tmp_t07_port8002.yaml" \
    --num-tasks 2 \
    --data-seed 42 \
    --detection-mode distilbert \
    --distilbert-checkpoint "$CHECKPOINT" \
    --pruning-mode skip \
    --output "$OUTDIR/_dryrun.json" \
    2>&1 | tail -20
DRY_EXIT=$?
if [ $DRY_EXIT -ne 0 ]; then
    echo "ABORT: dry-run failed (exit=$DRY_EXIT)"
    exit 1
fi
echo "[$(date +%H:%M:%S)] Dry-run passed"
rm -f "$OUTDIR/_dryrun.json"
echo ""

# === Phase 3: Full experiments (parallel GPU 2 + GPU 3) ===
echo "=== Full experiments starting at $(date) ==="

# GPU 2: seeds 42, 456 (serial)
(
    run_seed "configs/_tmp_t07_port8002.yaml" 42 $NUM_TASKS "GPU2"
    run_seed "configs/_tmp_t07_port8002.yaml" 456 $NUM_TASKS "GPU2"
) &
PID_GPU2=$!

# GPU 3: seed 123
(
    run_seed "configs/_tmp_t07_port8003.yaml" 123 $NUM_TASKS "GPU3"
) &
PID_GPU3=$!

wait $PID_GPU2
EC2=$?
wait $PID_GPU3
EC3=$?

echo ""
echo "=== GPU2 exit=$EC2, GPU3 exit=$EC3 ==="

# === Phase 4: Aggregate results ===
echo ""
echo "=== Results ==="
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
if len(deltas) >= 2:
    print(f'Mean delta: {np.mean(deltas):+.2f}pp +/- {np.std(deltas, ddof=1):.2f}pp')
    safe = np.mean(deltas) > -3
    print(f'Safe (delta > -3pp): {safe}')
else:
    print(f'Mean delta: {np.mean(deltas):+.2f}pp (only {len(deltas)} seed)')
"
echo ""
echo "=== ALL DONE at $(date) ==="
