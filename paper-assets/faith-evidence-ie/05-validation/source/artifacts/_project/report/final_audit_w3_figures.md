# Worker 3 Final Audit: Figure Data + Appendix Text Numbers

**Date**: 2026-05-23
**Scope**: fig_evidence_tax, fig_spectrum, appendix.tex numerical consistency, limitations.tex

---

## Task A: fig_evidence_tax Data Verification

### Script: `figures/paper/plot_evidence_tax.py`

| Model | tax_value | tax_error | n_seeds | Appendix Match |
|-------|-----------|-----------|---------|----------------|
| Qwen3-1.7B | -5.43 | 0 | 1 | tab:rsft_test_tax s42: 29.33-23.90=-5.43 |
| Qwen3-4B | +1.65 | 0.29 | 3 | 3-seed mean +1.65+-0.29 (text line 266) |
| Qwen3-8B | -0.91 | 0.74 | 3 | 3-seed mean -0.91+-0.74 (text line 266) |
| LLaMA-3.1-8B | -1.46 | 0.40 | 2 | 2-seed mean -1.46+-0.40 (text line 266) |
| Qwen3-14B | +0.43 | 0.49 | 2 | 2-seed mean +0.43+-0.49 (text line 266) |

**Per-seed arithmetic verification (script comments vs tab:rsft_test_tax s42 column):**
- 4B: s42=+1.51 (tab: 26.52-25.01=+1.51), s43=+1.99, s44=+1.46. mean=(1.51+1.99+1.46)/3=1.653->1.65, std=0.292->0.29
- 8B: s42=-0.34 (tab: 33.19-33.53=-0.34), s43=-1.74, s44=-0.65. mean=-0.91, std=0.735->0.74
- LLaMA: s42=-1.74 (tab: 33.80-35.54=-1.74), s43=-1.17. mean=-1.455->-1.46, std=0.403->0.40
- 14B: s42=+0.77 (tab: 39.26-38.49=+0.77), s43=+0.08. mean=0.425->0.43, std=0.488->0.49

## Task B: fig_spectrum Data Verification

### Script: `figures/paper/plot_spectrum.py`

| Point | Script (Rel-F1, Evi-F1) | tab:spectrum (Rel-F1, Evi-F1) | Match |
|-------|------------------------|-------------------------------|-------|
| SFT | (0.4439, 0.7961) = (44.39, 79.61) | 44.39, 79.61 | MATCH |
| RSFT CED | (0.4580, 0.8096) = (45.80, 80.96) | 45.80, 80.96 | MATCH |
| GRPO bf16 G=8 | (0.4549, 0.8086) = (45.49, 80.86) | 45.49, 80.86 | MATCH |
| DPO bf16 1ep | (0.3337, 0.8090) = (33.37, 80.90) | 33.37, 80.90 | MATCH |
| DPO bf16 3ep | (0.3145, 0.8484) = (31.45, 84.84) | 31.45, 84.84 | MATCH |
| GRPO QLoRA G=4 | (0.0138, 0.8504) = (1.38, 85.04) | 1.38, 85.04 | MATCH |

**DPO 1ep Rel-F1 = 33.37** confirmed (not 33.38, prior audit correction verified).

## Task C: Appendix Text-Number Verification

### C1: RSFT test-set evidence tax (sec:generalization_full, lines 265-287)

All multi-seed means and per-seed s42 values match between text, tab:rsft_test_tax, and fig_evidence_tax script.

### C2: Variance CI (sec:variance_ci, lines 117-141)

**Cohen's d verification** (pooled std, n1=n2=3):
| Scale | Computed d | Reported d | Match |
|-------|-----------|-----------|-------|
| 1.7B | 3.317 | 3.31 | MATCH |
| 4B | 0.457 | 0.46 | MATCH |
| 8B | 1.791 | 1.79 | MATCH |
| LLaMA | 2.578 | 2.58 | MATCH |

**95% CI verification** (chi-sq, df=2):
All SFT CIs verified. RSFT CIs for 1.7B are consistent with unrounded sigma ~ 0.0857 (CI: [0.04, 0.54]), NOT with displayed sigma=0.09 (which would give [0.05, 0.57]).

