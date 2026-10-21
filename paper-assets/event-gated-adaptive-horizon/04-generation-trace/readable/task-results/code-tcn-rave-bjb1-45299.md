# code tcn rave bjb1 45299

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tcn_rave_bjb1_45299_20260520T033809_result.json`
- **Structured JSON:** [`4d762422d28611d0ea8a.json`](../../sessions/4d/4d762422d28611d0ea8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务已完成。总结：

**代码实现** — TCN 和 RAVE 已在之前的 session 中实现完毕：
- **TCN**: `networks.py:257-258` — img_step 中 `tcn_sigma > 0` 时给 dt_emb 加高斯噪声
- **RAVE**: `models.py:746-753` — _compute_target 中 EMA anchor + ceiling clamp
- **Config**: `configs.yaml` 已有 `tcn_sigma: 0.0`, `rave_ceiling: 0.0`

**实验状态** — 两个实验已在 bjb1-45299 活跃运行中（今天 10:54 提交）：

| 实验 | GPU | 当前步数 | 关键参数 | train_return |
|------|-----|---------|---------|-------------|
| exp_027_tcn_walker_s0 | cuda:0 | 32k/105k | tcn_sigma=0.5 | ~200 |
| exp_028_rave_walker_s0 | cuda:1 | 32k/105k | rave_ceiling=2.0 | ~175 |

CIVO-inducing 基础配置：`gate_enabled=True, gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8`

**注意**：steps 是 105000 而非任务要求的 210000。另外还有两个灵敏度变体（σ=0.2 和 ceiling=1.5）在 bjb1-40020 上运行。

**Registry** — 已更新两个实验从 PREPARING → RUNNING，补全了 spec 字段。

---
