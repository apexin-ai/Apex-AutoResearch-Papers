# monitor 6144 hang watch

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_6144-hang-watch_20260514T114807_result.json`
- **Structured JSON:** [`95c44383bfc39bd38b0e.json`](../../sessions/95/95c44383bfc39bd38b0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都有结果了。

## 结果汇报

### 任务 A: 进程监控 — 顺利通过危险区间

| 检查 | 时间 (UTC) | Sample Index | Acc | 状态 |
|------|-----------|-------------|-----|------|
| #1 | 04:48:34 | 960/9335 | 88.1% | 正常 |
| #2 | 04:49:26 | 1120/9335 | 88.1% | 进入危险区 |
| #3 | 04:50:24 | 1320/9335 | 87.0% | **已通过 1200** |

**结论：进程正常通过 1100-1200 危险区间，无 hang。** 速度稳定在 ~10-14s/40样本。

---

### 任务 B: Token 长度分析

**整体分布：**
| 统计 | 值 |
|------|-----|
| Total | 9335 |
| Mean | 1251.7 |
| Median | 397.0 |
| P90 | 4865 |
| P95 | 4957 |
| P99 | 5406 |
| Max | 8768 (sympy__sympy-14248) |
| Min | 196 |

**分桶统计：**
| 区间 | 数量 | 占比 |
|------|------|------|
| 0-512 | 5599 | 60.0% |
| 512-1024 | 898 | 9.6% |
| 1024-2048 | 955 | 10.2% |
| 2048-3072 | 477 | 5.1% |
| 3072-4096 | 0 | 0.0% |
| 4096-5120 | 1171 | 12.5% |
| 5120-6144 | 199 | 2.1% |
| **6144-8192** | **27** | **0.3%** |
| **8192-16384** | **9** | **0.1%** |

**>6144 token（被截断）：36 个样本 (0.4%)**，全部来自 `sympy__sympy-14248`。

**>4096 token：1406 个样本 (15.1%)**，其中绝大多数也是 `sympy__sympy-14248`。

**1100-1200 区间分析：**
- 最长：index=1179, 6220 tokens (`sympy__sympy-14248`)
- 区间内有多个 sympy-14248 样本 (4803-6220 tokens) 和短样本 (196-1279 tokens) 交替出现
- 6220 tokens 在 max_seq_length=6144 内会被截断，但不会导致 hang

**关键发现：** 分布呈双峰态——60% 的样本 <512 tokens，但有 15% 集中在 4096-5120 区间。3072-4096 区间是空的（0 个样本），说明长样本几乎都来自同一个 instance (`sympy__sympy-14248`) 的大 diff。

**Top 20 最长样本全部是 `sympy__sympy-14248`**，该 instance 的 code diff 特别大，贡献了所有超长样本。

---
