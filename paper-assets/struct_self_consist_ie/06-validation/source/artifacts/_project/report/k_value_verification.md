# Holm-Bonferroni k Value Verification

## 1. Table 13 Selection Family — Complete Row Enumeration

Table 13 (`\label{tab:holm_family}`, appendix.tex line 324) lists **19 tests** under the *Selection* family:

| # | Test Description | Raw p |
|---|-----------------|-------|
| 1 | SciERC NER LP selection (N=8, Qwen, Table 3) | 0.290 |
| 2 | SciERC NER SJ selection (N=8, Qwen, Table 3) | 0.670 |
| 3 | SciERC NER FK selection (N=8, Qwen, Table 3) | 0.790 |
| 4 | WNUT-17 LP selection (N=8, Qwen) | 0.720 |
| 5 | CoNLL LP selection (N=8, Qwen) | 1.0 |
| 6 | Few-NERD LP selection (N=8, Qwen, 3-seed) | <.001 |
| 7 | SciERC NER SJ selection (N=8, LLaMA-3B) | 0.175 |
| 8 | SciERC NER LP selection (N=32, Qwen) | 0.091 |
| 9 | SciERC NER FK selection (N=32, Qwen) | 0.101 |
| 10 | SciERC NER SJ selection (N=32, Qwen) | 0.244 |
| 11 | SciERC NER EM selection (N=32, Qwen) | 0.355 |
| 12 | SciERC NER VC selection (N=32, Qwen) | 1.0 |
| 13 | SciERC RE LP selection (N=16, 4B, Fisher) | 0.058 |
| 14 | SciERC RE VC selection (N=16, 4B, Fisher) | 0.973 |
| 15 | SciERC RE FK selection (N=16, 4B, Fisher) | 0.985 |
| 16 | SciERC RE SJ selection (N=16, 4B, Fisher) | 0.993 |
| 17 | SciERC RE EM selection (N=16, 4B, Fisher) | 0.999 |
| 18 | SciERC LP selection, non-tied subset (ε=0.05) | 0.004 |
| 19 | Few-NERD LP selection (N=8, LLaMA, 3-seed) | <.001 |

Count: **19 rows exactly.** The abstract claim "selection family k=19" matches the table as written.

## 2. Source of Discrepancy: 2 Tests Misclassified in "Other"

Tests #56 and #57, currently in the **Other** family, are **conditional LP selection** tests:

| # | Family (current) | Test Description | Raw p |
|---|-----------------|-----------------|-------|
| 56 | Other | SciERC LP favorable subset (+2.47 pp) | 0.015 |
| 57 | Other | CoNLL LP favorable subset (−1.78 pp) | <.001 |

These test "does LP selection beat greedy on a specific subset?" — the same type of test as **#18** (SciERC LP selection, non-tied subset, ε=0.05), which IS in the Selection family.

**The inconsistency:** #18 (conditional LP selection → Selection) vs #56, #57 (conditional LP selection → Other). A reviewer examining Table 13 would reasonably count all three as selection tests: **19 + 2 = 21**.

Source: `\subsection{Conditional Decomposition of LP Selection}` (appendix.tex line 1910), Table `tab:conditional_decomp` (line 1919).

## 3. All Locations Citing k=19

| File | Line | Context |
|------|------|---------|
| `sections/abstract.tex` | 9 | "Holm-adjusted $p{=}0.019$, selection family $k{=}19$" |
| `sections/single_signal.tex` | 41 | "Holm $p_{\text{adj}}{=}0.019$, selection family $k{=}19$" |
| `sections/introduction.tex` | 21 | "Holm $p_{\text{adj}}{=}0.019$, selection family $k{=}19$" |
| `sections/experiments_main.tex` | 119 | footnote: "selection $k{=}19$, construction $k{=}10$, signal $k{=}9$" |

## 4. Recalculated Holm-Bonferroni with k=21

### Sorted raw p-values (21 tests)

| Rank | Test | Raw p |
|------|------|-------|
| 1 | #57 CoNLL LP favorable subset | <.001 |
| 2 | #6 Few-NERD LP (Qwen, 3-seed) | <.001 |
| 3 | #19 Few-NERD LP (LLaMA, 3-seed) | <.001 |
| 4 | #18 SciERC LP non-tied subset | 0.004 |
| 5 | #56 SciERC LP favorable subset | 0.015 |
| 6 | #13 SciERC RE LP (N=16, 4B) | 0.058 |
| 7 | #8 SciERC NER LP (N=32) | 0.091 |
| 8–21 | (remaining 14 tests) | 0.101–1.0 |

### Holm-Bonferroni adjusted p-values (k=21)

Formula: p_adj(i) = max_{j=1..i} [ p(j) × (k − j + 1) ]

Assuming p_raw ≈ 0.001 for all three "<.001" tests:

| Rank | Test | k=19 p_adj | k=21 p_adj | Significant? |
|------|------|-----------|-----------|-------------|
| 1 | CoNLL LP favorable | — (was in Other) | 0.001 × 21 = **0.021** | ✓ (α=0.05) |
| 2 | Few-NERD LP Qwen | **0.019** | max(0.021, 0.001 × 20) = **0.021** | ✓ |
| 3 | Few-NERD LP LLaMA | **0.019** | max(0.021, 0.001 × 19) = **0.021** | ✓ |
| 4 | SciERC LP non-tied | 0.068 | max(0.021, 0.004 × 18) = **0.072** | ✗ |
| 5 | SciERC LP favorable | — (was in Other) | max(0.072, 0.015 × 17) = **0.255** | ✗ |
| 6+ | All remaining | ≥ 0.928 | ≥ 0.928 | ✗ |

### Key Result

**No previously significant result becomes non-significant.** The Few-NERD LP selection claim (the paper's main positive selection result) remains significant:
- Old: p_adj = 0.019 (k=19)
- New: p_adj ≈ 0.021 (k=21)

The change is small (+0.002) and stays well under α=0.05.

If the exact raw p for the three "<.001" tests differ (e.g., CoNLL favorable has p=0.0005), the adjustment is even smaller (p_adj for Few-NERD LP ≈ 0.020).

## 5. Correction Recommendations

### Option A: Reclassify #56, #57 into Selection (recommended)

1. Move tests #56, #57 from "Other" to "Selection" in Table 13
2. Update all 4 locations from k=19 → k=21 and p_adj=0.019 → p_adj≈0.021
3. Update experiments_main.tex footnote: "selection k=21"
4. Recompute exact p_adj using precise raw p-values from bootstrap code
5. Update "Other" family count from k=6 to k=4

### Option B: Justify the current classification

Argue that #56/#57 are post-hoc subgroup analyses (not pre-registered selection tests), while #18 is a mechanistically motivated partition (LP compression). This is defensible but requires explicit justification in the text.

### Option C: Move #18 to "Other" as well (k stays at 19, but minus #18 = 18)

Less recommended — makes the Selection family less complete.

## 6. Additional Notes

- Test #53 ("RE LP selection reversal, free-form, 4-seed") is also arguably selection-type but tests the effect of decoding format, not selection itself. Excluding it from Selection is more defensible.
- LLaMA CoNLL N=16 VC/LP results (appendix line 266) report explicit p-values (p=0.003–0.027) but are NOT in Table 13 at all. This is a separate omission issue — these tests should arguably be added to the global enumeration (would increase global k beyond 57).
- DALS Few-NERD (appendix line 1900, p<.001) is also absent from Table 13.
