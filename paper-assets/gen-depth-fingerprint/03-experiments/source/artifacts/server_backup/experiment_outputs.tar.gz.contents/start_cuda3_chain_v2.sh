#!/bin/bash
set -e
PYTHIA1B_PID=$1

echo "Waiting for Pythia-1B (PID $PYTHIA1B_PID)..."
while kill -0 $PYTHIA1B_PID 2>/dev/null; do sleep 30; done
echo "Pythia-1B done at $(date)"

cd /root/gen-depth-fingerprint
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

echo "Starting Qwen3-0.6B greedy+topk on cuda:3..."
CUDA_VISIBLE_DEVICES=3 python3 generate_chain_decoding.py \
  --model-name qwen3-0.6b \
  --device cuda:0 \
  --strategies greedy topk \
  > /tmp/gen_qwen06b_decoding.log 2>&1
echo "Qwen3-0.6B done at $(date)"

echo "cuda:3 chain v2 complete (Qwen3-8B moved to free-GPU watcher)"
