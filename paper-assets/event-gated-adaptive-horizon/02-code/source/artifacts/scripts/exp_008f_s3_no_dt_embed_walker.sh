#!/bin/bash
# exp_008f_s3_no_dt_embed_walker — no_dt_emb seed 3, CI core ablation
# Parent: exp_008f_no_dt_embed_subsample_on_h8 (seed=1)
# 008f seeds: 0=009h, 1=008f, 2=009c, 3=this
# GPU: cuda:1 (after 018v2 finishes), MUJOCO_EGL_DEVICE_ID=1
# chmod +x before running

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/event-gated-adaptive-horizon

CUDA_VISIBLE_DEVICES=1 \
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 \
MUJOCO_GL=egl \
MUJOCO_EGL_DEVICE_ID=1 \
python -u dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/exp_008f_s3_no_dt_embed_walker \
  --steps 105000 \
  --seed 3 \
  --compile False \
  --device cuda:0 \
  --gate_enabled True \
  --gate_fixed_dt 2 \
  --gate_subsample_max_dt 2 \
  --imag_horizon 8 \
  --gate_dt_embed_dim 0 \
  --checkpoint_every 25000
