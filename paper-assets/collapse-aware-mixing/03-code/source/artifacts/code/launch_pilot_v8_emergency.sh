#!/bin/bash
# Contingency A: D008 emergency extension — 50M tokens/gen (2.5x v7)
# Use if v7 fails due to insufficient signal at 20M tokens/gen.
# Expected runtime: ~12-15 GPU-hours on RTX PRO 6000.
# submit_training_job timeout: 172800 (48h)
set -euo pipefail
source /root/collapse-aware-mixing/env_init.sh
bash /root/collapse-aware-mixing/preflight.sh
cd /root/collapse-aware-mixing
python3 pilot_pipeline.py \
    --output_dir /root/autodl-tmp/output_v8 \
    --num_generations 3 \
    --tokens_per_generation 50000000 \
    --checkpoint_interval_tokens 5000000 \
    --model_name EleutherAI/pythia-1b \
    --learning_rate 0.000002 \
    --seed 42 \
    --no_wandb
