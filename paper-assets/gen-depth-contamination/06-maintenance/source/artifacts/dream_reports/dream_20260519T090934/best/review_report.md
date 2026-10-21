---
dream_id: dream_20260519T090934
tier: best
overall_score: borderline accept
timestamp: 2026-05-19T10:06:06.513564+00:00
---

# Reviewer R1: Methodology and Experimental Rigor

## Summary

This paper formalizes recursive text generation as an iterated lossy channel and introduces K* (the generational discrimination boundary), measured empirically using 15 model-free statistical features and LightGBM under OBD. Across 9 model configurations (5 families, 1B-14B), 4 domains, and 4 decoding strategies, the authors find K* is bounded within {1,2,3} with a domain hierarchy: Wikipedia=1, C4/Code=2, arXiv=3. The experimental program is unusually thorough for this type of empirical study, with extensive cross-scorer validation, cross-model transfer, threshold sensitivity analysis, retrain-chain comparison, and honest reporting of negative results. The downstream curation claim (binary filtering outperforms graduated) is modest but directionally consistent with the measurement framework.

---

## Strengths

1. **Clean problem formalization with genuine novelty.** K* fills a real gap: no prior work estimates recursive generation depth. The DPI-motivated definition (Eq. 1) is well-constructed, and the CI-based operationalization (requiring CI lower bound > theta, not just point estimate) reflects mature statistical thinking. The distinction between K*_empirical (feature-set-specific lower bound) and K*_theory is explicitly maintained throughout.

2. **Exceptional experimental breadth and rigor.** The paper reports 77+ experiments spanning 9 model configurations, 4 domains, 4 decoding strategies, cross-scorer validation (22 configurations, 20/22 preserved), cross-model transfer (80-92% retention), base-vs-instruct ablation, length ablation (128/256/512), feature subset stability, self-BLEU independence, LaTeX markup ablation, neural probe comparison, retrain-chain ecological validity (both Qwen and Pythia yielding K*=7), and a formal power analysis. This is a substantially more thorough experimental program than typical for this problem class.

3. **Domain hierarchy is the paper's strongest and most interesting finding.** The Mistral-7B cross-domain evidence (K*=1 on C4 but K*=3 on arXiv within the same model) is particularly compelling for establishing domain as the primary factor. The JSD decay analysis provides a mechanistic explanation: C4 exhibits a sharp cliff (lambda~2.9) while arXiv decays gradually (lambda~1.0), connecting the empirical K* to information-theoretic contraction rates.

4. **Scorer confound handling is a model of careful experimental design.** The Wikipedia same-family scorer inflation was detected and controlled (Qwen-1.5B K* drops from 2 to 1 under cross-family scoring). The three-way ANOVA quantifies scorer influence as statistically significant but practically minor (eta^2_p = 0.192 vs. 0.998 for Depth-Pair). Cross-scorer validation on Code domain further confirms robustness (Delta <= 1.9pp).

5. **Transparent reporting of negative and borderline results.** The paper reports: Mistral K*=1 exception on C4, Pythia Code K*=1 (borderline), Wikipedia LOFO failure (1/6 agreement, explained), graduated filtering comprehensive failure (all domains), Pythia filtering null, arXiv filtering null, 512-token borderline CI, and Qwen-cont cross-scorer K* flip. This level of honesty is uncommon and substantially increases credibility.

6. **LOFO threshold validation is methodologically sound.** The leave-one-family-out cross-validation for theta yields theta-hat in [0.5725, 0.6004] on C4 with 8/9 agreement, and 6/6 on arXiv. This addresses the potential circularity concern with post-hoc threshold selection. The Wikipedia LOFO failure is honestly reported and properly explained.

---

## Weaknesses

### Major

**W1. Threshold sensitivity remains the central vulnerability (methodology, major).**

K*=2 on C4 is the headline finding, but multiple configurations sit dangerously close to theta=0.60:
- Qwen-cont: CI lower = 0.602, margin = +0.2pp. Cross-scorer flips to K*=1.
- LLaMA-8B: CI lower = 0.603, margin = +0.3pp. 1/5 folds below theta.
- OLMo-1B: CI lower = 0.605, margin = +0.5pp.

At theta=0.625, OLMo already drops to K*=1. At theta=0.65, roughly half the configurations fragment. The LOFO validation helps, but the derived theta-hat range [0.5725, 0.6004] barely includes 0.60 at the upper end. The paper's defense (5pp stability window, permutation null < 0.55, domain ordering preserved across theta) is reasonable but does not fully resolve the concern that the "dominant mode K*=2" characterization depends on 3-4 configurations being within 0.5pp of the threshold. The paper would benefit from framing K* less as a discrete universal constant and more as a regime characterization with explicit confidence bands.

**W2. Scale range is insufficient for the generality claimed (experimental coverage, major).**

