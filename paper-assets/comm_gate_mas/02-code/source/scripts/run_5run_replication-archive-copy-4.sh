#!/bin/bash
# 5-run replication: Qwen GSM8K online pruning with different data seeds.
# Each run: paired baseline + heuristic pruned, N=200.
# Usage: bash scripts/run_5run_replication.sh [config] [num_tasks]

set -e

CONFIG_BASENAME=$(basename "${1:-configs/qwen_gsm8k_rr_replication.yaml}")
if pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}" > /dev/null 2>&1; then
    echo "ABORT: instance already running ($(pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}"))"
    exit 1
fi

CONFIG="${1:-configs/qwen_gsm8k_rr_replication.yaml}"
NUM_TASKS="${2:-200}"
SEEDS=(42 123 456 789 1024)
OUTDIR="outputs/replication_5run"

mkdir -p "$OUTDIR"

for SEED in "${SEEDS[@]}"; do
    OUTFILE="$OUTDIR/seed_${SEED}.json"
    if [ -f "$OUTFILE" ]; then
        echo "[skip] seed=$SEED already exists: $OUTFILE"
        continue
    fi
    echo "========================================="
    echo "[run] seed=$SEED num_tasks=$NUM_TASKS"
    echo "========================================="
    python3 src/pruning_validation.py \
        --mode online_pruning \
        --config "$CONFIG" \
        --num-tasks "$NUM_TASKS" \
        --data-seed "$SEED" \
        --char-threshold 30 \
        --output "$OUTFILE"
    echo "[done] seed=$SEED → $OUTFILE"
done

echo ""
echo "All 5 runs complete. Aggregating..."
python3 -c "
import json, glob, numpy as np
files = sorted(glob.glob('$OUTDIR/seed_*.json'))
print(f'Found {len(files)} result files')
deltas = []
for f in files:
    d = json.load(open(f))
    bl = d.get('baseline', {}).get('accuracy', 0)
    sk = d.get('online_pruned', {}).get('accuracy', 0)
    if isinstance(bl, float) and bl <= 1: bl *= 100
    if isinstance(sk, float) and sk <= 1: sk *= 100
    delta = sk - bl
    deltas.append(delta)
    sr = d.get('online_pruned', {}).get('suppress_pct', 0)
    print(f'  {f}: baseline={bl:.1f}% skip={sk:.1f}% Δ={delta:+.1f}pp suppress={sr:.1f}%')
print(f'Mean Δ: {np.mean(deltas):+.2f}pp ± {np.std(deltas, ddof=1):.2f}pp')
print(f'Range: [{min(deltas):+.1f}, {max(deltas):+.1f}]pp')
"
