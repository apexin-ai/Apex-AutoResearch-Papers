# Evidence Tax Annotation Audit

**Date**: 2026-05-21  
**Scope**: All evidence tax numbers in `docs/paper/sections/*.tex`

---

## Executive Summary

The paper has a blanket dev-set statement (`experiments.tex:17`: "All results use the development set") and table captions say "DocRED dev Ign-F1." However, the **matched@2048 fair_tax numbers from D144/D146 are NOT in the paper**. The paper still uses the old, invalidated +7.5pp at 4B and the old -6.2pp controlled-subset number at 1.7B. The corrected fair_tax values and "matched 2048-token budget" methodology have not been incorporated.

---

## Part 1: Numbers NOT Yet in the Paper (Must Add)

The following corrected fair_tax numbers (matched@2048 fair comparison, from D144/D145/D146) do not appear anywhere in the .tex files:

| Model | fair_tax (matched@2048) | Status in paper |
|-------|------------------------|-----------------|
| Qwen3-1.7B | **-5.63pp** | Paper uses -6.2pp (old controlled subset, not matched@2048) |
| Qwen3-4B | **+0.25±0.47pp** (3-seed) | Paper uses +7.5pp (**INVALIDATED by D144**) |
| Qwen3-8B | **+0.04pp** | Paper uses +0.28pp (training-time, s42 only) |
| LLaMA-3.1-8B SFT | Unstable (s42=+1.35, s44=-12.62) | Paper uses +0.68pp (s42 only) |
| LLaMA-3.1-8B RSFT | **-1.14±0.76pp** (3-seed) | Paper uses -1.52pp (2-seed mean) |
| Qwen3-14B RSFT | **-4.54pp** (@1024, truncation symmetric) | Not in paper |
| Variance compression | 1.7B 31×, 4B 7.5×, 8B 17×, LLaMA 4.6× | ✅ Already in paper, correct |

---

## Part 2: Locations Requiring Modification

### 2.1 CRITICAL — 4B evidence tax still says +7.5pp (invalidated by D144)

**File**: `docs/paper/sections/abstract.tex:11`  
**Current**: `the evidence tax varies from beneficial ($-$6.2pp Ign-F1 on a controlled subset at 1.7B) to costly (+7.5pp at 4B) to negligible at $\geq$8B`  
**Issue**: +7.5pp invalidated; -6.2pp should be updated to matched@2048 value (-5.63pp)  
**Suggested**: `the evidence tax varies from beneficial ($-$5.6pp Ign-F1 at 1.7B) to negligible at $\geq$4B (+0.25$\pm$0.47pp at 4B, +0.04pp at 8B) on the development set with matched 2048-token generation budget`

**File**: `docs/paper/sections/introduction.tex:24`  
**Current**: `evidence generation provides implicit regularization at 1.7B ($-$6.2pp Ign-F1 on a controlled evaluation subset), imposes a substantial cost at 4B (+7.5pp), and approaches zero at $\geq$8B parameters`  
**Issue**: Same — +7.5pp invalidated, -6.2pp outdated  
**Suggested**: `evidence generation provides implicit regularization at 1.7B ($-$5.6pp Ign-F1) and approaches zero at $\geq$4B (+0.25$\pm$0.47pp at 4B, +0.04pp at 8B), measured on the development set with matched 2048-token generation budget (fair comparison subset)`

**File**: `docs/paper/sections/introduction.tex:30` (contribution list)  
**Current**: `varies from beneficial ($-$6.2pp at 1.7B) to costly (+7.5pp at 4B) to negligible ($\geq$8B)`  
**Issue**: Same invalidated numbers  
**Suggested**: `varies from beneficial ($-$5.6pp at 1.7B) to negligible at $\geq$4B (+0.25$\pm$0.47pp at 4B, +0.04pp at 8B)`

**File**: `docs/paper/sections/conclusion.tex:4`  
**Current**: `model capacity determines whether evidence acts as regularizer ($-$6.2pp at 1.7B) or burden (+7.5pp at 4B)`  
**Issue**: Same invalidated numbers  
**Suggested**: `model capacity determines whether evidence acts as regularizer ($-$5.6pp at 1.7B) or is absorbed at $\geq$4B (+0.25pp at 4B, near-zero at 8B)`

