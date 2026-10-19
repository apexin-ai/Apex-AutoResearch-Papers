# diagnose exp019b status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp019b-status-check_20260514T210052_result.json`
- **Structured JSON:** [`df9f45fcd1abad2b65d9.json`](../../sessions/df/df9f45fcd1abad2b65d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp019b_expert_sft_v3 状态报告

| 项目 | 状态 |
|------|------|
| **GPU 0** | 占用中 — 49567 MiB / 97887 MiB，利用率 100% |
| **GPU 1** | 空闲 — 0 MiB，利用率 0% |
| **训练进程** | 正在运行（PID 379346 的 nohup 进程） |
| **checkpoint** | 目录存在但为空，`final/` 不存在 |
| **训练进度** | **step 43/320**（13%），已耗时 ~6:24 |

**训练未完成，仍在跑。** 日志 `/tmp/exp019b.log` 显示最新进度为 step 43/320，速度 ~9s/step。

**预计剩余时间**：(320 - 43) × 9s ≈ 2493s ≈ **41 分钟**。

`exp019b_expert_sft_v3.log`（submit_training_job 的日志）确认是 PID 379905，因检测到 GPU 0 被占用直接退出（`[ERROR] GPU 0 has 49567MiB in use. Aborting.`），与预期一致。

---
