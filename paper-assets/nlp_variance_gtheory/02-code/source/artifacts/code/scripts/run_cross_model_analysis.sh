#!/bin/bash
# Cross-model G-theory analysis pipeline (bf16 + fp32 only)
# Usage: bash scripts/run_cross_model_analysis.sh

set -euo pipefail

cd /root/nlp_variance_gtheory
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export PYTHONPATH=/root/nlp_variance_gtheory:$PYTHONPATH

mkdir -p results/analysis

# Step 1: Merge data (cross-model: bf16+fp32 only)
echo "=== Step 1: Merging cross-model data ==="
python -m src.analysis.merge_cross_model \
  --input-glob "results/exp001_*/shard_*.jsonl" \
  --output results/analysis/cross_model_bf16_fp32.csv \
  --cross-model

# Step 2: 7-facet G-study (model as random facet)
echo "=== Step 2: G-study variance decomposition ==="
python -m src.analysis.model_facet_analysis \
  --input results/analysis/cross_model_bf16_fp32.csv \
  --output results/analysis/cross_model_gstudy.json

# Step 3: Bootstrap CIs (200 resamples for preliminary)
echo "=== Step 3: Bootstrap confidence intervals ==="
python -m src.analysis.bootstrap_ci \
  --input results/analysis/cross_model_bf16_fp32.csv \
  --n-boot 200 \
  --output results/analysis/cross_model_bootstrap.json

echo "=== Done ==="
