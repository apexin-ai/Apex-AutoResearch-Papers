#!/bin/bash
# Exp 022b: Untrained dt_emb + Learned Gate, NO Curriculum (Walker Walk)
# Hypothesis: with curriculum disabled (phase1=0, phase2=0), gate has dt>1
# freedom from step 1. If frozen dt_emb prevents CIVO while gate learns
# meaningful temporal abstraction, eval should match or approach baseline
# without value overestimation.
# dt_emb: randomly initialized, frozen (no gradients)
# gate: enabled, gumbel-softmax, receives gradients, no curriculum warmup

set -euo pipefail

unset CUDA_VISIBLE_DEVICES

CUDA_ID="${CUDA_ID:-0}"

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/event-gated-adaptive-horizon

MUJOCO_EGL_DEVICE_ID=${CUDA_ID} LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl \
python -u dreamer.py \
  --configs dmc_proprio \
  --task dmc_walker_walk \
  --steps 105000 \
  --seed 0 \
  --device cuda:${CUDA_ID} \
  --compile False \
  --checkpoint_every 10000 \
  --gate_enabled True \
  --gate_dt_embed_dim 32 \
  --dt_emb_freeze True \
  --gate_subsample_min_dt 1 \
  --gate_subsample_max_dt 2 \
  --gate_curriculum_phase1 0 \
  --gate_curriculum_phase2 0 \
  --imag_horizon 8 \
  --logdir ./logdir/exp_022b_no_curriculum
