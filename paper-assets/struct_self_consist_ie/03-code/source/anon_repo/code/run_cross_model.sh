#!/bin/bash
set -e

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

BASE=/root/autodl-tmp/struct_self_consist_ie
OUT=$BASE/output/exp_cross_model_consistency
SCRIPT=$BASE/code/cross_model_construction.py

mkdir -p $OUT

echo "=========================================="
echo "B5 Cross-Model Self-Consistency Experiment"
echo "=========================================="
echo ""

# --- SciERC ---
echo "[1/2] Running SciERC cross-model construction..."
python3 $SCRIPT \
  --qwen $BASE/output/exp_026_t10_seed42/samples.jsonl \
  --llama $BASE/output/exp007_llama_inference/samples.jsonl \
  --output $OUT/scierc_results.json \
  --dataset scierc

echo ""
echo "[SciERC] Done. Results: $OUT/scierc_results.json"
echo ""

# --- FewNERD ---
echo "[2/2] Running FewNERD cross-model construction..."
python3 $SCRIPT \
  --qwen $BASE/output/exp_021_inference/samples.jsonl \
  --llama $BASE/output/llama_fewnerd_s42/samples.jsonl \
  --output $OUT/fewnerd_results.json \
  --dataset fewnerd \
  --skip-m030

echo ""
echo "[FewNERD] Done. Results: $OUT/fewnerd_results.json"
echo ""
echo "=========================================="
echo "All done. Results in: $OUT/"
echo "=========================================="
