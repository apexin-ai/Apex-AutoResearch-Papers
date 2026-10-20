#!/bin/bash
set -e
cd /root/autodl-tmp/struct_self_consist_ie
source /root/miniconda3/bin/activate

export CUDA_VISIBLE_DEVICES=0

echo "=== Stage 1: Extract hidden states ==="
python3 code/probe/extract_hidden_states_exp016.py 2>&1

echo ""
echo "=== Stage 2: Run probe ==="
python3 code/probe/hidden_state_probe_exp016.py 2>&1

echo ""
echo "=== Done ==="
cat output/hidden_state_probe_exp016/results.json
