#!/bin/bash
# Qwen t=0.3 heuristic seed 1024 — final seed for 5-seed replication
export CUDA_VISIBLE_DEVICES=0,1
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

set -euo pipefail
cd "$(dirname "$0")/.."

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CONFIG="configs/qwen_heuristic_gsm8k_t03.yaml"
NUM_TASKS=200
OUTDIR="outputs/qwen_heuristic_t03_multiseed"

# Check vLLM
if ! curl -s --max-time 5 http://localhost:8000/v1/models > /dev/null 2>&1; then
    echo "ABORT: vLLM server not responding on localhost:8000"
    exit 1
fi

mkdir -p "$OUTDIR"

SEED=1024
OUTFILE="$OUTDIR/seed_${SEED}.json"

echo "========================================="
echo "[run] seed=$SEED num_tasks=$NUM_TASKS detection=heuristic char_threshold=150"
echo "========================================="
python3 src/pruning_validation.py \
    --mode online_pruning \
    --config "$CONFIG" \
    --num-tasks "$NUM_TASKS" \
    --data-seed "$SEED" \
    --detection-mode heuristic \
    --char-threshold 150 \
    --output "$OUTFILE" \
    2>&1 | tee "$OUTDIR/seed_${SEED}.log"
echo "[done] seed=$SEED → $OUTFILE"

echo ""
echo "=== Aggregate all 5 seeds ==="
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
