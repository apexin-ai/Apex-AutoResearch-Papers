---
dream_id: dream_20260520T185641
tier: worst
overall_score: weak reject
timestamp: 2026-05-20T19:56:52.262523+00:00
---

# Dream Review Report: "Does Probe-Based Calibration Work Beyond English?"

**Dream ID:** 20260520T185641
**Review Mode:** Full (2 Reviewers + Roundtable)
**Venue Standard:** Top ML venue (~25% acceptance, 6-point scale)

---

## Reviewer Assignments

- **R1** — Methods & Experiments
- **R2** — Novelty & Related Work

---

## Step 1: Independent Reviews

### Reviewer 1 (Methods & Experiments)

**Score: 4/6 (Weak Accept)**

**Strengths:**

1. **Scale is genuine and unprecedented.** 3 architectures × 20–52 languages × all probed layers × 5 transfer conditions. No prior work has evaluated probe-based calibration at this breadth. The experimental matrix is well-designed to answer the stated question.
2. **CaCLR ablation is thorough.** Sweeping β across 3 orders of magnitude and showing flat AUROC landscape is a clean demonstration that the consistency loss is inert. The component ablation (Table 4) isolates contributions clearly: SB-ECE helps (+1.6pp), consistency does not.
3. **Controls are adequate where present.** The random-direction control in the decomposition experiment (−0.3pp vs −1.4pp for difficulty) rules out dimensionality-reduction artifacts. INT8 validation (cosine 0.994, ρ=0.98) is responsible engineering.
4. **Cross-benchmark validation strengthens claims.** Testing on GlobalMMLU, Belebele, and MMLU-ProX with consistent results (CaCLR never beats linear projection) demonstrates robustness.
5. **Honest reporting of negative results.** The paper does not bury failures — it foregrounds them, which is scientifically valuable.

**Weaknesses:**

1. **No significance tests or confidence intervals.** The paper's key comparisons involve small effect sizes: CaCLR vs linear projection (0.3pp), decomposition effect (1.3–1.4pp), probe complexity (Cohen's d=0.18). Without statistical tests, it's impossible to assess whether these differences are meaningful or noise. This is a serious methodological gap for a paper whose claims rest on small deltas.
2. **The 0.65 AUROC threshold is arbitrary and load-bearing.** The headline numbers (7/19 pass, 4/19 pass, 23.5% pass at 52 languages) all depend on this threshold. No justification is provided. At 0.60, the narrative changes substantially (most mid-resource languages would pass on Qwen3). At 0.70, nearly everything fails. The paper needs sensitivity analysis across thresholds or a principled calibration-based criterion.
3. **CaCLR is underspecified.** The consistency loss "minimizes the distributional distance" — but which distance? KL divergence? MMD? Wasserstein? The choice matters enormously for alignment-based objectives. The paper doesn't specify, undermining reproducibility and making it impossible to assess whether a different distance metric would change the result.
4. **Oracle layer selection in Table 2.** "Best transfer layer" is selected per-language, per-architecture. In practice, a practitioner wouldn't know the best layer for a new language. The paper should report fixed-layer results (e.g., at 50% depth or at the English-optimal layer) alongside oracle selection.
5. **Linear projection baseline is surprisingly strong but under-analyzed.** Linear projection with ~50 parallel pairs matches or beats CaCLR everywhere. No sensitivity analysis on the number of parallel examples (would 20 suffice? 100?). No analysis of what the learned projection captures.
6. **Decomposition uses reduced grid (10 languages × 8 layers vs full 20 × 24).** Subsampling rationale not provided. The 9-language transfer mean in Table 6 may not represent the full distribution.
7. **Gemma 4 results are incomplete.** Table 5 summarizes Gemma4 in one row (ρ=0.48, ZS AUC=0.608) but provides no per-language breakdown, no CaCLR evaluation, no decomposition results. The third architecture is a thin addition rather than a full replication.
8. **Mean-shift explanation is hand-wavy.** "Subtracting the mean activation difference removes useful signal" — but what useful signal? The paper doesn't analyze what the mean difference encodes or why subtracting it is destructive. This could be explained via a simple decomposition of the mean into language-identity vs. content components.
9. **Sample sizes per language not reported.** GlobalMMLU has variable coverage across languages. If low-resource languages have fewer evaluation examples, AUROC estimates are noisier, which could explain the resource-tier gradient partially.

