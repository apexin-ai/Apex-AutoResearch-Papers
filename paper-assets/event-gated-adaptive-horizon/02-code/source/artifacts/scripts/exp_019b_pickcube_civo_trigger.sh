#!/bin/bash
# Exp 019b: PickCube CIVO Trigger (ManiSkill3 state-based)
# Condition: trained dt_emb + subsample ON + dt=2 imagination + H=8
# Expected: NVE>1.5x triggers CIVO validation

set -euo pipefail

unset CUDA_VISIBLE_DEVICES

CUDA_ID="${CUDA_ID:-1}"
EGL_ID="${EGL_ID:-${CUDA_ID}}"

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/event-gated-adaptive-horizon

export MUJOCO_GL=egl
export MUJOCO_EGL_DEVICE_ID=${EGL_ID}

LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 \
python -u dreamer.py \
  --configs maniskill_state \
  --task maniskill_PickCube-v1 \
  --steps 200000 \
  --seed 1 \
  --device cuda:${CUDA_ID} \
  --compile False \
  --checkpoint_every 25000 \
  --gate_enabled True \
  --gate_fixed_dt 2 \
  --gate_subsample_min_dt 1 \
  --gate_subsample_max_dt 2 \
  --imag_horizon 8 \
  --logdir ./logdir/exp_019b_pickcube_civo_trigger
