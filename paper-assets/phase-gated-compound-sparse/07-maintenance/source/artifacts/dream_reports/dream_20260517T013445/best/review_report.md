---
dream_id: dream_20260517T013445
tier: best
overall_score: reject
timestamp: 2026-05-17T02:04:00.159662+00:00
---

# Dream Review Report: Phase-Dependent Compound Sparsity

**Paper:** Phase-Dependent Compound Sparsity: Strategy-Specific Severity Emerges from the Interaction of Head Pruning and KV Cache Eviction

**Review mode:** Full (2 Reviewers, 4-step roundtable)
**Venue standard:** Top ML venue, ~25% acceptance, 6-point scale

---

## Roundtable Summary

| Reviewer | Focus | Independent Score | Post-Discussion Score |
|----------|-------|------------------|-----------------------|
| R1 | Methods + Experiments | 4 (Borderline Reject) | 4 (Borderline Reject) |
| R2 | Novelty + Related Work | 3 (Borderline Reject) | 3 (Borderline Reject) |
| **Consensus** | | | **3.5 (Reject, leaning borderline)** |

---

## Step 1: Independent Reviews

### R1 — Methods & Experiments (Score: 4)

**Strengths identified:**
- Interaction Index is well-defined and appropriate for measuring super-additivity
- Phase segmentation from uncompressed model largely eliminates circularity; recency control further addresses it
- Statistical framework (Wilcoxon signed-rank, Bonferroni, bootstrap CIs, Jonckheere-Terpstra) is rigorous and well-chosen given heavy right-skew
- Three eviction strategies with recency as scoring-independent control is an excellent experimental design choice
- Dose-response across 4 sparsity levels provides convincing monotonicity evidence
- Within-architecture and cross-architecture replication shows good experimental breadth

**Weaknesses:**

| # | Weakness | Severity |
|---|----------|----------|
| W1 | Placeholder tables (GPQA Table 6, 14B Table 7) with "Results pending." Paper claims contributions it cannot deliver as submitted. | **Major** |
| W2 | Spearman rho=1.0 on n=4 points used as headline evidence in abstract/intro. Any monotonic sequence of 4 values gives rho=1.0. Misleading presentation. | **Moderate** |
| W3 | No control for random seed variance in random eviction. Single random mask realization per problem could introduce systematic bias. | **Moderate** |
| W4 | Recency control has only 2 cleanly interpretable conditions (s=0.15 and s=0.25); s=0.30 declared numerically unreliable. n=100 vs n=500 asymmetry. Insufficient for dose-response characterization of the null. | **Moderate** |
| W5 | Discrimination collapse mechanism is explicitly correlational and accounts for "less than" the observed 15-17x divergence. Mechanistic contribution is thin. | **Moderate** |
| W6 | GSM8K evaluation severely underpowered (n=50); Qwen GSM8K "inconclusive due to truncation." Cross-benchmark evidence weaker than claimed. | **Moderate** |
| W7 | Pilot mitigation (18% PPL recovery, CI crosses zero) explicitly fails its own gate. Paper is purely descriptive with no actionable method. | **Minor** |
| W8 | Phase segmentation validated against `<think>` tokens on only n=48 GSM8K problems from a single model. Primary evaluation on MATH-500 lacks this validation. | **Minor** |
| W9 | The "15-17x" headline ratio has wide implicit uncertainty (could be 11-31x based on denominator CIs) but presented as precise. | **Minor** |

**Key questions for authors:**
1. How many random seeds were used for random eviction experiments? If one, is the phase gradient stable across seeds?
2. Will GPQA and 14B results be available? If not, why are placeholder sections included?
3. Negative recency gradient at s=0.25 (Delta=-0.091, significantly negative) is not discussed. What does it mean for compound interaction to be larger in high-sparsity phases under recency? This appears to be selective reporting.
4. Under compound sparsity, do actual attention patterns still show the same phase structure as the dense model, or does compression disrupt the phase boundaries?
5. Why is LLaMA strategy specificity so much weaker (2-2.6x vs 15-17x)? The paper attributes this to "architectural details" without concrete mechanistic explanation.

---

### R2 — Novelty & Related Work (Score: 3)

**Strengths identified:**
- Related work is well-organized with adequate coverage (30+ references across compound compression, phase-aware methods, importance scoring, adaptive eviction)
- The use of recency eviction as a methodological control (not just a performance baseline) is a genuinely clever and novel design choice
- Honest limitations section acknowledging correlational nature, failed mitigation, and model-dependent effects
- Thorough statistical reporting with proper CIs

**Weaknesses:**

