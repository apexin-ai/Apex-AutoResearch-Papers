#!/bin/bash
# Minimal real data baseline (w=0.1): matches PI controller's w_min
# Controls for "PI just happens to pick a good constant"
set -euo pipefail
source /root/collapse-aware-mixing/env_init.sh
bash /root/collapse-aware-mixing/preflight.sh
cd /root/collapse-aware-mixing
python3 pilot_pipeline.py \
    --output_dir /root/autodl-tmp/output_baseline_w01 \
    --num_generations 3 \
    --tokens_per_generation 20000000 \
    --checkpoint_interval_tokens 5000000 \
    --holdout_size 5000 \
    --learning_rate 0.000002 \
    --fixed-ratio 0.1 \
    --no_wandb \
    --seed 42
