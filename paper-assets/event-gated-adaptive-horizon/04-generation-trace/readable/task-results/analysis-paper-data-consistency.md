# analysis paper data consistency

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-data-consistency_20260517T105616_result.json`
- **Structured JSON:** [`d4bcfd2f8a4ca9d5e76c.json`](../../sessions/d4/d4bcfd2f8a4ca9d5e76c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I've gathered all the data needed. Here's the full consistency verification report.

---

## Results.tex Data Consistency Report

### TABLE 1 — Eval Return & NVE

| Row | Metric | Paper | Registry | Verdict |
|---|---|---|---|---|
| 001 Baseline | eval@105K | 915.7 | 915.67 | **PASS** |
| 006 Fixed dt=2 | eval@65K | 132.9 | 132.86 | **PASS** |
| 006 Fixed dt=2 | NVE | 4.83× | 2.722/0.563=4.834 | **PASS** |
| 007 Fixed dt=4 | eval@55K | 152.5 | 152.49 | **PASS** |
| 005 Learned gate | eval@145K | 98.8 | 98.84 | **PASS** |
| 008d Factorial s1 | eval@55K | 82.8 | 82.75 | **PASS** |
| 008d Factorial s1 | NVE | 4.12× | 4.12 (metrics summary) | **PASS** |
| 009b Factorial s2 | eval@105K | 267.9 | 267.93 | **PASS** |
| 009b Factorial s2 | NVE | 1.62× | 1.62@45K (35K+ window) | **PASS** |
| 008d_s3 Factorial s3 | eval@105K | 268 | 267.6 | **PASS** |
| 008d_s3 Factorial s3 | NVE | 1.53× | 1.53 | **PASS** |
| 008f No dt_emb | eval@105K | 503.0 | 503 | **PASS** |
| 008f No dt_emb | NVE | 0.97× | 0.97@55K | **PASS** |
| 008a Unexposed emb | eval@105K | 777.7 | 777.66 | **PASS** |
| 008a Unexposed emb | NVE | 0.93× | 0.93@55K | **PASS** |
| 015b Frozen emb | eval@105K | 204.2 | 204.2 | **PASS** |
| 015b Frozen emb | NVE | 0.47× | 0.467@85K | **PASS** |
| 018 s1 Full-SGS | eval@105K | 448.3 (macro) | 448.3 (018v2 registry) | **PASS** |
| 018 s1 Full-SGS | NVE | 1.66× (macro) | 1.66@95K (018v2) | **PASS** |
| 018 s2 Full-SGS | eval@105K | 40.8 | 40.8 (registry notes D074) | **PASS** |
| 008e_v3 s1 | eval@105K | 869.9 | 869.9 | **PASS** |
| 008e_v3 s1 | NVE | 0.80× | 0.527/0.656=0.803 | **PASS** |
| 008e_v3 s2 | eval@105K | 137.0 | 136.96 | **PASS** |
| 008e_v3 s2 | NVE | 3.78× | 3.78 | **PASS** |
| 010b Cheetah | eval@105K | 51.7 | 51.72 | **PASS** |
| 010b Cheetah | NVE | 14.59× | 14.59 | **PASS** |

### TABLE 2 — RSSM Fidelity

All 18 cells (3 configs × 6 metrics) match the registry `exp_rssm_fidelity_analysis` exactly. **PASS**.

### DETECTOR TABLE — Validation

| Metric | Paper | Computed | Verdict |
|---|---|---|---|
| TPR | 3/3 = 1.00 | 3/(3+0) = 1.00 | **PASS** |
| FPR | 2/7 = 0.29 | 2/(2+5) = 0.286 | **PASS** |
| Precision | 3/5 = 0.60 | 3/(3+2) = 0.60 | **PASS** |
| F1 | 0.75 | 2×0.6×1.0/(0.6+1.0) = 0.75 | **PASS** |
| Peak eval values | All 10 rows | Match registry within rounding | **PASS** |

### IN-TEXT PERCENTAGES (F1–F7)

| Claim | Computation | Verdict |
|---|---|---|
| 006 "14% of baseline" | 132.9/915.7 = 14.5% | **PASS** (rounded) |
| 007 "19%" | 176.9/915.7 = 19.3% | **PASS** |
| 005 "11%" | 98.8/915.7 = 10.8% | **PASS** |
| "mean eval 206.3" | (82.8+267.9+268)/3 = 206.2 | **PASS** (minor rounding) |
| "21.3% of baseline 970.41" | 206.3/970.41 = 21.3% | **PASS** |
| seed 2 "27.6% of baseline" | 267.9/970.41 = 27.6% | **PASS** |
| "-47% at dt=2" | 485.3/915.7 = 53% | **PASS** |
| "-81% at dt=4" | 176.9/915.7 = 19.3% | **PASS** |
| entropy "-5.21 → -3.83" | registry: -5.208 → -3.828 | **PASS** |
| SGS "-51% final" | 448.3/915.7 = 49% | **PASS** |
| 018 s2 "-96%" | 40.8/915.7 = 4.5% | **PASS** |
| 016e NVE 10.42× | registry: 10.42 | **PASS** |
| 010b peak 321.9 | registry: 321.89 | **PASS** |
| 010b NVE 14.59× | registry: 14.59 | **PASS** |
| "50% prevention rate" | 1/2 seeds | **PASS** |
| AUROC = 0.933 | decision D054/D055: 14/15≈0.933 | **PASS** |
| Fig 2 "-73% peak" | figure code: 250.0/915.67-1=-72.7% | **PASS** |
| Fig 2 "-86% final" | figure code: 131.08/915.67-1=-85.7% | **PASS** |

---

### MISMATCHES / ISSUES

**1. MISMATCH — Cheetah "collapsing to 22.7 (−93%)"**

The paper says: *"evaluation peaks at 321.9 before collapsing to 22.7 (−93%)"*

The value 22.7 is the **trough** at step 65K (civo_decomposition_data.json: 22.667), not the final eval. The actual final eval@105K = **51.72** (registry). The eval partially recovered from 22.7→146.7→109.7→48.0→51.7 over the remaining steps. Saying "collapsing to 22.7" implies that's the endpoint, which is misleading. The −93% is mathematically correct relative to the trough, but readers will assume it's the final performance.

**Suggested fix**: Change to *"evaluation peaks at 321.9, reaching a minimum of 22.7 at 65K (−93\% from peak) before partially recovering to 51.7 at 105K"* or simply use the final: *"collapsing to 51.7 (−84\%)"*.

**2. MINOR — F2: "8.6% of baseline"**

82.8/970.41 = 8.53%, rounds to 8.5%, not 8.6%. Off by 0.1pp.

**3. MINOR — Table 1 footnote: "1.61× at 35K"**

Analysis data: NVE@35K = 1.6039, rounds to **1.60**, not 1.61.

**4. CONSISTENCY — Dual baseline reference**

Most of the paper uses baseline = 915.7 (eval@105K). F2 switches to baseline = 970.41 (peak at 505K) for the "21.3% of baseline" calculation. This is explicitly stated but could confuse readers. Consider using one baseline consistently, or adding a clarifying note.

**5. CONSISTENCY — Figure 2 caption says "(008d, 009b)" but data is only 008d-extended**

The figure generation code (`gen_paper_figures.py:115`) plots only `exp_008d_subsample_on_h8` (extended to 105K via exp_009e with eval_105K=131.08). The caption claims two seeds (008d, 009b) but the actual bars use only one seed's trajectory. The "trained dt-emb" final bar shows 131.08 (from exp_009e), which doesn't appear in Table 1. Suggest correcting the caption to match the actual data source.

**6. CONSISTENCY — 008d eval data beyond 55K**

Table 1: 008d eval = 82.8@55K (the original experiment ended there). Figure 2's trained-dt-emb bar uses 008d_eval_105K = 131.08 from exp_009e (a continuation of the same config). This isn't documented in the paper — the reader would assume 008d stopped at 55K but the figure silently uses data up to 105K from a different experiment ID.

---

### SUMMARY

- **30 verified claims**: All PASS
- **1 misleading claim**: Cheetah eval "22.7" is a trough, not the final value (actual final = 51.72)
- **2 minor rounding errors**: "8.6%" should be 8.5%; "1.61×" should be 1.60×
- **3 internal consistency notes**: dual baseline, figure caption mismatch with data source, undocumented use of exp_009e data

---
