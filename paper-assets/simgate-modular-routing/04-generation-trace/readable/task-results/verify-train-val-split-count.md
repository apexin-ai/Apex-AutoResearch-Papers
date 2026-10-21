# verify train val split count

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_train-val-split-count_20260515T230029_result.json`
- **Structured JSON:** [`103bc7d98b40904b3a24.json`](../../sessions/10/103bc7d98b40904b3a24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果确认：

```
Total records: 2040
seed=42: n_train=1735, n_val=305, total=2040
seed=43: n_train=1735, n_val=305, total=2040
seed=44: n_train=1735, n_val=305, total=2040
seed=45: n_train=1735, n_val=305, total=2040
```

Split 结果与 seed 无关（因为 `int(len(items) * 0.15)` 是确定性的，shuffle 只影响顺序不影响数量）。

**结论：Reviewer 是对的，论文应写 "1735/305 steps"，而非 "1734/306 steps"。**

---
