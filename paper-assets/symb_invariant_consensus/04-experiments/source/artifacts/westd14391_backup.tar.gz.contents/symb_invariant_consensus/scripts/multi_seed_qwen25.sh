#!/bin/bash
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

APIBASE="http://localhost:8002/v1"
K=12
TEMP=0.7
MATH="data/empty.json"
PW_DATA="data/empty.json"
FOLIO="data/folio_full.json"
PW_FULL="data/proofwriter_full.json"

echo "=========================================="
echo "Multi-seed Qwen2.5-14B replication"
echo "Started: $(date)"
echo "=========================================="

# --- FOLIO-204 ---
for SEED in 123 456 789; do
    OUTDIR="results/multi_seed/qwen25_folio_seed${SEED}"
    mkdir -p "$OUTDIR"
    echo ""
    echo ">>> FOLIO seed=$SEED started at $(date)"
    python run_full_mvp.py \
      --mode vllm --api-base "$APIBASE" --k $K --temperature $TEMP \
      --seed $SEED \
      --math-data "$MATH" --pw-data "$PW_DATA" --folio-data "$FOLIO" \
      --output "$OUTDIR/results.json" \
      --save-intermediates \
      2>&1 | tee /tmp/qwen25_folio_seed${SEED}.log
    echo ">>> FOLIO seed=$SEED completed at $(date)"
done

# --- ProofWriter-600 ---
for SEED in 123 456 789; do
    OUTDIR="results/multi_seed/qwen25_pw_seed${SEED}"
    mkdir -p "$OUTDIR"
    echo ""
    echo ">>> ProofWriter seed=$SEED started at $(date)"
    python run_full_mvp.py \
      --mode vllm --api-base "$APIBASE" --k $K --temperature $TEMP \
      --seed $SEED \
      --math-data "$MATH" --pw-data "$PW_FULL" \
      --output "$OUTDIR/results.json" \
      --save-intermediates \
      2>&1 | tee /tmp/qwen25_pw_seed${SEED}.log
    echo ">>> ProofWriter seed=$SEED completed at $(date)"
done

echo ""
echo "=========================================="
echo "All 6 experiments completed at $(date)"
echo "=========================================="
