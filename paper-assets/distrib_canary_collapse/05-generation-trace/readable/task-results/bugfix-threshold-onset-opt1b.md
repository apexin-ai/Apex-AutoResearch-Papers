# bugfix threshold onset opt1b

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_threshold_onset_opt1b_20260517T130741_result.json`
- **Structured JSON:** [`61df12264a40fea6222b.json`](../../sessions/61/61df12264a40fea6222b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pythia results unchanged — it uses `method_ablation.py` (not modified). The 6 pairs shown are the overlap with Pythia's {entropy,ece} × {d1,d2,d3} set (Pythia analysis doesn't track mauve in this codepath).

---

## Results

### 1. Bug root cause

**`analyze_opt1b_full.py:91-95`** — `_onset()` computed baseline from `s[:3].mean()` and sigma from `s[:3].std()`. When canary onset occurs at gen1 (OPT entropy drops 38% in one step), the baseline window includes the onset point itself, inflating sigma (0.68) and pushing the threshold to -0.77 — above the max oriented value (-1.14). Every pair returns `onset=None` → 0/8 significant.

### 2. Fix

Replaced with `method_ablation.py`'s proven `_onset_gen` logic: baseline = `s[0]` (gen0 only), sigma = `np.std(s)` (full series), loop starts at `i=1`. Generic — no model-specific hardcoding.

### 3. OPT-1.3B Threshold Onset (fixed)

| Pair | onset_canary | onset_downstream | lead | sig |
|------|-------------|-----------------|------|-----|
| entropy→d1 | 1 | 3 | 2 | Y |
| entropy→d2 | 1 | 4 | 3 | Y |
| entropy→d3 | 1 | 5 | 4 | Y |
| entropy→mauve | 1 | 8 | 7 | Y |
| ece→d1 | 2 | 3 | 1 | Y |
| ece→d2 | 2 | 4 | 2 | Y |
| ece→d3 | 2 | 5 | 3 | Y |
| ece→mauve | 2 | 8 | 6 | Y |

**8/8 significant** (was 0/8).

### 4. Pythia-410M: unaffected
Uses `analyze_generalize.py` → `method_ablation.py:_onset_gen` which already had the correct algorithm. Results identical: entropy onset=1, ece onset=2, downstream d1=3, d2=3, d3=4.

### 5. Updated Table 5 (OPT-1.3B full 6-method summary)

| Method | Sig/8 | Key Pairs |
|--------|-------|-----------|
| Naive XCorr | 6/8 | entropy→d1,d2,d3; ece→d1,d2,d3 |
| Diff XCorr (FDR) | 6/8 | same |
| **Threshold Onset** | **8/8** | **all 8** (was 0/8) |
| PermG Fwd (FDR) | 6/8 | entropy→d1,d2,d3; ece→d1,d2,d3 |
| PermG Rev (FDR) | 0/8 | — |
| TY Granger | 2/8 | entropy→d1, ece→d1 |
| **Consensus ≥3/5** | **6/8** | entropy→d1,d2,d3; ece→d1,d2,d3 |
| **Consensus ≥4/5** | **6/8** | same |

Mauve pairs only reach significance via Threshold Onset (other methods lack power for mauve's weak 5.8% drift), so consensus stays at 6/8. Saved to `results/generalize/opt1b_wiki_a100_s42/analysis/opt1b_threshold_fixed.json`.

---
