---
dream_id: dream_20260518T125925
tier: worst
overall_score: weak reject
timestamp: 2026-05-18T14:02:13.054973+00:00
---

# Dream Review Report: "Do Sycophancy Directions Transfer to Training Rewards?"

**Dream ID**: 20260518T125925
**Review Mode**: Full (2 Reviewers + Roundtable)
**Paper**: "Do Sycophancy Directions Transfer to Training Rewards? Boundary Conditions of Representation-Level Signals for Multi-Turn Belief Revision"

---

## Reviewer Assignments

- **R1**: Methodology soundness + Experimental rigor
- **R2**: Novelty + Significance + Related work

---

## Step 1: Independent Reviews

### Reviewer R1 — Methods & Experiments

**Score: 3/6 (Weak Reject)**

#### Strengths

1. **Intellectually honest framing.** Reports a negative result transparently. Title and abstract accurately convey that DC-GRPO does not outperform simpler alternatives.
2. **Comprehensive experiment coverage.** 15 experiments systematically isolate design decisions: calibration quality, main comparison, 4 baselines, stability monitoring, disagreement analysis, ablations, turn-depth, cross-model transfer, three-way design, weight sensitivity.
3. **Continuous Probe baseline is the decisive experiment.** Cleanly separates signal continuity from directional geometry, yielding the paper's most informative finding.
4. **Direction stability monitoring is valuable.** Tracking cosine similarity and held-out AUROC throughout training provides practical guidance. Diminishing returns of recalibration (post-recalib cosine: 0.92 → 0.91 → 0.90) is a genuine contribution.
5. **Layer-wise emergence analysis is interpretable.** Progression from chance (L0: 0.52) to peak (L19: 0.801) with cross-model consistency (Llama peak at L18) is informative about architectural generality.
6. **Turn-depth analysis tests a specific mechanistic hypothesis.** The constant ~1.3pp advantage across turn depths directly falsifies the hypothesis that directional geometry captures commitment-specific mechanisms.
7. **Weight sensitivity has a clear message.** Monotonic degradation with increasing R1 weight, optimal trending toward zero, provides direct evidence for the negative conclusion.
8. **ACT baseline demonstrates the double-bind concretely.** WRR 0.571 falling below all targeted methods confirms undifferentiated constraints are counterproductive.

#### Weaknesses

1. **[Critical] 3 seeds is insufficient for the claims made.** Paired t-tests with 2 degrees of freedom cannot reliably support either positive or negative conclusions. The critical t-value at 2 df is 4.303; only very large effects can achieve significance. The central claim (DC-GRPO vs R3-only, p=0.187) is indistinguishable from "underpowered study." This is the paper's most serious limitation.
2. **[Major] R2 is not an independent reward component.** R2 assigns rewards based on rank ordering of R1 scores within a GRPO group. It carries no information independent of R1 — it is a monotonic transformation. The "three-component reward" framing is misleading. The ablation (R1+R2 vs R1-only: 0.375 vs 0.398) may reflect benefits of relative scaling, not independent signal.
3. **[Major] RC-AUC is undefined.** This composite metric is used throughout Results and Discussion but never formally specified (what threshold is swept, over what range). Not reproducible.
4. **[Major] Missing inference-time steering baseline.** Activation Addition using d_syc at inference time is the zero-training-cost alternative. If it achieves comparable NoF reduction, the entire training framework is unnecessary. Its absence is a significant gap.
5. **[Major] R1 uses unnormalized dot product.** Equation 2: R1 = -⟨h, d_syc⟩ conflates directional alignment with activation magnitude. Cosine similarity would be more principled. This design flaw could inject noise, potentially explaining part of R1's poor performance.
6. **[Moderate] R1-R3 initial correlation not reported.** Without knowing pre-training R1-R3 correlation, the paper cannot determine whether the direction ever provided independent information. If correlation is already high at step 0, the direction was always redundant.
7. **[Moderate] Direction drift lacks causal analysis.** The paper describes drift but doesn't analyze what drives it (LoRA updates? residual stream shifts? layer-specific vs global?). Without understanding the cause, prescriptive conclusions about RepE-as-reward are premature.
8. **[Moderate] Multiple comparisons uncorrected.** 8 pairwise tests in Table 7 without correction. Family-wise error rate exceeds 33%. The two significant results (DC-GRPO vs ACT) would not survive Bonferroni correction (adjusted alpha = 0.00625).
9. **[Moderate] Human validation sample too small.** 8 manually checked disagreement cases with 3 confirmed. Wilson 95% CI on true positive rate: [8%, 75%]. Uninformative.
10. **[Moderate] Calibration data generation undocumented.** Source model, filtering criteria (11 pairs removed), and quality control not described. If pairs were generated by Qwen3-8B itself, d_syc may capture generation artifacts.
11. **[Minor] PCA_1 vs mean-difference not compared.** Uses PCA_1 without justification or ablation against the standard RepE mean-difference approach.
12. **[Minor] No proper bibliography.** References are informal in-text mentions without \cite{} or bibliography entries.
13. **[Minor] Recalibration threshold (0.70) unjustified and not ablated.**