**File**: `docs/paper/sections/experiments.tex:92`  
**Current**: `the tax varies from beneficial at 1.7B ($-$6.2pp on a controlled subset; Appendix~\ref{sec:fair_subset}) to costly at 4B (+7.5pp) to negligible at $\geq$8B`  
**Issue**: Same invalidated numbers. This is the primary evidence tax prose.  
**Suggested**: `the tax varies from beneficial at 1.7B ($-$5.63pp on a matched-budget fair comparison subset; Appendix~\ref{sec:fair_subset}) to negligible at $\geq$4B (+0.25$\pm$0.47pp 3-seed mean at 4B, +0.04pp at 8B)`

### 2.2 Narrative Change — "non-monotonic" / "capacity valley" invalidated

The D144 correction (4B from +7.5pp → +0.25pp) eliminates the "costly at 4B" narrative. Per `paper_framing.md:141`, the new framing is **within-family capacity threshold** (1.7B benefits, ≥4B neutral) rather than non-monotonic curve. Check all instances of "costly" or "non-monotonic" language around 4B.

### 2.3 Token Budget Annotation — Missing "matched 2048-token budget"

The paper currently describes **mismatched** token budgets in Table 3 footnote (`experiments.tex:119`): no-evi@2048, with-evi@1024. The fair_tax numbers use **matched@2048** for both conditions. If incorporating fair_tax, the methodology must be explained:

**Suggested footnote/methodology text** (first occurrence, e.g., §4.4):  
> "All evidence tax values reported in this section are computed on the development set using a matched 2048-token generation budget for both with-evidence and no-evidence conditions, evaluated on the format-compliant document intersection (fair comparison subset) to control for differential truncation rates."

**Suggested table footnote** (for any fair_tax table):  
> "Dev set, matched @2048, fair comparison subset."

### 2.4 Existing Dev-Set Annotations (Already Adequate)

| Location | Annotation | Status |
|----------|-----------|--------|
| `experiments.tex:17` | "All results use the development set." | ✅ Blanket statement |
| `experiments.tex:102` (Table 3 caption) | "DocRED dev Ign-F1" | ✅ |
| `appendix.tex:145` (Table 8 caption) | "DocRED dev Ign-F1, s42 paired" | ✅ |
| `limitations.tex:3` | "All results use the DocRED development set; test set submission is pending." | ✅ |
| `appendix.tex:52,91,204` (other table captions) | "DocRED dev set" | ✅ |

### 2.5 14B RSFT Evidence Tax (-4.54pp) — Not in Paper

`paper_framing.md:167` documents 14B RSFT tax = -4.54pp (evidence strongly beneficial, truncation symmetric so @1024 is valid). This number does not appear in any .tex file. If adding it to Table 3 or the 14B row, annotate as: "Dev set, @1024 (truncation symmetric: no-evi 10.8% vs with-evi 10.7%)."

### 2.6 LLaMA RSFT Tax — Paper Has 2-Seed, Now 3-Seed Available

**File**: `docs/paper/sections/experiments.tex:114` (Table 3, LLaMA row)  
**Current**: `$-$1.52$^\ddagger$` with footnote "Two-seed mean (s42: $-$1.88, s43: $-$1.16); s44 pending."  
**Corrected value**: -1.14±0.76pp (3-seed mean, per D135/paper_framing.md:154)  
**Action**: Update to 3-seed value if s44 data is finalized.

---

## Part 3: Variance Compression Numbers — Already Correct

The variance compression numbers (1.7B 31×, 4B 7.5×, 8B 17×, LLaMA 4.6×) appear correctly in:
- `experiments.tex:96` (main text)
- `abstract.tex:15`
- `introduction.tex:26`
- `analysis.tex:14`
- `conclusion.tex:4` (as "7.5--17×" and "4.6×")

These are adequately covered by the blanket "All results use the development set" statement. No additional per-number annotation needed.

---

## Summary of Required Actions

1. **CRITICAL**: Replace all instances of +7.5pp (4B) with +0.25±0.47pp — 5 locations (abstract, intro×2, experiments, conclusion)
2. **CRITICAL**: Update -6.2pp (1.7B) to -5.63pp (matched@2048) — same 5 locations
3. **ADD**: Matched@2048 methodology explanation in §4.4 or Appendix controlled subset section
4. **ADD**: "fair comparison subset" annotation wherever fair_tax numbers appear
5. **UPDATE**: LLaMA RSFT tax from 2-seed -1.52pp to 3-seed -1.14±0.76pp (Table 3)
6. **CONSIDER**: Adding 14B RSFT tax (-4.54pp) to Table 3
7. **NARRATIVE**: Revise "costly at 4B" / "non-monotonic" language → "within-family capacity threshold"
