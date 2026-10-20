# analysis exp033 per problem data

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp033-per-problem-data_20260518T223148_result.json`
- **Structured JSON:** [`442e6c70d5efefb2b5bf.json`](../../sessions/44/442e6c70d5efefb2b5bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据提取完成。

### 产出

**文件路径**: `/root/symb_invariant_consensus/results/exp033_per_problem_analysis.json`（204 problems，含所有请求字段）

### 统计摘要

| 指标 | 值 |
|------|-----|
| SC accuracy | 0.5441 |
| SICA accuracy | 0.5931 |
| Overrides (SICA != SC) | 17 / 204 (8.3%) |
| Override precision | 12/17 = **70.59%** |
| Override correct / wrong | 12 / 5 |

**Entropy 分布**

| 分位 | 值 |
|------|-----|
| Q25 | 0.4395 |
| Q50 (median) | 0.8454 |
| Q75 | 1.1887 |
| Range | [0.0, 2.4464] |

**SC / SICA accuracy by entropy bin**

| Entropy Bin | n | SC Acc | SICA Acc | Overrides | Override Prec |
|-------------|---|--------|----------|-----------|---------------|
| Low (H<0.5) | 65 | 0.7692 | 0.7692 | 0 | N/A |
| Medium (0.5≤H<1.2) | 89 | 0.4944 | 0.5506 | 6 | 0.8333 |
| High (H≥1.2) | 50 | 0.3400 | 0.4400 | 11 | 0.6364 |

关键发现：SICA 的增益集中在 medium 和 high entropy 区间。Low entropy 下 SC 和 SICA 完全一致（zero overrides）。High entropy 区间 SICA 将 SC 的 34% 提升到 44%（+10pp），override precision 63.6%。

---
