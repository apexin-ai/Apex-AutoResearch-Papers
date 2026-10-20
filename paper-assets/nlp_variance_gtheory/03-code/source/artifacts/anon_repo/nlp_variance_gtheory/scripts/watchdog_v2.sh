#!/bin/bash
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
cd .
export HF_HOME=/path/to/model

LOG=/tmp/watchdog_v2.log
echo "=== Watchdog v2 started $(date) ===" >> $LOG

check_download_done() {
    local log_file=$1
    grep -q "DONE\|DOWNLOAD_COMPLETE" "$log_file" 2>/dev/null
}

SUBMITTED_3B=0
SUBMITTED_7B=1  # 7B already running
DONE_3B=0
DONE_7B=0
SUBMITTED_72B=0

for i in $(seq 1 120); do
    echo "--- Poll $i at $(date) ---" >> $LOG

    # 3B: check download log for completion signal, not just file existence
    if [ $SUBMITTED_3B -eq 0 ]; then
        if check_download_done /tmp/download_3b.log; then
            echo "3B download DONE (confirmed via log) - starting inference" >> $LOG
            CUDA_VISIBLE_DEVICES=0 nohup python -m src.inference.run_experiment \
                --design design_matrix_exp003_3b.csv \
                --items data/mmlu_items_exp001.json \
                --benchmark mmlu \
                --precision bfloat16 \
                --gpu-id 0 \
                --tensor-parallel 1 \
                --output results/exp003_scale_3b_mmlu.jsonl \
                > /tmp/inference_3b.log 2>&1 &
            echo "3B inference PID=$!" >> $LOG
            SUBMITTED_3B=1
        else
            echo "3B download not complete" >> $LOG
        fi
    else
        if [ $DONE_3B -eq 0 ]; then
            if pgrep -f "exp003_scale_3b_mmlu" > /dev/null; then
                LINES=$(wc -l < ./results/exp003_scale_3b_mmlu.jsonl 2>/dev/null || echo 0)
                echo "3B inference running ($LINES records)" >> $LOG
            else
                echo "3B inference DONE" >> $LOG
                DONE_3B=1
            fi
        fi
    fi

    # 7B: already submitted, just track completion
    if [ $DONE_7B -eq 0 ]; then
        if pgrep -f "exp003_scale_7b_mmlu" > /dev/null; then
            LINES=$(wc -l < ./results/exp003_scale_7b_mmlu.jsonl 2>/dev/null || echo 0)
            echo "7B inference running ($LINES records)" >> $LOG
        else
            echo "7B inference DONE" >> $LOG
            DONE_7B=1
        fi
    fi

    # 72B: wait for BOTH 3B and 7B to be DONE + 72B downloaded
    if [ $SUBMITTED_72B -eq 0 ] && [ $DONE_3B -eq 1 ] && [ $DONE_7B -eq 1 ]; then
        if check_download_done /tmp/download_72b.log; then
            echo "72B download DONE + 3B/7B done - starting inference" >> $LOG
            CUDA_VISIBLE_DEVICES=0,1,2,3 nohup python -m src.inference.run_experiment \
                --design design_matrix_exp003_72b.csv \
                --items data/mmlu_items_exp001.json \
                --benchmark mmlu \
                --precision bfloat16 \
                --gpu-id 0 \
                --tensor-parallel 4 \
                --output results/exp003_scale_72b_mmlu.jsonl \
                > /tmp/inference_72b.log 2>&1 &
            echo "72B inference PID=$!" >> $LOG
            SUBMITTED_72B=1
        else
            echo "72B waiting for download (3B/7B inference done)" >> $LOG
        fi
    fi

    # All done check
    if [ $DONE_3B -eq 1 ] && [ $DONE_7B -eq 1 ] && [ $SUBMITTED_72B -eq 1 ]; then
        if ! pgrep -f "exp003_scale_72b_mmlu" > /dev/null; then
            echo "ALL THREE DONE at $(date)" >> $LOG
            break
        fi
    fi

    sleep 180
done
echo "=== Watchdog v2 ended $(date) ===" >> $LOG
