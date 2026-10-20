# fix f2 per problem analysis

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_f2-per-problem-analysis_20260517T134034_result.json`
- **Structured JSON:** [`96d579e4114ed3cae47b.json`](../../sessions/96/96d579e4114ed3cae47b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。CSV 已保存到 `/root/symb_invariant_consensus/analysis/f2_per_problem.csv`，artifact 已注册。

## 统计摘要

| 指标 | 值 |
|------|-----|
| **Multi-candidate problems** | **307** (proofwriter: 235, folio: 72) |

### 相关性

| 关系 | Pearson r | p-value | Spearman ρ | p-value |
|------|-----------|---------|------------|---------|
| vote_entropy ↔ sica_flipped | 0.2491 | 1.0e-05 | **0.3574** | **1.1e-10** |
| constraint_count ↔ sica_correct | -0.0770 | 0.179 | -0.0884 | 0.122 |

vote_entropy 与 SICA 翻转之间有显著正相关（Spearman ρ=0.36, p<1e-10），答案分布越分散，SICA 越倾向于改变 SC 的结果。constraint_count 与 sica_correct 无显著相关。

### constraint_exclusion_rate 分布

| 统计量 | 值 |
|--------|-----|
| mean | 0.0536 |
| median | 0.0435 |
| std | 0.0400 |
| Q25 / Q75 | 0.0333 / 0.0625 |
| max | 0.5000 |
| 有排除的 problems | 305/307 (99.3%) |

### SICA Flip 分析

| 类型 | 数量 |
|------|------|
| 总 flips | 31 |
| 正确翻转 (SC wrong → SICA right) | **16** |
| 错误翻转 (SC right → SICA wrong) | **14** |
| 双方都错但答案不同 | 1 |
| **净收益** | **+2** |

Per-problem 粒度下 n=307，统计效力比 experiment-level 的 n=7 强得多。vote_entropy 是 F2 hero figure 最有力的 x 轴变量（ρ=0.36 高度显著）。

---
