#!/bin/bash
# Mistral-7B × FOLIO-204 single seed=789 only (cuda:3, port 8004)
# Created after killing duplicate multi-seed process
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

APIBASE="http://localhost:8004/v1"
K=12
TEMP=0.7
MATH="data/empty.json"
PW="data/empty.json"
FOLIO="data/folio_full.json"
SEED=789
OUTDIR="results/multi_seed/mistral_folio_seed${SEED}"

mkdir -p "$OUTDIR"

echo "=========================================="
echo "Mistral-7B × FOLIO-204 seed=$SEED (cuda:3)"
echo "Started: $(date)"
echo "=========================================="

python run_full_mvp.py \
  --mode vllm --api-base "$APIBASE" --k $K --temperature $TEMP \
  --seed $SEED \
  --math-data "$MATH" --pw-data "$PW" --folio-data "$FOLIO" \
  --output "$OUTDIR/results.json" \
  --save-intermediates \
  2>&1 | tee /tmp/mistral_folio_seed789.log

echo ">>> FOLIO seed=$SEED completed at $(date)"
echo "SENTINEL_MISTRAL_FOLIO_SEED789_DONE"
