# analysis premise count confound

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_premise-count-confound_20260522T154537_result.json`
- **Structured JSON:** [`4a6f26b36da331da1844.json`](../../sessions/4a/4a6f26b36da331da1844.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results complete. Here's the summary:

---

## P0-A: McNemar's Test (ISR β=0.1 vs Random β=0.1, seed 42)

**All 100 test problems are natural matched pairs** (both conditions evaluate the same problems, premise count inherently matched).

| | Random genuine | Random ¬genuine |
|---|---|---|
| **ISR genuine** | 3 | 10 |
| **ISR ¬genuine** | 15 | 72 |

- Discordant pairs: **25** (not 16 — the actual count)
- McNemar's χ² = (10−15)²/25 = **1.000**, p = **0.317**
- Exact binomial p = **0.424**
- **Not significant at α=0.05** — the genuine rate difference (ISR 16.0% vs Random 22.8% among proved) is not statistically significant under paired analysis.

Proved agreement table: a=67, b=14, c=12, d=7 → χ²=0.15, p=0.695 (also n.s.)

---

## P0-B: Premise-Count-Matched Mode Composition

| Bin | Cond | N_proved | CE% | TS% | PG% | Gen% |
|-----|------|----------|-----|-----|-----|------|
| ≤3 | ISR | 8 | 50.0 | 12.5 | 25.0 | 12.5 |
| ≤3 | Random | 6 | 50.0 | 0.0 | 0.0 | 50.0 |
| 4-6 | ISR | 61 | 47.5 | **19.7** | 18.0 | 14.8 |
| 4-6 | Random | 58 | 72.4 | **0.0** | 5.2 | 22.4 |
| ≥7 | ISR | 12 | 75.0 | 0.0 | 0.0 | 25.0 |
| ≥7 | Random | 15 | 86.7 | 0.0 | 0.0 | 13.3 |

**TS shift by bin:**
- ≤3: +12.5pp (tiny sample, n=6-8)
- 4-6: **+19.7pp** (main bin, n=58-61)  
- ≥7: +0.0pp (no TS hacking for complex problems)

**Key finding:** TS shift is concentrated in the 4-6 premise bin and absent for ≥7 premises. This is NOT a confound — it reveals that TS hacking is **premise-count-dependent**: models learn tautological shortcuts only for simpler problems where "ignore all premises, restate conclusion" is viable. For complex problems (≥7 premises), ISR actually produces higher genuine% (25.0%) than Random (13.3%), though the per-bin McNemar tests are all non-significant (small n).

**Minor note:** My script yields ISR genuine=13 vs pooled stats' 14 — one PG/genuine edge case. All conclusions hold either way.

---
