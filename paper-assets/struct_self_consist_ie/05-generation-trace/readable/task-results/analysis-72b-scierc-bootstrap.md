# analysis 72b scierc bootstrap

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_72b_scierc_bootstrap_20260519T160000_result.json`
- **Structured JSON:** [`7af6bf7f3d64a26a125c.json`](../../sessions/7a/7af6bf7f3d64a26a125c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

### Paired Bootstrap Test: Greedy vs LP-weighted Construction (72B ZS SciERC)

| 指标 | 值 |
|------|-----|
| Greedy F1 | 0.3993 |
| Construction F1 | 0.4146 |
| Diff | **+1.53pp** |
| **p-value** | **0.0082** |
| 95% CI of diff | **[+0.0025, +0.0282]** |
| Cohen's d | 0.1027 (small effect) |

**结论：显著。** p=0.0082 < 0.05，且 95% CI 完全在零以上，不跨零。

### Instance 分布 (n=529)

| 类别 | 数量 | 占比 |
|------|------|------|
| Construction > Greedy | 119 | 22.5% |
| Construction < Greedy | 72 | 13.6% |
| Tied | 338 | 63.9% |

### 非退化子集 (n=491, 92.8%)

| 指标 | 值 |
|------|-----|
| Non-degen diff | +1.65pp |
| Non-degen 95% CI | [+0.0031, +0.0306] |
| Non-degen p-value | 0.0069 |
| Positive/Negative/Tied | 119/72/300 |

退化实例仅 38 个 (7.2%)，construction 与 greedy 完全一致（diff=0）。排除退化后增益反而更大（+1.65pp vs +1.53pp），p 值更小。

**注意**：实际 gold-filtered 实例数 529（非 551），差异来自 22 个 gold entities 为空的实例被过滤。

---
