#!/bin/bash
set -e

PROJ=.
cd "$PROJ"

source $CONDA_PREFIX/etc/profile.d/conda.sh
conda activate base
export PYTHONPATH=$PROJ:$PYTHONPATH
export HF_HOME=/path/to/model
export HF_DATASETS_OFFLINE=1
export VLLM_USE_V1=0

run_sample() {
    local SAMPLE_ID=$1
    local SAMPLE_DIR="results/exp001b/sample${SAMPLE_ID}"
    local ITEMS="data/mmlu_items_exp001b_sample${SAMPLE_ID}.json"
    local FEW_SHOT="data/few_shot_exp001.json"

    echo "====== Starting sample ${SAMPLE_ID} at $(date) ======"

    # Shard the design if not already done
    if [ ! -f "${SAMPLE_DIR}/shards/shard_0.csv" ]; then
        python -m src.design.shard_design \
            --input "${SAMPLE_DIR}/design.csv" \
            --output-dir "${SAMPLE_DIR}/shards" \
            --n-shards 4 --shuffle-seed 42
    fi

    # Launch 4 GPU shards in parallel
    PIDS=()
    for GPU in 0 1 2 3; do
        CUDA_VISIBLE_DEVICES=$GPU python -m src.inference.run_experiment \
            --design "${SAMPLE_DIR}/shards/shard_${GPU}.csv" \
            --items "$ITEMS" \
            --few-shot "$FEW_SHOT" \
            --output "${SAMPLE_DIR}/shard_${GPU}.jsonl" \
            --precision bfloat16 \
            --gpu-id 0 \
            > "${SAMPLE_DIR}/shard_${GPU}.log" 2>&1 &
        PIDS+=($!)
        echo "  GPU $GPU: PID $! → shard_${GPU}.jsonl"
    done

    echo "  Waiting for ${#PIDS[@]} processes..."
    FAIL=0
    for PID in "${PIDS[@]}"; do
        if ! wait $PID; then
            echo "  ERROR: PID $PID failed"
            FAIL=1
        fi
    done

    if [ $FAIL -eq 1 ]; then
        echo "  Sample ${SAMPLE_ID} had failures. Check logs."
        return 1
    fi

    # Merge shards
    cat "${SAMPLE_DIR}"/shard_*.jsonl > "${SAMPLE_DIR}/all_results.jsonl"
    local N=$(wc -l < "${SAMPLE_DIR}/all_results.jsonl")
    echo "  Sample ${SAMPLE_ID} complete: ${N} records → ${SAMPLE_DIR}/all_results.jsonl"
    echo "====== Finished sample ${SAMPLE_ID} at $(date) ======"
}

# Run all 3 samples sequentially
for S in 1 2 3; do
    run_sample $S || echo "Sample $S failed, continuing..."
done

echo "All exp-001b samples done at $(date)"
