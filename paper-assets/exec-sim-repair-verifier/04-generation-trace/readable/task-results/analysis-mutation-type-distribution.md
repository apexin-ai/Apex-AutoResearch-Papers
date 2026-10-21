# analysis mutation type distribution

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mutation-type-distribution_20260517T112813_result.json`
- **Structured JSON:** [`9aa089d0d3be910c6cdf.json`](../../sessions/9a/9aa089d0d3be910c6cdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出写入 `artifacts/mutation_type_distribution.json`。

关键发现:

| Mutation Type | Val % | Test % | Shift | Test Acc (4B/8B s42) |
|---|---|---|---|---|
| gold | 45.2 | 47.4 | +2.2 | 98.3 / 96.2 |
| operator_swap | **19.1** | **34.3** | **+15.2** | 78.9 / 81.4 |
| boundary_removal | 15.0 | 10.7 | -4.3 | 46.9 / 46.9 |
| return_value | 10.7 | 5.7 | -5.0 | 68.0 / 75.4 |
| off_by_one | 10.0 | **1.9** | **-8.1** | 58.5 / 86.9 |

- `operator_swap` 从 val 19.1% 涨到 test 34.3%，且 val accuracy 97% 降到 test 79-83%，是 val→test 整体 accuracy 下降的主因
- `boundary_removal` 在所有 seed/size 上稳定 ~46% test accuracy，是 scale-invariant 的难度天花板
- `off_by_one` test 集仅 183 样本 (1.9%)，估计不稳定但 8B 获益最大 (+24pp over 4B)
- LaTeX table 已包含在 JSON 的 `latex_table` 字段中，可直接粘贴到 appendix

---
