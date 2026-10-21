# Experiment Launch Commands (D184 Priority Order)

Server: westd-51268 (1× RTX PRO 6000) or new AutoDL instance
Project dir: `/root/autodl-tmp/event-gated-adaptive-horizon`
STORM dir: `/root/autodl-tmp/event-gated-adaptive-horizon/storm_dmc`

## Environment Preamble (all experiments)

```bash
# For aml-train image:
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# MuJoCo EGL (required for all DMC experiments):
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
```

---

## Priority 1: exp_walker_no_dt_emb_s0_r2 (DreamerV3)

**Status**: RUNNING on westd-51268 since 2026-05-29, PID 59301. Server unreachable — status unknown.

### Step 1: Check if still running

```bash
ps -p 59301 -o pid,etime,cmd= 2>/dev/null && echo "ALIVE" || echo "DEAD"
# Also check tmux:
tmux ls 2>/dev/null | grep -i walker
# Check log for progress:
tail -20 ~/runs/event-gated-adaptive-horizon/exp_walker_no_dt_emb_s0_r2.log
```

### Step 2a: If ALIVE — monitor only

```bash
# Check current step count:
grep -o 'step [0-9]*' ~/runs/event-gated-adaptive-horizon/exp_walker_no_dt_emb_s0_r2.log | tail -1
# If near 105K, it will finish on its own. No action needed.
```

### Step 2b: If DEAD — restart

```bash
export MUJOCO_EGL_DEVICE_ID=0

cd /root/autodl-tmp/event-gated-adaptive-horizon

nohup bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && \
python -u dreamer.py \
    --configs defaults dmc_proprio \
    --task dmc_walker_walk \
    --logdir logdir/exp_walker_no_dt_emb_s0_r2 \
    --steps 105000 \
    --seed 0 \
    --compile False \
    --device cuda:0 \
    --gate_enabled True \
    --gate_fixed_dt 2 \
    --gate_subsample_max_dt 2 \
    --imag_horizon 8 \
    --gate_dt_embed_dim 0" \
    > ~/runs/event-gated-adaptive-horizon/exp_walker_no_dt_emb_s0_r2.log 2>&1 &

echo "PID: $!"
```

**Note**: DreamerV3 resumes from the latest checkpoint in `logdir/exp_walker_no_dt_emb_s0_r2/` automatically. No need to delete/reset.

---

## Priority 2: STORM Phase 1 — Baseline Verification (dt=1)

**Goal**: Confirm STORM DMC produces a healthy Walker Walk baseline (target: eval return ≥ 600 at 500K steps). This is the prerequisite for all STORM CIVO experiments.

**Prerequisites**: `setup_env.sh` completed (STORM DMC directory assembled).

### Single GPU launch (cuda:0)

```bash
export MUJOCO_EGL_DEVICE_ID=0
export CUDA_VISIBLE_DEVICES=0

cd /root/autodl-tmp/event-gated-adaptive-horizon/storm_dmc

nohup python -u train_dmc.py \
    -n storm_baseline_s0 \
    -seed 0 \
    -config_path config/dmc_walker.yaml \
    > ~/runs/event-gated-adaptive-horizon/storm_baseline_s0.log 2>&1 &

echo "PID: $!"
```

### With wandb

```bash
export MUJOCO_EGL_DEVICE_ID=0
export CUDA_VISIBLE_DEVICES=0
export WANDB_PROJECT=civo-storm

cd /root/autodl-tmp/event-gated-adaptive-horizon/storm_dmc

nohup python -u train_dmc.py \
    -n storm_baseline_s0 \
    -seed 0 \
    -config_path config/dmc_walker.yaml \
    > ~/runs/event-gated-adaptive-horizon/storm_baseline_s0.log 2>&1 &

echo "PID: $!"
```

### Without wandb

```bash
# Add --no-wandb flag:
nohup python -u train_dmc.py \
    -n storm_baseline_s0 \
    -seed 0 \
    -config_path config/dmc_walker.yaml \
    --no-wandb \
    > ~/runs/event-gated-adaptive-horizon/storm_baseline_s0.log 2>&1 &
```

**Estimated GPU-hours**: ~4-6h on RTX PRO 6000 (500K steps).

**Success criteria**: eval/return_mean ≥ 600 with stable learning curve → proceed to Priority 3.
**Failure criteria**: eval/return_mean < 400 at 500K → Scenario C (see storm_scenario_c_text.md).

---

## Priority 3: STORM Phase 2 — dt-Conditioning Experiments

**Prerequisite**: Priority 2 baseline passes (≥ 600 eval return).

Phase 2 requires code changes to add dt-embedding to STORM's transformer model. The implementation involves:
1. Add `DtEmbedding` module to transformer_model.py (learned embedding, concat to transformer input)
2. Modify imagination loop in agents.py to pass dt values
3. Add dt-subsampling to replay buffer

### 3a: STORM + trained dt_emb (seed 0)

