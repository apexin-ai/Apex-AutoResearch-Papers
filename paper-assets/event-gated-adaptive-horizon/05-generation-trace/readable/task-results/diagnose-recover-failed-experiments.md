# diagnose recover failed experiments

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_recover_failed_experiments_20260518T021421_result.json`
- **Structured JSON:** [`01ce0c05dd5ea4c76c1d.json`](../../sessions/01/01ce0c05dd5ea4c76c1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：两个实验均存活，正在正常训练

| 实验 | PID | 设备 | 当前 Step | 目标 Step | 最新 logdir 写入 | train_return |
|------|-----|------|-----------|-----------|-----------------|--------------|
| **exp_008d_civo_trigger_s4** (walker_walk) | 715124 | cuda:0 | 12000 | 105000 | 10:14 (1分钟前) | ~117.9 |
| **exp_010b_cheetah_civo_trigger_s0** (cheetah_run) | 715412 | cuda:1 | 12000 | 105000 | 10:15 (刚刚) | ~11.8 |

**状态**: 两个进程都在活跃运行（CPU 占用 ~1100%，logdir 文件在持续写入）。它们于 10:02 启动，当前运行约 13 分钟，已完成 ~11.4% 的训练。

**需要操作**: 重新注册 cron 监控，避免再次被误标为 failed。

---
