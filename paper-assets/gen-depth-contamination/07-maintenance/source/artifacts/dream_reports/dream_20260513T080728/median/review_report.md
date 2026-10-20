---
dream_id: dream_20260513T080728
tier: median
overall_score: weak reject
timestamp: 2026-05-13T08:59:48.335928+00:00
---

# Dream Review Report: Measuring the Generational Discrimination Boundary in Recursively Contaminated Text

**dream_id:** 20260513T080728  
**Review mode:** full  
**Date:** 2026-05-13  

---

## Roundtable Summary

Two reviewers conducted independent reviews (R1: Methods & Experiments; R2: Novelty & Related Work), followed by cross-sharing, convergence discussion, and synthesis.

- **R1 initial score:** 3/6 (Weak Reject), Confidence 4/5
- **R2 initial score:** 4/6 (Weak Accept), Confidence 4/5
- **Consensus score:** 3.5 → **3/6 (Weak Reject)**, Confidence 4/5

The reviewers agree on the core strengths (novel problem framing, comprehensive experiments, commendable honesty) and on the main weaknesses (DPI theory is standard, θ threshold is load-bearing, C3 application claim is effectively null). The key disagreement was whether the conceptual reframing alone is sufficient for a top venue — R2 initially thought yes at borderline, but converged toward R1's view that without stronger empirical grounding of K* (e.g., sensitivity to θ, K* under learned features), the characterization contribution is not yet convincing enough.

---

## Step 1: Independent Reviews

### Reviewer R1 — Methods & Experiments

**Score: 3/6 (Weak Reject) | Confidence: 4/5**

#### Strengths

- **S1. Novel problem formulation.** Formalizing depth estimation as an ordinal classification problem and defining K* as a measurable quantity is a genuine contribution that no prior work has attempted.
- **S2. Comprehensive experimental matrix.** 4 model configs × 2 generation modes × cross-scale × cross-model transfer × retrain-chain × 6 filtering strategies + supporting analyses. This is unusually thorough.
- **S3. Commendable honesty.** The paper does not hide uncomfortable results: DSIR matching graduated filtering, base model borderline K*, learned features outperforming by ~5pp. This scientific integrity is appreciated.
- **S4. Useful baselines.** LLM zero-shot (Table 8) and binary-confidence-as-proxy (Table 9) analyses directly address likely reviewer objections and confirm the non-triviality of depth estimation.

#### Weaknesses

- **W1 (Major). DPI theory is a framing device, not a substantive contribution.** The iterated lossy channel argument provides existence of K* but makes no quantitative predictions — any positive empirical result would be "consistent with DPI." The gap between DPI on full joint distributions and classifier discriminability on 15D feature projections is substantial and under-acknowledged. K*_empirical is a feature-dependent, threshold-dependent lower bound on K*_theory, not K*_theory itself.

- **W2 (Major). θ=0.60 threshold is arbitrary and load-bearing.** The base model's K* flips between 1 and 2 at exactly this value (AUC=0.599, CI lower=0.588). Qwen-1.5B continuation CI lower is only 0.002 above threshold (0.602). No sensitivity analysis over θ is provided. The headline result K*=2 depends critically on this single threshold choice, and several configurations are within noise of the boundary.

- **W3 (Major). Learned features outperform 15D by ~5pp consistently — K* under learned features is never reported.** Table 10 shows frozen embeddings + MLP beating hand-crafted features by ~5pp accuracy and ~4.9pp mean pairwise AUC across all three generator configs. If learned features push AUC_2v3 above 0.60, then K*=2 becomes an artifact of the feature set, not a property of recursive text. This is a critical omission.

- **W4 (Major). Graduated filtering fails practical significance.** At 30% contamination (the realistic operating point), graduated vs binary yields +0.6pp (p=0.072) — borderline by any standard. DSIR achieves comparable results without depth estimation. At 10% contamination, the difference is negligible (+0.2pp, p=0.32). Only at 50% (worst-case) does the difference reach significance (+1.1pp, p=0.038). The C3 application claim is effectively null at realistic contamination levels.

