#!/bin/bash
# 4-GPU parallel inference for exp_021 (fewnerd NER)
# 37648 instances / 4 = 9412 per shard

MODEL="checkpoints/qwen3-8b-fewnerd-exp021-merged"
DATA_DIR="data/fewnerd"
BASE_OUT="output/exp_021_inference"
PYTHON="/root/miniconda3/bin/python"

cd /root/autodl-tmp/struct_self_consist_ie

TOTAL=37648
SHARD_SIZE=9412

for GPU in 0 1 2 3; do
    START=$((GPU * SHARD_SIZE))
    if [ $GPU -eq 3 ]; then
        END=$TOTAL
    else
        END=$(((GPU + 1) * SHARD_SIZE))
    fi
    OUT_DIR="${BASE_OUT}/shard_${GPU}"
    LOG="/tmp/exp021_shard_${GPU}.log"

    echo "Launching shard $GPU: instances [$START, $END) on cuda:$GPU -> $OUT_DIR"
    CUDA_VISIBLE_DEVICES=$GPU nohup $PYTHON code/run_mvp_pilot.py \
        --model_path $MODEL \
        --data_dir $DATA_DIR \
        --dataset fewnerd \
        --subtask ner \
        --n_samples 8 \
        --temperature 1.0 \
        --max_tokens 1024 \
        --seed 42 \
        --collect_logprobs \
        --start_index $START \
        --end_index $END \
        --output_dir $OUT_DIR \
        > $LOG 2>&1 &
    echo "  PID=$!"
done

echo ""
echo "All 4 shards launched. Monitor with:"
echo "  tail -f /tmp/exp021_shard_{0,1,2,3}.log"
