#!/bin/bash
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_ENDPOINT=https://hf-mirror.com
export HF_HUB_DISABLE_XET=1
export CUDA_VISIBLE_DEVICES=5

PYTHON=/root/miniconda3/bin/python
SCRIPT=/root/contamcal-irt-calibration/exp002/compute_signals.py
MODEL=/root/autodl-tmp/models/Qwen/Qwen2___5-1___5B-Instruct
OUTBASE=/root/autodl-tmp/exp009/signals/Qwen2.5-1.5B-Instruct

for BENCH in mmlu arc_challenge gsm8k; do
    echo "=== 1.5B s2 $BENCH ==="
    $PYTHON $SCRIPT --model-path $MODEL --benchmark $BENCH --signal s2 --output-dir $OUTBASE/$BENCH
done

for BENCH in mmlu arc_challenge gsm8k; do
    echo "=== 1.5B s4 $BENCH ==="
    $PYTHON $SCRIPT --model-path $MODEL --benchmark $BENCH --signal s4 --output-dir $OUTBASE/$BENCH
done

echo "=== 1.5B signals DONE ==="
