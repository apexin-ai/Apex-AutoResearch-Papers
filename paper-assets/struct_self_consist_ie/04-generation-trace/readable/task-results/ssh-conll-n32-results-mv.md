# ssh conll n32 results mv

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_conll_n32_results_mv_20260522T041133_result.json`
- **Structured JSON:** [`c65fef5c7d816587cd5f.json`](../../sessions/c6/c65fef5c7d816587cd5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CoNLL N=32 MV recompute 完成。完整指标：

| 指标 | 值 |
|------|-----|
| greedy_f1 | 0.9120 |
| mv_strict_f1 | 0.9166 |
| mv_incl_f1 | 0.9169 |
| oracle_f1 | 0.9690 |
| mv_delta_strict | +0.46pp |
| mv_delta_incl | +0.49pp |
| degeneracy_rate | 40.5% |
| alpha_crit_strict | 0.4560 |
| alpha_crit_incl | 0.4560 |
| alpha_crit_eff_strict | 0.7663 |
| alpha_crit_eff_incl | 0.7663 |

注意：MV recompute 的 greedy_f1 (0.9120) 与 report.json (0.9072) 略有差异——recompute 只在 gold-nonempty 的 2756 条上计算，report.json 在全部 3453 条上计算。oracle_f1 同理（0.9690 vs 0.9645）。

---
