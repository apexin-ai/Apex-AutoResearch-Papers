---
dream_id: dream_20260513T054654
tier: median
overall_score: weak reject (3/6)
timestamp: 2026-05-13T06:33:30.828420+00:00
---

# Dream Review Report: "When Do Circuit Discovery Methods Agree?"

**Dream ID:** 20260513T054654 | **Review Mode:** full | **Date:** 2026-05-13

---

## Roundtable Summary

Two independent reviewers assessed this paper:
- **R1** (Methods + Experiments): Score **3/6** (Weak Reject), Confidence 4/5
- **R2** (Novelty + Related Work): Score **3/6** (Weak Reject), Confidence 4/5

After cross-sharing and convergence discussion, the panel reaches a **consensus score of 3/6 (Weak Reject)**.

---

## Paper Overview

The paper introduces Circuit Structure Consensus (CSS), a framework that scores each edge in a transformer computational graph by the fraction of K≥3 circuit discovery methods that independently include it. Full-consensus edges (CSS=1.0) form compact circuits. The paper frames CSS as a diagnostic tool for assessing when cross-method agreement is meaningful.

**Four claims:**
1. CSS=1.0 circuits achieve comparable faithfulness at 3–5× fewer edges, but only when max Jaccard < ~0.45
2. Negative correlation between Jaccard and CSS advantage (Spearman ρ=−0.90, p=0.037, n=5)
3. ACDC isinf binarization causes CSS=1.0 to degenerate; top-k normalization fixes it
4. Binary consensus (CSS) is more stable than score-based ensembling (CIRCUS)

---

## R1: Methods and Experiments

### Method Evaluation

- The CSS formulation (Eq. 1–2) is mathematically sound but extremely simple — it is the inclusion frequency of an edge across K binary circuits, followed by thresholding. The formalization is correct but adds minimal technical depth.
- Top-k normalization is well-motivated: the paper clearly demonstrates that mixing ACDC's variable-size circuits with fixed-size gradient circuits causes degeneration. This is arguably the paper's most actionable contribution.
- CPR and CMD are reasonable evaluation metrics for circuit faithfulness, though the paper does not discuss their known limitations (e.g., sensitivity to ablation method, as documented by Miller et al., COLM 2024, which is not cited).
- The CSS distribution diagnostic (§3.4) is interesting conceptually but only demonstrated on 3 tasks with no formal analysis of what distribution shapes imply beyond intuitive descriptions.

### Experimental Rigor

**n=5 correlation (Claim 2).** The central quantitative claim rests on 5 model–task data points. Spearman p=0.037 barely crosses 0.05; Pearson p=0.089 does not. The data has a two-cluster structure (IOI low-Jaccard/positive-advantage vs. Arithmetic high-Jaccard/negative-advantage) with SVA and Qwen-IOI as ambiguous middle points. A binary rule ("if Jaccard < 0.5, use CSS") fits the data equally well as a continuous correlation — the Spearman test overstates the evidence. The ~0.45 threshold is determined by two marginal data points within 0.012 CPR of zero. This is the paper's most prominent weakness.

**k=75 degree of freedom.** The sensitivity analysis (Table 10) shows stability for k∈[75,150] but a notable CPR drop at k=50 for SVA (−0.05) and Qwen IOI (−0.02). The paper recommends k=75 "based on prior work conventions" but provides no principled criterion. A reviewer could reasonably argue k=75 was selected post hoc to maximize CSS performance, though the paper discloses the full sweep.

**Ablation robustness (§5.5).** The zero/mean/resample comparison was completed only for IOI on GPT-2, revealing a 6× variation in CSS advantage magnitude (0.013 to 0.080). This is concerning: if the advantage swings from +0.08 (zero) to +0.013 (resample) on the most favorable task, the negative-advantage tasks (SVA, Arithmetic) might show even larger variation. The paper acknowledges this limitation but the incompleteness weakens Claim 1.

**Method set confound.** GPT-2 uses {EAP-IG, EP, ACDC} while Qwen uses {EAP-IG, EP, IFR}. Cross-model comparisons (e.g., "IOI CSS advantage is similar on both models") are confounded by having different third methods. The EP–IFR Jaccard of 0.55 on Qwen IOI reduces effective K to ~2.3, as the paper honestly acknowledges, but this means the Qwen results are not truly comparable to GPT-2 results.

**CSS wins only 2 of 5 configurations.** CSS=1.0 has positive CPR advantage only on IOI (GPT-2: +0.021, Qwen: +0.012). SVA is marginal (−0.012), and Arithmetic is clearly negative on both models (−0.066, −0.039). The abstract's "comparable or superior faithfulness" is misleading — "sometimes comparable, often inferior" is more accurate. The edge-efficiency claim (3–5× fewer edges) is always true but follows trivially from intersection being a subset.

### Completeness and Coverage