**Compression ratio:**
| Scale | Displayed ratio | Computed from displayed stds | Match |
|-------|----------------|------------------------------|-------|
| 1.7B | 32.6x | 2.79/0.09 = 31.0x | SEE BELOW |
| 4B | 7.5x | 3.80/0.51 = 7.45x -> 7.5x | MATCH |
| 8B | 6.5x | 3.23/0.50 = 6.46x -> 6.5x | MATCH |
| LLaMA | 4.6x | 2.92/0.64 = 4.56x -> 4.6x | MATCH |

Table caption says "ratio of SFT to RSFT point estimates (unrounded)" — so 32.6x is internally consistent (computed from unrounded stds). The CIs also confirm this.

**Sign test**: p=0.0625 stated as one-sided binomial with n=4. Correct: P(X>=4|n=4,p=0.5) = 0.5^4 = 0.0625.

### C3: Error Analysis (sec:error_analysis, lines 356-389)

Text states:
- 1.7B: -841 truncation FN, -22%; LLaMA: -593 hallucinated FP, -11.8%; 1.7B duplicates: -20.2%
- Table reports: Truncation -22%, -16%, -18%; Hallucinated -8%, -6%, -12%; Duplicates -20%, -11%, -14%

Text "6-22%" (line 11 of analysis.tex) matches the range across error categories and scales. Consistent.

### C4: Training-Time Tax (sec:training_tax, lines 170-200)

| Model | Tax | Source |
|-------|-----|--------|
| 1.7B | -5.63pp | tab:training_tax: 48.38-42.75=-5.63 |
| 4B | +0.25+-0.47pp (3-seed) | tab:training_tax footnote: range -0.19 to +0.73 |
| 8B | +0.04pp | tab:training_tax: 50.19-50.15=+0.04 |
| 14B | +0.03pp | tab:training_tax: 55.10-55.07=+0.03 |

All consistent with table values and text.

Evidence training seed variance: 4B 25x (0.02/0.50=0.04->text says 25x from 0.50/0.02=25), 8B 1.4x (0.48/0.35=1.37), 1.7B reversed (0.63>0.20). All consistent.

### C5: Cross-architecture (sec:generalization_full, lines 208-264)

LLaMA RSFT per-seed: s42=57.14, s43=56.62, s44=55.87.
- Mean: (57.14+56.62+55.87)/3 = 56.543 -> 56.54. MATCH
- Std: sqrt(((57.14-56.543)^2+(56.62-56.543)^2+(55.87-56.543)^2)/2) = sqrt((0.3564+0.0059+0.4532)/2) = sqrt(0.4078) = 0.639 -> 0.64. MATCH

LLaMA SFT: s42=53.84, s43=51.42, s44=48.02.
- Mean: 51.093 -> 51.09. MATCH
- Std: sqrt(((53.84-51.09)^2+(51.42-51.09)^2+(48.02-51.09)^2)/2) = 2.924 -> 2.92. MATCH
- Gain: 56.54-51.09 = 5.45. MATCH
- Compression: 2.92/0.64 = 4.56 -> 4.6x. MATCH

Re-DocRED: SFT 36.59, RSFT 41.45, gain +4.86. MATCH (41.45-36.59=4.86).

Test set dev-test drops: range 18.9-21.9pp. Verified from tab:test_results (min: 44.64-25.79=18.85->18.9; max: 51.19-29.33=21.86->21.9). MATCH.

### C6: Full Ablation (sec:ablation_full, lines 39-81)

Per-seed mean verification (4-seed):
- Ign-F1: (44.23+45.12+45.11+44.16)/4 = 44.655 -> 44.66. MATCH
- Rel-F1: (45.17+46.01+46.21+45.14)/4 = 45.6325 -> 45.63. MATCH
- Evi-F1: (81.74+80.63+80.50+81.74)/4 = 81.1525 -> 81.15. MATCH
- EDCR: (0.6569+0.6542+0.6350+0.6550)/4 = 0.65028 -> 0.6503. MATCH

SFT s42 improvement: 44.66-39.74 = 4.92. MATCH.
Random RSFT improvement: 41.14-39.74 = 1.40. MATCH.

