#!/bin/bash
# Mistral-7B × FOLIO-204 multi-seed experiment (seeds 123, 456, 789)
# vLLM on cuda:3, port 8004
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

APIBASE="http://localhost:8004/v1"
K=12
TEMP=0.7
MATH="data/empty.json"
PW="data/empty.json"
FOLIO="data/folio_full.json"

echo "=========================================="
echo "Mistral-7B × FOLIO-204 Multi-seed (cuda:3)"
echo "Started: $(date)"
echo "=========================================="

for SEED in 123 456 789; do
    OUTDIR="results/multi_seed/mistral_folio_seed${SEED}"
    mkdir -p "$OUTDIR"
    echo ""
    echo ">>> FOLIO seed=$SEED started at $(date)"
    python run_full_mvp.py \
      --mode vllm --api-base "$APIBASE" --k $K --temperature $TEMP \
      --seed $SEED \
      --math-data "$MATH" --pw-data "$PW" --folio-data "$FOLIO" \
      --output "$OUTDIR/results.json" \
      --save-intermediates \
      2>&1 | tee /tmp/mistral_folio_seed${SEED}.log
    echo ">>> FOLIO seed=$SEED completed at $(date)"
    echo "SENTINEL_MISTRAL_FOLIO_SEED${SEED}_DONE"
done

echo ""
echo "=========================================="
echo "All 3 FOLIO experiments completed at $(date)"
echo "=========================================="
echo "SENTINEL_MISTRAL_FOLIO_MULTISEED_DONE"
