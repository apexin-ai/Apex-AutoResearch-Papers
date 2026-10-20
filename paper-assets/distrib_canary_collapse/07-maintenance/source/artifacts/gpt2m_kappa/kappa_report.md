# Inter-Method Agreement κ: GPT-2 Medium (α=1.0, seed=42, T=11)

**Source:** `gen_wiki_gpt2m_a100_s42_v3/report/five_method_leadlag.md`
**Date:** 2026-05-15

---

## 1. Binary Significance Matrix (5 Methods × 12 Pairs)

Criteria: Naive |r|>0.9; Diff p_fdr<0.05; Onset Δgen>0; Perm.G p_fdr<0.05; TY p_fdr<0.05.

### Forward (Canary → Diversity)

| Pair | Naive | Diff | Onset | Perm.G | TY | Sum |
|------|:-----:|:----:|:-----:|:------:|:--:|:---:|
| entropy→d1 | 1 | 1 | 1 | 1 | 0 | 4/5 |
| entropy→d2 | 1 | 1 | 1 | 1 | 0 | 4/5 |
| entropy→d3 | 1 | 1 | 1 | 1 | 0 | 4/5 |
| ece→d1     | 1 | 1 | 1 | 1 | 0 | 4/5 |
| ece→d2     | 1 | 1 | 1 | 1 | 0 | 4/5 |
| ece→d3     | 1 | 1 | 1 | 1 | 0 | 4/5 |

### Reverse (Diversity → Canary)

| Pair | Naive | Diff | Onset | Perm.G | TY | Sum |
|------|:-----:|:----:|:-----:|:------:|:--:|:---:|
| d1→entropy | 1 | 0 | 0 | 0 | 0 | 1/5 |
| d2→entropy | 1 | 0 | 0 | 0 | 0 | 1/5 |
| d3→entropy | 1 | 0 | 0 | 0 | 0 | 1/5 |
| d1→ece     | 1 | 0 | 0 | 1 | 0 | 2/5 |
| d2→ece     | 1 | 0 | 0 | 1 | 0 | 2/5 |
| d3→ece     | 1 | 0 | 0 | 1 | 0 | 2/5 |

### Method Sig Rates

| Method | Sig/Total | Rate |
|--------|:---------:|:----:|
| Naive xcorr | 12/12 | 1.000 |
| Diff xcorr  |  6/12 | 0.500 |
| Onset       |  6/12 | 0.500 |
| Perm. Granger | 9/12 | 0.750 |
| TY Granger  |  0/12 | 0.000 |

---

## 2. Fleiss' κ (Multi-Rater Agreement)

| Scope | Fleiss' κ | P̄ | P_e | Interpretation |
|-------|:---------:|:---:|:---:|:--------------:|
| All 12 pairs | **0.091** | 0.550 | 0.505 | Slight |
| Forward 6    | −0.250 | 0.600 | 0.680 | Below chance (degenerate) |
| Reverse 6    | −0.190 | 0.500 | 0.580 | Below chance (degenerate) |

Forward/reverse subsets yield negative κ because within each direction the rating pattern is near-uniform across items (all forward = 4/5, reverse varies only slightly), so observed agreement falls below the inflated chance baseline.

---

## 3. Pairwise Cohen's κ

| Method Pair | κ | p_o | p_e | Note |
|-------------|:-:|:---:|:---:|:----:|
| Naive vs Diff  | 0.000 | 0.500 | 0.500 | Degenerate (Naive=all sig) |
| Naive vs Onset | 0.000 | 0.500 | 0.500 | Degenerate |
| Naive vs PermG | 0.000 | 0.750 | 0.750 | Degenerate |
| Naive vs TY    | 0.000 | 0.000 | 0.000 | Degenerate (both extremes) |
| **Diff vs Onset** | **1.000** | 1.000 | 0.500 | Perfect agreement |
| **Diff vs PermG** | **0.500** | 0.750 | 0.500 | Moderate |
| Diff vs TY     | 0.000 | 0.500 | 0.500 | Degenerate (TY=all not-sig) |
| **Onset vs PermG** | **0.500** | 0.750 | 0.500 | Moderate |
| Onset vs TY    | 0.000 | 0.500 | 0.500 | Degenerate |
| PermG vs TY    | 0.000 | 0.250 | 0.250 | Degenerate |

| Aggregate | κ |
|-----------|:-:|
| Mean (all 10 pairs) | **0.200** |
| Mean (3 non-degenerate pairs only) | **0.667** |

7/10 pairs are degenerate because Naive (always sig) and TY (never sig) have zero variance.

---

## 4. Cross-Architecture Comparison

| Metric | Pythia-410M (α=1.0, T=10) | GPT-2m (α=1.0, T=11) |
|--------|:-:|:-:|
| Fleiss' κ (all pairs) | 0.185 | 0.091 |
| Mean Cohen's κ (all pairwise) | — | 0.200 |
| Interpretation | Slight | Slight |
| Naive sig rate | high | 12/12 (100%) |
| TY sig rate | low | 0/12 (0%) |

Both architectures show "slight" agreement (κ < 0.20) across the 5-method panel.

---

## 5. Conclusion

**Low inter-method κ is a structural property of this 5-method panel at short T, not architecture-specific.**

Both Pythia-410M (κ=0.185) and GPT-2 Medium (κ=0.091) fall in the "slight agreement" range. The low κ is driven by two methodological extremes:

1. **Naive xcorr** (100% sig rate): Cannot discriminate direction because shared monotonic trends produce high |r| in both forward and reverse. Acts as a constant "sig" rater.

2. **TY Granger** (0% sig rate): Lacks statistical power at T=10-11 (df_resid=1-4). Acts as a constant "not-sig" rater. (See constraint C001.)

The 3 informative methods (Diff xcorr, Onset, Perm. Granger) show substantially higher agreement (mean non-degenerate κ = 0.667, "substantial"). Their disagreements are interpretable: Perm. Granger detects weak reverse d→ece effects that Diff/Onset reject, reflecting genuine sensitivity differences rather than noise.

**Implication for the paper:** Report the 5-method κ as evidence that method choice matters and that a multi-method consensus approach is necessary. The convergence of 3 trend-aware methods (κ=0.667) supports the robustness of the forward causal direction finding, while the full-panel κ=0.09-0.19 motivates why no single method should be trusted alone.
