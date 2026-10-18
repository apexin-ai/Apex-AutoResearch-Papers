# analysis per error mode bcs quartile

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per_error_mode_bcs_quartile_20260520T141053_result.json`
- **Structured JSON:** [`4d62251216db5ec57a43.json`](../../sessions/4d/4d62251216db5ec57a43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `/root/schema-dag-extraction/artifacts/w4_error_mode_quartile/results.json`.

## 结果

### BCS Quartile × Error Mode (%)

| Quartile | N | BCS range | Miss% | Boundary% | TypeSub% | Correct% |
|---|---|---|---|---|---|---|
| Q1 | 113 | [0.580, 0.801] | 55.53 | 6.54 | 3.05 | 33.81 |
| Q2 | 112 | [0.801, 0.808] | 48.26 | 5.48 | 9.85 | 32.95 |
| Q3 | 112 | [0.808, 0.815] | 55.51 | 5.11 | 7.60 | 29.18 |
| Q4 | 113 | [0.815, 0.936] | 53.65 | 6.44 | 3.11 | 35.78 |

### Spearman 相关 (N=450)

| Error mode | ρ | p | |
|---|---|---|---|
| miss | +0.017 | 0.722 | ns |
| boundary | −0.043 | 0.366 | ns |
| type_sub | −0.010 | 0.840 | ns |
| correct | −0.009 | 0.848 | ns |

### 总结

**三种 error mode 均与 BCS 无显著相关**（所有 p > 0.3）。BCS 既不选择性增加某一类错误，也不减少——miss 始终是主导 error mode（~49-56%），boundary 和 type_sub 占比在各 quartile 间无单调趋势。

值得注意的是 BCS 分布高度集中：Q2 和 Q3 的 BCS 范围极窄（0.801–0.815），这限制了检测 BCS 效应的统计功效。Q1 的低 BCS 主要来自小 count level（count_2 type 少→BCS 低），所以 quartile 间的变化可能被 count level 混淆。

---
