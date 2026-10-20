#!/bin/bash
# Exp 019a: PickCube Baseline (ManiSkill3 state-based)
# Restart of previously killed run.

set -euo pipefail

CUDA_ID="${CUDA_ID:-0}"
EGL_ID="${EGL_ID:-${CUDA_ID}}"

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/event-gated-adaptive-horizon

export MUJOCO_GL=egl
export MUJOCO_EGL_DEVICE_ID=${EGL_ID}

LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 \
python -u dreamer.py \
  --configs defaults maniskill_state \
  --task maniskill_PickCube-v1 \
  --steps 200000 \
  --seed 1 \
  --device cuda:${CUDA_ID} \
  --compile False \
  --checkpoint_every 25000 \
  --logdir logdir/exp_019a_pickcube_baseline
