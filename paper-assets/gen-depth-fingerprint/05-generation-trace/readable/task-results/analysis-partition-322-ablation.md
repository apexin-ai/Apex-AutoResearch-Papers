# analysis partition 322 ablation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_partition_322_ablation_20260521T025951_result.json`
- **Structured JSON:** [`123008f1faba2311d3ee.json`](../../sessions/12/123008f1faba2311d3ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Summary:

| Partition | Silhouette (k=3) |
|-----------|------------------|
| 3/1/3 (original) | 0.1759 |
| 3/2/2 (alternative) | 0.3320 |
| k=2 binary | 0.7352 |

**Key finding**: 3/2/2 has +0.1561 higher silhouette, driven almost entirely by tail_decay flipping from −0.45 to +0.45 when moved to intermediate. This confirms the reviewer's intuition — tail_decay sits closer to entropy_std in (|ρ|, d) space (both have |ρ| < 0.16, d < 0.03) and is a poor fit for the near-stationary cluster.

The k=2 binary separation (drifting vs non-drifting) is identical under both partitions and remains strong (0.7352). LOGO classification is unaffected since it uses all 7 features regardless of partition.

---
