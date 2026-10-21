#!/bin/bash
# exp_021_full_sgs_cheetah_s1 — Full-SGS Cheetah Run seed 1
# 验证 Full-SGS intervention 跨环境一致性
# Parent: exp_018v2_full_sgs_walker_s1 (Walker 版) + exp_010b_cheetah_civo_trigger (Cheetah CIVO baseline)
# Config: trained dt_emb + subsample ON + dt=2 + H=8 + full_sgs=True
# GPU: cuda:0 (CUDA_VISIBLE_DEVICES=0, --device cuda:0, MUJOCO_EGL_DEVICE_ID=0)

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/event-gated-adaptive-horizon

LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 \
MUJOCO_GL=egl \
MUJOCO_EGL_DEVICE_ID=0 \
python -u dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_cheetah_run \
  --logdir logdir/exp_021_full_sgs_cheetah_s1 \
  --steps 105000 \
  --seed 1 \
  --compile False \
  --device cuda:0 \
  --gate_enabled True \
  --gate_fixed_dt 2 \
  --gate_subsample_max_dt 2 \
  --imag_horizon 8 \
  --full_sgs True \
  --checkpoint_every 25000
