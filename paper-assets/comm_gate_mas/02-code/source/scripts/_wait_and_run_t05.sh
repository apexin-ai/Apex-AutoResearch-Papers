#!/bin/bash
# Wait for PID 201227 (P1: qwen_t03_seed42) to finish, then launch t=0.5 StratQA 5-seed
set -euo pipefail

TARGET_PID=201227
MAX_WAIT=1500  # 25 minutes
INTERVAL=30
WAITED=0

echo "[$(date -u '+%H:%M:%S UTC')] Waiting for PID $TARGET_PID to finish..."

while kill -0 "$TARGET_PID" 2>/dev/null; do
    WAITED=$((WAITED + INTERVAL))
    if [ "$WAITED" -ge "$MAX_WAIT" ]; then
        echo "[$(date -u '+%H:%M:%S UTC')] TIMEOUT: PID $TARGET_PID still running after ${MAX_WAIT}s"
        exit 1
    fi
    echo "[$(date -u '+%H:%M:%S UTC')] PID $TARGET_PID still running, waited ${WAITED}s/${MAX_WAIT}s"
    sleep "$INTERVAL"
done

echo "[$(date -u '+%H:%M:%S UTC')] PID $TARGET_PID finished. Starting t=0.5 StratQA 5-seed..."
sleep 5

exec bash /root/autodl-tmp/comm_gate_mas/scripts/run_heuristic_qwen_stratqa_t05_5seed.sh
