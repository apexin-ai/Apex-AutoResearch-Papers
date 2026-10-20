# ssh v3 s42 recompute final

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v3_s42_recompute_final_20260521T232846_result.json`
- **Structured JSON:** [`3c6f68c2c7c9398382aa.json`](../../sessions/3c/3c6f68c2c7c9398382aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mf4v2_s42_v3 结果

| 指标 | 值 |
|------|-----|
| **samples.jsonl 行数** | 37,648 (完整) |
| **Greedy F1** | 0.7911 |
| **MV F1 (strict, ≥5/8)** | 0.7586 |
| **MV Δ (pp)** | **−3.25pp** |
| **Keyset degeneracy** | **9.1%** |
| **α_crit_eff_strict** | **0.4352** |

补充数据：
- Gold-nonempty instances: 32,565 / 37,648
- MV F1 (inclusive, ≥4/8): 0.7783 (Δ = −1.28pp)
- Oracle F1: 0.8803
- α_crit_strict: 0.3956

MV strict 比 greedy 低 3.25pp，退化率 9.1%，α_crit_eff_strict = 0.4352。

---
