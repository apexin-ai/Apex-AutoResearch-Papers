# monitor v9d progress check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v9d_progress_check_20260520T061739_result.json`
- **Structured JSON:** [`c3ee9554322a6c345057.json`](../../sessions/c3/c3ee9554322a6c345057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v9d 训练状态报告

### 进度
- **当前 step: 7/30** (23%)，运行 48 分钟
- 进程 549487 正常运行，状态 `RNl`
- 每 step 约 20-23 分钟，预计剩余 ~8 小时

### 关键指标（log 数据）

| 指标 | Step 6 | Step 7 | 趋势 |
|------|--------|--------|------|
| train/success | 85.2% | **91.4%** | ↑ |
| pass@8 | 100% | 100% | 稳定 |
| pg_loss | 0.00097 | 0.00096 | 稳定 |
| entropy | 0.0597 | 0.0473 | ↓ (收敛中) |
| ppo_kl | -0.028 | -0.034 | 正常 |
| grad_norm | 0.497 | 0.573 | 正常 |

训练 success rate 从 step 6 的 85.2% 提升到 step 7 的 **91.4%**，趋势良好。

### GPU
- 4 卡均在工作：利用率 75%/61%/82%/100%
- 显存：每卡 ~24GB / 98GB（~24%）

### 磁盘
- `/root/autodl-tmp`: 159G / 250G（64%），剩余 92G
- **checkpoint `global_step_5` 占 92GB**，远超预期的 ~33GB（保存了 model + optimizer + extra）。按 save_freq=5，step 10 会写下一个 checkpoint，`max_actor_ckpt_to_keep=2`，但当前只有 1 个 ckpt 也已占 92GB。两个 ckpt 将占 184GB，剩余空间仅 92G — 刚好够，但比较紧张。

### 异常
- 无 NaN / OOM / loss spike
- 大量 `Skipping non-numeric metric 'anchor_obs'` 警告，不影响训练，可忽略
- **磁盘风险**: 如果 step 10 保存新 checkpoint 前旧的还没删除，可能瞬时需要 184GB 空间。建议关注。

---
