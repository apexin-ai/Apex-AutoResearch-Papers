# Data Consistency Fix Report

**Date**: 2026-05-25
**Trigger**: Reviewer flagged multiple references to stale L28 probe peak data contradicting fig6

## Changes Made

### 1. [CRITICAL] Abstract (`abstract.tex`)
- **Before**: "the probe signal peaks at late layers (88% depth)"
- **After**: "the probe signal is broadly distributed across mid-to-upper layers"
- Trimmed from ~200+ words to **149 words** (EMNLP limit: 200)

### 2. [CRITICAL] Introduction (`introduction.tex`)
- Line 21: L28 (88%) → L15 (47%); `p = 0.002` → `p < 0.001`
- Line 27: Rewrote Detection--decision dissociation bullet: L28 → L15, p = 0.002 → p < 0.001; shifted primary evidence framing to cross-model contrast

### 3. [CRITICAL] Experiments (`experiments.tex`)
- Line 33: "peak at layer 28, 88% depth" → "peak at layer 15, 47% depth"
- Line 44 (fig3 caption): removed L28 as EN→EN peak, updated Fisher p = 0.002 → p < 0.001
- Line 165 (fig5 caption): removed "probe peak" label from L28
- Line 170: "L28 (probe peak, 88% depth)" → "L28 (88% depth)"
- Line 174: "EN→EN at L28" → "EN→EN probe peak (L15, 47%)"

### 4. [CRITICAL] Discussion (`discussion.tex`)
- Line 5: Fisher p = 0.002 → p < 0.001; EN→EN at L28 → L15
- Line 6: "between the linear peak (L28) and the causal node (L13)" → "above both the linear peak (L15) and the causal node (L13)" (MLP peak L18 is now above linear peak L15, not between)

### 5. [CRITICAL] Conclusion (`conclusion.tex`)
- Rewrote three-way dissociation: removed "linear peak (L28)" framing
- New narrative: probe peak (L15), MLP peak (L18), causal node (L13) cluster in mid-layers; primary detection≠decision evidence is cross-model
- p = 0.002 → p < 0.001

### 6. [WARNING] Appendix D fig6 caption (`main.tex` line 99)
- "linear probe peak (L28, 88% depth)" → "(L15, 47% depth)"
- Added note about upper layers retaining signal without causal influence

### 7. [WARNING] Appendix E AUROC table (`main.tex` line 111)
- "at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data)" → "for conflict probes (matched-condition data, best layer per model)"

### 8. [WARNING] Appendix F matched-condition table (`main.tex` line 146)
- Llama: N=136 → N=201, probe accuracy 76.1% → 90.0%

## Verification Results

### LaTeX Compilation
- **Errors**: 0
- **Pages**: 12 total (main text ≤ 8, Limitations + References + Appendices on pages 9-12)

### Abstract Word Count
- **149 words** (limit: 200) ✅

### Residual L28 References (all legitimate)
| File | Line | Context | Status |
|------|------|---------|--------|
| experiments.tex | 160 | "six layers L12--L28" (tested range) | OK - factual |
| experiments.tex | 165 | "L28 (88%)" (steering result) | OK - no "probe peak" label |
| experiments.tex | 170 | "L28 (88% depth)" (negative steering result) | OK - no "probe peak" label |
| experiments.tex | 174 | "upper layers (e.g., L28)" | OK - supplementary evidence |
| experiments.tex | 200-201 | Table data rows | OK - actual data |
| main.tex | 80 | Boundary table data row | OK - actual data |
| main.tex | 99 | "upper layers (e.g., L28)" | OK - supplementary evidence |
| method.tex | 64 | "three Llama layers (L13, L18, L28)" | OK - method description |

### Residual 88% References
All in context of L28 being at 88% depth (factual layer position). None claim L28 as probe peak. ✅

### Residual p = 0.002 References
| File | Line | Context | Status |
|------|------|---------|--------|
| experiments.tex | 156 | "Fisher $p = 0.002$" for α=+5 at L13 | OK - specific α value p, not overall |
| experiments.tex | 160 | "L14 ($p = 0.002$)" | OK - L14's value, not L13's |

### "late layer" References
- related_work.tex:23: "late-layer intervention fails" — generic statement, still accurate. ✅

## Summary
All L28-as-probe-peak references eliminated. All p = 0.002 references for L13's overall significance corrected to p < 0.001. Remaining L28/88%/p=0.002 occurrences are legitimate (data tables, tested layers, specific α-value p-values for L13, or L14's p-value).
