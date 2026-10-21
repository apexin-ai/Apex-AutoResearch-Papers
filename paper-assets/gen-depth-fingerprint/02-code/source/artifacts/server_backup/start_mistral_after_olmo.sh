#!/bin/bash
# Wait for OLMo python process to finish, then start Mistral on cuda:1
OLMO_PID=283607
echo "Waiting for OLMo PID $OLMO_PID to finish..."
while kill -0 $OLMO_PID 2>/dev/null; do sleep 30; done
echo "OLMo done at $(date). Starting Mistral-7B on cuda:1..."
cd /root/gen-depth-fingerprint
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
CUDA_VISIBLE_DEVICES=1 python3 generate_chain_decoding.py \
  --model-name mistral-7b-v0.3 \
  --device cuda:0 \
  --strategies greedy topk \
  > /tmp/gen_mistral_decoding.log 2>&1
echo "Mistral done at $(date)"
