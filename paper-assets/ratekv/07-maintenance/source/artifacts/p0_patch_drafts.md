# P0 Patch Drafts: D048 Qwen Concentration Update

**Purpose**: Two pre-drafted patch plans for updating the paper once D048 produces Qwen's float32 hires top-5% concentration value. The current paper uses `0.59--0.66` (from buggy bf16 data).

**Placeholder**: `{CONC}` = D048 result (single hires float32 value). If both standard and hires values are available, use `{CONC_LO}--{CONC_HI}`.

---

## Inventory of All Affected Locations

| # | File | Line | Current Text (exact) | What Changes |
|---|------|------|---------------------|--------------|
| L1 | introduction.tex | 43 | `concentration 0.59--0.66, 27.3\% PPL improvement` | Qwen conc value |
| L2 | introduction.tex | 44 | `Yi-1.5 (concentration 0.49) falls just below the $0.50$ threshold` | Threshold framing (Plan B only) |
| L3 | analysis.tex | 12 | `top-5\% concentration 0.59--0.66` | Qwen conc value |
| L4 | analysis.tex | 14 | `concentration of $0.49$---just below the $0.50$ diagnostic threshold` | Threshold framing (Plan B only) |
| L5 | analysis.tex | 18 | `moderate heterogeneity (0.34--0.59)` | Llama range (unchanged unless Llama hires also re-measured) |
| L6 | analysis.tex | 34 | `Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\` | Table: Qwen conc |
| L7 | analysis.tex | 36 | `Llama-3.1-8B$^\dagger$ & 4:1 & 0.34--0.59 ...` | Table: Llama range (unchanged unless re-measured) |
| L8 | analysis.tex | 63 | `Concentration ${>}\,0.50$: non-uniform allocation recommended (Qwen; 27.3\% PPL improvement).` | Threshold (Plan B) |
| L9 | analysis.tex | 64 | `Concentration $0.30$--$0.50$: marginal or negative; ... Llama (0.34--0.59) ... Yi-1.5 (0.49)` | Threshold bands (Plan B) |
| L10 | analysis.tex | 71 | `correctly classify all five models (1 positive, 1 marginal, 3 negative)` | Classification claim (Plan B) |
| L11 | conclusion.tex | 6 | `Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) ... Yi-1.5-9B (0.49)` | Qwen conc, threshold framing |
| L12 | conclusion.tex | 7 | `placing it just below the $0.50$ diagnostic threshold` | Threshold (Plan B) |

---

## Plan A: concentration >= 0.50

**Trigger**: D048 returns {CONC} >= 0.50 (e.g., 0.52).

**Impact**: Claim 3 survives. Update numeric values only. Minor wording adjustments if {CONC} is close to 0.50.

### Sub-case A1: {CONC} >= 0.55

Straightforward value replacement; narrative "highest heterogeneity" remains natural.

### Sub-case A2: 0.50 <= {CONC} < 0.55

Value is close to Yi-1.5 (0.49) and Mistral (0.42). The gap between Qwen and the negatives narrows. Need to strengthen the "concentration + absolute distortion magnitude" framing since concentration alone barely separates.

### Patch Details

**L1 — introduction.tex:43**

Current:
```latex
On our five architectures, the concentration metric---combined with the absolute magnitude of per-head distortion---separates the beneficial case (Qwen, concentration 0.59--0.66, 27.3\% PPL improvement) from cases where non-uniform allocation provides marginal (Llama) or no benefit (Mistral, Yi-1.5, Gemma-2).
```

Replace with:
```latex
On our five architectures, the concentration metric---combined with the absolute magnitude of per-head distortion---separates the beneficial case (Qwen, concentration {CONC}, 27.3\% PPL improvement) from cases where non-uniform allocation provides marginal (Llama) or no benefit (Mistral, Yi-1.5, Gemma-2).
```

If {CONC} < 0.55 (sub-case A2), strengthen emphasis on dual criterion:
```latex
On our five architectures, the concentration metric together with the absolute magnitude of per-head distortion separates the beneficial case (Qwen, concentration {CONC} with Layer-0 distortion $26\times$ the median, 27.3\% PPL improvement) from cases where non-uniform allocation provides marginal (Llama) or no benefit (Mistral, Yi-1.5, Gemma-2).
```

**L2 — introduction.tex:44** — No change needed for Plan A. Yi-1.5 is still below 0.50.

**L3 — analysis.tex:12**

Current:
```latex
Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.
```

Replace with (A1, {CONC} >= 0.55):
```latex
Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration {CONC}), with Layer-0 heads contributing the majority of total 2-bit distortion.
```

Replace with (A2, 0.50 <= {CONC} < 0.55):
```latex
Qwen2.5-7B exhibits the highest effective heterogeneity (top-5\% concentration {CONC}), with Layer-0 heads contributing the majority of total 2-bit distortion and an L0 dominance ratio of $26\times$.
```

Note: "highest effective heterogeneity" adds "effective" because the raw concentration is only marginally above Yi-1.5. The distinction is the spread pattern + absolute magnitude.

**L4 — analysis.tex:14** — No change for Plan A.

**L5 — analysis.tex:18** — No change (Llama range not affected by D048).

**L6 — analysis.tex:34 (table)**

Current:
```latex
Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\
```

Replace with:
```latex
Qwen2.5-7B & 7:1 & {CONC} & $+$5.64 & $+$1.42 & Non-uniform \\
```

**L7 — analysis.tex:36** — No change.

**L8 — analysis.tex:63** — No change (threshold stays 0.50).

**L9 — analysis.tex:64** — No change.

**L10 — analysis.tex:71** — No change (still 5/5 classification).

**L11 — conclusion.tex:6**

Current:
```latex
Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\ 8.47 PPL), while Mistral-7B-v0.3 (0.42), Yi-1.5-9B (0.49), and Gemma-2-9B (0.23) are counterproductive.
```

Replace with:
```latex
Qwen2.5-7B (concentration {CONC}) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\ 8.47 PPL), while Mistral-7B-v0.3 (0.42), Yi-1.5-9B (0.49), and Gemma-2-9B (0.23) are counterproductive.
```

**L12 — conclusion.tex:7** — No change.

### Plan A Summary

- 4 locations change (L1, L3, L6, L11): value swap `0.59--0.66` → `{CONC}`
- If {CONC} is in [0.50, 0.55), add "effective" qualifier and L0 dominance ratio in L1 and L3 for narrative support
- 0 structural changes to claims

---

## Plan B: concentration < 0.50

**Trigger**: D048 returns {CONC} < 0.50 (e.g., 0.42).

**Impact**: The 0.50 threshold no longer separates Qwen (PASS) from the FAIL models. Claim 3 ("top-5% concentration > 0.50 correctly classifies all 5 models") breaks. Three restructuring options follow.

### Current classification landscape with {CONC} < 0.50

| Model | Conc | Outcome | 0.50 threshold says | Correct? |
|-------|------|---------|---------------------|----------|
| Qwen | {CONC} (e.g. 0.42) | PASS (+27.3%) | Negative | **WRONG** |
| Yi-1.5 | 0.49 | FAIL (-1.3%) | Negative | ✓ |
| Llama | 0.34-0.59 | Marginal (+0.2%) | Mixed | — |
| Mistral | 0.42 | FAIL (-0.4%) | Negative | ✓ |
| Gemma-2 | 0.23 | FAIL (-0.3%) | Negative | ✓ |

Problem: Qwen ({CONC}), Mistral (0.42), and Yi-1.5 (0.49) have overlapping concentrations but opposite outcomes. A scalar threshold on concentration alone **cannot** separate them.

### Option B1: Dual-Indicator Diagnostic (L0 dominance + concentration)

**Rationale**: Concentration measures *how much* distortion is concentrated in top heads; L0 dominance measures *where* and *how structured* the heterogeneity is. Qwen's distinguishing feature is a Layer-0 cluster with 26× dominance ratio—a "spread" pattern enabling multi-head differentiated allocation. Yi-1.5 has a single spike (L0 dom=0.07). Mistral has zero signal.

**New diagnostic rule**:
- L0 dominance ratio > 5× AND top-5% concentration > 0.30 → non-uniform recommended
- Otherwise → uniform or marginal

Classification with dual indicator:
| Model | Conc | L0 Dom | Rule says | Outcome | Correct? |
|-------|------|--------|-----------|---------|----------|
| Qwen | {CONC} | 26× | Non-uniform | PASS | ✓ |
| Yi-1.5 | 0.49 | 0.07 | Uniform | FAIL | ✓ |
| Llama | 0.34-0.59 | 高 | Depends on exact value | Marginal | ✓ (if L0 dom ~3-8×) |
| Mistral | 0.42 | ~0 (zero-signal) | Uniform | FAIL | ✓ |
| Gemma-2 | 0.23 | 1.32 | Uniform (conc < 0.30) | FAIL | ✓ |

5/5 accuracy preserved with dual indicator.

**Downside**: Introduces a second metric, adds complexity to the diagnostic framework. Needs exact L0 dominance values for all 5 models.

#### B1 Patch Details

**L1 — introduction.tex:43**

Replace with:
```latex
On our five architectures, the benefit of non-uniform allocation is predicted by a two-indicator diagnostic combining top-5\% concentration with the Layer-0 dominance ratio (\S\ref{sec:heterogeneity}).
Qwen (concentration {CONC}, L0 dominance $26\times$, 27.3\% PPL improvement) is the only architecture exhibiting both high concentration and structured Layer-0 heterogeneity; the remaining models lack one or both indicators.
```

**L2 — introduction.tex:44**

Replace with:
```latex
Yi-1.5 (concentration 0.49, L0 dominance $0.07\times$) is correctly classified as negative: despite having the highest GQA ratio tested (8:1), its heterogeneity is an unexploitable single-outlier spike rather than a structured Layer-0 cluster.
```

**L3 — analysis.tex:12**

Replace with:
```latex
Qwen2.5-7B exhibits the highest effective heterogeneity (top-5\% concentration {CONC}, L0 dominance ratio $26\times$), with Layer-0 heads forming a structured cluster that contributes the majority of total 2-bit distortion.
```

**L4 — analysis.tex:14**

Replace with:
```latex
Yi-1.5-9B has a higher raw concentration ($0.49$) than Qwen but an L0 dominance ratio of only $0.07\times$, reflecting a single extreme outlier (Layer-4 Head-3, contributing 34\% of total delta, CV${=}4.79$) rather than a structured cluster.
This ``spike'' pattern cannot be exploited by MCKP because the freed budget from one 2-bit head is insufficient to upgrade others meaningfully.
```

Note: removes "just below the $0.50$ diagnostic threshold" since 0.50 is no longer the threshold.

**L6 — analysis.tex:34 (table)**

Replace:
```latex
Qwen2.5-7B & 7:1 & {CONC} & $+$5.64 & $+$1.42 & Non-uniform \\
```

Consider adding L0 Dom column to the table:
```latex
\begin{tabular}{lcccccc}
\toprule
Model & GQA & Top-5\% & L0 Dom & $\Delta$ PPL & $\Delta$ PPL & Recommendation \\
 & Ratio & Conc. & Ratio & (Uniform) & (Ours) & \\
