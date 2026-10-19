# monitor all experiments status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_all-experiments-status_20260517T235839_result.json`
- **Structured JSON:** [`d7d6ba4af5f10ea20940.json`](../../sessions/d7/d7d6ba4af5f10ea20940.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 实验 | Step | train_success | val_success | action_valid | 状态 |
|------|------|--------------|-------------|--------------|------|
| **factorial_h2_episodeadv_seed1** (westd) | 4/15 | 20.3%→6.25% (step1→2) | 2.2% (OOD, step0) | 84-86% | **HEALTHY** |
| **hsweep_h2_seed2** (bjb1) | 11/15 | 0.8%→12.5%→3.9% (峰值step5) | 0% (step5,10) | 97% | **VAL失败** (train仍活但val=0) |
| **gsweep_g050_h5_seed1** (westd) | 10/15 | 0%→2.3%→0%→0%→0% (step4起全零) | 0% | 1.7% (step9) | **COLLAPSED** (entropy=0.03, invalid=98%) |

关键发现：
- **factorial** 表现最好，step1 达到 20.3% train success / pass@8=68.75%，是目前唯一健康的实验
- **hsweep_h2_seed2** 训练 action_valid 维持 97% 但 val 始终为 0，说明训练信号没有迁移到 val 分布
- **gsweep_g050_h5_seed1** 从 step 4 起完全崩溃，entropy 降至 0.03，已无恢复可能

bjb1 的 GPU 仍被 hsweep_h2_seed2 占用（11/15 还在跑）。

---