**Questions for Authors:**
- What specific distributional distance is used in L_consistency?
- Were non-linear alignment methods tested (CCA, Procrustes, RCCA)?
- How many evaluation examples per language in GlobalMMLU?
- What is the sensitivity of "pass rate" to the 0.65 threshold?

---

### Reviewer 2 (Novelty & Related Work)

**Score: 3/6 (Weak Reject)**

**Strengths:**

1. **Timely and important question.** The field is actively expanding probe-based methods (Miao et al. 2024 → Miao & Ungar 2026 → Xiao et al. 2025) without multilingual validation. Someone needs to run this experiment, and the paper does so at scale.
2. **Diagnostic framing is honest and effective.** Rather than overselling negative results, the paper positions itself as a community service — answering whether this research line generalizes before more resources are invested. This framing is appropriate for the results.
3. **The difficulty-entanglement finding (Section 5.5) is genuinely interesting.** Showing that difficulty is load-bearing for cross-lingual transfer (not a confound) contradicts English-only prior work's assumption of clean separation. This is the most novel finding in the paper.
4. **The dense-vs-MoE contrast (Table 5) provides architectural insight.** Implicating MoE routing as a source of non-monotonic perturbation in the Pareto frontier is a useful observation for the field.

**Weaknesses:**

1. **The negative result is largely predictable.** Domain adaptation theory (Ben-David et al., 2010) predicts that transfer degrades with distribution divergence. Low-resource languages have larger representation divergence from English — the resource-tier gradient follows directly. The paper neither cites this theoretical framework nor explains why anyone should have expected otherwise. Without engagement with transfer theory, the empirical finding reads as confirming the obvious.
2. **CaCLR's dual framing is incoherent.** The paper introduces CaCLR as "a novel consistency-based objective" (Section 3.3), then reports it as a negative result (Section 5.3). If CaCLR is the methodological contribution, its failure leaves the paper without a working method. If the diagnostic is the contribution, CaCLR is filler. The paper needs to commit to one framing. The honest framing is: "we tested the most natural distributional-matching approach and it doesn't work — here's why."
3. **Missing critical related work:**
   - **Cross-lingual alignment literature** (Conneau et al. 2018 MUSE; Artetxe et al. 2018 VecMap; Schuster et al. 2019) — directly relevant to why linear projection works and distributional matching doesn't.
   - **Probing methodology critiques** (Hewitt & Liang 2019 control tasks; Voita & Titov 2020 MDL probes; Pimentel et al. 2020 information-theoretic) — the paper uses probes uncritically without engaging with the literature on what probes actually measure.
   - **Representation similarity** (CKA, SVCCA, Raghu et al. 2017) — extensively used to study cross-lingual representation alignment. Could provide mechanistic explanation for the Pareto frontier.
   - **Domain adaptation theory** (Ben-David et al. 2010) — provides the theoretical framework for predicting transfer failure.
   - **Conformal prediction** — an alternative calibration approach that provides distribution-free guarantees and should be discussed as an alternative path.
4. **Descriptive without mechanistic depth.** The paper documents what fails (transfer, CaCLR, decomposition) but doesn't explain why at the representation level. Why does the correctness direction not align cross-lingually? Is it because languages occupy different subspaces? Because MoE routing creates language-specific expert patterns? The paper gestures at these explanations in the discussion but provides no evidence. A CKA or SVCCA analysis across layers and languages would provide the missing mechanistic story.
5. **Orthogonality extension is incremental.** The paper acknowledges this: extending Miao & Ungar's English result to 20 languages with qualitatively the same conclusion. The resource-tier modulation (0.054 vs 0.098) is the novel angle but the effect size is modest and the causal interpretation is ambiguous.
6. **No comparison with Xiao et al. [2025]'s partial success.** They report that knowledge-boundary probes partially generalize across 8 languages. The paper dismisses this as "answerability not correctness" but doesn't analyze whether the correctness-vs-answerability distinction explains the different outcomes. This is a missed opportunity for insight.
7. **No path forward.** The paper concludes that "fundamental methodological advances" are needed but offers no concrete directions. What would a successful approach look like? Language-specific probes? Multilingual probe training? Adapter-based alignment? The lack of any constructive proposal limits the paper's impact beyond a warning.