- **W5 (Moderate). Low statistical power.** 5 seeds for filtering experiments (power ~0.45 for 0.6pp effect size per the review context). 1K documents for 7B experiments (CI ±0.023). The 7B non-significant result (p=0.18) may simply be underpowered.

- **W6 (Moderate). Single-domain evaluation.** All experiments use C4 English web text. No evaluation on code, non-English text, domain-specific corpora, or different text lengths. The generality of K*=2 beyond this narrow domain is unknown.

- **W7 (Moderate). Retrain-chain ecological validity is limited.** LoRA rank=16 is a parameter-efficient approximation, not full fine-tuning. The retrain-chain attenuates signal by -3.3pp on 1v2, and the paper acknowledges this limitation, but the gap between LoRA retrain and real-world model collapse (full retraining on mixed data) remains uncharacterized.

#### Questions for Authors (R1)

1. What is K* when measured using learned features (frozen embeddings + MLP)? If AUC_2v3 exceeds 0.60 under learned features, the headline K*=2 is a property of the 15D feature set, not of recursive text.
2. How does K* vary as a function of θ ∈ {0.55, 0.575, 0.60, 0.625, 0.65}? Is K*=2 robust or is it an artifact of a single threshold choice?
3. What is the statistical power of the 5-seed filtering experiment to detect a 0.6pp effect? If power < 0.5, the borderline p-values are uninformative.
4. The DPI argument assumes homogeneous channel applications (same G at each step). In the prompt-chain setup, the model changes context at each step. How does this affect the theoretical guarantee?
5. Why was the greedy decoding ablation (exp-003, listed as RUNNING in the experiment plan) not included? This would directly test whether K* varies with decoding strategy.

---

### Reviewer R2 — Novelty & Related Work

**Score: 4/6 (Weak Accept) → revised to 3/6 after roundtable | Confidence: 4/5**

#### Strengths

- **S1. Genuine conceptual reframing.** The shift from binary (human vs. synthetic) to ordinal (depth estimation) opens a new problem space. No prior work operationalizes this boundary. This is confirmed by literature search.
- **S2. Thorough positioning against Drayson et al. (2025).** The closest prior work is correctly identified and the differentiation is clean: Drayson uses binary confidence for importance resampling; this work generalizes to ordinal depth with graduated weights. The binary-ours baseline provides fair isolation.
- **S3. Breadth of supporting analyses.** Retrain-chain, cross-model transfer, LLM zero-shot, binary confidence comparison, learned representations, Common Crawl validation — above-average experimental comprehensiveness.
- **S4. Honest self-assessment.** The paper correctly repositions from "engineering advantage" to "scientific characterization" when the application results are weak.

#### Weaknesses

- **W1 (Major). DPI theoretical contribution is standard.** The iterated lossy channel framing and DPI-based K* existence argument is textbook information theory (Markov chain data processing). Should be reframed as "motivation" not "contribution."

- **W2 (Major). K*=2 has narrow practical implications.** A 3-class ordinal signal (human/gen-1/gen-2+) is structurally close to "binary detection with a soft middle category." The graduated filtering formula (Eq. 3) reduces to: keep human (w=1), discount gen-1 (w=1-α), discard gen-2+ (w≈0). This is one additional threshold over binary. The operational gap from Drayson's continuous importance resampling weights is smaller than implied.

