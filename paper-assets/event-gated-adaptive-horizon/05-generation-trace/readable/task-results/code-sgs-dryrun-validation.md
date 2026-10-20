# code sgs dryrun validation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sgs_dryrun_validation_20260515T143357_result.json`
- **Structured JSON:** [`87c8c4cc5aecea859f10.json`](../../sessions/87/87c8c4cc5aecea859f10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## 分析结果

### 1. configs.yaml 中 dt_emb 相关配置项

| 行号 | 配置项 | 默认值 |
|------|--------|--------|
| 119 | `dt_emb_freeze` | `false` |
| 120 | `reward_dt_emb_detach` | `false` |
| 94 | `gate_dt_embed_dim` | `32` |

两个 flag 默认都是 false，命令行传 `--reward_dt_emb_detach True` 会正确覆盖默认值。

### 2. dt_emb_freeze vs reward_dt_emb_detach 冲突分析

代码逻辑（models.py）：

- **dt_emb_freeze** (L96-98, L230-231): 将 `_dt_embedding.weight.requires_grad_(False)` — 彻底冻结权重，所有 loss（reward/decoder/dyn）对 dt_emb 的梯度都为零。
- **reward_dt_emb_detach** (L337-353): 在 optimizer step 前用 `register_hook` 从 dt_emb 梯度中**减去** reward loss 对 dt_emb 的梯度分量 — 选择性地只阻断 reward→dt_emb 通路，保留 decoder/dyn→dt_emb 梯度。

**冲突情况**：如果两者同时为 True：
- freeze 把 `requires_grad` 设为 False → `autograd.grad(reward_loss, dt_emb_weight)` 返回 None
- SGS 代码在 L339 检查了 `_dt_embedding is not None`，但如果 `requires_grad=False`，`autograd.grad` 会返回 None，hook 不注册 → **不会报错，但 SGS 变成空操作**（detach 无意义因为 freeze 已阻断所有梯度）

**结论**：两者同时开启不会 crash，但 SGS 被 freeze 架空。exp_016 只开 `reward_dt_emb_detach=True` 不开 `dt_emb_freeze`（与 008d 一致），**无冲突**。

### 3. SGS 实验能否直接启动

**可以。** 理由：
- `reward_dt_emb_detach` 已在 configs.yaml defaults 中定义（L120），argparse 能正确解析 `--reward_dt_emb_detach True`
- SGS 实现（L337-353）用 `getattr(config, 'reward_dt_emb_detach', False)` 安全获取，兼容旧配置
- SGS 诊断（L389-417）每 1000/5000 步记录 grad norm 和 weight norm，不影响训练
- `allow_unused=True` 保证即使 reward loss 不经过 dt_emb 也不报错
- 不需要额外改代码，直接在 008d 命令基础上加 `--reward_dt_emb_detach True` 即可运行

---
