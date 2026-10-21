#!/bin/bash
# EXP-C: Pruning Rate Sensitivity Sweep
# 5 rates × 3 seeds = 15 runs
set -e

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

cd /root/autodl-tmp/comm_gate_mas
RATES="0.0 0.25 0.5 0.75 1.0"
SEEDS="42 0 1"
OUTPUT_BASE="outputs/pruning_rate_sweep"

mkdir -p $OUTPUT_BASE

for rate in $RATES; do
    for seed in $SEEDS; do
        rate_pct=$(python3 -c "print(int($rate * 100))")
        output="${OUTPUT_BASE}/rate${rate_pct}_seed${seed}.json"
        
        if [ -f "$output" ]; then
            echo "SKIP: $output already exists"
            continue
        fi
        
        echo "=== Running rate=$rate seed=$seed ==="
        python3 src/pruning_validation.py \
            --mode online_pruning \
            --config configs/oracle_qwen_gsm8k_local.yaml \
            --num-tasks 300 \
            --detection-mode heuristic \
            --pruning-mode skip \
            --ack-prune-rate $rate \
            --data-seed $seed \
            --output "$output"
        
        echo "DONE: rate=$rate seed=$seed → $output"
    done
done

echo "=== ALL 15 RUNS DONE ==="

# Aggregate results
python3 -c "
import json, glob, os
results = []
for f in sorted(glob.glob('${OUTPUT_BASE}/rate*_seed*.json')):
    with open(f) as fh:
        data = json.load(fh)
    fname = os.path.basename(f)
    rate = int(fname.split('rate')[1].split('_')[0])
    seed = int(fname.split('seed')[1].split('.')[0])
    bl = data.get('baseline', {})
    pr = data.get('online_pruned', {})
    results.append({
        'rate': rate, 'seed': seed,
        'baseline_acc': bl.get('accuracy'),
        'pruned_acc': pr.get('accuracy'),
        'n_tasks': data.get('total_completed'),
        'suppress_pct': pr.get('suppress_pct'),
        'delta_pp': data.get('delta_pp'),
    })
with open('${OUTPUT_BASE}/sweep_summary.json', 'w') as f:
    json.dump(results, f, indent=2)
print(json.dumps(results, indent=2))
"
