#!/bin/bash
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

echo "=== [$(date)] Wild 2: ASCII Perturbation Experiment ==="
echo "Using vLLM on port 8020 (Mistral-7B, GPU0)"

PYTHONUNBUFFERED=1 python -u analysis_ascii_perturbation.py 2>&1 | tee results/wild2_ascii_perturbation/wild2.log

echo "=== [$(date)] Wild 2 DONE ==="
