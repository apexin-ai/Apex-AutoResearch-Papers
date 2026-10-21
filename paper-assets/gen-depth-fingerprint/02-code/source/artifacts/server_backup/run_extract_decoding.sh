#!/bin/bash
# Extract features for all decoding strategy experiments
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/gen-depth-fingerprint

MODELS=("pythia-2.8b" "olmo-2-1b" "qwen3-1.7b")
STRATEGIES=("greedy" "topk")

for model in "${MODELS[@]}"; do
    for strategy in "${STRATEGIES[@]}"; do
        INPUT="data/${model}-${strategy}/generations_shard0.jsonl"
        OUTPUT="data/features_${model}-${strategy}.csv"
        if [ -f "$INPUT" ] && [ ! -f "$OUTPUT" ]; then
            echo "=== Extracting features: ${model}-${strategy} ==="
            python3 extract_features.py \
                --input "$INPUT" \
                --output "$OUTPUT" \
                --device cuda:0 \
                --batch-size 16
            echo "=== Done: ${model}-${strategy} ==="
        elif [ -f "$OUTPUT" ]; then
            echo "SKIP (exists): $OUTPUT"
        else
            echo "SKIP (no input): $INPUT"
        fi
    done
done

echo "All feature extraction done."