### C7: Scaling table (tab:scaling in experiments.tex)

RSFT Gain = RSFT - SFT verified for all 5 rows (6.55, 1.24, 4.14, 3.79, 5.45). All MATCH.

## Task D: Limitations Section

File: `docs/paper/sections/limitations.tex` (5 lines)

Three points covered. One specific number: **Evi-F1 -7.7pp** for sentence-level CED filtering disrupting co-reference chains.

This value also appears in `analysis.tex` line 5: "CED operates effectively at the response level but fails at sentence-level granularity (Evi-F1 -7.7pp)".

Source: `experiments.tex` line 67 mentions "-7.75" in a different context (RSFT inference-time tax at 1.7B). The -7.7pp for sentence-level CED filtering is a separate finding.

No dedicated table or appendix section provides the underlying data for the sentence-level CED ablation that produces -7.7pp. Both analysis.tex and limitations.tex cite it as an inline finding.

---

## CONSOLIDATED RESULTS

## Verified Consistent

1. **fig_evidence_tax**: All 5 tax_values, 5 tax_errors, 5 n_seeds match tab:rsft_test_tax and multi-seed computation
2. **fig_spectrum**: All 6 data points match tab:spectrum exactly; DPO 1ep = 33.37 confirmed
3. **Cohen's d**: All 4 values verified (3.31, 0.46, 1.79, 2.58)
4. **95% CIs**: All 8 intervals verified via chi-sq(df=2) computation
5. **Sign test**: p=0.0625 correct for one-sided binomial n=4
6. **Training-time tax**: All Qwen3 values match tab:training_tax
7. **LLaMA per-seed**: mean, std, gain, compression all verified
8. **Re-DocRED**: cross-dataset gain +4.86pp verified
9. **Test set drops**: range 18.9-21.9pp, Spearman rho=1.0 verified from tab:test_results ranking
10. **Ablation means**: 4-seed Ign-F1/Rel-F1/Evi-F1/EDCR all verified
11. **Error analysis**: percentages match between table and text
12. **RSFT Gain** in tab:scaling: all 5 values verified
13. **Per-seed evidence tax arithmetic**: all multi-seed means and stds verified from individual seed values
14. **Compression ratios** (4B, 8B, LLaMA): all match from displayed stds

## Discrepancy Found

1. **1.7B variance compression: 31x (experiments.tex line 63) vs 32.6x (appendix tab:variance_ci line 132)**
   - experiments.tex: "variance compression is 31x at 1.7B"
   - appendix table: "32.6x" with caption "ratio of ... point estimates (unrounded)"
   - Root cause: main paper computed 2.79/0.09 = 31.0 from rounded stds; appendix computed from unrounded stds (~2.793/0.0857 = 32.6). The appendix is internally consistent (CIs also computed from unrounded values).
   - **Fix**: change experiments.tex to "33x" (rounded from 32.6) or "32.6x" to match appendix. Alternatively add "approximately" qualifier.

2. **4-seed Ign-F1 std: reported 0.49 (appendix line 42) vs computed ~0.53 from displayed per-seed values**
   - Per-seed Ign-F1: 44.23, 45.12, 45.11, 44.16; mean=44.655
   - Sample std (n-1=3): 0.532; Population std (n=4): 0.461
   - Reported: 0.49 (matches neither)
   - Likely cause: std computed from higher-precision per-seed values before rounding to 2dp in the table. Not verifiable without raw data.
   - Severity: low (0.49 vs 0.53 is a minor difference; this value is not cited elsewhere in the paper).

## Pending Verification

1. **Evi-F1 -7.7pp (sentence-level CED filtering)**: cited in both analysis.tex and limitations.tex. No supporting table or appendix section provides the underlying experiment data. The value is consistent across both citations but untraceable to a specific result table. If a reviewer asks for the source, there is no table to point to.

2. **14B dev RSFT tax -4.54pp** (tab:scaling): single seed, no appendix table with the underlying with/without evidence Ign-F1 values for 14B RSFT inference-time on dev. The training-time tax is +0.03pp (tab:training_tax), but the inference-time RSFT tax (-4.54pp) lacks a decomposed table entry.
