#!/usr/bin/env bash
set -euo pipefail
cd .

source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
export CUDA_VISIBLE_DEVICES=0
export HF_HOME=/path/to/model
export HF_ENDPOINT=https://hf-mirror.com
export LD_LIBRARY_PATH=/usr/local/cuda-12.8/targets/x86_64-linux/lib/:${LD_LIBRARY_PATH:-}
export PYTHONPATH=.

echo "=== MVP Phase A: Start $(date) ==="
mkdir -p results

echo "=== Step 1: Inference (108 conditions × 50 items) ==="
python -m src.inference.run_experiment \
    --design  design_matrix.csv \
    --items   data/mmlu_items.json \
    --few-shot data/few_shot_examples.json \
    --gpu-id 0 \
    --output results/all_results.jsonl

echo "=== Step 2: Variance Decomposition ==="
python -m src.analysis.variance_decomposition --input results/all_results.jsonl

echo "=== Step 3: D-study ==="
python -m src.analysis.d_study --input results/variance_components.json

echo "=== Step 4: Visualization ==="
python -m src.analysis.visualize \
    --components results/variance_components.json \
    --dstudy results/d_study_results.json

echo "=== MVP Phase A: Complete $(date) ==="
echo "FILES:"
ls -la results/
