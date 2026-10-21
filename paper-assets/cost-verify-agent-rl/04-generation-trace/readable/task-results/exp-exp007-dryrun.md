# exp exp007 dryrun

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp007_dryrun_20260514T001832_result.json`
- **Structured JSON:** [`774c7d4389037dde5734.json`](../../sessions/77/774c7d4389037dde5734.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp007 Dryrun 结果报告

### 状态：训练步完成，checkpoint 保存失败

训练 step 1 的 rollout + policy update 正常完成，但保存 optimizer checkpoint 时 rank 1 写入失败（根分区 30GB 已用 27GB = 90%）。

---

### 三个关键指标

| 指标 | 数值 | 判定 |
|------|------|------|
| **invalid_action rate (manager)** | **6.5%** | 远优于预期（<20% 理想目标），解析器 fallback 有效 |
| **pg_loss** | **未捕获** — `compute_policy_loss` 已执行，但 console logger 未输出数值（crash 在 checkpoint save 阶段打断了 step summary 打印） |
| **步耗时** | **~12 min**（rollout + policy update，不含 validation） | 远优于 exp003 的 95 min/step |

### Initial Validation 详细指标（step 0, 训练前基线）

- `action_is_valid` = **5.4%** — 仅 5.4% 的 action 命中了 admissible actions list（语义层面）
- `manager_invalid_action` = **6.5%** — 解析器格式失败率（仅 6.5% 无法解析）
- `action_is_effective` = **93.5%** — action 对环境有效果
- `success` = **0.0**, `pass@1` = **0.0** — 无任务完成
- `num_actions` = **28.06** — 平均每 episode 28 步
- `response_length` = **2099.9** tokens — 模型输出较长
- Validation 用时: 335.9s (initial), 278.9s (post-step)

### 时间线

- 08:19 — 启动，Ray/vLLM 初始化
- ~08:25 — 初始 validation 完成（335.9s）
- ~08:25–08:37 — Step 1 rollout + policy update（~12 min）
- 08:37–08:42 — Post-step validation（278.9s）
- 08:42:25 — Model checkpoint 保存成功
- 08:42:43 — Optimizer checkpoint rank 0 成功，rank 1 失败（磁盘 I/O error）

### 问题

1. **根分区磁盘不足（90%）**：checkpoint 保存到了 `/root/cost-verify-agent-rl/RAGEN/checkpoints/` 即根分区，不是数据盘。正式训练需要把 checkpoint 路径改到 `/root/autodl-tmp/`。
2. **action_is_valid 极低（5.4%）**：解析器修复解决了格式问题（manager_invalid 仅 6.5%），但模型生成的 action 几乎都不在 admissible actions list 中。这是模型能力问题，不是解析器问题。

---