```bash
export MUJOCO_EGL_DEVICE_ID=0
export CUDA_VISIBLE_DEVICES=0

cd /root/autodl-tmp/event-gated-adaptive-horizon/storm_dmc

nohup python -u train_dmc.py \
    -n storm_trained_dt_emb_s0 \
    -seed 0 \
    -config_path config/dmc_walker.yaml \
    --dt_embed_dim 32 \
    --dt_embed_mode trained \
    --subsample_max_dt 2 \
    --imag_horizon 8 \
    > ~/runs/event-gated-adaptive-horizon/storm_trained_dt_emb_s0.log 2>&1 &

echo "PID: $!"
```

### 3b: STORM + frozen dt_emb (control)

```bash
export MUJOCO_EGL_DEVICE_ID=0
export CUDA_VISIBLE_DEVICES=0

cd /root/autodl-tmp/event-gated-adaptive-horizon/storm_dmc

nohup python -u train_dmc.py \
    -n storm_frozen_dt_emb_s0 \
    -seed 0 \
    -config_path config/dmc_walker.yaml \
    --dt_embed_dim 32 \
    --dt_embed_mode frozen \
    --subsample_max_dt 2 \
    --imag_horizon 8 \
    > ~/runs/event-gated-adaptive-horizon/storm_frozen_dt_emb_s0.log 2>&1 &

echo "PID: $!"
```

**Note**: Phase 2 CLI flags (`--dt_embed_dim`, `--dt_embed_mode`, `--subsample_max_dt`) are placeholders. Exact flag names depend on Phase 2 implementation. Update after code is written.

---

## Dual-GPU Parallel Scheme

If the server has 2 GPUs (cuda:0 + cuda:1), run two experiments simultaneously.

### Key principle

Each experiment needs THREE matching settings:
1. `CUDA_VISIBLE_DEVICES=N` — which physical GPU the process sees
2. `--device cuda:0` — always cuda:0 within the process (CVD remaps it)
3. `MUJOCO_EGL_DEVICE_ID=N` — which GPU MuJoCo EGL renders on (must match physical GPU)

### Recommended parallel assignments

| GPU | Experiment | Estimated Time |
|-----|-----------|---------------|
| cuda:0 | DreamerV3 exp_walker_no_dt_emb_s0_r2 (P1) | ~2-4h remaining |
| cuda:1 | STORM baseline s0 (P2) | ~4-6h |

### Terminal 1 (GPU 0): DreamerV3

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl
export CUDA_VISIBLE_DEVICES=0
export MUJOCO_EGL_DEVICE_ID=0

cd /root/autodl-tmp/event-gated-adaptive-horizon

nohup python -u dreamer.py \
    --configs defaults dmc_proprio \
    --task dmc_walker_walk \
    --logdir logdir/exp_walker_no_dt_emb_s0_r2 \
    --steps 105000 \
    --seed 0 \
    --compile False \
    --device cuda:0 \
    --gate_enabled True \
    --gate_fixed_dt 2 \
    --gate_subsample_max_dt 2 \
    --imag_horizon 8 \
    --gate_dt_embed_dim 0 \
    > ~/runs/event-gated-adaptive-horizon/exp_walker_no_dt_emb_s0_r2.log 2>&1 &

echo "GPU0 PID: $!"
```

### Terminal 2 (GPU 1): STORM baseline

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl
export CUDA_VISIBLE_DEVICES=1
export MUJOCO_EGL_DEVICE_ID=1

cd /root/autodl-tmp/event-gated-adaptive-horizon/storm_dmc

nohup python -u train_dmc.py \
    -n storm_baseline_s0 \
    -seed 0 \
    -config_path config/dmc_walker.yaml \
    --no-wandb \
    > ~/runs/event-gated-adaptive-horizon/storm_baseline_s0.log 2>&1 &

echo "GPU1 PID: $!"
```

### Monitoring both

```bash
# Check both processes:
nvidia-smi

# Tail logs side by side:
tail -f ~/runs/event-gated-adaptive-horizon/exp_walker_no_dt_emb_s0_r2.log &
tail -f ~/runs/event-gated-adaptive-horizon/storm_baseline_s0.log
```

### After P1 finishes (GPU 0 freed)

Start STORM Phase 2 (P3) on GPU 0 while STORM baseline (P2) continues on GPU 1:

```bash
export CUDA_VISIBLE_DEVICES=0
export MUJOCO_EGL_DEVICE_ID=0
# ... P3 command from above ...
```

---

## Log Directory Structure

```
~/runs/event-gated-adaptive-horizon/
├── exp_walker_no_dt_emb_s0_r2.log     # P1: DreamerV3 no-emb control
├── storm_baseline_s0.log               # P2: STORM baseline
├── storm_trained_dt_emb_s0.log         # P3a: STORM + trained emb
└── storm_frozen_dt_emb_s0.log          # P3b: STORM + frozen emb
```

Create log directory if not exists:
```bash
mkdir -p ~/runs/event-gated-adaptive-horizon/
```

---

## Quick Reference: Registry Updates

After each experiment completes, update the registry:

```
exp_id: storm_baseline_s0
hypothesis: "STORM (transformer WM) achieves healthy Walker Walk baseline (eval ≥ 600), confirming DMC adaptation is viable for cross-architecture CIVO testing"
parent: null
spec.server: <server_name>
spec.command: <full command from above>
```