#### Questions for Authors (R1)

1. What is the R1-R3 Pearson correlation at step 0 on calibration data?
2. Why PCA_1 rather than mean-difference (standard RepE)?
3. Why raw dot product in R1 rather than cosine similarity?
4. Formal definition of RC-AUC?
5. Which model generated the 200 contrastive pairs?
6. Have you tested inference-time activation steering as a zero-cost alternative?
7. What sample size would be needed to detect the observed 1.3pp effect at 80% power?
8. What drives the R1-R3 correlation collapse — genuine convergence, drift, or inherent collinearity?
9. What drives diminishing post-recalibration cosine (0.92 → 0.91 → 0.90)?
10. Were disagreement annotators blind to which reward flagged the case?

---

### Reviewer R2 — Novelty & Related Work

**Score: 3/6 (Weak Reject)**

#### Strengths

1. **Exemplary intellectual honesty.** The paper does not overclaim. The title frames a question, the abstract states the negative answer, the contributions list includes negative findings. This transparency is rare and valuable.
2. **Evidence-strength stratification is a sound design choice.** Breaking calibration data into weak/medium/strong evidence categories reveals the clinically important finding that d_syc discriminability is worst where sycophancy matters most (weak evidence: AUROC 0.773).
3. **Direction stability tracking is a reusable diagnostic.** The methodology for monitoring cosine similarity and held-out AUROC during training is applicable to any RepE-as-reward setting.
4. **Appropriate baseline coverage.** R3-only, ACT-style, Binary Probe, and Continuous Probe collectively isolate behavioral vs representational, targeted vs undifferentiated, and directional vs continuous signal dimensions.
5. **Style-controlled contrastive pair construction.** Controlling for surface style to isolate cognitive content is methodologically careful.

#### Weaknesses

1. **[Critical] Scope-claim mismatch.** The paper promises "boundary conditions" for representation-level training rewards but tests a single method configuration (PCA direction + dot-product reward + fixed recalibration) on one model (Qwen3-8B) at one scale (8B). This is a single data point, not a boundary map. True boundary conditions would require varying: (a) direction extraction method (PCA vs CCS vs learned probe vs cluster centroid), (b) reward integration (dot product vs cosine vs probability), (c) training algorithm (GRPO vs PPO vs DPO), (d) model scale, (e) task domain. The paper tests (b) partially via Continuous Probe and (d) partially via Llama, but remains far from the claimed scope.
2. **[Critical] Insufficient statistical power for null claims.** Same as R1's W1. 3 seeds cannot establish a negative result. The p=0.187 is compatible with both "no effect" and "small effect, underpowered." The paper needs either more seeds or explicit power analysis showing the study can detect relevant effect sizes.
3. **[Major] Missing CRAFT comparison and analysis.** CRAFT demonstrates that hidden-state GRPO rewards work for safety alignment. The paper reports failure for sycophancy with the same paradigm but never explains the divergence. Is sycophancy harder to encode directionally than safety concepts? Is CRAFT's prototype-clustering approach more robust than PCA direction extraction? Does CRAFT's reward formulation avoid the drift problem? This is the single most important missing analysis for establishing true "boundary conditions."
4. **[Major] Thin related work.** The paper cites approximately 15 works informally (no proper bibliography). A venue-ready paper on this topic should cite 30+ works. Key omissions include:
   - The original RepE paper (Zou et al., 2023) — cited only as "Representation Engineering" without proper reference
   - CCS (Burns et al., 2023) — mentioned but not properly cited
   - Activation Addition (Turner et al., 2023) — mentioned but not cited
   - Steering vector critique literature
   - INTUITOR and related internal-state probing during RL
   - Multi-turn dialogue safety literature beyond TRUTH DECAY
   - Reward model literature (reward hacking, reward misspecification)
