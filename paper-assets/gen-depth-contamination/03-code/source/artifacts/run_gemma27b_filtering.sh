#!/bin/bash
# Gemma-27B filtering experiment launcher
# 3 strategies × 3 seeds = 9 runs on cuda:3
# Expected: ~30-40 min per run, ~4.5-6 hours total

set -e

cd /root/autodl-tmp/gen-depth-contamination
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_ENDPOINT=https://hf-mirror.com
export HF_DATASETS_OFFLINE=1
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export CUDA_VISIBLE_DEVICES=3

DEVICE="cuda:0"  # maps to physical GPU 3 via CUDA_VISIBLE_DEVICES

STRATEGIES="no_filter binary_ours graduated_a09"
SEEDS="42 123 456"

echo "=========================================="
echo "Gemma-27B Filtering Experiment"
echo "Start: $(date)"
echo "=========================================="

for strategy in $STRATEGIES; do
    for seed in $SEEDS; do
        echo ""
        echo ">>> Running: strategy=$strategy seed=$seed [$(date)]"
        python scripts/exp_gemma27b_filtering.py \
            --strategy $strategy \
            --seed $seed \
            --device $DEVICE \
            2>&1 | tee -a logs/exp_gemma27b_filtering/run_all.log
        echo "<<< Done: strategy=$strategy seed=$seed [$(date)]"
    done
done

echo ""
echo "=========================================="
echo "All runs complete: $(date)"
echo "=========================================="
