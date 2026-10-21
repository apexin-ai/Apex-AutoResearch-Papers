---
dream_id: dream_20260519T143201
tier: median
overall_score: 2.5 — Borderline Findings (Resubmit next cycle)
timestamp: 2026-05-19T15:38:50.455750+00:00
---

# Dream Review Report — Full Roundtable

**Paper:** Task-Dependent Convergence and Per-Example Divergence in Attention-Augmented Linear Recurrent Models
**Venue:** EMNLP 2026 (ARR)
**Dream ID:** 20260519T143201
**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)

---

## Consolidated Scores

| Dimension | R1 | R2 | Consolidated |
|-----------|----|----|-------------|
| Soundness | 2.5 | 3.0 | 2.5 |
| Excitement | 2.0 | 2.0 | 2.0 |
| Reproducibility | 4.5 | 5.0 | 4.5 |
| **Overall Assessment** | **2.5** | **2.5** | **2.5** |

**Overall Assessment: 2.5 — Borderline Findings (Resubmit next cycle recommended)**

Calibration: EMNLP 2026 Main ≈ 4.0, Findings ≈ 3.0. This paper falls below the Findings bar in its current form but has a clear path to 3.0 with targeted revisions.

---

## Step 1: Independent Reviews

### Reviewer 1 (Methods + Experiments)

**Soundness: 2.5/5**

Critical and major issues:

1. **[Critical] Missing Jaccard random-null baseline.** The headline Claim 3 ("nearly non-overlapping" per-example effects, Jaccard < 0.10) is reported without comparison to the expected Jaccard under random set assignment. Back-of-envelope: for helped sets of ~462–548 samples from N≈5153 total LAMBADA examples, expected random Jaccard ≈ 0.045–0.054. Observed values of 0.07–0.10 are potentially *above* the random null, which would mean attention acts on *more* overlapping sets than chance — reversing the paper's central per-example claim. Without this computation, Claim 3 is uninterpretable.

2. **[Critical] n=5 Spearman power ceiling.** With 5 attention ratios, the minimum achievable two-tailed p-value is 2/120 = 0.0167. Every "significant" result (LAMBADA ρ=−1.0) achieves exactly this floor. The test cannot distinguish genuine task-dependent convergence from any monotonic confound correlated with attention ratio. There is zero resolution between "barely significant" and "strongly significant."

3. **[Major] Co-evolution inflated by definitional h0 anchor.** Section 4.6 reports ρ=−0.95 (p=0.05) between aggregate std and effect asymmetry, but the h0 point has |Δ|=0 by definition (pure recurrence vs. pure recurrence). Including this tautological anchor inflates the correlation. Excluding h0 leaves n=4 data points with minimum p = 2/24 = 0.083, likely non-significant.

4. **[Major] Scale comparison confounded by training tokens.** 340M models trained on 20B tokens vs. 1.3B on 100B tokens. The capacity-bottleneck interpretation of the 340M rebound is one hypothesis among several. Interaction between training duration and attention ratio is plausible but untested.

5. **[Major] GDN confound sensitivity.** Removing GDN (which has a known attn.num_heads configuration difference) drops LAMBADA from ρ=−1.0 (p=0.017) to ρ=−0.7 (p=0.233, non-significant). MMLU flips sign entirely. The main convergence result is fragile to removal of 1/3 of the data.

6. **[Major] BH-FDR pre-specification is imperfect.** The retrieval-demand taxonomy used to define the correction subset was built from initial benchmark data overlapping with the test set. Under full correction (m=9 benchmarks), no benchmark survives at α=0.05. LAMBADA BH-FDR adj-p=0.075.

7. **[Moderate] Bootstrap CI methodology.** Excluding 11.25% degenerate resamples (same-architecture triplicates given n=3) and reporting "100% of valid resamples have ρ<0" is potentially misleading. Conservative treatment (degenerate = ρ=0) would yield CI touching zero.

8. **[Moderate] No figures in the paper.** A tables-only presentation at a top venue is unusual and weakens communication of the core patterns (convergence trajectories, Jaccard heatmaps, the "scissors" co-evolution).

9. **[Minor] No visible Responsible NLP Research Checklist.** EMNLP 2026 requires Sections A–E; absence risks desk rejection.

**Reproducibility: 4.5/5** — All 72 models publicly available, standard lm-evaluation-harness, fully specified statistical tests. Deduction for no code release at review time.