5. **[Major] Novelty is limited.** The methodological contribution (DC-GRPO) is a straightforward combination of RepE direction extraction + GRPO reward integration. PCA on contrastive pairs is standard RepE. Using the projection as a reward is the natural extension. The negative result is the main contribution, but its interpretive value is limited by the implementation issues R1 identified (unnormalized R1, dependent R2, underpowered tests).
6. **[Moderate] The continuous probe equivalence undermines the entire framing.** If a logistic regression probe achieves equal or better results than directional projection without recalibration, the paper's exploration of directional geometry per se is moot. The real question becomes "do any representation-level signals help beyond behavioral rewards?" — and the answer (Cont. Probe vs R3-only: p=0.098, not significant at 0.05) is also negative. The paper partially recognizes this but doesn't restructure its narrative accordingly.
7. **[Moderate] Three-way decomposition (Exp 13) is underpowered.** Only 60 neutral pairs. The finding that d_gen and d_syc have cosine -0.82 is interesting but the sample is too small for reliable PCA estimation in high-dimensional space.
8. **[Moderate] Cross-model analysis is incomplete.** Llama AUROC 0.731 < 0.75 gate, so Phase B (training) was skipped. The paper therefore has zero evidence about whether DC-GRPO transfers across models. The claim about "model-family-specific geometry" rests entirely on Phase A (direction extraction), which is a weaker finding.

#### Questions for Authors (R2)

1. How do you reconcile your negative result with CRAFT's positive results for safety-related hidden-state rewards in GRPO? What is the key difference?
2. The paper claims to establish "boundary conditions" — can you enumerate the specific conditions you've mapped? Which conditions must change for the approach to succeed?
3. If you had 10 seeds instead of 3, and the DC-GRPO vs R3-only difference remained at 1.3pp but became significant (p<0.05), would you consider that a meaningful practical improvement?
4. Why not test DC-GRPO with cosine similarity instead of dot product as R1? This seems like a natural alternative that could address the magnitude confound.
5. Have you considered that the multi-turn dialogue setting may be uniquely difficult for directional rewards (due to context-length effects on activations), and that single-turn sycophancy might be more amenable?
6. The paper mentions the Knowledge-Prediction Gap literature reporting 13-29% disagreement in factual QA. You find 3.4% in multi-turn dialogue. Is this difference driven by the task (multi-turn vs single-turn), the model (Qwen3-8B vs larger models), or the measurement method (R1 probe vs specialized probes)?

---

## Step 2: Cross-Sharing

After exchanging reviews, both reviewers noted convergence on the following:

**Shared critical concerns:**
- Both independently rated 3/6 (Weak Reject)
- Both flagged 3 seeds as the most critical methodological issue
- Both identified the missing inference-time steering baseline
- Both noted the paper's intellectual honesty as its strongest quality

**Complementary insights:**
- R1 provides granular method-level critiques (R2 dependent on R1, unnormalized dot product, undefined RC-AUC, initial R1-R3 correlation) that R2 did not focus on
- R2 provides higher-level framing critiques (scope-claim mismatch, missing CRAFT comparison, thin related work, limited novelty) that R1 touched on less
- R1's observation that "the negative result is only as strong as the method it tests" and R2's observation that "this is a data point, not a boundary map" are two sides of the same coin: the paper cannot distinguish "directional rewards don't work" from "this specific implementation doesn't work"

**Points of tension:**
- R1 is somewhat more positive about the paper's experimental coverage (S2: "comprehensive"), while R2 views the same coverage as insufficient for the "boundary conditions" claim
- Both agree the continuous probe baseline is the most informative experiment, but R2 argues it undermines the paper's framing more fundamentally than R1 acknowledges

---

## Step 3: Convergence Discussion

Both reviewers agreed on the following assessment after discussion:

**The paper's core problem is an ambiguity it cannot resolve with its current design.** The negative result (DC-GRPO ≈ R3-only) could mean:
- (a) Directional geometry genuinely adds no training value beyond behavioral rewards — a meaningful negative finding
- (b) This specific implementation (unnormalized dot product, PCA_1 direction, fixed recalibration threshold, dependent R2) is suboptimal — a methodological failure, not a conceptual finding
- (c) The study lacks power to detect a real but small effect — a design limitation

The paper implicitly claims (a), but cannot rule out (b) or (c). The strongest evidence for (a) is the continuous probe comparison, which suggests that even well-implemented representation-level signals don't help. But Cont. Probe vs R3-only is also non-significant (p=0.098), so this too could be (c).

**Agreed recommendations for improvement:**
1. Increase to 5-10 seeds for primary comparisons
2. Use cosine similarity in R1 and test as a separate configuration
3. Include inference-time activation steering baseline
4. Report initial (step-0) R1-R3 correlation
5. Add CRAFT comparison or detailed analysis of why CRAFT succeeds where DC-GRPO fails
6. Formally define RC-AUC
7. Expand related work to 30+ properly cited references
8. Add power analysis for the DC-GRPO vs R3-only comparison
9. Narrow the "boundary conditions" claim to match the actual scope

