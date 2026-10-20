# Paper Numerical Consistency Report

Generated: 2026-05-14

---

## Critical Issues

### 1. Cohen's d: Introduction vs Table 3 (Cross-Section Mismatch)

**introduction.tex:15** uses Qwen Cohen's d values that contradict **results.tex Table 3 (tab:cohens-d)**:

| Sparsity | intro.tex | Table 3 (results.tex:186-189) |
|----------|-----------|-------------------------------|
| s=0.15   | d=0.37    | d=0.28                        |
| s>=0.20  | d>=0.72   | d=0.55 (s=0.20)               |

The intro's values (0.37, >=0.72) match the task-spec ground truth but **not** the paper's own results table. Meanwhile abstract.tex:10 ("d >= 0.55") and conclusion.tex:16 ("d >= 0.55") are consistent with Table 3 but disagree with the introduction.

**Recommendation**: Determine which Cohen's d calculation is canonical (per-problem paired d_z). If task-spec values (0.37, 0.72, 1.23, 1.44) are correct, update Table 3 and all references. If Table 3 is correct, update introduction.tex lines 15.

### 2. Cohen's d: Task-Spec Values vs Paper Values (Systematic Discrepancy)

The task spec defines ground-truth Cohen's d (paired, per-problem) as:

| Model    | s=0.15 | s=0.20 | s=0.25 | s=0.30 |
|----------|--------|--------|--------|--------|
| DeepSeek | 0.61   | 0.73   | 0.95   | 1.13   |
| Qwen     | 0.37   | 0.72   | 1.23   | 1.44   |

The paper (Table 3, cohens_d_bf16.json) has:

| Model    | s=0.15 | s=0.20 | s=0.25 | s=0.30 |
|----------|--------|--------|--------|--------|
| DeepSeek | 0.44   | 0.52   | 0.68   | 0.80   |
| Qwen     | 0.28   | 0.55   | 0.89   | 1.02   |

These are entirely different value sets. Affected locations:
- **abstract.tex:7** — "d growing from 0.44 to 0.80"
- **introduction.tex:14** — "d=0.44 to d=0.80"
- **results.tex:186-189** — Table 3 all values
- **results.tex:124** — "DeepSeek: 0.44 -> 0.80; Qwen: 0.28 -> 1.02"
- **results.tex:195-197** — inline d references
- **conclusion.tex:10** — "d=0.44 to d=0.80"
- **discussion.tex:29** — comment references cohens_d_bf16.json values

**Recommendation**: Verify which computation is correct. If task-spec values are ground truth, update all Cohen's d references throughout the paper.

### 3. Undefined Reference: \ref{sec:experiments}

**introduction.tex:27, 28, 33** reference `\S\ref{sec:experiments}`, but no `\label{sec:experiments}` exists in any active file. The results section is labeled `sec:results` (results.tex:3).

This will produce "??" in compiled LaTeX.

**Fix**: Replace `\ref{sec:experiments}` with `\ref{sec:results}` in introduction.tex (3 occurrences).

### 4. Duplicate \label Definitions: eq:ii and eq:gradient

Both **background.tex** and **methodology.tex** define:
- `\label{eq:ii}` (background.tex:58, methodology.tex:62)
- `\label{eq:gradient}` (background.tex:81, methodology.tex:69)

background.tex line 3 comment explicitly states: "Methodology.tex should reference these via \eqref rather than redefining."

**Fix**: In methodology.tex, replace the equation environments for II and G with `\eqref{eq:ii}` and `\eqref{eq:gradient}` references, removing the duplicate labels.

### 5. Methodology "p < 0.0001" Overstated

**methodology.tex:86**: "All tests yield $p < 0.0001$ at every sparsity level"

But the permutation test at s=0.15 has Bonferroni-corrected **p=0.0032** (results.tex Table tab:permutation, line 157). Even uncorrected, this is ~0.0008, not < 0.0001.

**Fix**: Change to "All tests yield $p < 0.005$" or "All tests yield $p_{\text{Bonf}} < 0.005$" to match the actual results.

---

## Moderate Issues

### 6. Paired vs Unpaired median_diff in Body Text

Per task constraints, body text (intro, abstract, conclusion) should use **paired** median_diff values. Currently all use **unpaired** (segment-level):

| Section | Currently Uses (unpaired) | Should Use (paired) |
|---------|---------------------------|---------------------|
| abstract.tex:7 | 0.39 ... 14.59 | 0.32 ... 9.94 |
| introduction.tex:14 | 0.39 ... 14.59 | 0.32 ... 9.94 |
| conclusion.tex:8 | 0.39--14.59 | 0.32--9.94 |
| discussion.tex:29 | 0.39 -> 14.59 | 0.32 -> 9.94 |

