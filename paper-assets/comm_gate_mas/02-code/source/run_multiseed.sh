#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas
mkdir -p outputs/distilbert_multiseed

for SEED in 0 1 2; do
    echo "=== Starting seed=$SEED at $(date) ==="
    python3 src/pruning_validation.py \
        --mode online_pruning \
        --config configs/oracle_qwen_gsm8k_local.yaml \
        --num-tasks 300 \
        --detection-mode distilbert \
        --distilbert-checkpoint artifacts/classifier/distilbert_ack/checkpoint-810 \
        --data-seed $SEED \
        --output outputs/distilbert_multiseed/seed_${SEED}.json \
        2>&1 | tee outputs/distilbert_multiseed/seed_${SEED}.log
    echo "=== Finished seed=$SEED at $(date) ==="
done