\midrule
Qwen2.5-7B & 7:1 & {CONC} & $26\times$ & $+$5.64 & $+$1.42 & Non-uniform \\
Yi-1.5-9B & 8:1 & 0.49 & $0.07\times$ & $+$0.20 & $+$0.30 & Uniform \\
Llama-3.1-8B$^\dagger$ & 4:1 & 0.34--0.59 & {L0_DOM_LLAMA}$\times$ & $+$0.38 & $+$0.36 & Marginal \\
Mistral-7B-v0.3$^\dagger$ & 4:1 & 0.42 & ${\approx}0\times$ & $+$0.10 & $+$0.13 & Uniform \\
Gemma-2-9B & 2:1 & 0.23 & $1.3\times$ & $+$0.13 & $+$0.15 & Uniform \\
\bottomrule
```

**L8 — analysis.tex:63 (diagnostic framework)**

Replace entire diagnostic enumeration (lines 58-67):
```latex
\item Compute the top-5\% concentration and the Layer-0 dominance ratio (mean distortion of Layer-0 heads divided by median distortion of all heads) from the profiling data.
\item Select allocation strategy:
  \begin{itemize}[nosep]
  \item Concentration ${>}\,0.30$ \textbf{and} L0 dominance ${>}\,5\times$: non-uniform allocation recommended. This combination indicates a structured cluster of sensitive heads that MCKP can exploit (Qwen: concentration {CONC}, L0 dominance $26\times$, 27.3\% PPL improvement).
  \item Otherwise: use uniform quantization. High concentration alone is insufficient---Yi-1.5 (0.49, L0 dom $0.07\times$) has a single-outlier spike that MCKP cannot exploit; Mistral (0.42, zero-signal) has near-zero absolute distortion.
  \item Llama (0.34--0.59, L0 dom {L0_DOM_LLAMA}$\times$) is a marginal case with 0.2\% improvement; the dual indicator correctly places it near the decision boundary.
  \end{itemize}
