#!/bin/bash
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

for SEED in 42 123 456 789; do
    echo "=== $(date) Starting Mistral-7B ProofWriter seed=$SEED ==="
    python run_cross_dataset_replication.py \
      --dataset proofwriter \
      --data-path data/proofwriter_full.json \
      --k 12 \
      --vllm-port 8003 \
      --seed $SEED \
      --temperature 0.7 \
      --output results/multi_seed/mistral_pw_seed${SEED}/results.json \
      2>&1 | tee /tmp/mistral_pw_seed${SEED}.log
    echo "=== $(date) Completed seed=$SEED ==="
done
echo "ALL_SEEDS_DONE $(date)"
