#!/bin/bash
set -e
source /root/miniconda3/bin/activate
cd /root/gen-depth-fingerprint

echo "=== Temperature Curve Generation ==="
echo "Start: $(date)"

# Job 1: Pythia-2.8B, t=0.5 (default model path finds pythia-2.8b)
echo ""
echo ">>> [1/3] Pythia-2.8B t=0.5 top_p=0.8"
python generate_chain.py \
    --model-name pythia-2.8b-t05 \
    --temperature 0.5 --top-p 0.8 \
    --output-dir data/ --device cuda:0

# Job 2: Pythia-2.8B, t=0.9
echo ""
echo ">>> [2/3] Pythia-2.8B t=0.9 top_p=0.95"
python generate_chain.py \
    --model-name pythia-2.8b-t09 \
    --temperature 0.9 --top-p 0.95 \
    --output-dir data/ --device cuda:0

# Job 3: Qwen3-1.7B, t=0.9
echo ""
echo ">>> [3/3] Qwen3-1.7B t=0.9 top_p=0.95"
python generate_chain.py \
    --model-name qwen3-1.7b-t09 \
    --model-path /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base \
    --temperature 0.9 --top-p 0.95 \
    --output-dir data/ --device cuda:0

echo ""
echo "=== Generation complete. Starting feature extraction ==="

# Feature extraction
echo ">>> Extracting features: pythia-2.8b-t05"
python extract_features.py \
    --input data/pythia-2.8b-t05/generations_shard0.jsonl \
    --output data/features_pythia-2.8b-t05.csv \
    --device cuda:0

echo ">>> Extracting features: pythia-2.8b-t09"
python extract_features.py \
    --input data/pythia-2.8b-t09/generations_shard0.jsonl \
    --output data/features_pythia-2.8b-t09.csv \
    --device cuda:0

echo ">>> Extracting features: qwen3-1.7b-t09"
python extract_features.py \
    --input data/qwen3-1.7b-t09/generations_shard0.jsonl \
    --output data/features_qwen3-1.7b-t09.csv \
    --device cuda:0

echo ""
echo "=== All done ==="
echo "End: $(date)"
