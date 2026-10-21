# ops collect new eval results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-new-eval-results_20260514T122015_result.json`
- **Structured JSON:** [`86f96856ccb52680a9d1.json`](../../sessions/86/86f96856ccb52680a9d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

## Eval 结果汇总（13/19 完成）

### Qwen2.5-0.5B

| 配置 | MMLU | GSM8K | ARC-C | HumanEval | 备注 |
|------|------|-------|-------|-----------|------|
| d000_s42 | 40.49 | 36.47 | 37.80 | — | baseline |
| d000_s123 | 41.82 | 34.04 | 39.76 | — | seed variant |
| d005_s42 | 29.29 | 36.01 | 28.58 | — | 5% contam |
| d100_s42 | 23.22 | 35.71 | 22.70 | — | 100% contam |
| **d000_s42_aligned** | 39.79 | 36.92 | **46.93** | 10.98 | **NEW** |
| **d000_s42_para_aligned** | 44.28* | 28.07 | **47.92** | 11.54 | **NEW**, para=true |

*para_aligned MMLU 在 6596 项（paraphrased 子集）上评估，其余在 14042 项上

### Qwen2.5-1.5B

| 配置 | MMLU | GSM8K | ARC-C | HumanEval | 备注 |
|------|------|-------|-------|-----------|------|
| d000_s42 | 57.53 | 63.68 | 77.56 | — | baseline |
| d000_s123 | 57.62 | 63.31 | 76.62 | — | seed variant |
| d100_s42 | 59.33 | 64.97 | 76.88 | — | 100% contam |
| **d000_s42_aligned** | **58.53** | **65.43** | **77.22** | 12.80 | **NEW** |

### Qwen2.5-3B

| 配置 | MMLU | GSM8K | ARC-C | 备注 |
|------|------|-------|-------|------|
| d000_s42 | 63.37 | 11.68 | 82.17 | baseline |
| d000_s123 | 63.62 | 17.59 | 82.94 | seed variant |
| raw | — | 60.50 | — | gsm8k only |

### 未完成（6 个空目录）

| 目录 | 状态 |
|------|------|
| 0.5B_d000_s42_para | 空，创建于 08:36 |
| 0.5B_d005_s42_aligned | 空，创建于 19:15 |
| 0.5B_raw | 空，创建于 14:52 |
| **1.5B_d000_s42_para_aligned** | **GPU 1 正在跑** (PID 362352)，创建于 20:03 |
| 3B_d000_s42_aligned | 空，创建于 17:52 |
| 3B_d100_s42_aligned | 空，创建于 20:06 |

### correctness_matrix.json
所有 13 个已完成的 eval 目录都有对应的 correctness_matrix.json，可供 ConStat 分析。

### 关键观察
- **aligned 格式显著提升 ARC-C**：0.5B aligned 从 37.80→46.93 (+9.13pp)，para_aligned 47.92
- **1.5B aligned 各指标微升**：MMLU +1.0pp, GSM8K +1.75pp, ARC-C 基本持平
- **3B GSM8K 异常低**（11.68/17.59 vs raw 60.50），可能是 eval 格式/prompt 问题，非真实能力

---
