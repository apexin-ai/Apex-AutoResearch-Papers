# analysis entity count stats

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_entity-count-stats_20260523T095059_result.json`
- **Structured JSON:** [`d4b3deebe0744820dad9.json`](../../sessions/d4/d4b3deebe0744820dad9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| Dataset | Docs | Mean | Median | P25 | P75 | Max |
|---------|------|------|--------|-----|-----|-----|
| SciERC  | 100  | 16.9 | 16.5   | 12.0 | 20.0 | 36 |
| DocRED  | 998  | 19.6 | 19.0   | 15.0 | 24.0 | 42 |

DocRED 每文档 unique entity 数略高于 SciERC（均值 19.6 vs 16.9），但两者量级接近，分布也较相似。DocRED 的上限更高（42 vs 36），下限差异更大（2 vs 5）。

---