**Agreed final scores:** Both maintain 3/6 (Weak Reject).

---

## Step 4: Consolidated Assessment

### Overall Score: 3/6 (Weak Reject)

### Summary

The paper investigates whether linear directions in LLM activation space that distinguish sycophantic from genuine responses can serve as training reward signals for multi-turn sycophancy reduction. The proposed DC-GRPO method combines directional projection, rank-based contrastive, and NLI behavioral rewards within GRPO. The paper reports a negative result: DC-GRPO does not significantly outperform behavioral-reward-only training, and a simpler continuous probe achieves equivalent results without directional decomposition. Direction drift during training, low R1-R3 disagreement (3.4%), and high R1-R3 correlation (r>0.9 after step 4000) are offered as explanations.

### Decision Rationale

**The paper does not meet the acceptance bar for a top ML venue** for the following reasons, ordered by severity:

1. **Underpowered statistical design undermines the central claim.** With only 3 seeds (2 df for paired t-tests), the study cannot distinguish "no effect" from "small effect masked by variance." The key comparison (DC-GRPO vs R3-only, p=0.187) is uninterpretable without power analysis. No effect sizes (Cohen's d) are reported. Multiple comparisons are uncorrected. This is not a minor limitation — it is the foundation on which the entire negative result rests.

2. **Implementation issues prevent attributing the negative result to the concept.** The unnormalized dot product in R1 (conflating direction and magnitude), the non-independent R2 (rank transformation of R1), the ad-hoc recalibration threshold, and the absence of initial R1-R3 correlation analysis all raise the possibility that DC-GRPO failed due to suboptimal design choices rather than a fundamental limitation of directional rewards. A negative result paper must demonstrate that the method tested was a fair and strong instantiation of the concept.

3. **Scope-claim mismatch.** The paper claims to establish "boundary conditions" for representation-level training rewards, but tests a single method configuration on one model at one scale. True boundary-condition mapping would vary direction extraction methods, reward formulations, training algorithms, model scales, and task domains. The missing CRAFT comparison is particularly notable: CRAFT demonstrates that hidden-state GRPO rewards work for safety, so explaining why they fail for sycophancy would be a genuine boundary-condition finding.

4. **Thin related work and missing baselines.** Approximately 15 informally cited works (no proper bibliography) is insufficient. Key omissions include proper citations for RepE, CCS, Activation Addition, and reward misspecification literature. The missing inference-time steering baseline (zero-cost alternative) is a significant experimental gap.

### What the Paper Does Well

- **Intellectual honesty** is exemplary. The paper does not hide or spin the negative result.
- **Experiment breadth** is impressive: 15 experiments covering calibration, comparisons, ablations, stability, cross-model, and sensitivity.
- **The continuous probe baseline** is the right decisive experiment and yields the paper's most informative finding.
- **Direction stability monitoring** provides a reusable diagnostic methodology.
- **Layer-wise emergence** and **evidence-strength interaction** are genuine representational findings with interpretive value.
- **The weight sensitivity analysis** cleanly shows optimal R1 weight trending to zero.

### Actionable Recommendations

1. **Increase seeds to 5-10** for all primary comparisons. Report Cohen's d and bootstrap CIs.
2. **Fix R1 formulation**: use cosine similarity with sigmoid scaling. Test as a separate configuration to isolate whether the negative result persists with a more principled reward.
3. **Add inference-time steering baseline** (Activation Addition with d_syc).
4. **Report initial R1-R3 correlation** (step 0, pre-training) to determine if the signals were ever independent.
5. **Add CRAFT comparison or analysis** explaining why prototype-based hidden-state rewards succeed for safety but directional rewards fail for sycophancy.
6. **Formally define RC-AUC** with the threshold sweep specification.
7. **Expand and properly format bibliography** to 30+ cited works.
8. **Narrow the title/framing** from "boundary conditions" to something matching the actual scope (e.g., "A Negative Result on Using Directional Projections as GRPO Rewards for Multi-Turn Sycophancy").
9. **Apply multiple comparison correction** (Holm-Sidak or Benjamini-Hochberg) to Table 7.
10. **Include power analysis** showing what effect size the study can detect at 80% power with 3 seeds.

### Reviewer Scores

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Methods + Experiments | 3/6 (Weak Reject) | High |
| R2 | Novelty + Related Work | 3/6 (Weak Reject) | High |
| **Consolidated** | | **3/6 (Weak Reject)** | **High** |