```

**L9 — analysis.tex:64** — Absorbed into L8 replacement above.

**L10 — analysis.tex:71**

Replace:
```latex
The thresholds above are derived from five architectures and correctly classify all five models (1 positive, 1 marginal, 3 negative), but should be validated on a broader set before being treated as general rules.
```
With:
```latex
The dual-indicator diagnostic correctly classifies all five tested models (1 positive, 1 marginal, 3 negative) and should be validated on a broader set before being treated as a general rule.
```

**L11 — conclusion.tex:6**

Replace:
```latex
The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\ 8.47 PPL), while Mistral-7B-v0.3 (0.42), Yi-1.5-9B (0.49), and Gemma-2-9B (0.23) are counterproductive.
```
With:
```latex
The benefit of non-uniform allocation depends on both the concentration and the spatial structure of head sensitivity heterogeneity, as captured by a dual indicator combining top-5\% concentration with the Layer-0 dominance ratio: Qwen2.5-7B (concentration {CONC}, L0 dominance $26\times$) shows large gains, while models lacking structured heterogeneity---Yi-1.5-9B (0.49, L0 dom $0.07\times$), Mistral-7B-v0.3 (0.42, zero-signal), and Gemma-2-9B (0.23)---are counterproductive; Llama-3.1-8B (0.34--0.59) is marginal.
```

**L12 — conclusion.tex:7**

Replace:
```latex
Yi-1.5-9B is a particularly instructive case: despite the highest GQA ratio tested (8:1), its sensitivity heterogeneity is a single-outlier spike rather than a spread, placing it just below the $0.50$ diagnostic threshold.
```
With:
```latex
Yi-1.5-9B is a particularly instructive case: despite the highest GQA ratio tested (8:1) and a higher raw concentration (0.49) than Qwen ({CONC}), its heterogeneity is a single-outlier spike (L0 dominance $0.07\times$) rather than a structured Layer-0 cluster, and the dual-indicator diagnostic correctly identifies it as negative.
```

#### B1 Abstract Patch

**abstract.tex:8** — Currently generic enough ("heterogeneity diagnostic based on the concentration of per-head sensitivity") to survive without change. But if reviewers notice the body uses dual indicator while abstract says "concentration," consider:

Current:
```latex
We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity, validated on five architectures, that can indicate before any allocation whether a given architecture will benefit from non-uniform quantization.
```

Optional replacement:
```latex
We propose a heterogeneity diagnostic based on the concentration and spatial structure of per-head sensitivity, validated on five architectures, that can indicate before any allocation whether a given architecture will benefit from non-uniform quantization.
```

---

### Option B2: Continuous Framing (No Threshold)

**Rationale**: Drop the binary/ternary classification entirely. Frame concentration as one factor among several (absolute distortion magnitude, distribution shape, L0 clustering). The diagnostic becomes qualitative guidance rather than a decision rule.

**Strength**: Most honest framing; doesn't overclaim from n=5 data.
**Weakness**: Weakens Contribution 3 from "diagnostic framework that classifies" to "qualitative observations about heterogeneity patterns." Reviewers may see this as under-specified.

#### B2 Patch Details

**L1 — introduction.tex:43**

Replace with:
```latex
On our five architectures, the benefit of non-uniform allocation correlates with the interaction of three heterogeneity properties: concentration of total distortion in a few heads, absolute distortion magnitude, and whether the sensitive heads form a structured cluster (``spread'') or an isolated outlier (``spike'').
Qwen (concentration {CONC}, 27.3\% PPL improvement) has all three; the remaining models lack at least one.
```

**L2 — introduction.tex:44**

Replace with:
```latex
Yi-1.5 (concentration 0.49) illustrates that concentration alone is insufficient: its heterogeneity resides in a single extreme outlier rather than a cluster, yielding a 1.3\% degradation despite the highest GQA ratio tested (8:1).
```

**L3 — analysis.tex:12**

Replace with:
```latex
Qwen2.5-7B exhibits the most exploitable heterogeneity pattern (top-5\% concentration {CONC}): its sensitive heads form a Layer-0 cluster rather than isolated outliers, and the absolute distortion magnitudes are an order of magnitude above the per-head median.
```

**L4 — analysis.tex:14**

Replace with:
```latex
Yi-1.5-9B has a concentration of $0.49$---comparable to Qwen---but its heterogeneity is concentrated in a single extreme outlier (Layer-4 Head-3, contributing 34\% of total delta, CV${=}4.79$), a ``spike'' pattern that MCKP cannot exploit because the freed budget from one 2-bit head is insufficient to upgrade others meaningfully.
```

**L6 — analysis.tex:34 (table)**

```latex
Qwen2.5-7B & 7:1 & {CONC} & $+$5.64 & $+$1.42 & Non-uniform \\
```

**L8/L9 — analysis.tex:63-64 (diagnostic framework)**

Replace the three-tier guideline with:
```latex
\item Assess allocation strategy based on three heterogeneity properties:
  \begin{itemize}[nosep]
  \item \textbf{Concentration}: higher top-5\% values indicate more distortion in a few heads, but concentration alone does not predict benefit---Yi-1.5 (0.49) and Mistral (0.42) have moderate concentration yet degrade.
  \item \textbf{Distribution shape}: a ``spread'' pattern (multiple sensitive heads, e.g., Qwen's Layer-0 cluster) enables differentiated allocation; a ``spike'' pattern (single outlier, e.g., Yi-1.5) does not.
  \item \textbf{Absolute magnitude}: near-zero absolute distortion (Mistral) leaves no reliable signal for the solver regardless of concentration.
  \end{itemize}
  Non-uniform allocation is recommended only when all three indicators are favorable. Among our five models, only Qwen meets this criterion.
```

**L10 — analysis.tex:71**

Replace with:
```latex
The qualitative diagnostic correctly identifies the single beneficial case among five architectures, but should be formalized with quantitative thresholds and validated on a broader set in future work.
```

**L11 — conclusion.tex:6**

Replace with:
```latex
The benefit of non-uniform allocation depends on the interaction of concentration, distribution shape, and absolute distortion magnitude: Qwen2.5-7B (concentration {CONC}, spread pattern) shows large gains, Llama-3.1-8B (0.34--0.59) is marginal, while Yi-1.5-9B (0.49, spike), Mistral-7B-v0.3 (0.42, zero-signal), and Gemma-2-9B (0.23) are counterproductive.
```

**L12 — conclusion.tex:7**

Replace with:
```latex
Yi-1.5-9B is particularly instructive: despite the highest GQA ratio tested (8:1) and concentration comparable to Qwen, its single-outlier spike pattern makes non-uniform allocation counterproductive, demonstrating that distribution shape, not concentration alone, determines the benefit.
```

**Contribution 3 (introduction.tex:53)**

Current:
```latex
\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on five models spanning beneficial, marginal, and counterproductive outcomes (\S\ref{sec:heterogeneity}).
```

Replace with:
```latex
\item We characterize the heterogeneity conditions under which non-uniform allocation is beneficial---concentration, distribution shape, and absolute distortion magnitude---validated on five models spanning beneficial, marginal, and counterproductive outcomes (\S\ref{sec:heterogeneity}).
```

---

### Option B3: Lower Threshold + Auxiliary Condition

**Rationale**: Keep a threshold-based framework but make it two-stage: concentration > X as a necessary-but-not-sufficient condition, then check distribution shape.

This is essentially B1 reframed. The difference is emphasis: B1 leads with "dual indicator," B3 leads with "concentration threshold + distribution shape qualifier."

**Not recommended** as a separate option—subsumes into B1. Mentioned for completeness.

---

## Recommendation

| Scenario | Recommended Option | Rationale |
|----------|-------------------|-----------|
| {CONC} >= 0.55 | Plan A (direct swap) | Clean separation, minimal edits |
| 0.50 <= {CONC} < 0.55 | Plan A sub-case A2 | Still works but add L0 dominance emphasis |
| 0.40 <= {CONC} < 0.50 | Plan B, Option B1 (dual indicator) | Preserves 5/5 classification claim; structured and reviewable |
| {CONC} < 0.40 | Plan B, Option B1 or B2 | B1 if L0 dom data is solid; B2 if we want maximum safety |

**Why B1 over B2**: B1 preserves a concrete, falsifiable diagnostic claim (Contribution 3) which is much stronger for reviewers. B2 is the safe fallback if L0 dominance data has issues.

**Required data for B1 not yet in hand**: Exact L0 dominance ratio for Llama (task says "较高" but no number). Before applying B1, need this value from existing profiling data.

---

## Checklist Before Applying Any Patch

- [ ] D048 result available: {CONC} = ???
- [ ] Decision: Plan A or Plan B?
- [ ] If Plan B1: verify L0 dominance values for all 5 models from profiling artifacts
- [ ] Apply patches to .tex files
- [ ] Recompile LaTeX, check no broken references
- [ ] Verify Table 5 (heterogeneity table) renders correctly
- [ ] Grep for any remaining "0.59" or "0.66" in .tex files
- [ ] If Plan B: update abstract.tex:8 if desired
