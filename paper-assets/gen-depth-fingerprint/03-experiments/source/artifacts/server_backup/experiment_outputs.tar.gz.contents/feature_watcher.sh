#!/bin/bash
cd /root/gen-depth-fingerprint
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

echo "$(date): Feature watcher started"

# Wait for Mistral-7B topk (PID 349080) to finish
echo "$(date): Waiting for Mistral-7B (PID 349080)..."
while kill -0 349080 2>/dev/null; do sleep 60; done
echo "$(date): Mistral-7B done, extracting mistral-7b-v0.3-topk features..."
python extract_features.py --input data/mistral-7b-v0.3-topk/generations_shard0.jsonl --output data/features_mistral-7b-v0.3-topk.csv --device cuda:0
echo "$(date): mistral-7b-v0.3-topk features done"

# Wait for Qwen3-0.6B topk (PID 357811) to finish
echo "$(date): Waiting for Qwen3-0.6B (PID 357811)..."
while kill -0 357811 2>/dev/null; do sleep 60; done
echo "$(date): Qwen3-0.6B done, extracting qwen3-0.6b-topk features..."
python extract_features.py --input data/qwen3-0.6b-topk/generations_shard0.jsonl --output data/features_qwen3-0.6b-topk.csv --device cuda:0
echo "$(date): qwen3-0.6b-topk features done"

# Wait for Qwen3-8B (PID 369104) to finish
echo "$(date): Waiting for Qwen3-8B (PID 369104)..."
while kill -0 369104 2>/dev/null; do sleep 60; done
echo "$(date): Qwen3-8B done, extracting qwen3-8b-greedy + qwen3-8b-topk features..."
python extract_features.py --input data/qwen3-8b-greedy/generations_shard0.jsonl --output data/features_qwen3-8b-greedy.csv --device cuda:0
echo "$(date): qwen3-8b-greedy features done"
if [ -d data/qwen3-8b-topk ]; then
    python extract_features.py --input data/qwen3-8b-topk/generations_shard0.jsonl --output data/features_qwen3-8b-topk.csv --device cuda:0
    echo "$(date): qwen3-8b-topk features done"
else
    echo "$(date): WARNING — qwen3-8b-topk directory not found"
fi

echo "$(date): All feature extractions complete!"
