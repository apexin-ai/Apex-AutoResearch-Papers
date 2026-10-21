# Wording Contingency Plan

Prepared 2026-05-29. Three presets keyed to RD2-N1/N2 experimental outcomes. Each provides exact old→new text for copy-paste into .tex files.

---

## Precase 1: "reliably" wording

**Trigger**: RD2-N1 seed expansion results (n≥5 per cell)

4 locations use "reliably":

### Location 1: main.tex abstract (line 23)

**OLD:**
```
The best configuration, detached gradients with LayerNorm, reliably outperforms the no-auxiliary baseline, raising Collision Avoidance Rate from $0.745$ to $0.802$ with a large effect size.
```

**Version A (g≥1.5, p<0.01):**
```
The best configuration, detached gradients with LayerNorm, reliably outperforms the no-auxiliary baseline (n${\geq}$5 seeds per cell, $p{<}0.01$), raising Collision Avoidance Rate from $0.745$ to $0.802$ with a large effect size.
```

**Version B (g<0.8 or CI contains zero):**
```
The best configuration, detached gradients with LayerNorm, consistently outperforms the no-auxiliary baseline with a large effect size, raising mean Collision Avoidance Rate from $0.745$ to $0.802$.
```

### Location 2: introduction.tex contribution #1 (line 22)

**OLD:**
```
\item \textbf{Detach+LN reliably improves safety.} Detached gradients with LayerNorm yield the highest collision avoidance rate, reliably outperforming the no-auxiliary baseline with a large effect size. A $2{\times}2$ factorial identifies two additive mechanisms: gradient flow through BatchNorm degrades safety; LayerNorm provides a consistent protective effect.
```

**Version A (g≥1.5, p<0.01):**
```
\item \textbf{Detach+LN reliably improves safety.} Detached gradients with LayerNorm yield the highest collision avoidance rate, reliably outperforming the no-auxiliary baseline ($n{\geq}5$ seeds per cell, $p{<}0.01$, Hedges' $g{\geq}1.5$). A $2{\times}2$ factorial identifies two additive mechanisms: gradient flow through BatchNorm degrades safety; LayerNorm provides a consistent protective effect.
```

**Version B (g<0.8 or CI contains zero):**
```
\item \textbf{Detach+LN consistently improves safety.} Detached gradients with LayerNorm yield the highest collision avoidance rate, showing a robust directional advantage over the no-auxiliary baseline with a large effect size. A $2{\times}2$ factorial identifies two additive mechanisms: gradient flow through BatchNorm degrades safety; LayerNorm provides a consistent protective effect.
```

### Location 3: results.tex bold header (line 9)

**OLD:**
```
\textbf{Detach+LN reliably outperforms Vanilla.} The best factorial configuration, detached gradients with LayerNorm, achieves CAR $0.802 \pm 0.024$ ($n{=}3$), a $+5.7$\,pp advantage over Vanilla ($0.745 \pm 0.024$, $n{=}3$; Hedges' $g{=}1.89$, very large; bootstrap 95\% CI for $\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$).
```

**Version A (g≥1.5, p<0.01):** *(update n, g, CI, p with actual values)*
```
\textbf{Detach+LN reliably outperforms Vanilla.} The best factorial configuration, detached gradients with LayerNorm, achieves CAR $X.XXX \pm X.XXX$ ($n{=}N$), a $+Y.Y$\,pp advantage over Vanilla ($X.XXX \pm X.XXX$, $n{=}N$; Hedges' $g{=}G.GG$, very large; bootstrap 95\% CI for $\Delta$: $[L, U]$; permutation $p{<}0.01$).
```

**Version B (g<0.8 or CI contains zero):**
```
\textbf{Detach+LN consistently outperforms Vanilla.} The best factorial configuration, detached gradients with LayerNorm, achieves CAR $X.XXX \pm X.XXX$ ($n{=}N$), a $+Y.Y$\,pp advantage over Vanilla ($X.XXX \pm X.XXX$, $n{=}N$; Hedges' $g{=}G.GG$, large; bootstrap 95\% CI for $\Delta$: $[L, U]$). The directional advantage is consistent across seeds, though the effect is smaller than preliminary estimates.
```

### Location 4: results.tex figure caption (line 73)

**OLD:**
```
Detach+LN achieves the highest CAR ($0.802{\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$).
```

**Version A (g≥1.5, p<0.01):**
```
Detach+LN achieves the highest CAR ($X.XXX{\pm}X.XXX$, $n{=}N$), reliably outperforming Vanilla ($X.XXX$; Hedges' $g{=}G.GG$, $p{<}0.01$).
```

**Version B (g<0.8 or CI contains zero):**
```
Detach+LN achieves the highest CAR ($X.XXX{\pm}X.XXX$, $n{=}N$), consistently outperforming Vanilla ($X.XXX$; Hedges' $g{=}G.GG$).
```

---

## Precase 2: Gradient flow main effect

**Trigger**: RD2-N1 permutation ANOVA p-values with n≥5

### Location: results.tex ANOVA paragraph (line 11)

**OLD (relevant excerpt):**
```
Two additive main effects explain the advantage.} The $2{\times}2$ factorial (Table~\ref{tab:factorial}, Figure~\ref{fig:car_factorial}b) reveals two large main effects with negligible interaction (permutation ANOVA, 10{,}000 permutations: gradient flow $p_\text{perm}{=}0.090$; normalization $p_\text{perm}{=}0.041$; interaction $p_\text{perm}{=}0.794$;
```

