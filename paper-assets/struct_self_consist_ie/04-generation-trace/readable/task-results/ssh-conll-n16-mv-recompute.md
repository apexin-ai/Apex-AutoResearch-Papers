# ssh conll n16 mv recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_conll_n16_mv_recompute_20260522T034320_result.json`
- **Structured JSON:** [`45408e008e18519e0f3a.json`](../../sessions/45/45408e008e18519e0f3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CoNLL N=16 (seed=42) MV recompute 完成。结果（gold-nonempty subset, n=2756）:

| 指标 | 值 |
|---|---|
| greedy_f1 | 0.9128 |
| **mv_strict_f1** | **0.9148** |
| mv_incl_f1 | 0.9139 |
| oracle_f1 | 0.9636 |
| **mv_delta (strict)** | **+0.19pp** |
| mv_delta (incl) | +0.10pp |
| **degeneracy_rate** | **49.7%** |
| **alpha_crit_eff_strict** | **1.6749** |
| alpha_crit_eff_incl | 1.6719 |
| alpha_crit_strict | 0.8429 |
| capture_rate (Δ_SC / headroom) | 0.19pp / 5.08pp ≈ 3.8% |

注：greedy_f1/oracle_f1 与原 report.json 的值略有不同（0.9128 vs 0.9080），因为 recompute 只看 gold-nonempty instances (2756)，而原报告包含所有 3453 instances。

---
