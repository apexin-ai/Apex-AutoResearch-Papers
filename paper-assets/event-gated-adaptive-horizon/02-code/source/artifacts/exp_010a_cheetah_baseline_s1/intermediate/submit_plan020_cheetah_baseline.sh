#!/bin/bash
# plan_020: Cheetah Run dt=1 baseline, 3 seeds (512K steps)
# Purpose: v/e calibration reference for second environment, cross-env C1/C2 validation
# Usage: copy individual tmux commands below. Replace cuda:0 with available GPU.
# DO NOT run this script directly.

CD="/root/autodl-tmp/event-gated-adaptive-horizon"
ENV_SETUP="source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd $CD"

# === Seed 1 ===
# tmux new-session -d -s exp_010a_s1 "eval \"$ENV_SETUP\" && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 512000 --seed 1 --compile False --device cuda:0 --gate_enabled False 2>&1 | tee logdir/exp_010a_cheetah_baseline_s1.log"

# === Seed 2 ===
# tmux new-session -d -s exp_010a_s2 "eval \"$ENV_SETUP\" && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s2 --steps 512000 --seed 2 --compile False --device cuda:0 --gate_enabled False 2>&1 | tee logdir/exp_010a_cheetah_baseline_s2.log"

# === Seed 3 ===
# tmux new-session -d -s exp_010a_s3 "eval \"$ENV_SETUP\" && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s3 --steps 512000 --seed 3 --compile False --device cuda:0 --gate_enabled False 2>&1 | tee logdir/exp_010a_cheetah_baseline_s3.log"