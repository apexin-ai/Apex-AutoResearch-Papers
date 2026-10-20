#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/gen-depth-fingerprint

echo "[$(date)] Waiting for OLMo generation to complete..."
# Wait for any olmo generation process to finish
while pgrep -f "generate_chain_decoding.*olmo" > /dev/null 2>&1; do
    sleep 60
done
echo "[$(date)] OLMo done. Starting Qwen3-1.7B on cuda:1..."
python3 generate_chain_decoding.py --model-name qwen3-1.7b --device cuda:1 --strategies greedy topk
echo "[$(date)] Qwen3-1.7B complete."

# After Qwen finishes, start feature extraction for all available data
echo "[$(date)] Starting feature extraction..."
for model in pythia-2.8b olmo-2-1b qwen3-1.7b; do
    for strategy in greedy topk; do
        INPUT="data/${model}-${strategy}/generations_shard0.jsonl"
        OUTPUT="data/features_${model}-${strategy}.csv"
        if [ -f "$INPUT" ] && [ ! -f "$OUTPUT" ]; then
            echo "[$(date)] Extracting: ${model}-${strategy}"
            python3 extract_features.py --input "$INPUT" --output "$OUTPUT" --device cuda:1 --batch-size 16
        fi
    done
done
echo "[$(date)] All feature extraction complete."

# Run analysis
echo "[$(date)] Running analysis..."
python3 analyze_decoding_strategy.py
echo "[$(date)] All done."
