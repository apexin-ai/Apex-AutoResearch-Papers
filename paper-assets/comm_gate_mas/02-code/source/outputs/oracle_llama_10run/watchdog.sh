#!/bin/bash
BASH_PID=84280
LOG_FILE="$(dirname "$0")/run.log"
CRASH_MARKER="/tmp/tost_crashed"
CHECK_INTERVAL=1800  # 30 minutes

while true; do
    sleep $CHECK_INTERVAL

    # Check 1: bash wrapper alive?
    if ! ps -p $BASH_PID -o pid= >/dev/null 2>&1; then
        # Wrapper exited — check if all 10 seeds completed (normal exit)
        COMPLETED=$(ls "$(dirname "$0")"/seed_*.json 2>/dev/null | grep -v partial | wc -l | tr -d ' ')
        if [ "$COMPLETED" -ge 10 ]; then
            echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) watchdog: all 10 seeds complete, exiting normally" >> "$(dirname "$0")/watchdog.log"
            exit 0
        fi
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) CRASH: bash wrapper PID $BASH_PID dead, only $COMPLETED/10 seeds complete" | tee -a "$(dirname "$0")/watchdog.log"
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) CRASH: $COMPLETED/10 seeds" > "$CRASH_MARKER"
        exit 1
    fi

    # Check 2: log updated in last 45 min? (allows for slow tasks)
    if [ -f "$LOG_FILE" ]; then
        LOG_AGE=$(( $(date +%s) - $(stat -f %m "$LOG_FILE") ))
        if [ "$LOG_AGE" -gt 2700 ]; then
            echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) STALL: log not updated for ${LOG_AGE}s" | tee -a "$(dirname "$0")/watchdog.log"
            echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) STALL: log stale ${LOG_AGE}s" > "$CRASH_MARKER"
            exit 1
        fi
    fi

    # Status heartbeat
    COMPLETED=$(ls "$(dirname "$0")"/seed_*.json 2>/dev/null | grep -v partial | wc -l | tr -d ' ')
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) heartbeat: $COMPLETED/10 seeds, PID $BASH_PID alive" >> "$(dirname "$0")/watchdog.log"
done
