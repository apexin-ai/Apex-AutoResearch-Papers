#!/bin/bash
# Auto-restart wrapper for oracle_qwen72b_n500 experiment.
# Handles semaphore leak crashes in Python 3.14 by restarting from checkpoint.
set -u
cd /Users/agent-001/.agent-ml-research/projects/comm_gate_mas

OUTPUT="outputs/oracle_qwen72b_n500/seed_42.json"
PARTIAL="${OUTPUT%.json}_partial.json"
LOG="outputs/oracle_qwen72b_n500/run_resume.log"
MAX_RESTARTS=50
restart_count=0

while [ ! -f "$OUTPUT" ] && [ "$restart_count" -lt "$MAX_RESTARTS" ]; do
    restart_count=$((restart_count + 1))
    echo "=== Restart #$restart_count at $(date) ===" >> "$LOG"

    python3 src/pruning_validation.py \
        --mode online_oracle \
        --config configs/oracle_qwen72b_gsm8k_n500.yaml \
        --detection-mode oracle_5class \
        --num-tasks 500 \
        --data-seed 42 \
        --output "$OUTPUT" >> "$LOG" 2>&1

    exit_code=$?
    echo "=== Process exited with code $exit_code at $(date) ===" >> "$LOG"

    if [ -f "$OUTPUT" ]; then
        echo "=== Experiment complete! ===" >> "$LOG"
        break
    fi

    if [ -f "$PARTIAL" ]; then
        completed=$(python3 -c "import json; print(json.load(open('$PARTIAL'))['total'])" 2>/dev/null || echo "?")
        echo "=== Checkpoint: $completed/500 tasks. Restarting in 5s... ===" >> "$LOG"
    fi
    sleep 5
done

echo "=== Wrapper finished: $restart_count restarts ===" >> "$LOG"
