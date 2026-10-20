# fix bootstrap ci and classifier

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bootstrap-ci-and-classifier_20260520T143238_result.json`
- **Structured JSON:** [`3c3f9fcc1cb87d3e4c7a.json`](../../sessions/3c/3c3f9fcc1cb87d3e4c7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both bugs fixed and results verified. Here are the deliverables:

---

## 1. Code Diff Description

**Bug #1 — n=2 Bootstrap CI degeneracy**: `bootstrap_mean_ci()` now returns a 4-tuple `(mean, ci_low, ci_high, method)`. For n≥3: BCa bootstrap (`"boot"`). For n=2: t-distribution CI with df=1 (`"t"`). For n=1: point estimate (`"pt"`). All callers updated to unpack 4 values. CI strings annotated with `(boot)`/`(t)`/`(pt)`. LaTeX table marks n=2 CIs with `$^t$`.

**Bug #2 — V-recovery misclassification**: Added dip-detection logic before the Immune check in `classify_pattern()`. If any middle dosage (d005/d025/d050) drops ≥2pp below baseline and d100 recovers ≥50% of the dip depth, pattern is classified as `V-recovery`.

**Additional fix**: Moved `global N_BOOTSTRAP` declaration to top of `main()` to fix `SyntaxError`.

## 2. Full Bootstrap Table Output

| Family | n | Baseline | Δ(d100) | 95% CI | Pattern |
|--------|---|----------|---------|--------|---------|
| Phi-4 | 1 | 76.38% | -0.17pp | [-0.17, -0.17](pt) | Immune |
| Qwen2.5-14B | 2 | 69.05% | -11.05pp | [-32.41, +10.30](t) | U-collapse |
| Qwen2.5-7B | 1 | 66.11% | -1.78pp | [-1.78, -1.78](pt) | **V-recovery** |
| Gemma-2-9B | 2 | 63.85% | +2.62pp | [-11.81, +17.06](t) | Benefit-sat† |
| OLMo-2-7B | 3 | 54.93% | +1.35pp | [-0.55, +2.60](boot) | Benefit-sat† |

## 3. bootstrap_table.tex

```latex
\begin{table}[t]
\centering
\caption{Triple-seed bootstrap analysis of MMLU dose-response patterns.}
\label{tab:bootstrap-mmlu}
\small
\begin{tabular}{lccccc}
\toprule
Family & Baseline (\%) & $\Delta$(d100) & 95\% CI & Pattern & $\bar{\rho}$ \\
\midrule
Phi-4 & 76.38 & -0.17 & [-0.17, -0.17] & Immune & --- \\
Qwen2.5-14B & 69.05 & -11.05 & [-32.41, +10.30]$^t$ & U-collapse & 0.80 \\
Qwen2.5-7B & 66.11 & -1.78 & [-1.78, -1.78] & V-recovery & --- \\
Gemma-2-9B & 63.85 & +2.62 & [-11.81, +17.06]$^t$ & Benefit-sat$^\dagger$ & 0.30 \\
OLMo-2-7B & 54.93 & +1.35 & [-0.55, +2.60] & Benefit-sat$^\dagger$ & 0.03 \\
\bottomrule
\end{tabular}
\vspace{1mm}
\raggedright\footnotesize
$\Delta$(d100) = acc(d100) $-$ acc(d000) in percentage points.
CI via BCa bootstrap (10{,}000 resamples) for $n \geq 3$;
$t$-distribution ($\mathrm{df}=1$) for $n=2$, marked $^t$.
$\bar{\rho}$: mean pairwise Spearman $\rho$ across seeds.
$^\dagger$Pattern inconsistent across seeds.
\end{table}
```

## 4. Pattern Classification Before vs After

| Family | Before | After | Changed? |
|--------|--------|-------|----------|
| Phi-4 (s42) | Immune | Immune | No |
| Qwen2.5-14B (s42) | U-collapse | U-collapse | No |
| Qwen2.5-14B (s123) | U-collapse | U-collapse | No |
| **Qwen2.5-7B (s42)** | **Immune** | **V-recovery** | **Yes** |
| Gemma-2-9B (s42) | Benefit-sat | Benefit-sat | No |
| Gemma-2-9B (s123) | V-recovery | V-recovery | No |
| OLMo-2-7B (s42) | Benefit-sat | Benefit-sat | No |
| OLMo-2-7B (s123) | Immune | Immune | No |
| OLMo-2-7B (s0) | Benefit-sat | Benefit-sat | No |

Qwen2.5-7B s42 correctly reclassified from Immune → V-recovery (middle dosages dip then recover at d100). n=2 CIs now use t-distribution and are visibly wider (e.g., Qwen2.5-14B: [-32.41, +10.30] vs previously degenerate). Other families unaffected.

---
