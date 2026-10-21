#!/bin/bash
set -e

cd /root/gen-depth-fingerprint
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

MODEL_NAME="qwen3-1.7b-instruct"
MODEL_PATH="/root/autodl-tmp/models/Qwen/Qwen3-1___7B"
DEVICE="cuda:1"

echo "=== Step 1: Generate chains ==="
python generate_chain_instruct.py \
  --model-name $MODEL_NAME \
  --model-path $MODEL_PATH \
  --input data/wiki_seed_1000.jsonl \
  --shard-id 0 --num-shards 1 \
  --device $DEVICE

echo ""
echo "=== Step 2: Extract features ==="
python extract_features.py \
  --input data/${MODEL_NAME}/generations_shard0.jsonl \
  --output data/features_${MODEL_NAME}.csv \
  --device $DEVICE \
  --batch-size 8

echo ""
echo "=== Step 3: Analyze ==="
python analyze_instruct.py \
  --input data/features_${MODEL_NAME}.csv \
  --output results/review_p1c_instruct.json \
  --model-name "Qwen3-1.7B-Instruct"

echo ""
echo "=== ALL DONE ==="
