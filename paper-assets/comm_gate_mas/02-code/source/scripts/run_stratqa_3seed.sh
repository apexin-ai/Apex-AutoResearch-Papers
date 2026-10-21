#!/bin/bash
# Llama StratQA heuristic pruning: 3-seed replication (0, 1, 2), N=200 per seed
# seed=42 already completed → outputs/llama_heuristic_stratqa.json
# Usage: bash scripts/run_stratqa_3seed.sh

set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

CONFIG="configs/llama_stratqa_rr_online.yaml"
NUM_TASKS=200
SEEDS=(0 1 2)
OUTDIR="outputs/llama_heuristic_stratqa_3seed"

# Pre-flight: check vLLM
if ! curl -s --max-time 5 http://localhost:8001/v1/models > /dev/null 2>&1; then
    echo "ABORT: vLLM server not responding on localhost:8001"
    exit 1
fi

mkdir -p "$OUTDIR"

COMPLETED=0
FAILED=0

for SEED in "${SEEDS[@]}"; do
    OUTFILE="$OUTDIR/seed_${SEED}.json"
    if [[ -f "$OUTFILE" ]]; then
        echo "[skip] seed=$SEED already exists: $OUTFILE"
        continue
    fi
    echo "========================================="
    echo "[run] seed=$SEED num_tasks=$NUM_TASKS detection=heuristic"
    echo "========================================="
    if CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0} python3 src/pruning_validation.py \
        --mode online_pruning \
        --config "$CONFIG" \
        --num-tasks "$NUM_TASKS" \
        --data-seed "$SEED" \
        --detection-mode heuristic \
        --output "$OUTFILE" \
        2>&1 | tee "$OUTDIR/seed_${SEED}.log"; then
        echo "[done] seed=$SEED → $OUTFILE"
        COMPLETED=$((COMPLETED + 1))
    else
        echo "[FAIL] seed=$SEED failed (exit=$?)"
        FAILED=$((FAILED + 1))
    fi
done

echo ""
echo "Finished: $COMPLETED completed, $FAILED failed"

# Aggregate results
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
