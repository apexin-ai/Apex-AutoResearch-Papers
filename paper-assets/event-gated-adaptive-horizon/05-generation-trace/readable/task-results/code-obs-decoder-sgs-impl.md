# code obs decoder sgs impl

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_obs-decoder-sgs-impl_20260519T162313_result.json`
- **Structured JSON:** [`da748a811a68075b9f6a.json`](../../sessions/da/da748a811a68075b9f6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 代码改动

**configs.yaml** — 新增一行：
```yaml
sgs_mode: "none"    # 新增，可选值: "none", "obs_decoder_only"
```

**models.py** (WorldModel._train, SGS block) — 在 `full_sgs` 分支前新增 `obs_decoder_only` 分支（+16行）：
- 检测 `sgs_mode == 'obs_decoder_only'`
- 计算所有非 reward/cont 的 loss（即 obs decoder 的 height/orientations/velocity 等）对 dt_emb.weight 的梯度
- 注册 hook 在反向传播时减去该梯度
- 效果：reward 和 KL dynamics 的梯度正常回传到 dt_embedding，仅 obs decoder 的梯度被阻断

现有 `full_sgs` 和 `reward_dt_emb_detach` 分支降级为 `elif`，功能不变。

### 2. 新增配置参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--sgs_mode` | str | `"none"` | `"none"` = 无 SGS；`"obs_decoder_only"` = 只阻断 obs decoder 梯度到 dt_emb |

优先级：`sgs_mode` > `full_sgs` > `reward_dt_emb_detach`

### 3. Dry run 结果

**成功**。训练 5000+ logged steps，关键指标正常：
- `model_loss=20.9`, `height_loss=0.1`, `orientations_loss=2.6`, `velocity_loss=9.9`
- `reward_loss=3.3`, `kl=8.4`, `value_loss=9.4`
- `gate_dt_mean=2.0` (fixed dt=2 正确)
- 无 NaN / Inf / RuntimeError

### 4. 完整实验命令模板（105K steps = 210K env steps）

```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --steps 210000 \
  --seed &lt;SEED> \
  --device cuda:0 \
  --compile False \
  --gate_enabled True \
  --gate_fixed_dt 2 \
  --imag_horizon 8 \
  --sgs_mode obs_decoder_only \
  --logdir logdir/exp_019_obs_sgs_walker_s&lt;SEED>' \
> /tmp/exp_019_obs_sgs.log 2>&1 &
```

---
