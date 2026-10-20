# analysis d112 table2 f1 fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d112_table2_f1_fix_20260516T094332_result.json`
- **Structured JSON:** [`97a55a0a9d52efab585a.json`](../../sessions/97/97a55a0a9d52efab585a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. All 6 outputs saved to `/root/autodl-tmp/struct_self_consist_ie/output/d112_table2_fix/`:

| File | Content |
|------|---------|
| `corrected_table2.json` | Unified macro F1 table (529 inst, 2-seed) |
| `bootstrap_results.json` | Paired bootstrap B=10000, CIs, p-values, Cohen's d |
| `cross_dataset_check.json` | CoNLL/WNUT/RE micro-macro comparison |
| `clarification_v2.txt` | 10 specific locations in paper to fix |
| `investigation.md` | Full diagnostic report |
| `fix_table2.py` | Reproducible recomputation script |

**Corrected Table 2 (SciERC NER, macro F1, n=529):**

| Method | F1 | Δ vs Greedy | p |
|--------|-----|-------------|---|
| Oracle | 0.778 | +13.3 pp | — |
| **Greedy (T=0)** | **0.645** | — | — |
| LP | 0.647 | +0.2 pp | .385 |
| SJ | 0.646 | +0.1 pp | .889 |
| FK | 0.646 | +0.1 pp | .881 |
| EM | 0.637 | -0.8 pp | .317 |
| VC | 0.623 | -2.2 pp | .060 |
| Random | 0.610 | -3.5 pp | — |

**Key impact**: The claim "Greedy surpasses all selection" (0.663 vs 0.647) was an artifact of micro/macro mixing. Corrected: Greedy (0.645) ≈ LP (0.647), statistically indistinguishable. The core thesis (correlation-selection gap) is strengthened — not weakened — because the framing shifts to "selection adds N=8 cost for zero gain."

---
