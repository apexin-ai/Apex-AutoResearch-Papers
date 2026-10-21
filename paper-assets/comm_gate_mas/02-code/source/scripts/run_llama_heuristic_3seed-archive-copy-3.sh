#!/bin/bash
# Llama GSM8K heuristic pruning: 3-seed replication (42, 123, 456), N=200 per seed
# Usage: bash scripts/run_llama_heuristic_3seed.sh [--force]

set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

FORCE=0
if [[ "${1:-}" == "--force" ]]; then
    FORCE=1
fi

CONFIG="configs/llama_heuristic_gsm8k_3seed.yaml"
NUM_TASKS=200
SEEDS=(42 123 456)
OUTDIR="outputs/llama_heuristic_3seed"

CONFIG_BASENAME=$(basename "$CONFIG")
if pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}" > /dev/null 2>&1; then
    echo "ABORT: instance already running ($(pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}"))"
    exit 1
fi

if ! curl -s --max-time 5 http://localhost:8001/v1/models > /dev/null 2>&1; then
    echo "ABORT: vLLM server not responding on localhost:8001"
    exit 1
fi

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
    echo "[run] seed=$SEED num_tasks=$NUM_TASKS detection=heuristic"
    echo "========================================="
    CUDA_VISIBLE_DEVICES=1 python3 src/pruning_validation.py \
        --mode online_pruning \
        --config "$CONFIG" \
        --num-tasks "$NUM_TASKS" \
        --data-seed "$SEED" \
        --detection-mode heuristic \
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
