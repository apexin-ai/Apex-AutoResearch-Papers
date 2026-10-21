# submit sweep isr b02 batch

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_sweep-isr-b02-batch_20260516T034827_result.json`
- **Structured JSON:** [`fef1fb13287f0ad4fdc5.json`](../../sessions/fe/fef1fb13287f0ad4fdc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**停止提交。任务前提"两块 GPU 空闲"与实际不符。**

## 现场探测结果

**GPU 占用情况**：
- **cuda:0** (pid 604569, 79.5GB, 90% util, 已运行 34:24)：`sweep-isr-b01-s45-r3` — β=0.1 seed=45 retry 3
- **cuda:1** (pid 626802, 78.9GB, 92% util, 已运行 01:36)：`sweep-isr-b02-s42` — β=0.2 seed=42 (**已是本任务的目标实验之一**)

**Registry 状态**：
- `sweep-isr-b02-s42` 已注册为 RUNNING（2026-05-16T02:42:03Z），spec 中 pid=626802、gpu=cuda:1，与 nvidia-smi 一致 ✓
- 没有 `sweep-isr-b02-s43` 记录

**配置探测**：
- `configs/grpo_additive_bonus_b02.yaml` **已存在**（不需要创建）：beta=0.2, seed=42, num_steps=500, per_device_batch_size=4, gradient_accumulation_steps=2, num_generations=4
- ⚠️ config 的 `per_device_batch_size=4, gradient_accumulation_steps=2, num_generations=4` 与任务上下文中"K=4, per_device_batch_size=2"不一致——但 s42 已用该 config 启动

**D098 fix 验证**：scripts/train_grpo.py 第 356-384 行所有 argparse default 均为 `None` ✓ 已生效

**Seed 处理**：seed 在 config 中（`seed: 42`），但 CLI `--seed` 在 D098 fix 后会通过 None 检查正常覆盖 config 值。已运行的 s42 命令使用 `--seed 42` 显式覆盖。

## 决策

**不执行任何提交。** 原因：
1. **s42 已在 cuda:1 跑**——重复提交会冲突并违反 C002/C007
2. **cuda:0 被 s45-r3 占满 79.5GB**——s43 提交必 OOM
3. 没有任何可用 GPU 容纳 s43

## 建议下一步

- 等待 cuda:0 上 `sweep-isr-b01-s45-r3` 完成（500 steps, 34:24/?, 用 check-training-status 查 ETA）
- s45 完成且 GPU 释放（按 C007 必须 nvidia-smi 确认）后，再提交 `sweep-isr-b02-s43` 到 cuda:0
- s42 已在跑，命令使用了 `--no_wandb`（"missing WANDB_API_KEY on server"），s43 提交时是否需要相同处理待确认
- 若用户确认必须立即提交 s43，需先告知是否 kill s45-r3

---
