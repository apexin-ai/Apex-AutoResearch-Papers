#!/usr/bin/env bash
# G-theory MVP Phase A experiment pipeline.
#
# All inference runs on a SINGLE GPU (cuda:0) to avoid cross-card
# manufacturing-variance confounds.
#
# Usage:
#   bash run_mvp.sh              # full pipeline
#   bash run_mvp.sh --sanity     # sanity check only

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

export CUDA_VISIBLE_DEVICES=0

echo "=== Step 1: Data Preparation ==="
python -m src.data.sample_mmlu --output data/mmlu_items.json
python -m src.data.few_shot    --output data/few_shot_examples.json

echo "=== Step 2: Design Matrix ==="
python -m src.design.generate_design --output design_matrix.csv

# Sanity check mode
if [[ "${1:-}" == "--sanity" ]]; then
    echo "=== Sanity Check ==="
    python -m src.inference.sanity_check --gpu-id 0 --output results/sanity_check.json
    echo "=== Sanity Check Done ==="
    exit 0
fi

echo "=== Step 3: Inference (108 conditions, single GPU) ==="
mkdir -p results
python -m src.inference.run_experiment \
    --design  design_matrix.csv \
    --items   data/mmlu_items.json \
    --few-shot data/few_shot_examples.json \
    --gpu-id 0 \
    --output results/all_results.jsonl

echo "=== Step 4: Analysis ==="
python -m src.analysis.variance_decomposition --input results/all_results.jsonl
python -m src.analysis.d_study --input results/variance_components.json
python -m src.analysis.visualize \
    --components results/variance_components.json \
    --dstudy results/d_study_results.json

echo ""
echo "=== Done ==="