- **3 tasks, 2 small models** is below the bar for generalization claims. The abandoned DocQA task and unfinished Gemma-2/Llama experiments are honestly disclosed, but the result is a paper built on a narrow empirical base.
- **CIRCUS comparison** (Table 11) uses zero ablation on IOI only, not the default mean ablation used throughout the rest of the paper. Zero ablation is known to disproportionately favor smaller circuits (CSS=1.0 has 7 edges vs. CIRCUS's 15). Additionally, the CIRCUS implementation's correctness is not verified — if threshold diversity produces nested circuits (violating CIRCUS's design), the negative CPR may reflect a bug, not a fundamental limitation.
- **No confidence intervals** are reported on any CPR difference. The +0.021 advantage on IOI could easily be within noise without error bars.

### Specific Technical Issues

- Table 1 reports Arith GPT-2 best single CPR=0.985 but the YAML context shows EAP-IG CPR=0.985 is plausible (the paper's own per-method tables are not shown for GPT-2 Arithmetic, making verification impossible). This should be shown.
- No per-method breakdown tables for GPT-2 IOI or GPT-2 Arithmetic in the main paper — only SVA, Qwen IOI, and Qwen Arithmetic get detailed tables. This selective reporting is a gap.

### R1 Questions for Authors

1. What are the 95% confidence intervals on CPR differences (CSS advantage)? Without error bars, a +0.021 advantage is indistinguishable from noise.
2. What happens if you compare CSS=1.0 (N edges) against the top-N edges of the best single method? If EAP-IG's top-18 edges on IOI also achieve CPR≈0.11, the advantage is from circuit size, not consensus.
3. How sensitive is the Jaccard–utility correlation to leaving out a single data point (leave-one-out stability)?
4. Why was the CIRCUS comparison run under zero ablation rather than mean ablation (the paper's default)?
5. Can you report CSS=1.0 results for k=75 on all tasks under all three ablation methods, not just IOI?

---

## R2: Novelty and Related Work

### Novelty Assessment

**CSS is the feature selection stability index.** The formula CSS(e) = (1/K) Σ 1[e ∈ C_mi] is mathematically identical to the feature selection stability measure formalized by Nogueira & Brown (JMLR 2016) and used since Saeys et al. (Bioinformatics 2007). The application to circuit edges across algorithmically diverse methods is domain-specific novelty, but the mathematical framework is well-established. This connection is entirely unacknowledged, which inflates the apparent novelty.

**Incremental over Mondorf et al. (2025).** Mondorf et al. already performed cross-method aggregation including intersection (equivalent to CSS=1.0) and found that continuous score averaging outperforms intersection. The paper's claimed differentiation — binary consensus vs. score averaging, cross-family vs. within-gradient — is valid but the paper never runs a head-to-head comparison. This is a critical omission: it is possible that Mondorf et al.'s approach extended to cross-family methods would dominate CSS.

**Binarization pathology is genuinely novel.** The documentation that ACDC's isinf threshold causes CSS to collapse to the ACDC circuit is concrete, actionable, and stands independently of whether CSS itself is adopted. This is the paper's most valuable contribution.

**Jaccard-as-predictor is intuitive.** The directional insight (consensus helps when methods disagree) is arguably obvious. The quantification via Spearman correlation attempts to make it actionable, but n=5 is insufficient.

**Diagnostic framing is honest but thin.** The paper offers three diagnostic contributions: (1) CSS distribution reveals task structure, (2) Jaccard predicts CSS utility, (3) binarization pathology detection. Only (3) is fully validated. (1) is demonstrated on 2–3 tasks without formal analysis. (2) rests on 5 data points.

### Related Work Gaps

The paper has only 14 references, which is severely insufficient for a paper positioning itself within a rapidly growing literature. Critical missing references include:

- **Feature selection stability literature** (Saeys et al. 2007; Nogueira & Brown, JMLR 2016) — CSS is mathematically identical
- **Ensemble methods** (Breiman 1996; Dietterich 2000) — conditions for ensemble agreement informativeness are well-studied
- **Miller et al. (COLM 2024)** — "Transformer Circuit Faithfulness Metrics are not Robust" — directly motivates CSS
- **MIB benchmark (ICML 2025)** — standardized circuit evaluation
- **Recent discovery methods** (CD-T, GIM, HAP, Sparse Feature Circuits) — potential additional methods and positioning context
- **Circuit non-uniqueness** ("Everything Everywhere All at Once", ICLR 2025) — challenges the theoretical basis for intersecting circuits

### Claim-Evidence Alignment

| Claim | Evidence Strength | Calibration |
|-------|------------------|-------------|
| 1. CSS=1.0 comparable at fewer edges (Jaccard < 0.45) | Weak: wins 2/5, margins tiny, no CIs | Overclaimed in abstract |
| 2. Jaccard–utility correlation | Weak: n=5, two-cluster structure | Appropriately hedged in text, overclaimed in abstract |
| 3. ACDC binarization pathology | Strong: clearly demonstrated | Well-calibrated |
| 4. CSS > CIRCUS stability | Unreliable: single task, non-default ablation, possible implementation issues | Overclaimed |

### R2 Questions for Authors

1. How does CSS differ from the feature selection stability index (Nogueira & Brown, JMLR 2016)? If the only difference is domain transfer, what is the MI-specific contribution?
2. Have you compared CSS against Mondorf et al.'s continuous score averaging on the same tasks?
3. What is the computational cost of running K=3 methods? Is CSS practical for researchers with limited compute?
4. Why are no union or weighted-voting baselines compared alongside intersection (CSS=1.0)?
5. Was the CIRCUS implementation verified against the original paper's specifications, particularly the non-nesting constraint?

---

## Roundtable Convergence

### Points of Agreement

1. **ACDC binarization pathology (Claim 3) is the paper's strongest and most actionable contribution.** Both reviewers agree this finding is well-demonstrated, genuinely useful, and would benefit the community regardless of CSS adoption. The top-k normalization recommendation is practical.

2. **The Jaccard–utility correlation (Claim 2) is statistically underpowered.** n=5 with a two-cluster structure and barely-significant p-value cannot establish a reliable threshold. Both reviewers agree the mechanistic intuition is sound but the quantitative claim oversells the evidence.

3. **CSS wins only on IOI**, and even there the margins are small (+0.021 and +0.012 CPR) without confidence intervals. The "comparable or superior faithfulness" framing in the abstract is misleading. Both reviewers agree the edge-efficiency claim, while always true, follows trivially from taking the intersection.

4. **The diagnostic framing is honest and scientifically mature**, but both reviewers feel the diagnostic analysis is too shallow for this framing to carry the paper at a top venue. The CSS distribution analysis is descriptive rather than formal.

5. **The paper is severely underreferenced** (14 citations). The missing connection to feature selection stability literature is a significant novelty concern.

### Points of Divergence

- R2 raises the **feature selection stability connection** as a near-fatal novelty issue; R1 did not identify this but agrees upon cross-sharing that it significantly weakens the novelty claim. **Resolved: both agree this must be addressed.**

- R1 emphasizes **method set confound** (different K=3 methods across models) more than R2. R2 agrees this is a real issue but considers it secondary to the novelty concerns. **Resolved: real but addressable limitation.**

- R2 questions the **CIRCUS implementation validity** more forcefully than R1. R1 agrees the comparison is narrow (one task, non-default ablation) but did not flag potential implementation bugs. **Resolved: both agree Claim 4 is the weakest of the four claims.**

### Consensus Assessment

The panel agrees on **3/6 (Weak Reject)** as the appropriate score.

**Rationale:** The paper addresses a genuinely important question (when and why do circuit discovery methods agree?) and provides one solid contribution (ACDC binarization pathology + top-k normalization fix). The diagnostic framing is intellectually honest and the inclusion of negative results (Arithmetic) shows scientific maturity. However, the paper falls short of the top-venue bar due to: (a) insufficient novelty — CSS is a known technique from feature selection stability applied to a new domain without acknowledgment; (b) weak statistical support for the central claim — n=5 is inadequate for the Jaccard–utility correlation; (c) narrow experimental scope — 3 tasks on 2 small models with incomplete ablation robustness; (d) missing critical comparisons — no head-to-head with Mondorf et al.'s continuous averaging, no size-controlled baselines; (e) unreliable CIRCUS comparison.

---

## Scores

| | R1 | R2 | Consensus |
|---|---|---|---|
| **Overall** | 3/6 (Weak Reject) | 3/6 (Weak Reject) | **3/6 (Weak Reject)** |
| **Confidence** | 4/5 | 4/5 | **4/5** |

---

## Actionable Recommendations for Revision

To move toward acceptance at a top venue, the authors should:

1. **Acknowledge and discuss the feature selection stability literature.** Position CSS as a domain-specific application of inclusion frequency, and argue what the MI-specific application contributes (e.g., the Jaccard diagnostic, the binarization pathology).

2. **Add 5–10 more model–task configurations** to strengthen the Jaccard–utility correlation. n≥10 data points with a clear trend would make this publishable; n=5 does not.

3. **Run size-controlled baselines**: compare CSS=1.0 (N edges) against the top-N edges of each single method. If the edge-efficiency claim survives this comparison, it becomes much stronger.

4. **Report confidence intervals** on all CPR differences. Bootstrap over evaluation examples.

5. **Complete the ablation robustness analysis** for all tasks, not just IOI. If CSS advantage varies 6× across ablation methods, this must be characterized.

6. **Either fix the CIRCUS comparison or remove Claim 4.** Use mean ablation (the paper's default), verify the implementation, and test on multiple tasks.

7. **Add a head-to-head comparison with Mondorf et al.'s continuous averaging** extended to cross-family methods. If CSS loses, reposition the contribution around the diagnostic aspects.

8. **Expand the reference list** to 30+ papers, covering feature selection stability, ensemble methods, recent MI work (MIB, circuit non-uniqueness, metric robustness).

---

## Meta-Assessment

The paper is best described as an **empirical observation paper with one solid methodological finding** (binarization pathology) and an **underpowered but directionally interesting hypothesis** (Jaccard predicts consensus utility). In its current form, it would be appropriate for a **Findings track** or **workshop paper** at a top venue, but does not meet the bar for Main conference. The honest framing and negative results are commendable and suggest a strong revision could reach acceptance with substantially expanded experiments and proper literature positioning.
