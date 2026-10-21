# analysis harvest seed456 codellama

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_harvest_seed456_codellama_20260519T013316_result.json`
- **Structured JSON:** [`a625b47bccd864e4d3cc.json`](../../sessions/a6/a625b47bccd864e4d3cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
codellama13b_seed456: accuracy=98.24% [97.48%, 98.99%] — DONE (success)

Seed comparison:
  seed42:  97.50%
  seed123: 98.24%
  seed456: 98.24%
```

三个 seed 全部 ≥97.5%，seed robustness 跨架构成立。seed123 和 seed456 完全一致（98.24%），seed42 略低但仍在 CI 重叠范围内。

---