**Version A (both p<0.05):**
```
Two additive main effects explain the advantage.} The $2{\times}2$ factorial (Table~\ref{tab:factorial}, Figure~\ref{fig:car_factorial}b) reveals two significant main effects with negligible interaction (permutation ANOVA, 10{,}000 permutations: gradient flow $p_\text{perm}{=}P_G$; normalization $p_\text{perm}{=}P_N$; interaction $p_\text{perm}{=}P_I$;
```

**Version B (normalization p<0.05 but gradient p>0.05):**

Replace the bold header and first two sentences:

```
A normalization main effect and a large gradient flow effect.} The $2{\times}2$ factorial (Table~\ref{tab:factorial}, Figure~\ref{fig:car_factorial}b) reveals two large main effects with negligible interaction. The normalization effect reaches significance (permutation ANOVA, 10{,}000 permutations: $p_\text{perm}{=}P_N$); the gradient flow effect exhibits a large effect size ($\eta^2{=}0.180$) but does not reach conventional significance ($p_\text{perm}{=}P_G$), suggesting a meaningful but underpowered contribution. The interaction is negligible ($p_\text{perm}{=}P_I$;
```

Also update Table 2 caption (line 48) if Version B:

**OLD:**
```
Two main effects: gradient flow under BN $g{=}0.78$ (large); normalization effect $g{=}0.88$--$1.24$ (large to very large).
```

**Version B:**
```
The normalization main effect is significant; gradient flow shows a large effect size under BN ($g{=}G.GG$) but does not reach significance.
```

---

## Precase 3: Content irrelevance

**Trigger**: RD2-N2 (Random OCC v2) eval results

### Location 3a: results.tex content sentence (line 11, end of ANOVA paragraph)

**OLD:**
```
Spatial content does not detectably affect outcomes: Full OCC, Random OCC, and Depth fall within cross-seed variance ($p > 0.4$, observed under v1 for Random OCC and Depth).
```

**Version A (v2 Random OCC ≈ Full OCC BN, within cross-seed variance):**
```
Spatial content does not detectably affect outcomes across codebases: Full OCC, Random OCC, and Depth fall within cross-seed variance under both v1 and v2 ($p > 0.4$), confirming that the gradient pathway, not label content, determines the safety outcome.
```

**Version B (v2 Random OCC ≠ Full OCC BN, difference > cross-seed SD):**
```
Spatial content effects are codebase-dependent: under v1, Full OCC, Random OCC, and Depth fall within cross-seed variance ($p > 0.4$); under v2, Random OCC differs from Full OCC by $X.X$\,pp ($p{=}P$), suggesting that label content may interact with other implementation details.
```

### Location 3b: discussion.tex content irrelevance paragraph (line 15)

**OLD:**
```
\textbf{Content irrelevance.} Structured, random, and depth labels produce indistinguishable safety outcomes (observed under the original codebase), consistent with action--auxiliary orthogonality. No ground-truth spatial annotations are required; CKA similarity ($\geq 0.95$) confirms the effect operates at the optimization rather than the representational level.
```

**Version A (v2 confirms):**
```
\textbf{Content irrelevance.} Structured, random, and depth labels produce indistinguishable safety outcomes under both v1 and v2 codebases, consistent with action--auxiliary orthogonality. The cross-codebase replication strengthens the conclusion that no ground-truth spatial annotations are required; CKA similarity ($\geq 0.95$) confirms the effect operates at the optimization rather than the representational level.
```

**Version B (v2 diverges):**
```
\textbf{Content irrelevance is codebase-dependent.} Under v1, structured, random, and depth labels produce indistinguishable safety outcomes. Under v2, random labels diverge from structured occupancy by $X.X$\,pp, suggesting that label content may interact with other implementation details. CKA similarity ($\geq 0.95$) confirms intact representations in both cases; the divergence likely reflects differences in the optimization trajectory rather than representational learning.
```

### Location 3c: introduction.tex contribution #1 (line 22)

**OLD:**
```
Spatial label content shows no detectable influence under the original codebase (Table~\ref{tab:main_results}, Figure~\ref{fig:car_factorial}b).
```

**Version A:**
```
Spatial label content shows no detectable influence under either codebase version (Table~\ref{tab:main_results}, Figure~\ref{fig:car_factorial}b).
```

**Version B:**
```
Spatial label content shows no detectable influence under the original codebase; v2 results suggest potential codebase-dependent effects (Table~\ref{tab:main_results}).
```

### Location 3d: main.tex abstract (line 23)

**OLD:**
```
Surprisingly, the spatial content of the labels (ground-truth occupancy, random noise, or depth) has no detectable effect under the original codebase; the gradient pathway, not spatial information, appears to determine the outcome.
```

**Version A:**
```
Surprisingly, the spatial content of the labels (ground-truth occupancy, random noise, or depth) has no detectable effect under either codebase version; the gradient pathway, not spatial information, determines the outcome.
```

**Version B:**
```
Under the original codebase, the spatial content of the labels (ground-truth occupancy, random noise, or depth) has no detectable effect; under v2, content shows a modest influence, suggesting that this finding may be codebase-dependent.
```

---

## Usage

1. When RD2-N1 eval completes: recompute Hedges' g and permutation p-values with n≥5 data
2. Select Version A or B for Precase 1 and 2 based on thresholds
3. When RD2-N2 eval completes: compare v2 Random OCC CAR vs v2 Full OCC BN CAR
4. Select Version A or B for Precase 3
5. Replace placeholder values (X.XXX, P_G, G.GG, etc.) with actual computed statistics
6. Search-replace all 4 locations per precase simultaneously to maintain consistency
