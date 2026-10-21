#!/bin/bash
# exp_023b_cheetah_baseline_s1 — Cheetah Run vanilla baseline seed=1
# Pure DreamerV3, no temporal embedding, no gate
# Cross-environment validation: Cheetah baseline for NVE normalization

set -euo pipefail
unset CUDA_VISIBLE_DEVICES

CUDA_ID="${CUDA_ID:-1}"

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/event-gated-adaptive-horizon

MUJOCO_EGL_DEVICE_ID=${CUDA_ID} \
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 \
MUJOCO_GL=egl \
python -u dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_cheetah_run \
  --steps 200000 \
  --seed 1 \
  --device cuda:${CUDA_ID} \
  --compile False \
  --gate_enabled False \
  --checkpoint_every 10000 \
  --logdir ./logdir/exp_023b_cheetah_baseline_s1
