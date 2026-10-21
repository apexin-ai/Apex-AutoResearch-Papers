# diagnose ssh failure recovery

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ssh_failure_recovery_20260517T093200_result.json`
- **Structured JSON:** [`9318e3f9237045720efb.json`](../../sessions/93/9318e3f9237045720efb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部存活，正常训练中。

## 汇报

| 实验 | PID | 状态 | 进度 | 运行时长 |
|------|-----|------|------|----------|
| rho02_adaptive_tau09_seed42 | 367604/367617 | **alive** | 2149/8477 (25%) | 10h33m |
| batch_adaptive_tau_rho06_seed42 | 372152 | **alive** | 7997/8477 (94%) | 9h45m |
| bs8_auto_nmin_seed42 | 370023 | **alive** | 4830/6103 (79%) | 10h05m |

## GPU 使用情况

| GPU | 利用率 | 显存使用 |
|-----|--------|----------|
| 0 | 99% | 46523 / 97887 MiB |
| 1 | 87% | 57165 / 97887 MiB |
| 2 | 86% | 57165 / 97887 MiB |
| 3 | 89% | 46019 / 97887 MiB |

`batch_adaptive_tau_rho06_seed42` 预计约 2.5 分钟内完成（剩余 480 步，3.27 it/s）。`bs8_auto_nmin_seed42` 预计约 55 分钟完成。`rho02_adaptive_tau09_seed42` 预计约 32 分钟完成。

---
