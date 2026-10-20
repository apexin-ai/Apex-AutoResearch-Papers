# analysis minority constraint direction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_minority-constraint-direction_20260524T233125_result.json`
- **Structured JSON:** [`9a82d82ebd187bb41f00.json`](../../sessions/9a/9a82d82ebd187bb41f00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

```
=== Minority Constraint Direction Analysis ===
Non-unanimous problems: 148
Total minority unique constraints: 2169
  - Minority-exclusive (support own trace): 1596 (73.6%)
  - Cross-group shared (undirected): 573 (26.4%)
Per-problem stats:
  - Minority-exclusive ratio: 0.687 ± 0.236 (median: 0.722)
  - Shared ratio: 0.313 ± 0.236 (median: 0.278)
Variable overlap (minority-exclusive vs majority):
  - Predicate token overlap: 66.2% ± 22.4%
```

**Margin breakdown**: exclusive ratio 在各 margin 区间稳定在 0.45–0.83，无明显趋势（margin=6 和 10 的 shared 比例偏高但样本仅 7 个）。

---

**Paper-ready paragraph:**

> Among minority-vote traces in non-unanimous problems (Mistral-7B, FOLIO, $n = 148$), 73.6\% of unique constraints are exclusive to the minority group (per-problem mean: $0.69 \pm 0.24$), while only 26.4\% are cross-group shared formulas appearing in both answer groups (per-problem mean: $0.31 \pm 0.24$). Despite this surface-level exclusivity, minority-exclusive constraints share 66.2\% of their predicate tokens with majority-group constraints, indicating that the symbolic content is largely overlapping but expressed with different variable names. Under source-attribution scoring, each constraint votes exclusively for its originating trace's answer, so this near-total surface exclusivity means constraint-weighted aggregation reduces to a count of supporting traces---effectively majority vote.

结果已保存至服务器 `minority_constraint_direction.json` 和本地 `artifacts/_project/data/`。

---
