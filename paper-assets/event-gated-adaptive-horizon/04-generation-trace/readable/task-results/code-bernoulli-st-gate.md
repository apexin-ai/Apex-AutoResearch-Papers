# code bernoulli st gate

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bernoulli_st_gate_20260513T224003_result.json`
- **Structured JSON:** [`0c65a97953cbed25e62b.json`](../../sessions/0c/0c65a97953cbed25e62b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Implementation complete. Here's the summary:

## 实现方案

### 改动文件

1. **networks.py** — 新增 `BernoulliSTGate` 类（~60行）
   - MLP → single logit → sigmoid → hard threshold with straight-through gradient
   - `forward()` 返回 `(p_skip, dt, logit)`，API 与 EventGate 兼容
   - `entropy()` 计算 binary entropy

2. **models.py** — 6处改动
   - RSSM `max_dt=2` when bernoulli_st
   - Gate 构造分支：gate_type → BernoulliSTGate / EventGate
   - `_update_gate_schedule` 限制 effective_max_dt ≤ 2
   - subsample max_dt=2 for bernoulli_st
   - Gate loss：bernoulli_st 用 BCE + state-delta binary supervision，gumbel 保持 categorical CE
   - Gate metrics：bincount/fraction 用 effective max_dt=2

3. **configs.yaml** — 新增 `gate_type: "gumbel"` 参数

### Dry-run 结果

```
Optimizer model_opt has 16946265 variables.
gate_dt_mean 1.0 / gate_dt_std 0.0 / gate_dt_min 1.0 / gate_dt_max 1.0
gate_dt_1_frac 1.0 / gate_dt_2_frac 0.0
gate_loss 0.0 / gate_scale 0.0 / gate_entropy_bonus 0.1
gate_empirical_entropy 0.0 / gate_entropy_ratio 0.0
model_loss 42.9 / model_grad_norm 90.2
```

- 模型初始化成功，无报错
- gate_dt_mean=1.0（符合预期：step=1000 < 25000，gate 处于 phase 1，scale=0.0，全部 dt=1）
- gate_dt_2_frac=0.0（gate 未激活时不会 skip）
- 所有 metrics 正常输出

### git commit

```
2ffb24e feat: add Bernoulli straight-through gate (--gate_type bernoulli_st)
```

### 设计决策

- **`_imagine` 无需改动**：BernoulliSTGate 与 EventGate API 兼容（`_, next_dt, _ = gate(...)`），imagination 循环天然支持
- **Gate supervision**：bernoulli_st 在 WorldModel._train 中用 BCE + state-delta binary target（大 delta → don't skip, 小 delta → skip），与 Gumbel 的 categorical CE 对称
- **Curriculum**：复用现有 gate_scale schedule（phase 1 不训练 gate，phase 2 逐步引入），对 bernoulli_st 同样适用
- **Entropy bonus**：复用 `gate_entropy_bonus_init/final` 退火机制，BernoulliSTGate.entropy 计算 binary entropy

### 使用方式

```bash
python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk \
    --gate_enabled True --gate_type bernoulli_st
```

---
