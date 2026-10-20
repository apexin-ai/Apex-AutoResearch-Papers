# code plan015 critic dt emb detach

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan015-critic-dt-emb-detach_20260515T075725_result.json`
- **Structured JSON:** [`24dc36930570722c71b2.json`](../../sessions/24/24dc36930570722c71b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 代码修改总结

| 文件 | 行号 | 修改 |
|------|------|------|
| `configs.yaml` | 119 | 新增 `critic_dt_emb_detach: false` |
| `networks.py` | 241 | `img_step()` 新增 `detach_dt_emb=False` 参数 |
| `networks.py` | 256-257 | `if detach_dt_emb: dt_emb = dt_emb.detach()` |
| `models.py` | 609 | 读取 config: `detach_dt = getattr(config, 'critic_dt_emb_detach', False)` |
| `models.py` | 621 | 传递给 `img_step(state, action, dt=prev_dt, detach_dt_emb=detach_dt)` |

## Dry run 结果

200 步训练成功完成，无报错。`[200]` 输出确认训练循环正常执行了带 `detach_dt_emb=True` 的 imagination rollout。

## 待执行提交命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && \
export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && \
cd /root/autodl-tmp/event-gated-adaptive-horizon && \
nohup python -u dreamer.py --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/exp_015_critic_dt_detach \
  --steps 105000 --seed 1 --compile False --device cuda:1 \
  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \
  --imag_horizon 8 --critic_dt_emb_detach True \
  > logdir/exp_015_critic_dt_detach.log 2>&1 &
```

命令已保存到 artifact，等 009e 完成后提交到 cuda:1。

---
