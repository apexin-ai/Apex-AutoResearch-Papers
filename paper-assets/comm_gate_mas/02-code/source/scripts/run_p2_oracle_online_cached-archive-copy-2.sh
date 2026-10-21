#!/bin/bash
# P2: Oracle online pruning with precomputed labels
# Prerequisite: P1 oracle labels uploaded to outputs/oracle_labels/llama_n300_oracle.json
# Hardware: cuda:1 only
set -euo pipefail

CONFIG_BASENAME=$(basename "configs/oracle_online_llama_gsm8k_cached.yaml")
if pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}" > /dev/null 2>&1; then
    echo "ABORT: instance already running ($(pgrep -f "pruning_validation.py.*${CONFIG_BASENAME}"))"
    exit 1
fi

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

cd /root/autodl-tmp/comm_gate_mas

export CUDA_VISIBLE_DEVICES=1

CACHE_PATH="outputs/oracle_labels/llama_n300_oracle.json"

if [ ! -f "$CACHE_PATH" ]; then
    echo "ERROR: Oracle labels not found at $CACHE_PATH"
    echo "Upload from Mac: scp outputs/oracle_labels/llama_n300_oracle.json westb-4x6000-a:/root/autodl-tmp/comm_gate_mas/outputs/oracle_labels/"
    exit 1
fi

echo "=== P2 oracle_online_cached starting at $(date) ==="
echo "Oracle cache: $(python3 -c "import json; d=json.load(open('$CACHE_PATH')); print(f'{len(d)} entries')")"

for seed in 42 123 456; do
    echo "--- Seed $seed at $(date) ---"
    python src/pruning_validation.py \
        --mode online_oracle \
        --config configs/oracle_online_llama_gsm8k_cached.yaml \
        --num-tasks 200 \
        --data-seed $seed \
        --detection-mode oracle_5class \
        --oracle-cache "$CACHE_PATH" \
        --output "outputs/oracle_online_llama_cached/seed_${seed}.json" \
        2>&1

    echo "--- Seed $seed done (exit=$?) at $(date) ---"
done

echo "=== P2 ALL SEEDS COMPLETE at $(date) ==="
