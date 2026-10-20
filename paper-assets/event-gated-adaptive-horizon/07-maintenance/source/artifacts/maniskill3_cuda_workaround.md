# ManiSkill3 CUDA_VISIBLE_DEVICES Workaround

## Problem

SAPIEN (ManiSkill3 physics engine) segfaults during `gymnasium.make()` when `CUDA_VISIBLE_DEVICES` maps to a non-existent GPU index. This blocks `submit_training_job`, which uses `CUDA_VISIBLE_DEVICES` for GPU isolation.

Root cause: SAPIEN's C++ code unconditionally probes CUDA devices during env creation (even with `sim_backend='cpu'` + `render_backend='cpu'`). When the remapped GPU index doesn't exist, the probe triggers a segfault (exit code 139).

## Solution

Modified `envs/maniskill.py` with two changes:

### 1. Remove CUDA_VISIBLE_DEVICES before env creation

```python
cvd = os.environ.pop("CUDA_VISIBLE_DEVICES", None)
if cvd is not None:
    _cvd_stash = cvd
```

In `ManiSkill.__init__`, before `gymnasium.make()`. SAPIEN then sees all physical GPUs and skips the problematic remapped-index probe. The original value is saved in `_cvd_stash` for device translation.

**CUDA_VISIBLE_DEVICES is NOT restored** after env creation because SAPIEN's CUDA initialization expands GPU visibility for the entire process. Restoring the env var would be misleading (CUDA runtime ignores it post-init).

### 2. CPU render backend for state-based envs

```python
if not self._use_image:
    make_kwargs["render_backend"] = "cpu"
```

State-based obs (`obs_mode="state"`) doesn't need GPU rendering. Explicitly setting `render_backend="cpu"` prevents SAPIEN from allocating a CUDA render device.

### 3. Device translation helper

```python
from envs.maniskill import maniskill_target_device
device = maniskill_target_device()  # e.g. "cuda:2" if CVD was "2"
```

Since CVD is removed, PyTorch sees all physical GPUs. Training code must use the physical GPU index (from `maniskill_target_device()`) instead of assuming `cuda:0`.

## GPU Memory Impact

State-based ManiSkill allocates ~118 MiB on GPU 0 (SAPIEN's internal `fork_rng` CUDA context overhead). This is:
- 0.12% of 98 GB total VRAM
- Constant (doesn't grow with steps)
- Only on GPU 0 (other GPUs unaffected)
- Not freed by `env.close()` (CUDA context lifetime)

## Correct Launch Pattern

```bash
# submit_training_job sets CUDA_VISIBLE_DEVICES=N
# The wrapper removes it internally. Training script should use
# physical device index via --device flag:

# Option A: Let the training framework handle device
python train.py --task PickCube-v1 --device cuda:2

# Option B: Use maniskill_target_device() in code
from envs.maniskill import maniskill_target_device
device = maniskill_target_device() or "cuda:0"
model = model.to(device)
```

## Verification

Tested on bjb1-45299 (2x RTX PRO 6000 Blackwell, ManiSkill3 v3.0.1):

| Test | Result |
|------|--------|
| `CUDA_VISIBLE_DEVICES=2` (non-existent GPU) | Pass (was segfault) |
| `CUDA_VISIBLE_DEVICES=0` (existing GPU) | Pass |
| No CVD set | Pass |
| 50-step rollout | Pass, stable memory |
| Episode boundary (done + reset) | Pass |
| `maniskill_target_device()` returns correct device | Pass |
| GPU memory isolation (GPU 1 unaffected) | Pass |

## Approaches Evaluated

| Approach | Result |
|----------|--------|
| `render_backend='cpu'` only | Segfault - SAPIEN probes CUDA regardless |
| `sim_backend='cpu'` + `render_backend='cpu'` | Segfault - same reason |
| Remove CVD at import time | Works but too early (might not be needed) |
| Remove CVD in `__init__` + `render_backend='cpu'` | **Adopted** - minimal scope, reliable |
| Init torch first, then remove CVD | SAPIEN overrides torch's CUDA context |
