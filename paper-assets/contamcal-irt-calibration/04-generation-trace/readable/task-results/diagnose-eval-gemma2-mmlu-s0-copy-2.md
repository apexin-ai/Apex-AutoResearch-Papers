# diagnose eval gemma2 mmlu s0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gemma2_mmlu_s0_20260520T222500_result.json`
- **Structured JSON:** [`fc5201a6d192cbaf6816.json`](../../sessions/fc/fc5201a6d192cbaf6816.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**进程状态：运行中**
- PID 443479 在 GPU 1 上活跃，占用 24GB 显存，GPU 利用率 93%
- 当前正在评测 **d005_s0** MMLU，进度 81%（11395/14042），速度 ~17.7 it/s
- cron 的 "process gone" 报告是**误报**

**已完成的 dosage：**

| dosage | accuracy |
|--------|----------|
| d000_s0 | **64.88%** (9111/14042) |

**进行中：**
- d005_s0：81%，预计 ~2.5 分钟完成

**未完成：**
- d025_s0, d050_s0（d005_s0 完成后依次运行）

**GPU 状态：**

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 98% | 72.4/97.9 GB |
| 1 | 93% | 24.2/97.9 GB（MMLU eval） |
| 2 | **0% 空闲** | 0/97.9 GB |
| 3 | 83% | 64.8/97.9 GB |

不需要干预，eval 正常运行中。d005_s0 即将完成，之后会继续 d025_s0 和 d050_s0。

---
