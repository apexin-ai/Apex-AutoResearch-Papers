# monitor c2 n500 deepseek

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_c2_n500_deepseek_20260514T192537_result.json`
- **Structured JSON:** [`158e1f76d32709305203.json`](../../sessions/15/158e1f76d32709305203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据足够，汇总报告。

---

## c2_n500_deepseek 进度报告（2026-05-15 03:26 UTC）

### Condition 状态

| Condition | GPU | 进度 | 状态 |
|-----------|-----|------|------|
| imp_s015 | 0 | 500/500 | **完成** (02:31 UTC) |
| rand_s015 | 1 | 500/500 | **完成** (02:05 UTC) |
| **imp_s020** | **0** | **110/500 (22%)** | **进行中** PID 156554 |
| **rand_s020** | **1** | **157/500 (31%)** | **进行中** PID 154305 |
| imp_s025 | 0 | 0/500 | 待跑 |
| rand_s025 | 1 | 0/500 | 待跑 |
| imp_s030 | 0 | 0/500 | 待跑 |
| rand_s030 | 1 | 0/500 | 待跑 |

**总体进度：1267/4000 = 31.7%**

### 速率

基于 s015 完整 run 和当前 s020 日志推算：

| 通道 | 速率 | 每 condition 耗时 |
|------|------|--------------------|
| GPU0 (importance) | ~35s/sample | ~4h50min |
| GPU1 (random) | ~32s/sample | ~4h25min |

### ETA 时间线 (UTC, May 15)

| Condition | 开始 | 预计完成 |
|-----------|------|----------|
| imp_s015 | 21:41 (May 14) | **02:31 ✓** |
| rand_s015 | 21:41 (May 14) | **02:05 ✓** |
| imp_s020 | 02:31 | **~07:15** |
| rand_s020 | 02:05 | **~06:30** |
| imp_s025 | ~07:15 | **~12:05** |
| rand_s025 | ~06:30 | **~10:55** |
| imp_s030 | ~12:05 | **~16:55** |
| rand_s030 | ~10:55 | **~15:20** |

**全量完成 ETA：~16:55 UTC May 15（约13.5小时后）**

### GPU 利用率

| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 77% | 23.7/97.9 GB | ds_imp_s020 |
| 1 | 96% | 24.2/97.9 GB | ds_rand_s020 |
| 2 | 78% | 25.1/97.9 GB | qw_imp_s020 (另一任务) |
| 3 | 77% | 25.7/97.9 GB | qw_rand_s020 (另一任务) |

### 异常信号

- **无异常**。两个进程稳定运行，GPU 利用率正常。
- 原始 PID (130124, 130263) 已被新进程取代（脚本串行执行，s015 完成后自动启动 s020），这是正常行为。
- GPU 2/3 上还同时跑着 Qwen 的 n500 s020 任务（c5b 或另一批次）。

---
