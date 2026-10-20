#!/bin/bash
set -e

cd .
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
export PYTHONPATH=.:$PYTHONPATH
export VLLM_USE_V1=0

# Usage: run_exp002_gpu.sh <gpu_id> <model_short_name>
# Runs all 4 benchmarks serially for one model on one GPU
# MC benchmarks first (fast), GSM8K last (slow)

run_model_benchmarks() {
    local GPU_ID=$1
    local MODEL=$2
    local LOGFILE="results/exp002/gpu${GPU_ID}_${MODEL}.log"

    echo "=== GPU ${GPU_ID} ${MODEL} start: $(date) ===" >> "$LOGFILE"

    # Run MC benchmarks first (fast: max_tokens=16)
    for BM in mmlu arc hellaswag; do
        echo "" >> "$LOGFILE"
        echo "=== ${MODEL}/${BM} start: $(date) ===" >> "$LOGFILE"

        ITEMS_ARG=""
        if [ "$BM" = "mmlu" ]; then
            ITEMS_ARG="--items data/mmlu_items_exp001.json"
        fi

        CUDA_VISIBLE_DEVICES=$GPU_ID python -m src.inference.run_experiment \
            --design "results/exp002/shard_${MODEL}_${BM}.csv" \
            --benchmark "$BM" \
            $ITEMS_ARG \
            --gpu-id 0 \
            --output "results/exp002/${MODEL}_${BM}.jsonl" \
            >> "$LOGFILE" 2>&1

        echo "=== ${MODEL}/${BM} done: $(date) ===" >> "$LOGFILE"
    done

    # GSM8K last (slow: max_tokens=512)
    echo "" >> "$LOGFILE"
    echo "=== ${MODEL}/gsm8k start: $(date) ===" >> "$LOGFILE"

    CUDA_VISIBLE_DEVICES=$GPU_ID python -m src.inference.run_experiment \
        --design "results/exp002/shard_${MODEL}_gsm8k.csv" \
        --benchmark gsm8k \
        --gpu-id 0 \
        --output "results/exp002/${MODEL}_gsm8k.jsonl" \
        >> "$LOGFILE" 2>&1

    echo "=== ${MODEL}/gsm8k done: $(date) ===" >> "$LOGFILE"
    echo "" >> "$LOGFILE"
    echo "=== GPU ${GPU_ID} ${MODEL} ALL DONE: $(date) ===" >> "$LOGFILE"
    echo "GPU${GPU_ID}_${MODEL}_DONE"
}

echo "=== exp-002 full run start: $(date) ==="

# Launch 4 GPUs in parallel
run_model_benchmarks 0 qwen &
PID_0=$!
run_model_benchmarks 1 llama &
PID_1=$!
run_model_benchmarks 2 gemma &
PID_2=$!
run_model_benchmarks 3 mistral &
PID_3=$!

echo "PIDs: qwen=$PID_0 llama=$PID_1 gemma=$PID_2 mistral=$PID_3"

# Wait for all to finish
wait $PID_0 && echo "GPU0 qwen done" || echo "GPU0 qwen FAILED"
wait $PID_1 && echo "GPU1 llama done" || echo "GPU1 llama FAILED"
wait $PID_2 && echo "GPU2 gemma done" || echo "GPU2 gemma FAILED"
wait $PID_3 && echo "GPU3 mistral done" || echo "GPU3 mistral FAILED"

echo "=== exp-002 full run complete: $(date) ==="
echo "EXP002_ALL_DONE"