**Novelty Assessment:**
The paper's novelty is moderate-to-low. The main contribution is empirical measurement at scale. The specific findings are:
- Transfer failure: predictable from first principles (low novelty)
- CaCLR failure: moderately novel as a specific negative result, but distributional matching failing under low SNR is a known phenomenon
- Difficulty entanglement: genuinely novel and interesting (moderate-high novelty)
- Orthogonality extension: incremental (low novelty)
- Architecture dependence of Pareto frontier: moderately novel
- Dense vs MoE contrast: moderately novel

For a top ML venue (~25% acceptance), empirical measurement without methodological contribution or deep theoretical insight typically falls below the bar.

---

## Step 2: Cross-Sharing

**R1 → R2:** "I share your concern about missing domain adaptation theory — it would reframe the resource-tier gradient from 'surprising finding' to 'expected consequence.' I also agree the CaCLR framing is problematic. However, I weigh the experimental thoroughness more heavily — the scale is real and no one has done this before."

**R2 → R1:** "The scale is impressive, I agree. But your statistical rigor concern actually strengthens my novelty worry: if we can't even tell whether the small effects are significant, the claimed findings are on even weaker ground. The arbitrary threshold compounds this — the headline narrative is fragile. I'm also concerned that Gemma4's thin treatment weakens the '3 architectures' claim."

---

## Step 3: Convergence

**Agreed Strengths:**
- The question is important and timely; someone needs to answer it
- The experimental scale (3 models × 20–52 languages × all layers × 5 conditions × 3 benchmarks) is genuinely unprecedented
- CaCLR ablation is well-executed and the inert-consistency-loss finding is clean
- Difficulty-entanglement finding is the most novel result
- Honest reporting of negative results is commendable

**Agreed Weaknesses:**
1. **No statistical testing** on key small-effect claims (most critical gap)
2. **Arbitrary AUROC threshold** drives the headline narrative without sensitivity analysis
3. **CaCLR is underspecified** (which distance metric?) **and incoherently framed** (contribution vs. negative result)
4. **Predictability** — the resource-tier gradient follows from domain adaptation theory, which is not cited
5. **Missing related work** in alignment, probing critique, and representation similarity literature
6. **No mechanistic explanation** for why transfer fails at the representation level
7. **No constructive path forward** — pure diagnostic without solutions
8. **Gemma4 is thin** — per-language breakdowns and CaCLR results missing

**Resolved Disagreement:**
R1 initially scored 4 (Weak Accept), R2 scored 3 (Weak Reject). After cross-sharing:
- R1 concedes that without significance tests, the small-effect claims (decomposition, CaCLR vs linproj) are on shaky ground, and the arbitrary threshold weakens the narrative further
- R2 concedes the scale is real and the difficulty-entanglement finding is novel enough to have standalone value
- Both agree: for a top ML venue, the paper falls slightly below the bar. The combination of predictable main result + no working method + no mechanistic depth + statistical gaps is too much. For a venue like EACL that values systematic empirical work, it would be more competitive.

**Converged Score: 3/6 (Weak Reject)**

---

## Step 4: Consolidated Assessment

### Overall Score: 3/6 (Weak Reject)

### Meta-Review

This paper addresses a genuinely important question — whether probe-based calibration, a promising English-only research line, generalizes cross-lingually — and answers it at unprecedented scale. The experimental matrix (3 architectures × 20–52 languages × all probed layers × 5 transfer methods × 3 benchmarks) is ambitious and well-structured. The predominantly negative results are reported honestly, and the CaCLR ablation demonstrating that the consistency loss is inert is a clean piece of empirical work.

However, the paper falls below the acceptance threshold for a top ML venue for several compounding reasons:

**1. The main finding is predictable.** The resource-tier gradient in transfer failure follows from domain adaptation theory (Ben-David et al., 2010), which the paper neither cites nor engages with. Without theoretical grounding, the paper reads as confirming what cross-lingual NLP practitioners would expect: representations diverge with linguistic distance and training data scarcity, so English-trained probes fail on distant/low-resource languages. The paper would be substantially stronger if it derived predictions from transfer theory and then tested them, rather than presenting the gradient as a discovery.

