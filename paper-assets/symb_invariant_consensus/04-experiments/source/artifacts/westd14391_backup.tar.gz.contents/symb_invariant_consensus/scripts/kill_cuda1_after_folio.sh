#!/bin/bash
# Guard: kill cuda:1 master (PID 510872) after FOLIO seed=789 completes

TARGET_PID=510872
WATCH_DIR="/root/symb_invariant_consensus/results/multi_seed/qwen25_folio_seed789/intermediates"
THRESHOLD=204
LOG="/tmp/cuda1_folio_guard.log"

echo "[$(date)] Guard started. Watching $WATCH_DIR for >= $THRESHOLD files. Target PID=$TARGET_PID" >> "$LOG"

while true; do
    # Check if target process still alive
    if ! kill -0 "$TARGET_PID" 2>/dev/null; then
        echo "[$(date)] Target PID $TARGET_PID no longer exists. Guard exiting." >> "$LOG"
        exit 0
    fi

    # Count intermediate json files
    if [ -d "$WATCH_DIR" ]; then
        COUNT=$(find "$WATCH_DIR" -name "*.json" -type f | wc -l)
    else
        COUNT=0
    fi

    echo "[$(date)] File count: $COUNT / $THRESHOLD" >> "$LOG"

    if [ "$COUNT" -ge "$THRESHOLD" ]; then
        echo "[$(date)] FOLIO seed=789 complete ($COUNT files). Killing PID $TARGET_PID..." >> "$LOG"
        kill "$TARGET_PID" 2>/dev/null
        sleep 2
        # Force kill if still alive
        if kill -0 "$TARGET_PID" 2>/dev/null; then
            echo "[$(date)] Process still alive, sending SIGKILL..." >> "$LOG"
            kill -9 "$TARGET_PID" 2>/dev/null
        fi
        echo "[$(date)] Done. Guard exiting." >> "$LOG"
        exit 0
    fi

    sleep 60
done
