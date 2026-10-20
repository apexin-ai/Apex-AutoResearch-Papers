# diagnose v5 all status

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v5-all-status_20260514T014456_result.json`
- **Structured JSON:** [`e1fda63fc084572602e4.json`](../../sessions/e1/e1fda63fc084572602e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 个 v5 实验状态汇总

全部 4 个实验**仍在运行中**，无错误，进度稳定。

| 实验 | GPU | PID | 进度 | 最新日志时间 | 备注 |
|------|-----|-----|------|-------------|------|
| mvp_v5_fixed_s020 | cuda:0 | 46574 | **28/50** | 09:45:11 | 正常，无 NaN 警告 |
| mvp_v5_fixed_s030 | cuda:1 | 46940 | **29/50** | 09:45:34 | 正常，无 NaN 警告 |
| mvp_v5_fixed_s015 | cuda:2 | 48262 | **22/50** | 09:45:22 | 每个 problem 都有 layer 27 NaN 警告 |
| mvp_v5_fixed_s025 | cuda:3 | 48403 | **22/50** | 09:45:22 | 每个 problem 都有 layer 27 NaN 警告 |

**GPU 利用率**: 全部 4 卡活跃（77-93%），每卡占用 ~33.5GB / 97.9GB。

**关键观察**:
- s020 和 s030 早启动约 6 分钟，进度领先
- s015 和 s025 每个 problem 都出现 `Skipped 1 NaN attention layers: [27]` 警告（layer 27 在低/中 sparsity 下产生 NaN attention），但被正常跳过处理，不影响运行
- s020 和 s030 无此 NaN 问题
- 每个 problem 约 1-1.5 分钟，预计 s020/s030 约 20 分钟后完成，s015/s025 约 40 分钟后完成

**不更新 registry**，因为所有实验仍在正常运行中。

---
