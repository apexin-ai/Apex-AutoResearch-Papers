#!/bin/bash
# Alpha=0.3 spatial-only restart (in case full sweep was interrupted)
python3 -u scripts/eval_acib.py \
  --checkpoint_dir /root/acib/outputs/acib_v7_contrastive \
  --checkpoint_step 20000 \
  --base_model lerobot/smolvla_libero \
  --suites libero_spatial \
  --n_episodes 50 \
  --gpu 0 --seed 42 \
  --out_dir /root/autodl-tmp/v7_alpha_sweep/alpha_0.3_spatial_restart \
  --scoring_alpha 0.3
