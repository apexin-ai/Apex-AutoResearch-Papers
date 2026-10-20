# ssh cls v4 progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cls-v4-progress-check_20260513T000413_result.json`
- **Structured JSON:** [`eca41744411a9b6a4cbf.json`](../../sessions/ec/eca41744411a9b6a4cbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CLS v4 训练状态汇总

| 项目 | 状态 |
|------|------|
| **进程** | PID 2885139 存活，运行时间 2h09m23s |
| **GPU** | 利用率 89%，显存 19465/32607 MiB (60%) |
| **训练进度** | **754 / 6633 步 (11.4%)**，epoch 0.34 |
| **Loss** | 0.6798 (step 750)，eval_loss 0.1317 (step 600) |
| **Learning Rate** | 1.97e-4 |
| **Grad Norm** | 2.27 |
| **速度** | ~6.9-7.0 s/it |
| **最新 Checkpoint** | checkpoint-600 (2026-05-12 16:46) |
| **磁盘** | 663G / 1.1T used (66%)，剩余 351G |

### 预计剩余时间

- 已完成 754 步，用时 ~2h06m
- 剩余 5879 步，按 ~7.0 s/step 估算：**约 11.4 小时**
- 预计完成时间：约 **今晚 ~03:30**（基于当前时间推算）

训练正常进行，loss 从 0.72 (step 700) 降到 0.68 (step 750)，eval_loss 0.132 表现良好。每 200 步保存 checkpoint，下一个 checkpoint-800 预计约 40 分钟后保存。

---
