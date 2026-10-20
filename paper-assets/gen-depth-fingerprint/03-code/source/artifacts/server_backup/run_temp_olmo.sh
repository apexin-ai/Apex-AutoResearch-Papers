#!/bin/bash
set -e
source /root/miniconda3/bin/activate
cd /root/gen-depth-fingerprint

echo "=== Temperature Curve: OLMo-2-1B (GPU 0) ==="
echo "Start: $(date)"

# OLMo-2-1B t=0.5 only; t=0.9 runs separately in temp_olmo_t09 session (GPU 2)
echo ""
echo ">>> OLMo-2-1B t=0.5 top_p=0.9"
python generate_chain.py \
    --model-name olmo-2-1b-t05 \
    --model-path /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B \
    --temperature 0.5 --top-p 0.9 \
    --output-dir data/ --device cuda:0

echo ""
echo "=== OLMo-2-1B t=0.5 generation done ==="
echo "End: $(date)"
