#!/bin/bash
# Master script: merge -> inference -> analysis
set -e

source /root/miniconda3/bin/activate
cd /root/autodl-tmp/struct_self_consist_ie

echo "============================================"
echo "  exp_028 Post-Processing Pipeline"
echo "  5-epoch LoRA Few-NERD convergence test"
echo "============================================"
echo ""

echo "=== Step 1: Merge LoRA ==="
bash scripts/exp_028_postprocess/01_merge_lora.sh
echo ""

echo "=== Step 2: Inference (N=8, T=1.0, logprobs) ==="
bash scripts/exp_028_postprocess/02_inference.sh
echo ""

echo "=== Step 3: Analysis ==="
python scripts/exp_028_postprocess/03_analyze.py
echo ""

echo "============================================"
echo "  All done. Results at:"
echo "  output/exp_028_fewnerd_5epoch/analysis_results.json"
echo "============================================"
