#!/bin/bash
cd .

TARGET=57600
MODELS=("llama" "mistral" "qwen" "gemma")

echo "$(date) — Monitor started. Waiting for MATH to finish (target=$TARGET per model)."

while true; do
    # Check if any MATH python processes still running
    MATH_PROCS=$(pgrep -fc "run_experiment.*math" 2>/dev/null || echo 0)

    if [ "$MATH_PROCS" -eq 0 ]; then
        echo "$(date) — No MATH processes running. Checking output files..."
        ALL_DONE=true
        for m in "${MODELS[@]}"; do
            f="results/exp002/${m}_math.jsonl"
            LINES=$(wc -l < "$f" 2>/dev/null || echo 0)
            if [ "$LINES" -lt "$TARGET" ]; then
                ALL_DONE=false
                echo "  INCOMPLETE: ${m}_math.jsonl = $LINES / $TARGET"
            else
                echo "  OK: ${m}_math.jsonl = $LINES"
            fi
        done

        if $ALL_DONE; then
            echo ""
            echo "$(date) — All 4 MATH runs complete! Launching InternLM + DeepSeek..."
            bash scripts/auto_start_new_models.sh 2>&1 | tee results/exp002/new_models_run.log
            exit 0
        else
            echo "$(date) — Some MATH runs incomplete but processes exited. Check for errors."
            exit 1
        fi
    fi

    # Print progress
    echo -n "$(date '+%H:%M:%S') MATH running ($MATH_PROCS procs): "
    for m in "${MODELS[@]}"; do
        f="results/exp002/${m}_math.jsonl"
        LINES=$(wc -l < "$f" 2>/dev/null || echo 0)
        PCT=$((LINES * 100 / TARGET))
        echo -n "${m}=${PCT}% "
    done
    echo ""

    sleep 120
done
