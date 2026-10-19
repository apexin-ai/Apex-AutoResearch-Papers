# infra plan009 iv filtered supplement

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan009-iv-filtered-supplement_20260520T185334_result.json`
- **Structured JSON:** [`86b7b63e0c05e1761846.json`](../../sessions/86/86b7b63e0c05e1761846.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`iv_filtering` 字段已写入，值正确：

```json
"iv_filtering": {
  "n_filtered": 3000,
  "n_total": 28000,
  "pct_infinite": 10.7,
  "note": "Non-finite Wald estimates (division by near-zero first-stage) silently excluded from regression analysis. Paper citations must note this exclusion."
}
```

与 IV 回归 `n_obs=25000`（其余 topology 均为 28000）一致，差值 3000 = 10.7%。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "n_filtered": 3000,
    "n_total": 28000,
    "pct_infinite": 10.7,
    "note": "Non-finite Wald estimates (division by near-zero first-stage) silently excluded from regression analysis. Paper citations must note this exclusion."
  }
}
```

</details>

---
