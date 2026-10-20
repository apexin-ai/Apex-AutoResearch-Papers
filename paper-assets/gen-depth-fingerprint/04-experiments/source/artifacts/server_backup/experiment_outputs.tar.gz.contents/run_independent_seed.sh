#!/bin/bash
set -e
source /root/miniconda3/bin/activate
cd /root/gen-depth-fingerprint
export HF_HOME=/root/autodl-tmp/.hf_cache

echo "=== Independent-Seed Control Experiment ==="
echo "Start: $(date)"

# Step 1: Generate Pythia-2.8B chains with Set A seeds
echo ""
echo ">>> [1/4] Generating Pythia-2.8B with independent Set A seeds"
python generate_chain.py \
    --model-name pythia-2.8b-indepA \
    --input data/independent_seeds_A.jsonl \
    --temperature 0.7 --top-p 0.9 \
    --output-dir data/independent_seed/ --device cuda:0

# Step 2: Generate OLMo-2-1B chains with Set B seeds
echo ""
echo ">>> [2/4] Generating OLMo-2-1B with independent Set B seeds"
python generate_chain.py \
    --model-name olmo-2-1b-indepB \
    --model-path /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B \
    --input data/independent_seeds_B.jsonl \
    --temperature 0.7 --top-p 0.9 \
    --output-dir data/independent_seed/ --device cuda:0

# Step 3: Extract features
echo ""
echo ">>> [3/4] Extracting features for Pythia-2.8B Set A"
python extract_features.py \
    --input data/independent_seed/pythia-2.8b-indepA/generations_shard0.jsonl \
    --output data/features_indep_pythia-2.8b.csv \
    --device cuda:0

echo ""
echo ">>> [3/4] Extracting features for OLMo-2-1B Set B"
python extract_features.py \
    --input data/independent_seed/olmo-2-1b-indepB/generations_shard0.jsonl \
    --output data/features_indep_olmo-2-1b.csv \
    --device cuda:0

# Step 4: Cross-generator evaluation
echo ""
echo ">>> [4/4] Running cross-generator evaluation"
python eval_independent_seed.py

echo ""
echo "=== All done ==="
echo "End: $(date)"
