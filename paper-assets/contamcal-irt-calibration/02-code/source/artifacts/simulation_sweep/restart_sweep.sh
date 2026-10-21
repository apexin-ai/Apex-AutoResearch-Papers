#!/bin/bash
# Wait for current seed to finish, then kill sweep and restart with new condition order.
set -e

SWEEP_PID=340553
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RESULTS_DIR="$SCRIPT_DIR/results"
CONDITION_FILE="$RESULTS_DIR/auc0.55_n100_prior1.0_binary.json"
VENV="/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.venv/bin/activate"

count_seeds() {
    python3 -c "
import json
with open('$CONDITION_FILE') as f:
    data = json.load(f)
print(len(data['runs']))
" 2>/dev/null || echo "0"
}

INITIAL_SEEDS=$(count_seeds)
echo "[$(date +%H:%M:%S)] Current seeds saved: $INITIAL_SEEDS. Waiting for seed $INITIAL_SEEDS to complete..."

# Poll every 5 seconds for the JSON file to update
while true; do
    CURRENT_SEEDS=$(count_seeds)
    if [ "$CURRENT_SEEDS" -gt "$INITIAL_SEEDS" ] 2>/dev/null; then
        echo "[$(date +%H:%M:%S)] Seed saved! Now $CURRENT_SEEDS seeds. Killing sweep immediately..."
        break
    fi

    # Also check if sweep already exited
    if ! kill -0 $SWEEP_PID 2>/dev/null; then
        echo "[$(date +%H:%M:%S)] Sweep already exited."
        break
    fi

    sleep 5
done

# Kill the sweep process and any children
if kill -0 $SWEEP_PID 2>/dev/null; then
    echo "[$(date +%H:%M:%S)] Sending SIGTERM to sweep PID $SWEEP_PID..."
    kill $SWEEP_PID 2>/dev/null || true
    sleep 3

    # Kill any orphaned Stan processes from this sweep
    for cpid in $(pgrep -P $SWEEP_PID 2>/dev/null); do
        echo "  Killing child PID $cpid"
        kill $cpid 2>/dev/null || true
    done

    # Force kill if still alive
    if kill -0 $SWEEP_PID 2>/dev/null; then
        echo "  Force killing PID $SWEEP_PID"
        kill -9 $SWEEP_PID 2>/dev/null || true
    fi
    echo "[$(date +%H:%M:%S)] Sweep terminated."
fi

# Also kill any orphaned contam_irt_4pl_sweep processes from the old sweep
for pid in $(pgrep -f "contam_irt_4pl_sweep.*seed="); do
    # Only kill sweep processes, not other experiments
    CMD=$(ps -p $pid -o cmd= 2>/dev/null)
    if echo "$CMD" | grep -q "simulation_sweep/contam_irt_4pl_sweep"; then
        echo "  Killing orphan Stan PID $pid"
        kill $pid 2>/dev/null || true
    fi
done

sleep 2

# Restart with new condition order (AUC=0.80 first)
echo "[$(date +%H:%M:%S)] Restarting sweep with AUC=0.80 priority..."
cd "$SCRIPT_DIR"
source "$VENV"
nohup python run_sweep.py subset > /tmp/sweep_restart.log 2>&1 &
NEW_PID=$!
echo "[$(date +%H:%M:%S)] New sweep started: PID $NEW_PID"
echo "Log: /tmp/sweep_restart.log"
echo "RESTART_DONE"
