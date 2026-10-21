# analysis docred dr consistency check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred-dr-consistency-check_20260523T015919_result.json`
- **Structured JSON:** [`1d58dd810d51eb3d9843.json`](../../sessions/1d/1d58dd810d51eb3d9843.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都完成。结果如下：

## 任务 1：70B LoRA DocRED 200 Unconstrained

| 指标 | 分子/分母 | 百分比 |
|------|-----------|--------|
| **DR** | 7/3159 | **0.22%** |
| **RV** | 18/3159 | **0.57%** |
| **ET** | 0/3381 | **0.00%** |
| **CF** | 2 (entities) | 0.06% |
| **E-F1** | 80.34 (P=85.13, R=76.05) | |
| **R-F1** | 43.80 (P=39.60, R=48.99) | |
| PF | 20/200 | 10.0% |
| max_samples | **200 行** | |

DR = 0.22% 与之前的报告一致（不是 0.88%）。差异可能来自不同的 violation_checker 版本或不同的 DR 计算基数（有的版本用 total_triples 含 RV-invalid 的三元组作分母，有的版本只在 RV-valid 子集上算 DR）。

## 任务 2：70B LoRA DocRED 200 Grammar-only

| 指标 | 分子/分母 | 百分比 |
|------|-----------|--------|
| **DR** | 12/3154 | **0.38%** |
| **RV** | 0/3154 | **0.00%** |
| **ET** | 0/3362 | **0.00%** |
| **CF** | 2 | 0.06% |
| **E-F1** | **80.13** (P=85.16, R=75.66) | |
| **R-F1** | 43.96 (P=39.78, R=49.11) | |
| PF | 21/200 | 10.5% |

E-F1=80.13 确认与之前 worker 报告一致。

---
