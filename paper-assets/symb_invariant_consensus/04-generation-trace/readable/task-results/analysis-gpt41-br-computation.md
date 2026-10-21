# analysis gpt41 br computation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt41-br-computation_20260521T164951_result.json`
- **Structured JSON:** [`9a1bfa17f6f42f85cb38.json`](../../sessions/9a/9a1bfa17f6f42f85cb38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整指标表：

| 指标 | gpt-4.1 | gpt-4o (参照) |
|---|---|---|
| SC accuracy | 82.84% (169/204) | 73.91% |
| SICA accuracy | 81.37% (166/204) | 72.05% |
| Δ (SICA-SC) | -1.47pp | -1.86pp |
| Mean BR | **2.697** | 2.94 |
| Median BR | **1.534** | 1.91 |
| Weighted BR | **3.2099** | 3.07 |
| n_br_finite | **16** (38-22) | 25 |
| BR=∞ | **22** | 20 |
| extraction_rate | **1.0000** | — |
| Process-κ | 0.792 | 0.788 |
| Answer-κ | 0.862 | 0.801 |

要点：
- Mean/Median BR 比 gpt-4o 低（2.70 vs 2.94, 1.53 vs 1.91），说明 gpt-4.1 在 SICA-wrong 题上的偏差程度更温和
- Weighted BR 略高（3.21 vs 3.07），因为高权重题目上偏差更大
- BR=∞ 占比更高（22/38=57.9% vs 20/45=44.4%），gold answer 零权重的情况更多——n_br_finite 只有 16 题
- extraction_rate = 100%，所有 trace 都成功提取了约束

结果已保存到 `/root/symb_invariant_consensus/results/exp_d135_frontier_scb/gpt-4.1/cross_model/gpt41_full_metrics.json`。

---
