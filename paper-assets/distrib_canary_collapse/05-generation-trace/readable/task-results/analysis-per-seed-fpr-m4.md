# analysis per seed fpr m4

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per_seed_fpr_m4_20260521T022147_result.json`
- **Structured JSON:** [`864126e2d381a43265c7.json`](../../sessions/86/864126e2d381a43265c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已生成并注册。结果摘要：

| Method | s42 | s43 | s44 | Pooled | 95% Cluster-Bootstrap CI |
|--------|-----|-----|-----|--------|--------------------------|
| **PermG** | 0/8 | 0/8 | 0/8 | 0.000 | [0.000, 0.000] |
| DiffXCorr | 4/8 | 2/8 | 3/8 | 0.375 | [0.250, 0.500] |
| NaiveXCorr | 8/8 | 7/8 | 7/8 | 0.917 | [0.875, 1.000] |
| ThresholdOnset | 3/8 | 1/8 | 2/8 | 0.250 | [0.167, 0.375] |
| TY | 2/8 | 2/8 | 0/8 | 0.167 | [0.000, 0.250] |

PermG 在 3 个 seed 全部 0 false positives，bootstrap CI 退化为 [0, 0]（因为所有 cluster 的 FPR 均为 0）。其余 4 个方法的 FPR 在 seed 间有变异但 bootstrap CI 仍远高于 nominal α=0.05，进一步确认 PermG 作为 primary indicator 的选择合理性。

输出保存在 `artifacts/m4_per_seed_fpr_breakdown.json`。

---