- **W3 (Moderate). Significant related work gaps.**
  - **Watermarking literature** (Kirchenbauer et al., 2023): Active provenance tracking via watermarks is an alternative to passive depth estimation. The paper should discuss the relationship.
  - **Schaeffer et al. (ICML 2025), "Position: Model Collapse Does Not Mean What You Think":** Identifies 8 definitions of model collapse across 3 families. K* belongs to Family B (distribution deformation). Citing this would sharpen positioning.
  - **Kazdan et al. (ICML 2025), "Collapse or Thrive?":** Formalizes replace vs. accumulate vs. accumulate-subsample regimes. The prompt-chain setup = replace regime (harshest). K*=2 should be contextualized as specific to this regime.
  - **Self-refinement literature:** Texts undergoing multiple LLM self-refinement passes could produce similar statistical signatures but are not "recursive contamination." False positive risk is undiscussed.
  - **Membership inference connections** (Carlini et al., 2022; Shi et al., 2024 Min-K%++): Depth estimation has structural similarity to membership inference. Deserves discussion.

- **W4 (Minor). Missing citation "[?]" in the introduction.** Broken reference visible in §1. Preparation issue.

- **W5 (Moderate). ~5pp gap to learned features complicates the characterization narrative.** The paper argues for hand-crafted features based on interpretability, but the ~5pp gap is consistent across all configurations (Table 10). If the primary contribution is "scientific characterization," a reader might reasonably ask: characterization using suboptimal features? The interpretability-performance tradeoff argument needs stronger justification — specifically, what characterization insights are uniquely enabled by per-feature analysis that couldn't be obtained from probing learned representations?

- **W6 (Moderate). Scope narrowness relative to claims.** 1.5B-7B models, English web text, nucleus sampling only. No non-English text, no code, no models above 7B. The "information-theoretic" framing suggests generality that the experiments cannot support.

#### Questions for Authors (R2)

1. How does K* vary across θ values? Is the K*=2 finding robust across {0.55, 0.575, 0.625, 0.65}?
2. The cross-model transfer "91% retention" comes from the Pythia↔OLMo pair. What is the average retention across all off-diagonal transfer pairs? Table 1 shows Qwen-rw has much higher AUC_1v2 (0.696) than others — does transfer from/to this config drag the average down substantially?
3. How would the depth classifier behave on text that underwent multiple LLM self-refinement passes (not recursive contamination)? Is there a false-positive risk for iteratively edited text?
4. If watermarks were applied at each generation stage, depth could be tracked without statistical classifiers. How do you position passive depth estimation against active watermarking-based provenance?
5. What specific characterization insights are uniquely enabled by per-feature interpretability that could not be obtained by probing or explaining learned representations?

---

## Step 2: Cross-Sharing — Key Observations

After exchanging reviews, both reviewers identified convergent and divergent assessments.

**Points of agreement:**
- DPI theory is standard, not a real contribution (R1-W1, R2-W1)
- θ=0.60 sensitivity is a critical unaddressed issue (R1-W2, R2 Q1)
- The paper's honesty about weak C3 results is a genuine strength
- Comprehensive experimental coverage is above average
- The conceptual reframing (binary → ordinal) is novel and valuable

**Points of divergence:**
- R1 sees the learned-features gap (W3) as potentially undermining the headline K*=2 finding; R2 sees it as a narrative complication but not fatal
- R2 initially found the conceptual novelty sufficient for borderline accept; R1 argued the concept without robust measurement is insufficient
- R2 identified more related work gaps; R1 identified more methodological gaps

---

## Step 3: Convergence Discussion

The central debate was whether K*=2 is a robust empirical finding or a threshold-dependent artifact:

**R1's argument:** K*=2 stands or falls on θ=0.60. Three configurations have AUC_1v2 within 0.02 of the threshold (Qwen-cont: 0.611, OLMo: 0.615, base: 0.599). If learned features push AUC_2v3 above 0.60, K* changes. Without θ sensitivity analysis and K* under learned features, the headline result is insufficiently grounded.

**R2's argument:** The conceptual contribution (naming and measuring K*) has value even if the specific K*=2 value shifts slightly. The cross-model transfer and degradation ordering results are θ-independent and constitute a real contribution.

**Resolution:** Both reviewers agree that the concept is valuable but the specific measurement needs more robustness analysis. R2 revised downward from 4 to 3, agreeing that for a top venue, the combination of (a) threshold sensitivity, (b) learned-features omission, and (c) null application result places this below the acceptance bar. However, both note the paper is close to the bar and could be strengthened with specific revisions.

