#!/bin/bash
set -e

cd .
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
export PYTHONPATH=.:$PYTHONPATH
export VLLM_USE_V1=0

TARGET=57600
LOG_DIR="results/exp002"

run_job() {
    local GPU=$1 MODEL=$2 BM=$3
    local LOGFILE="${LOG_DIR}/gpu${GPU}_${MODEL}_${BM}.log"
    local OUTFILE="${LOG_DIR}/${MODEL}_${BM}.jsonl"
    local SHARD="${LOG_DIR}/shard_${MODEL}_${BM}.csv"

    ITEMS_ARG=""
    if [ "$BM" = "mmlu" ]; then
        ITEMS_ARG="--items data/mmlu_items_exp001.json"
    fi

    echo "$(date '+%H:%M:%S') Starting ${MODEL}/${BM} on GPU ${GPU}" | tee -a "$LOGFILE"
    CUDA_VISIBLE_DEVICES=$GPU python -m src.inference.run_experiment \
        --design "$SHARD" \
        --benchmark "$BM" \
        $ITEMS_ARG \
        --gpu-id 0 \
        --output "$OUTFILE" \
        >> "$LOGFILE" 2>&1
    local LINES=$(wc -l < "$OUTFILE")
    echo "$(date '+%H:%M:%S') Done ${MODEL}/${BM}: ${LINES} lines" | tee -a "$LOGFILE"
}

echo "============================================="
echo "$(date) — Starting InternLM + DeepSeek inference"
echo "============================================="

# Round 1: MMLU + ARC (4 parallel)
echo ""
echo "$(date '+%H:%M:%S') — Round 1: MMLU + ARC"
run_job 0 internlm mmlu &
PID1=$!
run_job 1 internlm arc &
PID2=$!
run_job 2 deepseek mmlu &
PID3=$!
run_job 3 deepseek arc &
PID4=$!
wait $PID1 $PID2 $PID3 $PID4
echo "$(date '+%H:%M:%S') — Round 1 complete"

# Round 2: HellaSwag + GSM8K (4 parallel)
echo ""
echo "$(date '+%H:%M:%S') — Round 2: HellaSwag + GSM8K"
run_job 0 internlm hellaswag &
PID1=$!
run_job 1 internlm gsm8k &
PID2=$!
run_job 2 deepseek hellaswag &
PID3=$!
run_job 3 deepseek gsm8k &
PID4=$!
wait $PID1 $PID2 $PID3 $PID4
echo "$(date '+%H:%M:%S') — Round 2 complete"

# Round 3: MATH (2 parallel — 1 GPU each)
echo ""
echo "$(date '+%H:%M:%S') — Round 3: MATH"
run_job 0 internlm math &
PID1=$!
run_job 2 deepseek math &
PID2=$!
wait $PID1 $PID2
echo "$(date '+%H:%M:%S') — Round 3 complete"

# Final validation
echo ""
echo "============================================="
echo "$(date) — Validating all outputs"
echo "============================================="
PASS=0
FAIL=0
for MODEL in internlm deepseek; do
    for BM in mmlu arc hellaswag gsm8k math; do
        f="${LOG_DIR}/${MODEL}_${BM}.jsonl"
        if [ ! -f "$f" ]; then
            echo "  MISSING: $f"
            FAIL=$((FAIL + 1))
            continue
        fi
        COUNT=$(wc -l < "$f")
        if [ "$COUNT" -eq "$TARGET" ]; then
            echo "  OK: ${MODEL}_${BM} ($COUNT)"
            PASS=$((PASS + 1))
        else
            echo "  FAIL: ${MODEL}_${BM} ($COUNT / $TARGET)"
            FAIL=$((FAIL + 1))
        fi
    done
done
echo "Validation: $PASS passed, $FAIL failed out of 10"
echo ""
echo "$(date) — ALL DONE"
