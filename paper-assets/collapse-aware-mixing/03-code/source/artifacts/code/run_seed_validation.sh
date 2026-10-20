#!/bin/bash
# 3-seed validation runner: PI controller vs fixed ratio baseline
# Runs 6 experiments serially (3 seeds x 2 methods) on a single GPU.
# Set FIXED_RATIO env var to override the fixed mixing ratio (default 0.5).
set -euo pipefail
source /root/collapse-aware-mixing/env_init.sh
cd /root/collapse-aware-mixing

SEEDS="42 123 456"
FIXED_RATIO=${FIXED_RATIO:-0.5}

for seed in $SEEDS; do
  echo "=== Seed $seed: PI controller ==="
  python3 controlled_pipeline.py \
    --output_dir /root/autodl-tmp/output_seed_${seed}_pi \
    --num_generations 3 \
    --tokens_per_generation 20000000 \
    --checkpoint_interval_tokens 5000000 \
    --model_name EleutherAI/pythia-1b \
    --learning_rate 0.000002 \
    --seed $seed \
    --no_wandb

  echo "=== Seed $seed: Fixed ratio ==="
  python3 controlled_pipeline.py \
    --output_dir /root/autodl-tmp/output_seed_${seed}_fixed \
    --num_generations 3 \
    --tokens_per_generation 20000000 \
    --checkpoint_interval_tokens 5000000 \
    --model_name EleutherAI/pythia-1b \
    --learning_rate 0.000002 \
    --Kp 0 --Ki 0 --w_init $FIXED_RATIO \
    --seed $seed \
    --no_wandb
done

echo "=== All seeds complete. Run analyze_seed_validation.py ==="
