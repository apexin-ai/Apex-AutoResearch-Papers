# ops check westd41074 full

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_westd41074_full_20260522T035325_result.json`
- **Structured JSON:** [`e531b2c8247574dee6c7.json`](../../sessions/e5/e531b2c8247574dee6c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41074 全 GPU 审计快照 (2026-05-22 ~11:54)

| GPU | 利用率 | 显存 | PID | 实验 | 进度 | 当前状态 |
|-----|--------|------|-----|------|------|----------|
| **0** | 38% | 10.6/98 GB | 13535 | Random k=0.95 Spatial v4 | T4/10 (ep30, 57%) | 累计 SR 85.5%: T0=98%, T1=90%, T2=92%, T3=62%, T4 进行中 |
| **1** | 70% | 21.2/98 GB | 922934 | Random k=0.85 Object s43 v3 | T7/10 (ep40, 5%) | 累计 SR 3.1%（Object suite 极差） |
| **1** | — | — | 942398 | Random k=0.925 Spatial | T6/10 (ep10, 80%) | 累计 SR 56.7%: T0-T5 完成 |
| **2** | 0% | 28.5/98 GB | 68539 | **VTC M96 train** | step 84800/100000 (**84.8%**) | loss~2.5, 0.5 sps, 正常 |
| **3** | 0% | 27.5/98 GB | 59671 | **VTC M64v6 train** | step 38250/100000 (**38.3%**) | loss~2.7, 0.6 sps, 正常 |

### 关键结论

- **VTC M96 (PID 68539)**: 存活，稳步推进。剩余 15200 步 × 100s/50步 ≈ **8.4h 完成**（约今晚 20:00）。
- **VTC M64v6 (PID 59671)**: 存活，剩余 61750 步 ≈ **28.5h**（约明天 16:00）。
- **GPU 0/1 利用率低**：eval 任务间歇式推理，属正常。
- **Random k=0.85 Object**: SR 极低（3.1%），基本可判定为失败配置。
- **Random k=0.925 Spatial**: 中等表现（56.7%），T4 拉低了均值。
- **Random k=0.95 Spatial v4**: 表现强劲（85.5%），有望接近 full-FT baseline。

---
