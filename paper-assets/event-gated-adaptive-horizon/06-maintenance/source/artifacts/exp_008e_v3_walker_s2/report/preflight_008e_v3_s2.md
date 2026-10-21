# Preflight Report: exp_008e_v3_walker_s2

**Server**: bjb1-45299 | **Date**: 2026-05-15 06:35 CST

## Checklist

| # | Check | Result | Details |
|---|-------|--------|---------|
| 1 | Disk space | **PASS** | /root/autodl-tmp: 241GB free (4% used of 250GB) |
| 2 | GPU status | **PASS** | GPU 0: 4165/97887 MiB, 20% util (s1 running); GPU 1: 4167/97887 MiB, 9% util |
| 3 | s1 progress | **RUNNING** | See below |
| 4 | s2 logdir | **PASS** | Path does not exist — no overwrite risk |
| 5 | Code integrity | **PASS** | dreamer.py exists; configs.yaml has gate_enabled, gate_fixed_dt, gate_subsample_max_dt, imag_horizon, gate_dt_embed_dim |
| 6 | Env vars | **PASS** | MUJOCO_GL/PYOPENGL_PLATFORM hardcoded in dreamer.py (lines 7-8) + set in launch command |

## s1 Progress

- **Train step**: 92000 / 105000 (87.6%)
- **Last eval step**: 85000, eval_return = 657.31
- **Train return** (latest): 576 ~ 748 (step 88000-92000)
- **Started**: 2026-05-15 02:50 CST
- **Elapsed**: ~3h 45m to reach step 92000
- **Rate**: ~409 steps/min
- **Remaining**: 13000 steps → ~32 min
- **ETA**: ~07:07 CST (2026-05-15)

## s2 Submit Command

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && MUJOCO_GL=osmesa PYOPENGL_PLATFORM=osmesa LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 15 --gate_dt_embed_dim 32
```

**Note**: device=cuda:0 — submit_training_job maps physical GPU, script always uses cuda:0.

## Verdict

All checks **PASS**. s1 still running, estimated completion ~07:07 CST. s2 can be submitted after s1 finishes, or immediately on the other GPU.
