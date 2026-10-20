#!/bin/bash
# Contingency B: Lower learning rate — lr=1e-6 (half of v7)
# Use if v7 fails due to training instability at lr=2e-6.
# Same 20M tokens/gen as v7, only LR changes.
# Expected runtime: ~5 GPU-hours on RTX PRO 6000.
set -euo pipefail
source /root/collapse-aware-mixing/env_init.sh
bash /root/collapse-aware-mixing/preflight.sh
cd /root/collapse-aware-mixing
python3 pilot_pipeline.py \
    --output_dir /root/autodl-tmp/output_v8_lowlr \
    --num_generations 3 \
    --tokens_per_generation 20000000 \
    --checkpoint_interval_tokens 5000000 \
    --model_name EleutherAI/pythia-1b \
    --learning_rate 0.000001 \
    --seed 42 \
    --no_wandb
