#!/bin/bash
# Wait for any of cuda:0/1/2 to become free, then run Qwen3-8B greedy+topk there.
set -e
PROJECT=/root/gen-depth-fingerprint

echo "$(date): Qwen3-8B watcher started, monitoring cuda:0/1/2 for free GPU..."

while true; do
    for GPU_ID in 0 1 2; do
        PROCS=$(nvidia-smi --query-compute-apps=pid --format=csv,noheader -i $GPU_ID 2>/dev/null | grep -c '[0-9]' || true)
        if [ "$PROCS" -eq 0 ]; then
            echo "$(date): cuda:$GPU_ID is free, starting Qwen3-8B greedy+topk"
            cd $PROJECT
            source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

            CUDA_VISIBLE_DEVICES=$GPU_ID python3 generate_chain_decoding.py \
              --model-name qwen3-8b \
              --device cuda:0 \
              --strategies greedy topk \
              > /tmp/gen_qwen8b_decoding.log 2>&1

            echo "$(date): Qwen3-8B completed on cuda:$GPU_ID"
            exit 0
        fi
    done
    sleep 60
done
