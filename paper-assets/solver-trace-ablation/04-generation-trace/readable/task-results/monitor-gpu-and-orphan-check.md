# monitor gpu and orphan check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu-and-orphan-check_20260516T035005_result.json`
- **Structured JSON:** [`8f55cb881ee7f0df8d2d.json`](../../sessions/8f/8f55cb881ee7f0df8d2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重要更正：这些**不是孤儿进程**。它们是今天 11:21 启动的**新 tmux session（r3 重试）**，带 W&B 日志（`--wandb_run sweep-isr-b005-s42-r3` / `sweep-isr-b01-s45-r3`）。

服务器时区 UTC+8，reward_log 时间戳是 UTC，所以 03:49 UTC = 11:49 本地时间，完全对得上。

---

## 报告

| 项目 | GPU 0 (cuda:0) | GPU 1 (cuda:1) |
|------|----------------|----------------|
| 实验 | sweep-isr-b01-s45 (β=0.1, s45) | sweep-isr-b005-s42 (β=0.05, s42) |
| 显存 | 79,547 / 97,887 MiB | 80,355 / 97,887 MiB |
| GPU 利用率 | **98%** (活跃训练) | **4%** (刚完成) |
| 状态 | **运行中** 177/500 步 | **已完成** 500/500 步 |

### b005-s42 (β=0.05, seed 42) — ✅ 完成
- **总步数**: 500/500
- **完成时间**: 11:49 本地 (运行约 28 min)
- **checkpoint-500**: 已保存 (~15GB, 11:49-11:50)
- **DONE sentinel**: 无
- **Last 50 步 avg**:
  - **prove_rate ≈ 0.995** (49/50 步 PR=1.0, 仅 step 461 PR=0.75)
  - **isr_mean ≈ 0.74** (大部分 0.75, 少量偏低)
  - **loss = 0.0** (训练已饱和)
- **特征**: 完全饱和，PR 锁定 1.0，ISR 稳定 ~0.75，loss=0

### b01-s45 (β=0.1, seed 45) — 🔄 运行中
- **当前步数**: 177/500
- **每步耗时**: ~9.8s (比 b005 慢，β=0.1 生成更长)
- **预计完成**: ~53 min 后 (~12:43 本地)
- **训练状态**: 非常不稳定
  - prove_rate 在 0.0-0.875 剧烈波动
  - 大量步骤 PR=0.0, ISR=0.0
  - 偶尔爆发到 PR=0.75-0.875
- **趋势**: 无清晰收敛迹象，可能是 struggling run

### 其他进程
- 无其他 train_grpo.py 进程
- 两个 GPU 均被上述 r3 run 占用，无残留/泄漏进程

---
