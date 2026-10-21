#!/bin/bash
# Launch script for exp-d126 cross-model SICA
# Starts Mistral-7B on GPU 0 (port 8000) and Qwen3-14B on GPU 1 (port 8001)

set -e

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

echo "=== Starting Mistral-7B on GPU 0, port 8000 ==="
CUDA_VISIBLE_DEVICES=0 nohup python -m vllm.entrypoints.openai.api_server \
    --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 \
    --port 8000 \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.85 \
    --max-model-len 8192 \
    --seed 42 \
    > /tmp/vllm_mistral_d126.log 2>&1 &
echo "Mistral PID: $!"

echo "=== Starting Qwen3-14B on GPU 1, port 8001 ==="
CUDA_VISIBLE_DEVICES=1 nohup python -m vllm.entrypoints.openai.api_server \
    --model /root/autodl-tmp/models/Qwen3-14B \
    --port 8001 \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.85 \
    --max-model-len 8192 \
    --seed 42 \
    > /tmp/vllm_qwen3_d126.log 2>&1 &
echo "Qwen3 PID: $!"

echo "=== Waiting for servers to start ==="
for port in 8000 8001; do
    echo -n "Waiting for port $port..."
    for i in $(seq 1 120); do
        if curl -s http://localhost:$port/v1/models > /dev/null 2>&1; then
            echo " ready!"
            break
        fi
        sleep 5
        echo -n "."
    done
done

echo "=== Both servers ready, starting experiment ==="
python /root/symb_invariant_consensus/exp_d126_crossmodel_sica.py --phase all \
    2>&1 | tee /root/symb_invariant_consensus/results/exp_d126_crossmodel_sica/run.log