The paper covers 1.4B-14B (with 32B running but not yet included). The 0v1 AUC trend is informative: 0.99+ at 1.5B, 0.96 at 7-14B, 0.92 at 8B (LLaMA). This declining trend, combined with the surprisal attenuation analysis (Mistral's compressed dynamic range predicts K* decrease with capability), raises a genuine concern: at 70B+ or frontier scale, the entire AUC curve may shift downward enough to make K*=1 the dominant mode even on C4. The paper's own Discussion acknowledges this, predicting "K* may decrease as capability scales beyond 14B." This candid prediction actually undermines the claimed scale invariance. The absence of 70B+ data is a significant gap for a paper claiming domain as the "primary" determinant over model competence.

**W3. Code domain "ceiling=2" is weakly supported (experimental rigor, major).**

The paper claims Code ceiling=2 but the evidence is thin:
- 3 completed models at submission time (Qwen-1.5B: K*=2, LLaMA-8B: K*=2, Pythia-1.4B: K*=1). Two more running (Mistral-7B and Qwen-7B TBD).
- The cross-model table still has TBD entries, meaning the claim is based on 2/3 completed models reaching K*=2.
- Pythia's K*=1 is explained as "competence-limited," but this same argument could apply to any model failing to reach the ceiling, making the ceiling claim unfalsifiable within the current framing.
- The "domain ceiling + model competence" framework is elegant but risks being circular: any K* below the claimed ceiling is attributed to insufficient competence, while any K* at the ceiling confirms the ceiling.

The paper should either (a) complete all 5 code experiments before claiming ceiling=2, or (b) soften the claim to "K*=2 for code-competent models (2/3 tested)" with appropriate caveats about the small sample.

**W4. Curation contribution (C3) is oversold relative to evidence (claims vs. evidence, major).**

- Binary-ours MMLU gain: +0.76pp over no-filter (0.5941 vs. 0.5865). All strategies degrade relative to the base model (0.6018), so filtering mitigates rather than prevents contamination harm.
- At lower contamination ratios (10-50%), synthetic data is net-beneficial and binary filtering's MMLU advantage is borderline (p=0.074 at 30%).
- Graduated filtering fails comprehensively: on C4, arXiv, and across contamination ratios.
- Pythia filtering is null (MMLU~0.26, near random).
- The paper's own insight ("K* characterizes discriminability, not data utility") effectively concedes the gap between measurement and application.

The filtering section occupies substantial space for a contribution that yields <1pp on one benchmark under a 100% synthetic stress test. The claim that "binary filtering outperforms graduated weighting" is technically correct but the practical significance is minimal. The paper would be stronger either (a) positioning C3 as a consistency check (2-3 paragraphs) rather than a full contribution, or (b) finding a stronger downstream application.

### Minor

**W5. DPI theoretical grounding is thin (minor).** The DPI argument guarantees monotonic information loss and finite K*, but provides no bound on magnitude. Framing it as "theoretical contribution" overstates its role; "theoretical motivation" is more accurate.

**W6. Neural probe inconsistency deserves more prominent treatment (minor).** Qwen K*_neural=3 vs K*_15D=2 raises the question of whether the 15D feature set imposes an artificial ceiling. The paper correctly notes this is a self-familiarity artifact (Pythia/OLMo remain at 2), but the possibility that richer feature sets could yield higher K* for all models is not explored.

**W7. Qwen family overrepresentation (minor).** 5/9 configurations use Qwen models. The 8/9 K*=2 headline would be 3/4 non-Qwen families reaching K*=2 and 1/4 at K*=1.

**W8. Feature Spearman rho across decoding strategies shows moderate correlation (minor).** Cross-config feature rho ranges from 0.532 to 0.914. The low rho values suggest that while K* is stable across decoding, the feature mechanisms differ substantially, complicating the "generator-independent features" narrative.

---

## Questions for Authors

1. Would the paper be strengthened by reporting K* as a distribution over theta rather than anchoring to a single threshold? This would make the borderline cases a feature of the characterization rather than a weakness.

2. The Discussion predicts K* may decrease at larger scales. If the 32B experiment shows K*=2, does this alleviate the concern, or is 32B still too small? What is the expected scale at which K*=1 becomes dominant for C4?

3. Under the domain ceiling + model competence framework, what empirical evidence would falsify the claim that Code ceiling=2? If Mistral-7B and Qwen-7B both yield Code K*=1, would this change the ceiling assignment?

4. The cross-scorer experiment flips Qwen-cont from K*=2 to K*=1. Can you definitively distinguish between "borderline K*=2" and "scorer-inflated K*=1"?

5. K*=7 under retrain-chain is striking. Have you considered a hybrid protocol mixing prompt-chain and retrain-chain processes, which would better approximate real-world contamination?

---

## Minor Issues

- The Conclusion is extremely terse (one sentence). For EMNLP, a 3-5 sentence conclusion would be appropriate.
- arXiv's n=2200 sits close to the minimum reliable sample size (power analysis shows 100% detection at n=2000). Explicit acknowledgment would strengthen the paper.
- Table 1 footnote references "fp16" for Qwen-7B specifically; other models' precision is not noted.
- Some appendix cross-references may appear before their targets in the flow.

---

## Score: 3.5 (Borderline Conference) | Confidence: High (4/5)

**Justification**: The paper addresses a genuinely novel question (generational depth estimation) with an unusually thorough experimental program and commendable transparency about negative results. The domain hierarchy finding and cross-domain Mistral evidence are the strongest contributions. However, the headline K*=2 finding on C4 rests on narrow statistical margins for multiple configurations (3-4 within 0.5pp of theta), the scale range is insufficient for the claimed generality (no 70B+ models, and the paper's own analysis predicts K* decrease at larger scales), the Code domain ceiling claim is based on incomplete data (2/3 completed models with TBD entries), and the curation contribution delivers <1pp gains under a stress test with comprehensive failure of graduated approaches. The methodological care and novel problem formulation lift it above a clear reject, but the margin fragility and scope gaps prevent confident acceptance at this stage.