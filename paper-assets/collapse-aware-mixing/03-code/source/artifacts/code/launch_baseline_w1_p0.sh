#!/bin/bash
# P0 Baseline: Pure Real (w=1.0) — no-collapse upper bound
# submit_training_job timeout: 86400
set -euo pipefail
source /root/collapse-aware-mixing/env_init.sh

# Preflight
[ -f /root/collapse-aware-mixing/controlled_pipeline.py ] || { echo "FAIL: controlled_pipeline.py not found"; exit 1; }
python3 -c "import torch; assert torch.cuda.is_available(), 'No GPU'" || exit 1
[ -d /root/autodl-tmp/output_p0/baseline_w1 ] && { echo "WARN: output dir exists, results may be overwritten"; }

cd /root/collapse-aware-mixing
python3 controlled_pipeline.py \
    --output_dir /root/autodl-tmp/output_p0/baseline_w1 \
    --num_generations 3 \
    --tokens_per_generation 20000000 \
    --checkpoint_interval_tokens 5000000 \
    --model_name EleutherAI/pythia-1b \
    --learning_rate 0.000002 \
    --Kp 0 --Ki 0 \
    --w_init 1.0 --w_min 1.0 --w_max 1.0 \
    --seed 42 \
    --no_wandb
