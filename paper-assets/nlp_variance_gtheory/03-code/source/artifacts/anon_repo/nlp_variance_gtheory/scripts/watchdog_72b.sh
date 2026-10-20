#!/bin/bash
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
cd .
export HF_HOME=/path/to/model
export PYTHONPATH=.

LOG=/tmp/watchdog_72b.log
MODEL_DIR=Qwen/Qwen2.5-72B-Instruct
TOTAL_SHARDS=37

echo "=== Watchdog 72B started $(date) ===" >> $LOG

for i in $(seq 1 240); do
    EXISTING=$(ls $MODEL_DIR/model-000*-of-00037.safetensors 2>/dev/null | wc -l)
    echo "--- Poll $i at $(date): $EXISTING/$TOTAL_SHARDS shards ---" >> $LOG

    if [ "$EXISTING" -eq "$TOTAL_SHARDS" ]; then
        echo "All $TOTAL_SHARDS shards present! Starting 72B inference..." >> $LOG

        nohup python -m src.inference.run_experiment \
            --design design_matrix_exp003_72b.csv \
            --items data/mmlu_items_exp001.json \
            --benchmark mmlu \
            --precision bfloat16 \
            --gpu-id 0 \
            --tensor-parallel 4 \
            --output results/exp003_scale_72b_mmlu.jsonl \
            > /tmp/inference_72b.log 2>&1 &

        echo "72B inference PID=$! launched at $(date)" >> $LOG
        echo "Watchdog done." >> $LOG
        exit 0
    fi

    sleep 180
done

echo "=== Watchdog 72B timed out after 240 polls ===" >> $LOG
