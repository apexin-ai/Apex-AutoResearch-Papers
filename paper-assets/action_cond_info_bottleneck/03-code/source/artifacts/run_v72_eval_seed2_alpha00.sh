#!/bin/bash
# v7.2 seed2 eval: alpha=0.0 passthrough
cd /root/acib
CUDA_VISIBLE_DEVICES=0 python3 -u scripts/eval_acib.py \
  --checkpoint_dir /root/autodl-tmp/acib_v7.2_connector_scorer_seed2 \
  --checkpoint_step 20000 \
  --base_model lerobot/smolvla_libero \
  --suites libero_spatial libero_object libero_goal libero_10 \
  --n_episodes 50 \
  --gpu 0 --seed 42 \
  --scoring_alpha 0.0 \
  --out_dir /root/autodl-tmp/v72_eval/alpha_0.0_seed2
