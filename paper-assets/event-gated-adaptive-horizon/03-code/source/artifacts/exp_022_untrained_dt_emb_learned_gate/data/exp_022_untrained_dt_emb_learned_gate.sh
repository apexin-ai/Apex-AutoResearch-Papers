#!/bin/bash
# Exp 022: Untrained dt_emb + Learned Gate (Walker Walk)
# Hypothesis: frozen dt_emb prevents CIVO while gate still learns adaptive horizon selection
# dt_emb: randomly initialized, frozen (no gradients)
# gate: enabled, gumbel-softmax, receives gradients

set -euo pipefail

unset CUDA_VISIBLE_DEVICES

CUDA_ID="${CUDA_ID:-0}"

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/event-gated-adaptive-horizon

LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl \
python -u dreamer.py \
  --configs dmc_vision \
  --task dmc_walker_walk \
  --steps 105000 \
  --seed 0 \
  --device cuda:${CUDA_ID} \
  --compile True \
  --checkpoint_every 10000 \
  --gate_enabled True \
  --gate_dt_embed_dim 32 \
  --dt_emb_freeze True \
  --gate_subsample_min_dt 1 \
  --gate_subsample_max_dt 2 \
  --imag_horizon 8 \
  --logdir ./logdir/exp_022_untrained_dt_emb_learned_gate
