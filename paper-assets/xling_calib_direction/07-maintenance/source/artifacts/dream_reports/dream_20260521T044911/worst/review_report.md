---
dream_id: dream_20260521T044911
tier: worst
overall_score: 2/5 — Reject (with encouragement to revise around control task contribution)
timestamp: 2026-05-21T06:12:19.620172+00:00
---

# Dream Review Report — Full Roundtable

**Paper**: "The Limits of Cross-Lingual Calibration Probe Transfer: A Large-Scale Negative Result with Methodological Implications"
**Venue**: ACL ARR (1–5 scale: Soundness, Excitement, Overall)
**Review mode**: full (2 Reviewers, 4-step roundtable)

---

## Step 1: Independent Reviews

### R1 — Methods & Experiments

#### Summary
This paper presents a large-scale negative result on cross-lingual correctness probe transfer across 3 architectures, 20 languages, and 5 transfer conditions. The experimental design is comprehensive (2,400+ language–layer–condition combinations), with appropriate controls including Hewitt & Liang selectivity, random-direction baselines, and quantization validation. The strongest finding is the control task analysis revealing 37–42% artifact rates in mid/low-resource language–layer combinations.

#### Strengths
- **S1 (Scale & coverage)**: 3 architectures (2 MoE + 1 dense), 20 languages across 3 resource tiers, 12–24 probed layers per model, 5 transfer conditions. Camera-ready extensions to 52 languages and additional architecture. This is among the most comprehensive probing studies in cross-lingual NLP.
- **S2 (Control methodology)**: The Hewitt & Liang selectivity extension to cross-lingual settings is well-executed. The selectivity–AUROC correlation (ρ=0.68, p<0.001) is a striking finding with clear implications. Artifact rate tables by tier, model, and depth range (Table 10, 12) are thorough.
- **S3 (CaCLR ablation thoroughness)**: The β sweep across 3 orders of magnitude (0.001–1.0) with component ablation (BCE-only, BCE+SB-ECE, BCE+MMD, full) systematically eliminates each component. The monotonic degradation pattern is convincing.
- **S4 (Simpson's Paradox falsification)**: Clean comparison of 5-language pilot vs. 20-language full-scale partial correlations (Llama ρ: +0.41→+0.08). Same-layer cross-language analysis (Table 7) provides an independent test.
- **S5 (Random-direction control for decomposition)**: Comparing difficulty projection (Δ=−0.003) against random-direction projection (Δ=−0.005) with paired test (p=0.42) is a clean null-result demonstration.
- **S6 (Quantization validation)**: Testing FP16 vs. quantized at 5 depth percentiles (Table 18/22) is responsible. Reporting rank preservation alongside AUROC delta is good practice.

#### Weaknesses
- **W1 (Quantization confound not fully resolved)**: All three production models are quantized (INT4/W4A16). The validation shows increasing bias with depth: Qwen INT4 Δ reaches −0.022 at 95% depth, with rank disruption at ≥60% depth. Since the paper's key conclusions involve deep-layer probes (EN-optimal layers at 72/40/48), the 1–2pp systematic bias is non-negligible. The paper acknowledges this in Limitations but understates the impact: claims about absolute AUROC values at deep layers are systematically affected. A stronger treatment would re-derive all headline numbers with quantization-corrected confidence intervals.
- **W2 (CaCLR structural limitation is predictable)**: The paper designs CaCLR to operate MMD on 1-D probe logits, then reports that 1-D MMD cannot capture directional structure. This is a foreseeable design limitation, not a surprising negative result. A stronger design would have compared MMD in representation space (pre-probe, high-dimensional) vs. logit space. The paper's Discussion acknowledges the 1-D limitation but does not test the obvious alternative. This weakens the claim that "distributional matching fails" — what fails is 1-D marginal matching specifically.
- **W3 (Difficulty probe quality too low for definitive conclusion)**: The IRT difficulty probe achieves R²=0.31, meaning it captures only 31% of difficulty variance. The decomposition test projects out this weak direction — but if the difficulty direction is poorly estimated, projecting it out is almost the same as projecting out a random direction. The paired test (p=0.42) conflates "decomposition doesn't help" with "our difficulty probe isn't good enough to enable a clean test." The paper should discuss this ambiguity.
- **W4 (MoE vs. dense comparison confounded with scale)**: Qwen3-235B (MoE, 22B active) and Llama 4 Scout (MoE, 17B active) are compared against Gemma 4 31B (Dense, 31B). The architecture comparison is confounded with model scale and training data. The paper attributes non-monotonic depth patterns to MoE routing, but this hypothesis is not tested against scale-matched dense models.
- **W5 (ZS "pass" threshold arbitrary)**: The 0.55 AUROC threshold for "passing" zero-shot transfer is not justified. It's described as "chance + meaningful margin" but chance for binary classification is 0.50. Whether 0.55 represents a meaningful margin depends on the application. A sensitivity analysis across thresholds (0.52, 0.55, 0.58) would strengthen the claims about pass rates.
- **W6 (Missing statistical details)**: (a) Bonferroni correction is mentioned but not applied consistently — Table 1 reports hi (p=0.041) as significant with n=20 languages, where Bonferroni threshold would be 0.0025. (b) Bootstrap CI widths for artifact rates (Table 10) are not reported. (c) Effect sizes (Cohen's d) are missing for most comparisons.

#### Questions for Authors
- Q1: Why not test MMD in the high-dimensional representation space rather than 1-D logit space? This seems like the natural stronger baseline for distributional matching.
- Q2: With Bonferroni correction for 20 languages, hi (p=0.041) in Table 1 would not be significant. Do any per-language Pareto results survive multiple-comparison correction?
- Q3: The selectivity < 0.05 threshold for "capacity artifact" — how sensitive are the artifact rates to this threshold? What are the rates at 0.03 and 0.10?
- Q4: The quantization validation uses a 5% data subset. How was this subset selected, and could it introduce sampling bias?

#### Minor Issues
- Table 1 caption says "Only hi reaches p<0.05" but this does not survive Bonferroni correction
- Mean-shift ΔAUROC ≡ 0 is presented as an empirical finding but is a mathematical identity under StandardScaler + LR — should be stated as such (it is mentioned in text but the table presentation is misleading)
- Section 3.4 (Difficulty Decomposition) is very brief — 3 sentences for a full experimental component
- Several references in Related Work appear to be unnamed/incomplete (likely anonymization artifacts)
- Appendix sections B–E are listed but appear empty in the submitted PDF

#### Scores
- **Soundness**: 3/5 (Acceptable — sufficient support for main claims but with notable methodological caveats)
- **Excitement**: 2/5 (Mediocre — most negative results are unsurprising; control task finding is the standout)
- **Overall**: 2/5 (Reject — needs revision to address quantization confound, CaCLR design limitation, and statistical rigor issues)
- **Confidence**: 4/5

---

### R2 — Novelty & Related Work

#### Summary
The paper frames itself as the "first large-scale study" of cross-lingual correctness probe transfer, extending English-only work (Miao & Ungar) and the authors' own pilot study to 3 large architectures and 20 languages. The core narrative is a series of negative results (Pareto generalization failure, CaCLR failure, decomposition failure, CKA artifact) bookended by a methodological contribution (control task artifact rates). The framing as a negative result paper is reasonable but the contribution density is uneven.

#### Strengths
- **S1 (Genuine methodological novelty in control tasks)**: The extension of Hewitt & Liang (2019) selectivity to cross-lingual probing appears genuinely novel. No prior work has systematically applied control tasks to cross-lingual probe transfer. The finding that 37% of *mid-resource* language–layer combinations are artifacts — not just low-resource — has broader implications for the cross-lingual probing literature (where mid-resource languages like ar, hi, ko are commonly studied).
- **S2 (Scale of negative result is informative)**: Closing two candidate paths (distributional matching + geometric alignment) simultaneously, with component-level ablations, is a useful community contribution. The CaCLR sweep data, if released, would save others from repeating these experiments.
- **S3 (Simpson's Paradox as cautionary tale)**: The 5-language → 20-language collapse of the CKA partial correlation is a well-told cautionary tale about small-sample multilingual studies. The insight that pilot samples can systematically overrepresent languages with the strongest effects is broadly relevant.
- **S4 (Honest about practical limitations)**: The paper does not oversell linear projection — the "inconsistent reversal threshold" (0.48–0.68 overlap zone) is reported transparently rather than swept under the rug.
- **S5 (Good theoretical grounding)**: CaCLR failure is connected to Zhao et al. (2019) conditional distribution theory. The 1-D structural limitation is theoretically motivated. Ben-David's H-divergence framework is appropriately cited.

#### Weaknesses
- **W1 (Novelty of negative results is inherently limited)**: The paper's four main negative results (Pareto, CaCLR, decomposition, CKA) are individually unsurprising: (a) MoE non-monotonicity is expected from expert routing; (b) 1-D MMD failure is predictable; (c) IRT decomposition with R²=0.31 is too weak to be informative; (d) 5-language pilot results failing to scale is common in multilingual NLP. The aggregate pattern is more interesting than any individual result, but the paper treats each as a separate contribution.
- **W2 (Missing related work)**: Several important references appear absent or unnamed: (a) Pires et al. (2019) and Wu & Dredze (2019, 2020) on multilingual BERT representation analysis; (b) Muller et al. (2021) on language-specific vs. shared representations; (c) Stanczak et al. (2022) on cross-lingual probing surveys; (d) Chi et al. (2020) on multilingual syntactic structure. The Related Work section (§2) uses unnamed citations in several places, which is likely an anonymization issue but creates gaps.
- **W3 (Relationship to pilot work unclear)**: The paper is clearly an extension of the authors' own pilot study on Qwen2.5-7B and Llama-3.1-8B. However, the pilot is referenced obliquely ("prior pilot studies", "small dense models"). The contribution relative to the pilot should be more explicitly stated: what was found in the pilot that doesn't hold up, what is genuinely new, what is confirmed at scale.
- **W4 (Contribution hierarchy is debatable)**: The paper ranks control tasks > negative result > practical guidance. But the control task finding, while novel, is a single observation (artifact rate by tier) rather than a full methodological framework. It does not propose a solution — it just says "include control tasks." The negative result is the bulk of the paper but is individually unsurprising. The practical guidance is acknowledged to be weak. This leaves the paper without a strong central contribution.
- **W5 (Writing gaps)**: (a) Section 3.4 (Difficulty Decomposition) is 3 sentences — insufficient for a full experimental component; (b) Appendix sections B–E are listed but appear empty; (c) the paper is 14 pages (10 main + 4 appendix) but Appendix is sparse; (d) several Related Work citations appear unnamed.
- **W6 (Negative result bar is high)**: For ACL venues, negative result papers need to be either (a) debunking a widely-held belief, or (b) providing a methodological framework that changes future practice. This paper debunks a pilot study result (which hasn't been widely adopted) rather than a community-wide assumption. The control task methodology is the strongest candidate for (b), but it's a single table and recommendation rather than a framework.

#### Questions for Authors
- Q1: Can you clarify the relationship between this paper and the pilot study? Is the pilot published or also under review? Understanding the incremental contribution requires knowing what the pilot established.
- Q2: Why not test distributional matching in the representation space (high-dimensional) rather than only in the 1-D logit space? This seems like an obvious extension that would strengthen the negative result.
- Q3: The selectivity finding (ρ=0.68 with ZS AUROC) has a strong causal implication — that many cross-lingual transfer "successes" are artifacts. Have you checked whether this correlation holds controlling for resource tier? It could be driven by the tier confound (low-resource = low selectivity AND low AUROC).
- Q4: For the 52-language extension (Appendix A), are these fully new experiments or extrapolations? The sparse Appendix raises concerns about completeness.

#### Minor Issues
- The title "A Large-Scale Negative Result with Methodological Implications" sets expectations that the methodology section is strong — but §3.4 is 3 sentences
- Table 5 presents CaCLR "best" but best β is 0.001 with Δ=−0.003 — calling it "best" is misleading when all are negative
- The paper uses "first" multiple times without sufficient verification of priority claims
- Anonymization appears incomplete (unnamed citations in Related Work)

#### Scores
- **Soundness**: 3/5 (Acceptable — the methodology is mostly appropriate, but related work gaps and the CaCLR design limitation weaken the claims)
- **Excitement**: 2/5 (Mediocre — control task finding has appeal but most negative results are predictable)
- **Overall**: 3/5 (Borderline — the aggregate negative result and control task contribution have value, but individual findings lack surprise)
- **Confidence**: 4/5

---

## Step 2: Cross-Share

### R1 → R2 shared findings:
- The quantization confound (W1) is more severe than acknowledged: 1–2pp systematic bias at deep layers affects all three models and all headline AUROC numbers
- CaCLR's 1-D limitation (W2) is a design flaw, not a genuine negative result about distributional matching in general
- Statistical issues: Bonferroni correction eliminates the only per-language significant Pareto result (hi, p=0.041 > 0.0025 Bonferroni threshold)
- Difficulty decomposition is hampered by poor difficulty probe quality (R²=0.31)

### R2 → R1 shared findings:
- The novelty concern (W1, W4) applies to methodological evaluation too: if each negative result is predictable, the aggregate value depends on scale and thoroughness rather than surprise
- Related work gaps (W2) suggest positioning may overstate novelty ("first" claims)
- The pilot relationship (W3) is important for evaluating whether this is a genuine new contribution or an extended pilot
- The contribution hierarchy is inverted: the paper devotes most space to the weakest contributions (Pareto, CaCLR) and least space to the strongest (control tasks, §3.3 and §5.5)

---

## Step 3: Convergence

### Points of Agreement
1. **Control task finding is the strongest contribution** (both R1 and R2). The 37% mid-resource artifact rate has genuine field-level implications. However, both agree this contribution is underdeveloped — it occupies ~1.5 pages of a 14-page paper.
2. **CaCLR failure is partly predictable** (R1-W2, R2-W1b). The 1-D logit space limitation makes the failure foreseeable. The absence of a representation-space MMD comparison weakens the "distributional matching fails" claim.
3. **Statistical rigor has gaps** (R1-W6, R2-W5). Bonferroni correction, bootstrap CIs, and effect sizes are inconsistently reported.
4. **Writing has notable gaps** (R1 minor, R2-W5). Section 3.4 is too brief; appendix sections appear empty; related work has unnamed citations.
5. **Quantization confound is a real concern** (R1-W1). 1–2pp bias at deep layers affects absolute numbers, though not the direction of negative results.

### Points of Disagreement → Resolution
1. **Overall score**: R1 gives 2/5, R2 gives 3/5. R1's concerns about methodological flaws (quantization, CaCLR design, statistical rigor) are concrete and affect the paper's soundness. R2's borderline assessment gives more credit to the aggregate negative result and control task novelty. **Resolution**: The paper has genuine value (control tasks, scale, Simpson's Paradox cautionary tale) but also has substantial methodological issues that would need addressing in revision. **Converged: 2.5 → round to 2/5** given that the methodological flaws (especially CaCLR design, difficulty probe quality, statistical rigor) are core issues, not surface problems.
2. **Excitement**: Both give 2/5. The control task finding could push excitement up, but it's underdeveloped. **Converged: 2/5**.

---

## Step 4: Consolidated Report

### Paper Summary
This paper presents a large-scale study of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20 languages, and 5 transfer conditions. The results are predominantly negative: the depth–transferability Pareto frontier observed in small dense pilot models does not generalize to large-scale MoE architectures; CaCLR distributional matching is uniformly harmful; difficulty decomposition is indistinguishable from random-direction controls; and the CKA geometric explanation from a 5-language pilot is confirmed as a small-sample artifact. The paper's strongest contribution is methodological: extending Hewitt & Liang selectivity controls to cross-lingual probing reveals that 42% of low-resource and 37% of mid-resource language–layer probing results are capacity artifacts.

### Consolidated Strengths
- **S1 (Scale)**: 2,400+ language–layer–condition combinations across 3 architectures, with camera-ready extensions to 52 languages. Among the most comprehensive cross-lingual probing studies to date.
- **S2 (Control task methodology)**: The first application of Hewitt & Liang selectivity to cross-lingual probing. The 37% mid-resource artifact rate is a field-relevant finding that challenges existing cross-lingual probing literature.
- **S3 (Systematic ablation)**: CaCLR β sweep (3 OOM), component ablation, α sweep, and comparison across 5 transfer conditions provide thorough elimination of the distributional matching path.
- **S4 (Simpson's Paradox falsification)**: Well-executed demonstration that 5-language pilot results inflate effect sizes, with same-layer cross-language analysis as independent verification.
- **S5 (Transparency)**: Honest reporting of weak practical guidance (inconsistent reversal thresholds), quantization limitations, and format-specificity concerns.

### Consolidated Weaknesses
- **W1 (CaCLR design flaw ≠ general distributional matching failure)**: CaCLR operates MMD on 1-D probe logits, a structurally insufficient space for matching directional information. The paper does not test the natural alternative — MMD in high-dimensional representation space. The claim that "distributional matching fails" is overstated; what fails is 1-D marginal matching. This is predictable from first principles and Zhao et al.'s theory. A stronger paper would test and reject higher-dimensional matching.
- **W2 (Quantization confound)**: All three models use quantized inference. The validation shows systematic depth-dependent bias (up to −0.022 AUROC at 95% depth), with rank disruption at ≥60% depth for both models. Since the paper's conclusions rely on deep-layer probes, this confound is non-trivial. The paper should either (a) derive quantization-corrected confidence intervals for headline numbers, or (b) include at least one FP16 model.
- **W3 (Statistical rigor gaps)**: (a) Bonferroni correction would eliminate the only per-language significant Pareto result (hi, p=0.041 > 0.05/20=0.0025); the paper claims Bonferroni is applied but does not reflect this in Table 1. (b) Bootstrap CIs for artifact rates are not reported. (c) Effect sizes (Cohen's d) are missing throughout. (d) The ZS "pass" threshold (0.55) and selectivity artifact threshold (0.05) are not justified or sensitivity-tested.
- **W4 (Difficulty decomposition is inconclusive, not negative)**: The IRT difficulty probe achieves only R²=0.31. Projecting out a poorly estimated direction is nearly equivalent to projecting out a random direction — the paired test (p=0.42) cannot distinguish "decomposition doesn't work" from "our difficulty estimate is too noisy." The paper should present this as an inconclusive result rather than a definitive negative.
- **W5 (Contribution structure is inverted)**: The paper devotes most space to its weakest contributions (Pareto: §5.1, CaCLR: §5.2, CKA: §5.3, Decomposition: §5.4) and least to its strongest (Control Tasks: §5.5 is ~1.5 pages; Method §3.3 is 4 sentences). The narrative would be stronger if the control task methodology were central and the other negative results were presented as supporting context.
- **W6 (Missing comparisons and related work)**: (a) No representation-space distributional matching baseline. (b) No comparison with other alignment methods (CCA, ICP). (c) Related work omits Pires et al. (2019), Wu & Dredze (2019), and other cross-lingual representation studies. (d) Several citations appear unnamed (anonymization artifacts). (e) Relationship to authors' pilot study is unclear.
- **W7 (Writing issues)**: (a) Section 3.4 is 3 sentences for a full experimental component. (b) Appendix B–E listed but appear empty in submitted version. (c) Mean-shift ΔAUROC ≡ 0 is a mathematical identity presented as an empirical finding. (d) "CaCLR (best)" in Table 5 is misleading when all configurations are negative.

### Consolidated Questions
1. Why not test MMD in the high-dimensional representation space? This is the natural ablation to distinguish "1-D matching fails" from "distributional matching fails."
2. Do any per-language Pareto results survive Bonferroni correction (0.05/20 = 0.0025)?
3. How sensitive are artifact rates to the selectivity < 0.05 threshold? Rates at 0.03 and 0.10 would help assess robustness.
4. Does the selectivity–AUROC correlation (ρ=0.68) survive controlling for resource tier?
5. What is the relationship between this paper and the pilot study on Qwen2.5-7B / Llama-3.1-8B?
6. The 52-language extension and Gemma results are in Appendix — are these fully computed or placeholders?

### Consolidated Scores

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3 | 3 | **3/5** (Acceptable) |
| Excitement | 2 | 2 | **2/5** (Mediocre) |
| Overall | 2 | 3 | **2/5** (Reject) |
| Confidence | 4 | 4 | **4/5** |

### Score Justification

**Soundness 3/5**: The experimental setup is comprehensive in scale but has methodological issues that undermine several claims. The CaCLR design flaw (1-D MMD) makes its failure uninformative about distributional matching in general. The difficulty decomposition is inconclusive due to poor difficulty probe quality (R²=0.31). The quantization confound creates systematic bias at deep layers. Statistical reporting is inconsistent (Bonferroni not properly reflected; CIs and effect sizes missing). The control task methodology is the most sound component, but it is underdeveloped in the paper.

**Excitement 2/5**: The individual negative results are largely predictable: MoE non-monotonicity, 1-D MMD failure, small-sample pilot inflation. The control task artifact rate finding has genuine excitement — it challenges existing literature — but is not developed into a full methodological framework. The practical guidance is acknowledged to be weak (inconsistent thresholds). The paper fills a gap (large-scale cross-lingual probing evaluation) but does not produce surprising insights beyond "pilot results don't scale" and "include control tasks."

**Overall 2/5 (Reject with encouragement to revise)**: The paper attempts an ambitious scope and has genuine value — particularly the control task methodology and the cautionary tale about small-sample multilingual studies. However, the current version has too many methodological issues for acceptance: (a) the CaCLR claim overstates the negative result by not testing representation-space matching; (b) statistical rigor is inconsistent; (c) the contribution structure is inverted, burying the strongest finding; (d) writing has notable gaps (§3.4, empty appendices, unnamed citations). A revision that (1) restructures around the control task contribution, (2) adds representation-space MMD, (3) fixes statistical reporting, and (4) acknowledges difficulty decomposition as inconclusive rather than negative could make this a borderline accept.

### Recommendation for Revision
1. **Restructure**: Make control task methodology the central contribution; frame other negative results as supporting evidence
2. **Add representation-space MMD**: Test MMD in high-dimensional space to make the distributional matching claim credible
3. **Fix statistics**: Apply Bonferroni consistently, add bootstrap CIs for artifact rates, report effect sizes, sensitivity-test thresholds
4. **Expand §3.3/3.4**: Control task and difficulty decomposition methods need more detail
5. **Complete appendix**: Fill empty sections B–E
6. **Address quantization**: Add corrected confidence intervals or include one FP16 model
7. **Clarify pilot relationship**: State explicitly what the pilot found and what this paper adds

### Experiment Coverage Assessment
The paper covers all 13 imagined experiments from the experimental design (review_context.yaml):
- ✅ plan_001: Qwen3-235B Pareto (§5.1, Table 1)
- ✅ plan_002: Llama 4 Scout Pareto (§5.1, Table 2)
- ✅ plan_003: CaCLR evaluation (§5.2, Tables 3–5)
- ✅ plan_004: Difficulty decomposition (§5.4, Table 9)
- ✅ plan_005: Cross-lingual orthogonality (§5.9, Table 23)
- ✅ plan_006: Probe complexity (§5.8, Table 17)
- ✅ plan_007: Additional benchmarks (§5.7, Table 16)
- ✅ plan_008: Gemma 4 31B (§5.1, Appendix B, Table 20)
- ✅ plan_009: 52-language extension (Appendix A, Table 19)
- ✅ plan_010: Quantization validation (§4, §5.8, Tables 18, 22)
- ✅ plan_011: CKA analysis (§5.3, Tables 6–8)
- ✅ plan_012: Linear projection sensitivity (§5.6, Tables 13–15)
- ✅ plan_013: Control tasks (§5.5, Tables 10–12)

Coverage is complete. All imagined experiments are represented in the paper, though some (Gemma, 52-language) are in sparse appendix sections.