#!/bin/bash
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
cd .
export HF_HOME=/path/to/model

LOG=/tmp/watchdog_inference.log
echo "=== Watchdog started $(date) ===" >> $LOG

check_model_ready() {
    local model_dir=$1
    # Check if safetensors exist in the ModelScope cache dir
    if ls ${model_dir}/*.safetensors >/dev/null 2>&1; then
        return 0
    fi
    return 1
}

# Track what's been submitted
SUBMITTED_3B=0
SUBMITTED_7B=0
SUBMITTED_72B=0

for i in $(seq 1 60); do
    echo "--- Poll $i at $(date) ---" >> $LOG

    # Check 3B
    if [ $SUBMITTED_3B -eq 0 ]; then
        if check_model_ready "Qwen/Qwen2.5-3B-Instruct"; then
            echo "3B READY - starting inference" >> $LOG
            CUDA_VISIBLE_DEVICES=0 nohup python -m src.inference.run_experiment \
                --design design_matrix_exp003_3b.csv \
                --items data/mmlu_items_exp001.json \
                --benchmark mmlu \
                --precision bfloat16 \
                --gpu-id 0 \
                --tensor-parallel 1 \
                --output results/exp003_scale_3b_mmlu.jsonl \
                > /tmp/inference_3b.log 2>&1 &
            echo "3B PID=$!" >> $LOG
            SUBMITTED_3B=1
        else
            echo "3B not ready" >> $LOG
        fi
    else
        # Check if 3B inference is still running
        if pgrep -f "exp003_scale_3b" > /dev/null; then
            echo "3B inference running" >> $LOG
        else
            echo "3B inference DONE" >> $LOG
        fi
    fi

    # Check 7B
    if [ $SUBMITTED_7B -eq 0 ]; then
        if check_model_ready "Qwen/Qwen2.5-7B-Instruct"; then
            echo "7B READY - starting inference" >> $LOG
            CUDA_VISIBLE_DEVICES=1 nohup python -m src.inference.run_experiment \
                --design design_matrix_exp003_7b.csv \
                --items data/mmlu_items_exp001.json \
                --benchmark mmlu \
                --precision bfloat16 \
                --gpu-id 0 \
                --tensor-parallel 1 \
                --output results/exp003_scale_7b_mmlu.jsonl \
                > /tmp/inference_7b.log 2>&1 &
            echo "7B PID=$!" >> $LOG
            SUBMITTED_7B=1
        else
            echo "7B not ready" >> $LOG
        fi
    else
        if pgrep -f "exp003_scale_7b" > /dev/null; then
            echo "7B inference running" >> $LOG
        else
            echo "7B inference DONE" >> $LOG
        fi
    fi

    # Check 72B - only after 3B and 7B inference are DONE
    if [ $SUBMITTED_72B -eq 0 ] && [ $SUBMITTED_3B -eq 1 ] && [ $SUBMITTED_7B -eq 1 ]; then
        if ! pgrep -f "exp003_scale_3b" > /dev/null && ! pgrep -f "exp003_scale_7b" > /dev/null; then
            if check_model_ready "Qwen/Qwen2.5-72B-Instruct"; then
                echo "72B READY + 3B/7B done - starting inference" >> $LOG
                CUDA_VISIBLE_DEVICES=0,1,2,3 nohup python -m src.inference.run_experiment \
                    --design design_matrix_exp003_72b.csv \
                    --items data/mmlu_items_exp001.json \
                    --benchmark mmlu \
                    --precision bfloat16 \
                    --gpu-id 0 \
                    --tensor-parallel 4 \
                    --output results/exp003_scale_72b_mmlu.jsonl \
                    > /tmp/inference_72b.log 2>&1 &
                echo "72B PID=$!" >> $LOG
                SUBMITTED_72B=1
            else
                echo "72B not ready (download pending)" >> $LOG
            fi
        else
            echo "72B waiting for 3B/7B inference to finish" >> $LOG
        fi
    fi

    # Exit if all submitted and all done
    if [ $SUBMITTED_3B -eq 1 ] && [ $SUBMITTED_7B -eq 1 ] && [ $SUBMITTED_72B -eq 1 ]; then
        if ! pgrep -f "exp003_scale_3b\|exp003_scale_7b\|exp003_scale_72b" > /dev/null; then
            echo "ALL DONE at $(date)" >> $LOG
            break
        fi
    fi

    sleep 180  # 3 min
done
echo "=== Watchdog ended $(date) ===" >> $LOG
