#!/bin/bash
# Monitor d000_s42 original completion, then kill "both" mode and restart as original-only
set -euo pipefail

MARKER=/root/autodl-tmp/exp001/eval_results/Qwen2.5-7B_d000_s42_aligned/eval_results.json
LOGDIR=/root/autodl-tmp/exp001/logs

echo "[$(date)] Waiting for d000_s42 original to complete (watching $MARKER)..."

while [ ! -f "$MARKER" ]; do
    sleep 60
done

echo "[$(date)] d000_s42 original complete. Killing both-mode process..."

# Kill the parent bash script (run_aligned_eval_7B.sh both)
pkill -f "run_aligned_eval_7B.sh both" || true
sleep 5
# Make sure python children are dead too
pkill -f "evaluate.py.*d000_s42.*aligned" || true
sleep 3

echo "[$(date)] Starting original-only eval..."
CUDA_VISIBLE_DEVICES=0 bash /root/contamcal-irt-calibration/exp001/run_aligned_eval_7B.sh original >> "$LOGDIR/eval_7b_original_only.log" 2>&1
echo "[$(date)] Original-only eval finished."
