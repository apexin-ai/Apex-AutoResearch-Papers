# plan_015: Critic dt_embedding detach experiment
# Purpose: Test whether trained dt_embedding is a CIVO vulnerability source
# Method: detach dt_emb in imagination img_step, so critic can't exploit dt gradients
# Base config: same as exp_008d (subsample ON, dt_embed_dim=32, fixed_dt=2, H=8)

# === Submission command (run on cuda:1 after 009e completes) ===

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && nohup python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_015_critic_dt_detach --steps 105000 --seed 1 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --critic_dt_emb_detach True > logdir/exp_015_critic_dt_detach.log 2>&1 &

# === Code changes summary ===
# 1. configs.yaml:119 — added `critic_dt_emb_detach: false` (default off)
# 2. networks.py:241 — RSSM.img_step() accepts `detach_dt_emb=False` parameter
# 3. networks.py:255-257 — when detach_dt_emb=True, dt_emb = dt_emb.detach()
# 4. models.py:609 — reads config flag: detach_dt = getattr(config, 'critic_dt_emb_detach', False)
# 5. models.py:621 — passes detach_dt_emb=detach_dt to dynamics.img_step() in _imagine()

# === Backup files ===
# networks.py.bak.pre_plan015
# models.py.bak.pre_plan015
# configs.yaml.bak.pre_plan015
