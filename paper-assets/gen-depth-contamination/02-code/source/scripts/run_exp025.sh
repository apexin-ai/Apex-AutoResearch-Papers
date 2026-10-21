#!/bin/bash
# exp-025: Pythia-1.4B filtering validation
# 9 runs (3 strategies x 3 seeds) on 4x 4090D
#
# Batch 1 (cuda:0-3): no_filter x3 + binary_ours seed42
# Batch 2 (cuda:0-3): binary_ours x2 + graduated_a09 x2
# Batch 3 (cuda:0):   graduated_a09 seed456

set -e
cd /root/autodl-tmp/gen-depth-contamination

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

LOG_DIR="logs/exp025"
mkdir -p "$LOG_DIR"

echo "[$(date)] Starting exp-025 Pythia-1.4B filtering experiments..."
echo "Config: LoRA rank=8 alpha=16, 3 strategies x 3 seeds = 9 runs"
echo ""

# --- Batch 1: 4 parallel runs ---
echo "[$(date)] Batch 1: no_filter x3 + binary_ours seed42"

python scripts/exp025_pythia_filtering.py \
    --strategy no_filter --seed 42 --device cuda:0 \
    > "$LOG_DIR/no_filter_seed42.log" 2>&1 &
PID1=$!

python scripts/exp025_pythia_filtering.py \
    --strategy no_filter --seed 123 --device cuda:1 \
    > "$LOG_DIR/no_filter_seed123.log" 2>&1 &
PID2=$!

python scripts/exp025_pythia_filtering.py \
    --strategy no_filter --seed 456 --device cuda:2 \
    > "$LOG_DIR/no_filter_seed456.log" 2>&1 &
PID3=$!

python scripts/exp025_pythia_filtering.py \
    --strategy binary_ours --seed 42 --device cuda:3 \
    > "$LOG_DIR/binary_ours_seed42.log" 2>&1 &
PID4=$!

echo "  PIDs: $PID1 $PID2 $PID3 $PID4"
wait $PID1 $PID2 $PID3 $PID4
echo "[$(date)] Batch 1 complete."
echo ""

# --- Batch 2: 4 parallel runs ---
echo "[$(date)] Batch 2: binary_ours x2 + graduated_a09 x2"

python scripts/exp025_pythia_filtering.py \
    --strategy binary_ours --seed 123 --device cuda:0 \
    > "$LOG_DIR/binary_ours_seed123.log" 2>&1 &
PID5=$!

python scripts/exp025_pythia_filtering.py \
    --strategy binary_ours --seed 456 --device cuda:1 \
    > "$LOG_DIR/binary_ours_seed456.log" 2>&1 &
PID6=$!

python scripts/exp025_pythia_filtering.py \
    --strategy graduated_a09 --seed 42 --device cuda:2 \
    > "$LOG_DIR/graduated_a09_seed42.log" 2>&1 &
PID7=$!

python scripts/exp025_pythia_filtering.py \
    --strategy graduated_a09 --seed 123 --device cuda:3 \
    > "$LOG_DIR/graduated_a09_seed123.log" 2>&1 &
PID8=$!

echo "  PIDs: $PID5 $PID6 $PID7 $PID8"
wait $PID5 $PID6 $PID7 $PID8
echo "[$(date)] Batch 2 complete."
echo ""

# --- Batch 3: 1 run ---
echo "[$(date)] Batch 3: graduated_a09 seed456"

python scripts/exp025_pythia_filtering.py \
    --strategy graduated_a09 --seed 456 --device cuda:0 \
    > "$LOG_DIR/graduated_a09_seed456.log" 2>&1
echo "[$(date)] Batch 3 complete."
echo ""

# --- Summary ---
echo "=========================================="
echo "  exp-025 Results Summary"
echo "=========================================="
python3 -c "
import json, numpy as np
from pathlib import Path

results_dir = Path('results/exp_025_pythia_filtering')
strategies = ['no_filter', 'binary_ours', 'graduated_a09']
seeds = [42, 123, 456]

print(f\"{'Strategy':<18} {'Seed':<6} {'MMLU':<10} {'HellaSwag':<10}\")
print('-' * 48)

for strategy in strategies:
    mmlu_vals, hs_vals = [], []
    for seed in seeds:
        ep = results_dir / f'{strategy}_seed{seed}' / 'eval_results.json'
        if ep.exists():
            d = json.load(open(ep))
            m = d['scores'].get('mmlu', 0)
            h = d['scores'].get('hellaswag', 0)
            mmlu_vals.append(m)
            hs_vals.append(h)
            print(f'{strategy:<18} {seed:<6} {m:<10.4f} {h:<10.4f}')
        else:
            print(f'{strategy:<18} {seed:<6} MISSING    MISSING')
    if mmlu_vals:
        print(f'  mean +/- std     {\"\":<6} '
              f'{np.mean(mmlu_vals):.4f}+/-{np.std(mmlu_vals):.4f} '
              f'{np.mean(hs_vals):.4f}+/-{np.std(hs_vals):.4f}')
    print()

# Cross-strategy comparison
if all((results_dir / f'{s}_seed{sd}' / 'eval_results.json').exists()
       for s in strategies for sd in seeds):
    print('--- Comparisons ---')
    for metric in ['mmlu', 'hellaswag']:
        vals = {}
        for s in strategies:
            vals[s] = [json.load(open(results_dir / f'{s}_seed{sd}' / 'eval_results.json'))
                       ['scores'][metric] for sd in seeds]
        nf = np.mean(vals['no_filter'])
        bo = np.mean(vals['binary_ours'])
        ga = np.mean(vals['graduated_a09'])
        print(f'{metric}: binary_ours - no_filter = {bo - nf:+.4f}')
        print(f'{metric}: graduated   - no_filter = {ga - nf:+.4f}')
"

echo ""
echo "[$(date)] All exp-025 experiments complete!"
