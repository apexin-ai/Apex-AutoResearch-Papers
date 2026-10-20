# ManiSkill3 → DreamerV3 Integration Report

## Changes Made

### 1. `dreamer.py` — `make_env` function (line 198)
Added `maniskill` suite branch before the `else: raise NotImplementedError` fallback:

```python
elif suite == "maniskill":
    import envs.maniskill as maniskill
    env = maniskill.ManiSkill(
        task, config.action_repeat, config.size,
        obs_mode="state", max_episode_steps=config.time_limit,
        seed=config.seed + id,
    )
    env = wrappers.NormalizeActions(env)
```

Task parsing: `config.task.split("_", 1)` correctly maps `maniskill_PickCube-v1` → suite=`maniskill`, task=`PickCube-v1`.

### 2. `configs.yaml` — `maniskill_state` preset (line 205)
Added as top-level section between `memorymaze` and `debug`:

```yaml
maniskill_state:
  task: maniskill_PickCube-v1
  steps: 5e5
  action_repeat: 1
  envs: 1
  train_ratio: 512
  time_limit: 200
  video_pred_log: false
  encoder: {mlp_keys: '.*', cnn_keys: '$^'}
  decoder: {mlp_keys: '.*', cnn_keys: '$^'}
```

## Verification Results

### Config parsing
- `maniskill_state` correctly appears as top-level key
- All fields parse correctly (steps=500000, action_repeat=1, etc.)
- `defaults` section integrity preserved

### Environment creation (full make_env pipeline)
```
observation_space: Dict(state:Box(-inf, inf, (42,), float32))
action_space: Box(-1.0, 1.0, (8,), float32)
obs keys: ['state', 'is_first', 'is_terminal']
  state: shape=(42,), dtype=float32
step OK, reward: 0.0556, done: False
Full make_env integration test passed!
```

Wrappers applied in order: `ManiSkill → NormalizeActions → TimeLimit → SelectAction → UUID` — all compatible.

## Usage

```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl \
  python dreamer.py --configs maniskill_state --logdir ./logdir/maniskill_pickcube
```

Note: Do NOT set `CUDA_VISIBLE_DEVICES` — SAPIEN/ManiSkill3 segfaults with GPU isolation.
