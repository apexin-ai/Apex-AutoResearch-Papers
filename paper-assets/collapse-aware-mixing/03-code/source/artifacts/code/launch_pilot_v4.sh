#!/bin/bash
set -euo pipefail
source /root/collapse-aware-mixing/env_init.sh
bash /root/collapse-aware-mixing/preflight.sh
cd /root/collapse-aware-mixing
python3 pilot_pipeline.py \
    --output_dir /root/autodl-tmp/output \
    --num_generations 3 \
    --tokens_per_generation 90000000 \
    --checkpoint_interval_tokens 10000000 \
    --holdout_size 5000 \
    --no_wandb \
    --seed 42
