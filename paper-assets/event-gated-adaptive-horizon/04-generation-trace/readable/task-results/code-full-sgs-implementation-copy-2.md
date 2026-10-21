# code full sgs implementation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full-sgs-implementation_20260515T230749_result.json`
- **Structured JSON:** [`d28c6f50409afe42a02d.json`](../../sessions/d2/d28c6f50409afe42a02d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成。下面是完整报告。

---

## 报告

### 1. dt_emb 在各 head 中的使用方式

| 模块 | dt_emb 参与方式 | SGS 策略 |
|------|----------------|----------|
| RSSM dynamics | dt_emb 融入 GRU deter state | **保留梯度**（唯一的 dt_emb 训练信号） |
| WorldModel heads (decoder/reward/cont) | 通过 feat=stoch+deter 间接包含 dt_emb | Hook 减去 head loss 梯度（line 346-358） |
| Actor | `_compute_actor_loss` 中 target 通过 imag_feat 连接 dt_emb | `requires_grad_(False)` 阻断（line 644） |
| Value | `value(value_input.detach())` — **已 detach** | 不需要额外处理（但 actor_opt backward 时 target 路径仍有连接） |

### 2. Full-SGS 实现方案和代码修改

**发现**: `full_sgs` flag 和核心逻辑已实现（configs.yaml line 121, models.py lines 346-358 + 642-644），但有一个 **关键 bug**。

**Bug**: `ImagBehavior._train()` line 644 设置 `dt_emb.weight.requires_grad_(False)` 后永不恢复。下个 iteration 的 `WorldModel._train()` 中 `torch.autograd.grad()` 返回 None → dynamics KL loss 也无法训练 dt_emb → **等同于 dt_emb_freeze**。

**修复** (1行代码): 在 `with RequiresGrad(self)` 块之后恢复 `requires_grad_(True)`:

```python
# models.py line 647-649 (新增)
if getattr(self._config, 'full_sgs', False) and self._world_model.dynamics._dt_embedding is not None:
    if not getattr(self._config, 'dt_emb_freeze', False):
        self._world_model.dynamics._dt_embedding.weight.requires_grad_(True)
```

### 3. Dry-run 结果

**成功** — 100 training updates，无报错。

关键 metrics:
- `model_loss=20.6`, `model_grad_norm=164.0` — 正常
- `actor_loss=-0.1`, `actor_grad_norm=0.0` — 正常（early training）
- `value_loss=9.2`, `value_grad_norm=17.8` — 正常
- `gate_dt_mean=2.0`, `gate_dt_2_frac=1.0` — 符合 `gate_fixed_dt=2`

### 4. 建议的提交命令

```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl nohup python -u dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/exp_018_full_sgs_walker_s1 \
  --steps 502000 --seed 1 --compile False --device cuda:1 \
  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \
  --imag_horizon 8 --full_sgs True \
  > /tmp/exp_018_full_sgs.log 2>&1 &
```

注意：需等 cuda:1 上 010a（Cheetah）完成后再提交，否则可能 OOM。或确认 010a 显存用量后判断能否并行。

---
