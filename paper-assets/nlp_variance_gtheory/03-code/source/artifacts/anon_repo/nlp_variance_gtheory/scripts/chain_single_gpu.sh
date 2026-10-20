#!/bin/bash
set -e

cd .
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
export PYTHONPATH=.:$PYTHONPATH
export VLLM_USE_V1=0

MODEL=$1
GPU=$2
TARGET=57600
LOG_DIR="results/exp002"

echo "$(date) — Starting $MODEL chain on GPU $GPU"

for BM in mmlu arc hellaswag gsm8k math; do
    OUTFILE="${LOG_DIR}/${MODEL}_${BM}.jsonl"
    SHARD="${LOG_DIR}/shard_${MODEL}_${BM}.csv"
    LOGFILE="${LOG_DIR}/gpu${GPU}_${MODEL}_${BM}.log"

    # Skip if already complete
    if [ -f "$OUTFILE" ]; then
        LINES=$(wc -l < "$OUTFILE")
        if [ "$LINES" -ge "$TARGET" ]; then
            echo "$(date) — SKIP ${MODEL}/${BM} (already done: ${LINES} lines)"
            continue
        fi
    fi

    ITEMS_ARG=""
    if [ "$BM" = "mmlu" ]; then
        ITEMS_ARG="--items data/mmlu_items_exp001.json"
    fi

    echo "$(date) — START ${MODEL}/${BM} on GPU ${GPU}"
    CUDA_VISIBLE_DEVICES=$GPU python -m src.inference.run_experiment \
        --design "$SHARD" \
        --benchmark "$BM" \
        $ITEMS_ARG \
        --gpu-id 0 \
        --output "$OUTFILE" \
        >> "$LOGFILE" 2>&1
    LINES=$(wc -l < "$OUTFILE" 2>/dev/null || echo 0)
    echo "$(date) — DONE ${MODEL}/${BM}: ${LINES} lines"
done

echo "$(date) — ALL DONE for $MODEL on GPU $GPU"