---

## Step 4: Consolidated Assessment

### Overall Score: 3/6 (Weak Reject) | Confidence: 4/5

### Contribution Assessment

The paper introduces K* as a named, measurable quantity for recursive text contamination depth — a genuinely novel concept absent from prior literature. The binary-to-ordinal reframing opens a new research direction. The experimental breadth (4 model configs, cross-scale, cross-model, retrain-chain, 6 filtering strategies, multiple supporting analyses) is commendable. The paper's scientific honesty about weak application results and limitations is exemplary.

However, several issues prevent acceptance at a top venue:

### Critical Issues (must address)

1. **θ sensitivity analysis is missing and essential.** The headline K*=2 depends on θ=0.60, with multiple configurations within noise of the boundary. Report K* as a function of θ and demonstrate that the qualitative conclusions hold across reasonable threshold choices.

2. **K* under learned features must be reported.** If frozen-embedding features (which outperform 15D by ~5pp consistently) yield K*=3 or higher, the headline result becomes a feature-set artifact. This is the single most important missing experiment.

3. **C3 (graduated filtering) does not meet the significance bar.** At realistic contamination (10-30%), graduated filtering provides no significant advantage over binary filtering. DSIR matches without depth estimation. The paper is honest about this, but the contribution list should not include C3 as a claim — it should be reported as a negative/null finding.

### Important Issues (should address)

4. **DPI framing is oversold.** The theory provides existence of K* but no quantitative prediction. Reframe §3.1 as motivation, not contribution. Acknowledge more prominently that K*_empirical is a feature-dependent lower bound on K*_theory.

5. **Related work gaps.** Add discussion of: (a) watermarking as alternative provenance tracking, (b) Schaeffer et al. (ICML 2025) model-collapse taxonomy, (c) Kazdan et al. (ICML 2025) replace/accumulate regimes, (d) self-refinement false-positive risk.

6. **Cross-model transfer figure needs full reporting.** The "91% retention" is from the best pair (Pythia↔OLMo). Report the full transfer matrix and average retention across all pairs.

7. **Missing greedy decoding ablation.** The experiment plan lists exp-003 (greedy, expected K*=1) as a running experiment. This result would directly test whether K* varies with decoding strategy and would substantially strengthen the characterization.

8. **Statistical power.** 5 seeds for filtering (power ~0.45) and 1K docs for 7B (wide CIs) limit the informativeness of non-significant results. Either increase sample sizes or explicitly compute and report power.

### Minor Issues

9. **Broken citation "[?]" in §1.** Must fix before submission.
10. **Single-domain limitation.** All experiments on C4 English web text. Acknowledge that K*=2 may not generalize to code, non-English, or domain-specific text.

### What Would Change the Score

- **To 4 (Weak Accept):** Address critical issues 1-2 (θ sensitivity + K* under learned features) and demonstrate that K*=2 is robust. Add greedy decoding ablation.
- **To 5 (Accept):** Additionally show that K* varies meaningfully with decoding strategy (confirming K* as a controllable property of the generation channel), expand to one additional domain, and increase filtering experiment seeds.

### Verdict

The paper tackles a well-motivated problem with a novel formulation and thorough experiments, but the central empirical claim (K*=2) rests on an arbitrary threshold with insufficient robustness analysis. The most critical omission — K* under learned features — could either validate or invalidate the headline result. The application contribution (C3) is effectively null at realistic contamination levels. With the specific revisions outlined above, particularly θ sensitivity analysis and K* under learned features, this could become a solid contribution. In its current form, it falls just below the acceptance bar for a top ML venue.

### Recommended Venue Targeting

- **Current form:** EMNLP 2026 Findings (good fit for characterization with caveats)
- **After revisions:** EMNLP 2026 Main (borderline) or NeurIPS 2026 Datasets & Benchmarks track
