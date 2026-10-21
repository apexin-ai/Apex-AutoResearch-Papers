#!/bin/bash
set -e

CONFIG_BASENAME=$(basename "configs/llama_length_only_gsm8k.yaml")
if pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}" > /dev/null 2>&1; then
    echo "ABORT: instance already running ($(pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}"))"
    exit 1
fi

cd /Users/agent-001/.agent-ml-research/projects/comm_gate_mas

OUTPUT_DIR="outputs/llama_length_only_gsm8k"
mkdir -p "$OUTPUT_DIR"

for SEED in 42 123 456; do
    echo "=== Running seed $SEED ==="
    python3 src/pruning_validation.py \
        --mode online_pruning \
        --config configs/llama_length_only_gsm8k.yaml \
        --num-tasks 200 \
        --data-seed $SEED \
        --detection-mode length_only \
        --char-threshold 30 \
        --output "$OUTPUT_DIR/seed_${SEED}.json" \
        2>&1 | tee "$OUTPUT_DIR/seed_${SEED}.log"
    echo "=== Seed $SEED complete ==="
done

echo "ALL_SEEDS_DONE"

# Aggregate results
python3 -c "
import json, glob, numpy as np
files = sorted(glob.glob('$OUTPUT_DIR/seed_*.json'))
deltas = []
for f in files:
    with open(f) as fh:
        d = json.load(fh)
    bl = d['baseline']['accuracy'] * 100
    pr = d['online_pruned']['accuracy'] * 100
    delta = d['delta_pp']
    deltas.append(delta)
    supp = d['online_pruned'].get('suppress_pct', 0)
    print(f'{f}: baseline={bl:.1f}%, pruned={pr:.1f}%, delta={delta:+.1f}pp, suppress={supp:.1f}%')
print(f'Mean delta: {np.mean(deltas):+.2f}pp, SD: {np.std(deltas, ddof=1):.2f}')
"
