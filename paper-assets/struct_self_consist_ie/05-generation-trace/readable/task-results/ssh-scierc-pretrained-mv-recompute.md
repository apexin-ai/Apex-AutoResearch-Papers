# ssh scierc pretrained mv recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scierc_pretrained_mv_recompute_20260521T200938_result.json`
- **Structured JSON:** [`c4dc8cca03b9a4ee8e4e.json`](../../sessions/c4/c4dc8cca03b9a4ee8e4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 seed 都跑完了。汇总 3-seed 结果：

## SciERC Pretrained — 3-Seed Results

| Metric | s42_v2 | s123 | s456 | **Mean ± Std** |
|---|---|---|---|---|
| greedy_f1 | 0.2434 | 0.2436 | 0.2436 | **0.2435 ± 0.0001** |
| mv_strict_f1 | 0.2618 | 0.2548 | 0.2642 | **0.2603 ± 0.0040** |
| oracle_f1 | 0.3888 | 0.3941 | 0.3952 | **0.3927 ± 0.0028** |
| degeneracy | 0.009 | 0.006 | 0.009 | **0.008 ± 0.002** |
| n_instances | 529 | 529 | 529 | 529 |
| MV Δ (pp) | +1.84 | +1.12 | +2.06 | **+1.67 ± 0.40** |
| α_crit_eff_strict | — | 0.1468 | 0.1537 | — |

**关键数字**: MV strict F1 = **0.2603 ± 0.0040**, MV Δ = **+1.67 ± 0.40 pp**, degeneracy 很低 (0.8%)。

---
