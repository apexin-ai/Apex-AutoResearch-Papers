#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/gen-depth-fingerprint

echo "[$(date)] Waiting for Pythia generation to complete..."
while pgrep -f "generate_chain_decoding.*pythia" > /dev/null 2>&1; do
    sleep 60
done
echo "[$(date)] Pythia done. Extracting features on cuda:0..."
for strategy in greedy topk; do
    INPUT="data/pythia-2.8b-${strategy}/generations_shard0.jsonl"
    OUTPUT="data/features_pythia-2.8b-${strategy}.csv"
    if [ -f "$INPUT" ] && [ ! -f "$OUTPUT" ]; then
        echo "[$(date)] Extracting: pythia-2.8b-${strategy}"
        python3 extract_features.py --input "$INPUT" --output "$OUTPUT" --device cuda:0 --batch-size 16
    fi
done
echo "[$(date)] Pythia feature extraction complete."
