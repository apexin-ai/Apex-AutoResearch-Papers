#!/bin/bash
set -e
source /root/miniconda3/bin/activate
cd /root/gen-depth-fingerprint

echo "=== Temperature Curve: Qwen3-0.6B (GPU 1) ==="
echo "Start: $(date)"

# Qwen3-0.6B t=0.5 only; t=0.9 runs separately in temp_qwen06_t09 session (GPU 3)
echo ""
echo ">>> Qwen3-0.6B t=0.5 top_p=0.9"
python generate_chain.py \
    --model-name qwen3-0.6b-t05 \
    --model-path /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base \
    --temperature 0.5 --top-p 0.9 \
    --output-dir data/ --device cuda:1

echo ""
echo "=== Qwen3-0.6B t=0.5 generation done ==="
echo "End: $(date)"