**Excitement: 2/5** — Core findings confirm expected predictions from underspecification theory (D'Amour et al. 2022). Task-dependency of convergence is intuitive given attention's known retrieval role. No surprising insight emerges.

**R1 Overall: 2.5 (Borderline Findings)**

**R1 Strengths:**
- Exemplary statistical transparency: three-layer multiple comparison correction honestly reported, including the full-correction failure
- Pre-specified confirmatory design for additional benchmarks
- Informative negative results: within-architecture surface features/perplexity all non-significant (rules out trivial explanations), while cross-architecture KW test is significant (structured divergence)
- Public infrastructure enables full reproduction
- Appropriate epistemic caution throughout (descriptive not causal, community analysis not discovery)

**R1 Weaknesses:**
- Missing Jaccard null baseline is potentially claim-reversing
- n=5 power ceiling limits all convergence claims to floor-level p-values
- Co-evolution section inflated by definitional anchor
- Scale confound unresolved
- GDN confound makes n=3 effectively n=2 for clean analysis

---

### Reviewer 2 (Novelty + Related Work)

**Novelty Assessment: Low-to-moderate.**

The research question ("do aggregately similar models differ per-example?") is the definition of underspecification. The more specific question about attention's role in hybrid recurrent models is moderately novel in specificity, but Wang et al. (2025) already qualitatively observed convergence. The paper's contribution is quantifying what Wang et al. noted in 1–2 sentences — valid but intellectually short distance.

Methods novelty is low: the entire analytical toolkit (Spearman, Jaccard, KW, BH-FDR, bootstrap) is standard. No new method proposed. Per-example helped/hurt decomposition with Jaccard is clean but routine in ensemble diversity literature.

The paper explicitly frames itself as "characterization, not discovery" and "community analysis on public infrastructure." This is honest and appropriate framing, but it constrains the novelty ceiling. EMNLP Main requires either surprising findings or methodological contribution; this paper offers neither. For Findings, the characterization must be solid — and the statistical fragility weakens even this case.

**Related Work Assessment: Adequate with gaps.**

The paper cites ~20 references spanning hybrid architectures, underspecification, ensemble diversity, dataset cartography, and attention analysis. Organization into three paragraphs is clear.

Missing references of note:
- Fort et al. (2019) — deep ensemble per-example diversity (most directly relevant precedent)
- McCoy et al. (2020) — BERT per-example disagreement
- Arora et al. (2024) — attention's role in recurrent architectures
- Jain & Wallace (2019), Wiegreffe & Pinter (2019) — attention interpretability debate (relevant to §4.5)
- De et al. (2024) Griffin — hybrid architecture
- Poli et al. (2023) Hyena, Fu et al. (2023) H3 — earlier hybrids for historical context

The Wang et al. differentiation is well-executed (four concrete analytical dimensions with side-by-side comparison). The "medical meta-analysis" analogy is convincing.

The paper underemphasizes a key distinction from classical ensemble diversity: here, diversity arises from *architectural mechanism differences* under identical training conditions, not from constructed diversity (different seeds/data/hyperparameters). This is a potentially interesting angle that is underexplored.

**Framing Assessment:**

The evolution from "Equalizer Paradox" to the current title is a significant improvement — no longer overclaiming novelty by calling a known phenomenon a paradox. The narrative has a structural weakness: Claims 1 and 3 are somewhat independent, and the bridge between them (§4.6 co-evolution) is the statistically weakest section.

The underspecification framing (D'Amour et al. 2022) adds theoretical grounding but risks being seen as window-dressing if the analysis does not extend the framework.

Practical implications ("inform architecture selection") are overstated given the evidence. No actionable framework provided, no ensemble validation experiment conducted.

**Soundness: 3/5** — Statistical methodology is honest and transparent, but co-evolution section and Jaccard interpretation are flawed.

**Excitement: 2/5** — Findings confirm rather than overturn predictions. No surprise.

**Reproducibility: 5/5** — All models public, standard tools, fully specified tests. Exemplary.

**R2 Overall: 2.5 (Borderline Findings)**

**R2 Strengths:**
- Exemplary statistical transparency and epistemic calibration
- Clean per-example decomposition framework (helped/hurt with Jaccard is well-operationalized)
- Effective differentiation from Wang et al.
- Perfect reproducibility
- Informative negative results (surface features non-significant, cross-arch KW significant)
- Pre-specified confirmatory design for new benchmarks

**R2 Weaknesses:**
- Limited novelty: standard tools on known phenomenon, confirms underspecification predictions
- Missing Jaccard null baseline makes Claim 3 uninterpretable
- Co-evolution section statistically unsound (h0 anchor)
- StoryCloze confirmation is structurally expected (too similar to LAMBADA for strong cross-task validation)
- Related work gaps (Fort 2019, McCoy 2020, Arora 2024)
- Practical implications overstated without validation
- No figures

---

## Step 2: Cross-Sharing Reactions

### R1 reacting to R2:

**Agreements:** R1 strongly endorses R2's Jaccard null concern (independent convergence on the same critical gap), co-evolution critique, and "characterization not discovery" framing. R1 accepts R2's StoryCloze point — structural similarity to LAMBADA weakens the cross-task confirmation claim.

**Disagreements:** R1 is cautious about R2's suggestion that some results may be projections rather than measurements (regarding exp-004 attention weights and Mamba2), noting the paper should be given benefit of the doubt without concrete evidence. R1 considers R2's missing-references concern valid but a presentation gap rather than methodological.

**No score change:** R1 maintains 2.5.

### R2 reacting to R1:

**Agreements:** R2 strongly endorses R1's quantitative Jaccard null computation (the most damaging finding across both reviews). R2 agrees on n=5 Spearman power ceiling and bootstrap CI critique. R2 had not examined bootstrap degenerate-sample treatment at that granularity.

**Disagreements:** R2 thinks R1 overweights the GDN-specific confound — the real issue is n=3 being too small regardless of whether GDN is clean. R2 considers R1's checklist point procedural not substantive.

**No score change:** R2 maintains 2.5.

---

## Step 3: Convergence

### Points of Full Agreement (both reviewers):

1. **Missing Jaccard null baseline is the most critical issue.** Both independently flagged this as potentially claim-reversing. R1's computation (random Jaccard ≈ 0.045–0.054 vs. observed 0.07–0.10) makes the problem concrete. Claim 3 may be directionally wrong.

2. **Co-evolution section (§4.6) is inflated by h0 definitional anchor.** Both agree this is a major methodological flaw that can be fixed with existing data.

3. **n=5 Spearman power ceiling limits all convergence claims.** The test has no resolution above its floor p-value.

4. **Excitement is low (both score 2/5).** Findings confirm underspecification theory predictions without producing surprises or actionable insights.

5. **Reproducibility is excellent (4.5–5/5).** Public models, standard tools, fully specified tests.

6. **Statistical transparency is exemplary.** The three-layer correction reporting is rare and commendable.

7. **No figures weakens presentation.** Both note this is unusual for a top venue.

8. **Overall assessment: 2.5 (Borderline Findings).** Both converge independently.

### Points of Partial Disagreement:

1. **Soundness divergence (R1: 2.5, R2: 3.0).** R1 is harsher on soundness due to more granular critique of GDN confound, bootstrap methodology, and BH-FDR pre-specification. R2 focuses more on the broader picture (honest methodology applied to weak data). **Resolved at 2.5** — R2 accepts R1's bootstrap and Jaccard computations as sharpening the case.

2. **GDN confound framing.** R1 treats it as a specific architectural concern; R2 subsumes it under general n=3 insufficiency. **Resolved:** Both agree n=3 is fundamentally limiting; whether GDN specifically is confounded is secondary.

3. **Related work gaps.** R2 flags Fort 2019, McCoy 2020, Arora 2024 as significant omissions; R1 considers them presentation not substance. **Resolved:** Both agree these should be cited but their absence does not change experimental conclusions.

4. **Projection vs. measurement concern.** R2 raised the possibility that attention weight results (§4.5) may be projections. R1 urges benefit of the doubt. **Resolved:** The paper as submitted includes §4.5 with specific numbers (cosine sim=0.35, r=0.22); we evaluate what is presented, noting that these numbers should be verifiable from the public models.

---

## Step 4: Consolidated Assessment

### Final Overall Assessment: 2.5 / 5 (Borderline Findings — Resubmit Next Cycle)

### Justification

The paper demonstrates genuine analytical effort, exemplary statistical transparency, and appropriate epistemic calibration. The three-layer multiple comparison correction with honest reporting of all three levels (including the full-correction failure) sets a standard that most empirical NLP papers do not meet. The per-example decomposition framework is clean and well-operationalized. Reproducibility is excellent.

However, the evidence does not robustly support the claims at the level required for EMNLP Findings:

**Claim 1 (task-dependent convergence):** Rests on the minimum possible p-value of a 5-point Spearman test (p=0.017 is the combinatorial floor, not a strong result). Nothing survives full BH-FDR correction (m=9). The pre-specified subset correction (m=5) is debatable because the taxonomy was derived from overlapping data. GDN removal drops LAMBADA to non-significant.

**Claim 2 (scale-dependent convergence):** Two scale points confounded by 5× training token difference. Binary observation, not an extrapolatable trend. The paper appropriately disclaims scaling-law claims, but the residual claim (capacity threshold) is one hypothesis among several.

**Claim 3 (per-example divergence):** The most critical gap: Jaccard < 0.10 is reported as "nearly non-overlapping" without computing the random-null expectation. For the observed set sizes, random Jaccard ≈ 0.05. Observed values of 0.07–0.10 may be marginally *above* chance, potentially meaning attention effects are *more* overlapping than random — reversing the narrative. This gap alone makes the paper's signature finding uninterpretable.

**Novelty:** Low. The paper confirms expected predictions from underspecification theory (D'Amour et al. 2022) using standard statistical tools. No new method proposed. No surprising finding. The domain application (hybrid recurrent architectures) is relevant but the characterization does not yield actionable insights beyond intuition.

### Path to 3.0 (Findings)

The following revisions could elevate the paper, all achievable from existing data:

1. **Compute and report Jaccard null baseline.** If observed Jaccard is significantly above random → reframe as "structured overlap with architecture-specific residuals." If at or below random → the per-example divergence claim strengthens. Either way, the computation is essential.

2. **Remove or reframe co-evolution section.** Exclude h0 anchor, report n=4 correlation honestly. If non-significant, reframe as descriptive observation rather than statistical claim.

3. **Add figures.** Convergence trajectories, Jaccard heatmaps, and the "scissors" pattern deserve visualization. A tables-only paper is a handicap at EMNLP.

4. **Add missing references.** Fort et al. (2019), McCoy et al. (2020), Arora et al. (2024), attention interpretability papers.

5. **Strengthen StoryCloze confirmation.** Report per-example Jaccard for StoryCloze (not just aggregate ρ). If Jaccard patterns parallel LAMBADA, this strengthens the cross-task story.

6. **Address GDN sensitivity in main text.** Currently buried in appendix. The reader deserves to know the main result weakens substantially when one architecture is removed.

### Consolidated Strengths

- **Exemplary statistical transparency.** Three-layer multiple comparison correction with honest reporting at all levels, including full-correction failure. This is rare and commendable.
- **Appropriate epistemic calibration.** "Community analysis" framing, descriptive (not causal) attention analysis, no overclaiming.
- **Clean per-example decomposition.** Helped/hurt sets with Jaccard, cross-architecture KW tests, within-architecture null results. Well-structured analytical framework.
- **Informative negative results.** Surface features and baseline perplexity non-significant within architecture; cross-architecture comparison significant. Rules out trivial explanations.
- **Excellent reproducibility.** All models public, standard evaluation tools, fully specified tests.
- **Pre-specified confirmatory design** for additional benchmarks (StoryCloze, BoolQ, COPA).

### Consolidated Weaknesses

- **[Critical] Missing Jaccard null baseline** makes the signature per-example finding (Claim 3) uninterpretable and potentially reversed in direction.
- **[Critical] n=5 Spearman power ceiling** means every "significant" result hits the test's combinatorial floor (p=0.017). No result can be more significant, and the test cannot distinguish the hypothesis from monotonic confounds.
- **[Major] Co-evolution section inflated** by definitional h0 anchor point. Correctable from existing data.
- **[Major] Scale comparison confounded** by 5× training token difference (20B vs 100B). Capacity-threshold interpretation is one of multiple hypotheses.
- **[Major] GDN sensitivity.** Main LAMBADA result drops to non-significant when one (potentially confounded) architecture is removed.
- **[Major] Low novelty.** Standard analytical tools applied to confirm expected predictions from underspecification theory. No new method or surprising finding.
- **[Major] BH-FDR correction scope debatable.** Under full correction (m=9), nothing survives. Pre-specified subset overlaps with taxonomy-derivation data.
- **[Moderate] Related work gaps.** Fort et al. (2019), McCoy et al. (2020), Arora et al. (2024), attention interpretability literature.
- **[Moderate] StoryCloze confirmation is structurally expected** (too similar to LAMBADA for strong cross-task validation).
- **[Moderate] Practical implications overstated** without validation (no ensemble experiment).
- **[Moderate] No figures** in a paper about trajectories, heatmaps, and co-evolution patterns.
- **[Minor] No visible Responsible NLP Research Checklist** — EMNLP 2026 requires Sections A–E.

### Questions for Authors (Consolidated)

1. What is the expected Jaccard similarity under random set assignment for the observed helped/hurt set sizes? How many σ above/below random are the observed values?
2. What is the σ-vs-|Δ| Spearman correlation excluding the definitional h0 point?
3. Were per-example Jaccard decompositions computed for StoryCloze and BoolQ?
4. What is the result if degenerate bootstrap resamples are assigned ρ=0 rather than excluded?
5. Can you rule out attention-ratio × training-duration interaction as an alternative explanation for the 340M rebound?
6. Given the GDN sensitivity, should RetNet+HGRN2-only results be primary, with GDN as supplementary?
7. Why was no ensemble experiment conducted to validate the practical implications of per-example divergence?
8. Could you formalize the retrieval-demand taxonomy (e.g., proportion of questions answerable from passage alone) rather than using informal classification?