| # | Weakness | Severity |
|---|----------|----------|
| W1 | Core finding is predictable from combining prior work: HIES (importance score collapse under pruning) + ThinKV (phase-dependent compression sensitivity) + SparK (super-additive compound interaction). The logical chain "head pruning degrades importance scores, so importance-based eviction suffers more in phases where scoring matters most" is short. | **Major** |
| W2 | No deployable method. Pilot mitigation failed its pre-registered gate (18% recovery, CI crosses zero). Paper provides a diagnostic but no solution. | **Major** |
| W3 | Incomplete manuscript: placeholder tables for GPQA Diamond and 14B experiments. Cannot be reviewed as a complete contribution. | **Major** |
| W4 | Effect attenuates substantially: 15-17x (DeepSeek/MATH-500) to 2.0-2.6x (LLaMA) to 2.3-3.8x (GSM8K). The phenomenon may be concentrated in favorable configurations rather than general. | **Moderate** |
| W5 | Discrimination collapse is correlational and cannot explain the full 15-17x divergence. Acknowledged by authors, but undermines the mechanistic contribution claim. | **Moderate** |
| W6 | Recency control uses only n=100 vs n=500 main experiments, only on DeepSeek. s=0.30 numerically unreliable. The paper's main methodological control has limited power. | **Moderate** |
| W7 | Overclaiming: "phase-gated analysis framework" (simple per-phase decomposition), "novel experimental design" (using a simpler baseline as control), "challenges the uniformity assumption" (prior work simply didn't measure phase dependence, not that it assumed uniformity). | **Minor** |
| W8 | Dense and repetitive: same numbers (0.39-8.48, 15-17x) appear in Abstract, Introduction, Results, Discussion, and Conclusion. | **Minor** |

**Key questions for authors:**
1. Given that HIES shows score collapse and ThinKV shows phase-dependent sensitivity, what specific aspect of your finding would NOT be predicted by combining these two prior results? What is the genuine surprise beyond quantification?
2. At what point does the strategy specificity effect become practically negligible? Is the phenomenon robust or concentrated in DeepSeek + MATH-500?
3. What concrete engineering action should a practitioner take beyond "be aware this exists"?
4. Could the phase gradient simply reflect that low-sparsity phases have higher baseline perplexity, meaning the same perturbation manifests as a larger ratio?

**Related work gaps (minor):**
- Missing recent LLM-specific structured pruning (ShortGPT, SliceGPT, LaCo)
- Connection to MoE and conditional computation underdeveloped

---

## Step 2: Cross-Reactions

### R1 reacting to R2:

**Agreements:** R1 agrees with R2's novelty concern but grades it moderate rather than major, noting that "predictable in hindsight" and "obvious ex ante" are different standards. The magnitude (15-17x) was not predictable from prior work, even if the direction was. Agrees on incomplete manuscript and presentation repetition.

**Disagreements:** R1 considers R2's "no method contribution" framing overstated, citing precedent of diagnostic papers at ML venues (attention sinks, positional encoding failures). On attenuation, R1 views the 2-17x range across configurations as informative (characterizing boundary conditions) rather than undermining generality.

**Score impact:** R1 remains at 4, anchored on incomplete manuscript. Notes that if placeholder results were filled and consistent, could move to 5.

### R2 reacting to R1:

**Agreements:** R2 agrees strongly with rho=1.0 on n=4 concern (should have flagged it independently). Agrees on placeholder tables. GSM8K underpowered point strengthens R2's attenuation concern.

**Disagreements:** R2 considers R1's random seed control concern somewhat overstated for a descriptive study, since inter-seed variance primarily affects which tokens are dropped, not the structural phase-difference claim.

**New concern adopted:** R2 flags R1's observation about the negative recency gradient at s=0.25 as a red flag for selective reporting. The paper ignores an inconvenient result that contradicts its narrative.

**Score impact:** R2 remains at 3.

---

## Step 3: Convergence

### Points of convergence (both reviewers agree):

1. **Incomplete manuscript is disqualifying** — placeholder tables for GPQA and 14B experiments make the paper unsubmittable as-is. Both rate this as Major.
2. **Methodology is sound** — II definition, paired design, nonparametric statistics, bootstrap CIs are all appropriate. The experimental framework itself is rigorous.
3. **Three-way dissociation design is genuinely creative** — using recency as a scoring-independent control rather than just a baseline is novel in this literature.
4. **Discrimination collapse is insufficient** — correlational, cannot explain the full divergence, weakens the mechanistic contribution.
5. **GSM8K evidence is weak** — n=50, one model's results inconclusive.
6. **Statistical overclaiming** — rho=1.0 on n=4, "15-17x" without uncertainty, repetitive use of same numbers.

### Point of disagreement:

**Novelty:** R2 considers the finding fundamentally predictable from prior work (Major weakness). R1 acknowledges the direction is predictable but argues the magnitude and cross-benchmark characterization add value (Moderate weakness). R1 also argues diagnostic/finding papers have precedent at top venues.

**Resolution:** Both agree the paper's contribution would be strengthened if it either (a) demonstrated the finding is quantitatively surprising (not just directionally expected), or (b) delivered a working phase-aware method. Neither condition is met. The disagreement is on degree, not kind.

### Selective reporting concern (raised in cross-reaction):

The negative recency gradient at s=0.25 (Delta=-0.091, significantly negative) is reported in the data but not discussed in the text. This result contradicts the paper's narrative and its omission from the discussion is a concern.

---

## Step 4: Consolidated Assessment

### Overall Score: 3.5 → **Reject** (between Borderline Reject and Weak Reject)

### Strengths (in order of importance):
1. **Rigorous statistical methodology.** Paired design, nonparametric tests, Bonferroni correction, bootstrap CIs, and effect sizes are all well-chosen and properly applied. This is above-average statistical rigor for ML papers.
2. **Creative experimental design.** The three-way dissociation using recency as a scoring-independent control is a genuine methodological contribution to the sparsity analysis literature.
3. **Honest limitations.** The paper does not hide the failed mitigation pilot, the correlational nature of the mechanism, or the architecture-dependent effects. This transparency is commendable.
4. **Sound interaction metric.** The Interaction Index cleanly captures super-additivity and the per-phase decomposition is well-motivated.

### Weaknesses (in order of severity):
1. **[Major] Incomplete manuscript.** Placeholder tables for GPQA Diamond and 14B experiments with "Results pending." The paper claims contributions it cannot substantiate as submitted.
2. **[Major] Limited novelty.** The core finding (importance-based eviction suffers more under compound sparsity in phases where scoring is critical) is a natural prediction from combining HIES (score collapse under pruning), ThinKV (phase-dependent sensitivity), and SparK (super-additive interaction). The contribution is quantification, not discovery.
3. **[Major] No method contribution.** Purely diagnostic with no deployable solution. The pilot mitigation failed (18% recovery, CI crosses zero). For a top venue, an empirical finding paper must offer either a surprising discovery or a practical advance; this paper offers neither.
4. **[Moderate] Generality concerns.** Strategy specificity attenuates dramatically across configurations (15-17x on DeepSeek/MATH-500, 2-2.6x on LLaMA, 2.3-3.8x on GSM8K). The strong effect may be specific to particular architecture/benchmark combinations.
5. **[Moderate] Weak mechanistic explanation.** Discrimination collapse is correlational, cannot quantitatively account for the observed divergence, and is largely a restatement of HIES in the compound setting.
6. **[Moderate] Statistical overclaiming.** Spearman rho=1.0 on n=4 used as headline evidence; "15-17x" presented without uncertainty; same numbers repeated across all sections.
7. **[Moderate] Selective reporting.** Negative recency gradient at s=0.25 is reported in data but not discussed, despite contradicting the narrative.
8. **[Moderate] Underpowered secondary benchmarks.** GSM8K n=50, Qwen GSM8K inconclusive, recency n=100 with only 2 clean conditions.

### Recommendation:

**Reject.** The paper presents a methodologically careful empirical study, but it falls below the acceptance threshold on three independent grounds: (1) the manuscript is incomplete with placeholder data for claimed contributions; (2) the core finding is predictable from combining existing results and lacks a genuinely surprising element; (3) no practical method is delivered or even shown to be feasible. Any one of these could be overcome, but together they place the paper below the bar.

### Path to acceptance:
- Complete all experiments (GPQA, 14B, full recency dose-response)
- Either develop a working phase-aware allocation method that recovers meaningful performance, or reframe the contribution around the three-way dissociation design itself as a reusable methodology for sparsity analysis
- Address the negative recency gradient finding transparently
- Remove rho=1.0 on n=4 from abstract/intro or properly contextualize
- Report uncertainty on strategy specificity ratios
- Add random seed sensitivity analysis for random eviction
- Strengthen the mechanistic analysis beyond correlation (e.g., interventional experiments on Gini coefficient)

### Experiment Coverage Assessment:

Comparing against the review_context.yaml experiment list:
- GPQA importance s=0.15: reported (gradient=0.947)
- GPQA importance s=0.20, 0.25, 0.30: reported (3.08, 8.62, 10.68) — matches expected values closely
- GPQA random s=0.15, 0.20: reported as NS — matches expectations
- GPQA random s=0.25, 0.30: reported (0.76, 1.37) — matches expectations
- Cross-benchmark synthesis: reported in Table 4
- Recency experiments: partially reported (n=100, s=0.30 unreliable)
- GPQA per-phase detailed statistics (Table 1): s=0.15 lacks phase breakdown, s=0.20-0.30 reported

The paper covers most imagined experiments for the GPQA DeepSeek importance/random conditions. Gaps are in phase-level detail at s=0.15 and in the recency dose-response completeness. The paper mentions 14B and additional GPQA tables as placeholders, which the review_context does not list as imagined experiments, suggesting these may have been aspirational extensions.