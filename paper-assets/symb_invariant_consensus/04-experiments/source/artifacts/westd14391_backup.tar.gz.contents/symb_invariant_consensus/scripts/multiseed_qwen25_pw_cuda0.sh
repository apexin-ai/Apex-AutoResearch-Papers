#!/bin/bash
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

APIBASE="http://localhost:8005/v1"
K=12
TEMP=0.7
MATH="data/empty.json"
PW_FULL="data/proofwriter_full.json"

echo "=========================================="
echo "Qwen2.5 × ProofWriter Multi-seed (cuda:0)"
echo "Started: $(date)"
echo "=========================================="

for SEED in 123 456 789; do
    OUTDIR="results/multi_seed/qwen25_pw_seed${SEED}"
    mkdir -p "$OUTDIR"
    echo ""
    echo ">>> PW seed=$SEED started at $(date)"
    python run_full_mvp.py \
      --mode vllm --api-base "$APIBASE" --k $K --temperature $TEMP \
      --seed $SEED \
      --math-data "$MATH" --pw-data "$PW_FULL" \
      --output "$OUTDIR/results.json" \
      --save-intermediates \
      2>&1 | tee /tmp/qwen25_pw_seed${SEED}.log
    echo ">>> PW seed=$SEED completed at $(date)"
done

echo ""
echo "=========================================="
echo "All 3 PW experiments completed at $(date)"
echo "=========================================="
echo "SENTINEL_QWEN25_PW_MULTISEED_DONE"