Note: Tables 1 (tab:aggregate-ii) and 2 (tab:main-results) correctly use unpaired and are labeled accordingly. Table 3 (tab:cohens-d) correctly uses paired. The issue is that **inline text** references the unpaired values when it should reference paired.

**Recommendation**: Either update inline text to use paired values, or explicitly annotate that the inline statistics use segment-level (unpaired) medians. If switching to paired, the full DS sequence is 0.32 -> 1.15 -> 3.97 -> 9.94 and QW sequence is 0.048 -> 0.208 -> 1.109 -> 2.619.

### 7. Self-Reference in discussion.tex

**discussion.tex:54**: "the entropy redistribution component is model-dependent (\S\ref{sec:discussion})" references its own section. Should likely reference `\S\ref{sec:entropy-redistribution}` or `\S\ref{sec:analysis}`.

### 8. Unreferenced Figures

Two figures are defined but never `\ref{}`'d in the text:
- **fig:cross-model** (results.tex:132) — Figure 5, cross-model comparison
- **fig:permtest-forest** (results.tex:171) — Figure 4, forest plot

**Fix**: Add `Figure~\ref{fig:cross-model}` and `Figure~\ref{fig:permtest-forest}` references in the surrounding text.

---

## Confirmed Consistent

### DeepSeek Unpaired median_diff
Values 0.39 / 1.48 / 7.16 / 14.59 are consistent across:
- abstract.tex:7 (endpoints only)
- introduction.tex:14 (endpoints only)
- results.tex Table 1 (tab:aggregate-ii, line 29)
- results.tex Table 2 (tab:main-results, lines 54-63)
- results.tex Table cross-model (line 118)
- conclusion.tex:8 (range)
- discussion.tex:29 (full sequence)

### DeepSeek Paired median_diff
Values 0.32 / 1.15 / 3.97 / 9.94 are consistent in results.tex Table 3 (tab:cohens-d, lines 186-189).

### Qwen Unpaired median_diff
Values 0.04 / 0.23 / 1.27 / 2.94 are consistent across:
- results.tex Table cross-model (line 119)
- discussion.tex:29 (0.039/0.235/1.268/2.943 — precision consistent)

### Qwen Paired median_diff
Values 0.05 / 0.21 / 1.11 / 2.62 in results.tex Table 3 (lines 186-189), matching task spec 0.048/0.208/1.109/2.619 with rounding.

### Severity Gradient G
Values 69 / 103 / 222 / 274 are consistent across:
- results.tex Table 2 (lines 54-63)
- results.tex Figure 1 caption (line 74)
- analysis.tex:5
- discussion.tex:9

### Random 7/8 FAIL
Consistent across abstract.tex:8, introduction.tex:16, discussion.tex:21, conclusion.tex:8. Single exception (Qwen s=0.30, p=0.012, d=-0.04) correctly noted in all locations.

### Crossover at s=0.25
imp_high=0.032, rand_high=0.818, imp_low=7.196, rand_low=1.363 — consistent across:
- abstract.tex:9
- results.tex:84 and Table 2 (line 60-61)
- discussion.tex:13
- conclusion.tex:12

### Bonferroni-Corrected Permutation p
"p < 0.005 at all four levels" — consistent with Table tab:permutation (s=0.15: 0.0032, rest: <0.001).

### Qwen s=0.15 Marginal Annotation
"marginal at s=0.15, CI includes zero" correctly noted in:
- results.tex Table 3 footnote (line 191)
- results.tex:196
- introduction.tex:15 (though d value differs — see Issue #1)

### No Cross-Architecture Claims
All cross-model references correctly state "Qwen2ForCausalLM architecture" / "same backbone architecture":
- results.tex:103, 135
- discussion.tex:70-74
- conclusion.tex:22

### results_5_1.tex (Old fp16)
Not \input'd or \include'd by any active file. Contains extensive PENDING-BF16 markers — correctly quarantined.

### No PENDING/fp16/Placeholder in Active Files
Grep confirms zero occurrences of PENDING, fp16, or placeholder in the 9 active tex files. All such markers are confined to results_5_1.tex and the _hash backup files.

### Spearman/Gradient Permutation
rho=1.0 and p=0.043 consistent across abstract.tex:10, results.tex:124, conclusion.tex:16, discussion.tex:25.

### Per-Problem Concordance
mean rho=-0.11, p=0.926 consistent in results.tex:124.

---

## Summary

| Category | Count |
|----------|-------|
| Critical (affects correctness) | 5 |
| Moderate (presentation/completeness) | 3 |
| Confirmed consistent | 14 |

**Priority fix order**: #3 (undefined ref — trivial fix) > #4 (duplicate labels — trivial fix) > #5 (p-value overstatement) > #1 (Cohen's d cross-section) > #2 (Cohen's d ground truth) > #6 (paired/unpaired policy) > #7-8 (minor).
