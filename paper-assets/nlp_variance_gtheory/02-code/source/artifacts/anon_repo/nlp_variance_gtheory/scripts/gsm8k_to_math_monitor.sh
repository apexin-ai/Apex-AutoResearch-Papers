#!/bin/bash
cd .
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base

TARGET=57600
INTERVAL=30

MISTRAL_STARTED=0
QWEN_STARTED=0
GEMMA_STARTED=0

echo "$(date) Monitor started. Target=$TARGET lines per model."

while true; do
    # Check Mistral (GPU 3)
    if [ "$MISTRAL_STARTED" -eq 0 ]; then
        COUNT=$(wc -l < results/exp002/mistral_gsm8k.jsonl 2>/dev/null || echo 0)
        if [ "$COUNT" -ge "$TARGET" ]; then
            echo "$(date) Mistral GSM8K done ($COUNT lines). Starting MATH on GPU 3."
            CUDA_VISIBLE_DEVICES=3 nohup python -m src.inference.run_experiment \
                --design results/exp002/shard_mistral_math.csv \
                --benchmark math --gpu-id 0 \
                --output results/exp002/mistral_math.jsonl \
                > /tmp/math_mistral.log 2>&1 &
            echo "Mistral MATH PID: $!"
            MISTRAL_STARTED=1
        else
            echo "$(date) Mistral GSM8K: $COUNT / $TARGET"
        fi
    fi

    # Check Qwen (GPU 0)
    if [ "$QWEN_STARTED" -eq 0 ]; then
        COUNT=$(wc -l < results/exp002/qwen_gsm8k.jsonl 2>/dev/null || echo 0)
        if [ "$COUNT" -ge "$TARGET" ]; then
            echo "$(date) Qwen GSM8K done ($COUNT lines). Starting MATH on GPU 0."
            CUDA_VISIBLE_DEVICES=0 nohup python -m src.inference.run_experiment \
                --design results/exp002/shard_qwen_math.csv \
                --benchmark math --gpu-id 0 \
                --output results/exp002/qwen_math.jsonl \
                > /tmp/math_qwen.log 2>&1 &
            echo "Qwen MATH PID: $!"
            QWEN_STARTED=1
        else
            echo "$(date) Qwen GSM8K: $COUNT / $TARGET"
        fi
    fi

    # Check Gemma (GPU 2)
    if [ "$GEMMA_STARTED" -eq 0 ]; then
        COUNT=$(wc -l < results/exp002/gemma_gsm8k.jsonl 2>/dev/null || echo 0)
        if [ "$COUNT" -ge "$TARGET" ]; then
            echo "$(date) Gemma GSM8K done ($COUNT lines). Starting MATH on GPU 2."
            CUDA_VISIBLE_DEVICES=2 nohup python -m src.inference.run_experiment \
                --design results/exp002/shard_gemma_math.csv \
                --benchmark math --gpu-id 0 \
                --output results/exp002/gemma_math.jsonl \
                > /tmp/math_gemma.log 2>&1 &
            echo "Gemma MATH PID: $!"
            GEMMA_STARTED=1
        else
            echo "$(date) Gemma GSM8K: $COUNT / $TARGET"
        fi
    fi

    # All done?
    if [ "$MISTRAL_STARTED" -eq 1 ] && [ "$QWEN_STARTED" -eq 1 ] && [ "$GEMMA_STARTED" -eq 1 ]; then
        echo "$(date) All 3 models switched to MATH. Monitor exiting."
        break
    fi

    sleep $INTERVAL
done