**2. No working method and no mechanistic depth.** The paper proposes CaCLR, shows it doesn't work, and offers no alternative that does. The diagnostic framing is honest but leaves the reader with "things are broken" and no path to fixing them. More critically, the paper doesn't explain *why* things are broken at the representation level. A CKA or SVCCA analysis showing how cross-lingual representation similarity correlates with transfer success would provide the missing mechanistic story and transform this from a measurement paper into an insight paper.

**3. Statistical rigor gaps undermine key claims.** No significance tests or confidence intervals are reported for any comparison. The paper's narrative relies on small deltas: CaCLR vs. linear projection (0.3pp), decomposition effect (1.3–1.4pp), probe complexity (Cohen's d=0.18). Without statistical validation, these could be noise. The 0.65 AUROC threshold that drives the headline pass/fail rates is arbitrary and unjustified — the paper should include sensitivity analysis.

**4. CaCLR is underspecified and incoherently framed.** The consistency loss's distributional distance metric is never stated. CaCLR is simultaneously positioned as a methodological contribution and a negative result, creating a framing tension the paper doesn't resolve. The honest approach is to frame CaCLR purely as a natural baseline that demonstrates distributional matching doesn't work for this problem class.

**5. Incomplete third architecture and missing related work.** Gemma4 appears only in Table 5 — no per-language breakdown, no CaCLR evaluation, no decomposition results. The "3 architectures" claim is effectively "2 architectures + 1 summary row." The related work misses cross-lingual alignment (MUSE/VecMap), probing critiques (Hewitt & Liang 2019), representation similarity analysis (CKA/SVCCA), and domain adaptation theory.

### What Would Strengthen the Paper

1. Add significance tests (bootstrap CIs) for all key comparisons
2. Replace or supplement the arbitrary 0.65 threshold with continuous analysis (e.g., AUROC as a function of linguistic distance or training data size)
3. Add CKA/SVCCA analysis to provide mechanistic explanation for the Pareto frontier and transfer failures
4. Engage with domain adaptation theory to derive predictions before testing them
5. Complete Gemma4 evaluation to full parity with Qwen3/Llama4
6. Reframe CaCLR purely as a negative-result baseline, not a contribution
7. Offer concrete constructive directions (language-specific probes? multilingual probe training? adapter-based alignment?)

### Experiment Coverage vs. Design

Comparing the paper against the full experiment design (9 planned experiments):
- **Plans 1–3** (Qwen3/Llama4 Pareto + CaCLR): Fully covered in the paper with detailed tables
- **Plan 4** (Decomposition): Covered but at reduced scale (10 langs × 8 layers vs. full grid); rationale for subsampling not provided
- **Plan 5** (Orthogonality): Fully covered
- **Plan 6** (Probe complexity): Covered, appropriately treated as minor
- **Plan 7** (Cross-benchmark): Fully covered
- **Plan 8** (Gemma4): Only summary statistics — missing per-language detail, CaCLR evaluation, decomposition
- **Plan 9** (52 languages): Covered in Table 10 but only for Qwen3, not other architectures
- **Plan 10** (INT8 validation): Fully covered in appendix

Coverage is adequate for the core claims but thin for the extended analyses (Gemma4, 52-language). The paper would benefit from completing Gemma4 to full depth.

### Strengths to Preserve
- The scale and systematic design
- The CaCLR ablation methodology (β sweep + component ablation)
- The difficulty-entanglement finding and random-direction control
- The cross-benchmark validation approach
- The honest diagnostic framing

### Summary
A well-executed measurement study addressing an important question, but lacking the methodological contribution, theoretical depth, or mechanistic insight needed for a top ML venue. The difficulty-entanglement finding is the standout novel result. Recommended for resubmission with statistical tests, mechanistic analysis (CKA/SVCCA), engagement with transfer theory, and completed third-architecture evaluation.

---

**R1 Final Score: 4/6 → adjusted to 3/6**
**R2 Final Score: 3/6**
**Consolidated Score: 3/6 (Weak Reject)**
**Confidence: 4/5 (High)**