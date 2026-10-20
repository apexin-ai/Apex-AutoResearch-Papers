#!/bin/bash
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/bin/activate

echo "=== EXP-060 Dry-run (n=3) ==="
PYTHONUNBUFFERED=1 python -u scripts/cross_model_extract.py \
    --traces-dir results/exp033_mistral_7b_folio204/intermediates \
    --api-base http://localhost:8001/v1 \
    --model auto \
    --temperature 0.3 \
    --output results/exp060_cross_qwen25_14b_extractor/dryrun_results.json \
    2>&1 | head -100

echo "DRY_RUN_SCRIPT_DONE"
