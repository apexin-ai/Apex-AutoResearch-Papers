#!/bin/bash
# Wait for all Mistral processes to finish
while ps aux | grep 'run_experiment.*exp001_mistral' | grep -v grep > /dev/null 2>&1; do
    sleep 60
done

echo "$(date) Mistral done, starting Qwen..." >> /tmp/auto_chain.log

cd .
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
export PYTHONPATH=.:$PYTHONPATH

for gpu in 0 1 2 3; do
    nohup python -m src.inference.run_experiment \
        --design results/exp001_qwen/shards/shard_${gpu}.csv \
        --items data/mmlu_items_exp001.json \
        --few-shot data/few_shot_examples.json \
        --gpu-id ${gpu} \
        --output results/exp001_qwen/shard_${gpu}.jsonl \
        > /tmp/qwen_gpu${gpu}.log 2>&1 &
    echo "$(date) Qwen GPU $gpu started PID=$!" >> /tmp/auto_chain.log
done
