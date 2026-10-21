---
dream_id: dream_20260516T105241
tier: best
overall_score: 4 — Weak Accept
timestamp: 2026-05-16T11:35:12.483921+00:00
---

# Dream Review Report

**Paper:** Differential Depth Response in Recursive LLM Generation: Distributional Profiling Beyond Binary Detection
**Review mode:** simple (1 reviewer, full coverage)
**Venue standard:** Top ML venue, ~25% acceptance, 6-point scale

---

## Summary

This paper formulates generation depth estimation — predicting how many recursive LLM generation steps a text has undergone — as an ordinal classification task beyond binary AI-text detection. The key empirical finding is a "differential depth response": central-tendency and diversity features (entropy mean, TTR, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy std, tail decay) remain near-stationary, consistent with a location shift in the token-level NLL distribution. A 7-feature XGBoost classifier evaluated under leave-one-generator-out (LOGO) cross-validation across 9 base-model generators from 6 families (0.6B–7.6B) achieves binary F1 = 0.73 and 3-class F1 = 0.78. A negative finding on downstream utility (depth-aware curation does not improve LM training) is reported transparently.

---

## Strengths

- **Genuinely novel task formulation.** No prior work addresses ordinal depth estimation in recursive LLM generation chains. The framing as provenance characterization beyond binary detection is timely and well-motivated given concerns about recursive web contamination.

- **Rigorous evaluation protocol.** LOGO cross-validation is the correct design for testing cross-generator generalization — the test generator is completely unseen during training. Additional validation axes (leave-one-family-out F1 = 0.72, cross-reference model analysis with 2.4pp spread, rp-LOFO sensitivity) provide multi-dimensional robustness evidence.

- **Excellent intellectual honesty.** The paper explicitly acknowledges that (a) the method applies only to base models, (b) 3-class is the practical resolution ceiling, (c) depth-aware curation provides no downstream benefit, and (d) an end-to-end neural model substantially outperforms the proposed features. This calibration of claims is commendable and rare.

- **Comprehensive experiment coverage.** Feature ablation (Table 2), per-generator LOGO (Table 3), baseline comparison (Table 4), cross-reference analysis (Table 5), continuation vs. paraphrastic chains (Table 6), 5-class ordinal (Table 7), QLoRA upper bound (Table 8), rp-LOFO (Table 10) — all planned experiments appear fully executed and reported.

- **Interpretable theoretical framing.** The location-shift model provides a clean explanation for why certain features drift and others don't, making the system transparent and the findings reproducible. The QLoRA comparison (Section 5.2) effectively positions the handcrafted features as the interpretability-focused contribution while acknowledging that more signal exists.

- **Careful methodological decisions.** Binary evaluation excludes gen-0 to avoid shared-seed leakage. Gemma's rp=1.1 requirement is diagnosed, gated (rp-LOFO ≥ 0.70), and documented. The scale gradient observation (smaller models easier to classify) aligns with the theoretical framework.

---

## Weaknesses

### Major

1. **Narrow ecological validity undermines the stated motivation.** The paper motivates depth estimation as relevant to web-crawled training corpora contamination, but the method operates exclusively on base models with continuation prompts. Real-world LLM-generated web text overwhelmingly comes from instruct/chat models. The paper acknowledges base-model scope as a limitation (Section 5.5), but the gap between the introduction's framing ("LLMs are increasingly deployed to generate text at scale... scraped from the web") and the operational scope (9 base models, continuation chains only) is substantial. The practical impact claim needs significant downscaling, or instruct-model results need to be provided.

2. **The "differential depth response" is conceptually predictable.** The observation that mean NLL decreases with recursive generation (text becomes more predictable) while distributional shape is preserved follows from well-understood properties: autoregressive LMs assign higher probability to their own outputs, and this compounds under recursion. The location-shift framing is a clear articulation of this, but it is closer to an empirical confirmation of a theoretically expected pattern than a surprising discovery. The model collapse literature (Shumailov et al., 2024; Dohmatob et al., 2024) already establishes that recursive generation concentrates distributions. The empirical breadth (9 generators, 6 families) adds value, but the conceptual contribution is incremental.

3. **Modest absolute performance with marginal gains over baselines.** Binary LOGO F1 = 0.73 means roughly 1 in 4 predictions is wrong under the most favorable (gen-1 vs gen-2+) framing. The improvement over the best single baseline (Avg-LogProb, 0.70) is +3.0pp and over the 4-baseline ensemble (0.71) is +2.0pp. While statistically significant (p < 0.001), the practical margin is slim. Per-generator F1 ranges from 0.69 (Gemma-2-2B) to 0.86 (Pythia-1B) with std = 0.056, indicating considerable variability across generators.

### Moderate

4. **Scale ceiling is concerning and under-explored.** The largest generator (Qwen3-8B, 7.6B params) already shows the lowest family-normalized F1 (0.70 3-class). The scale gradient implies that at frontier scale (70B+), where generation is more fluent and feature margins compress, the method may approach chance performance. This is acknowledged as a limitation but not experimentally bounded — even a single experiment with a larger model would help characterize the degradation curve.

5. **Downstream utility experiment is statistically underpowered.** The negative finding on depth-aware curation (Section 5.4) is based on CLM perplexity differences of < 0.05 (2.387 vs 2.367 vs 2.335) on a small dataset. The paper does not report confidence intervals or significance tests for these comparisons. While the honest reporting is appreciated, presenting this as a firm negative finding ("data quantity, not depth composition") overstates the evidence from what appears to be a single underpowered experiment.

6. **Single-domain evaluation (English Wikipedia seeds).** All chains originate from ~1000 Wikipedia passages. Transfer to other domains (news, code, creative writing, social media) — which differ substantially in vocabulary distribution and stylistic properties — is untested. The features (especially TTR and hapax ratio) are known to be domain-sensitive.

### Minor

7. **Features are standard; the novelty is purely in their application.** TTR, hapax ratio, and NLL summary statistics are well-established in stylometry and AI-text detection. The contribution is combining them for a new task, not methodological innovation in feature engineering.

8. **The "LLM as Broken Telephone" reference (Section 2) has a placeholder citation mark ("?")** suggesting an incomplete bibliography entry.

---

## Questions for Authors

1. **Instruct model gap:** Have you tested whether *any* feature set or learned representation can estimate depth in instruct-model chains? If depth is fundamentally undetectable for instruct models, how does this affect the paper's relevance to the stated web-contamination motivation?

2. **Shared seed pool:** All 9 generators use the same ~1000 Wikipedia seeds. Could the classifier exploit seed-specific distributional signatures rather than learning generator-independent depth features? What would happen with disjoint seed pools per generator?

3. **Scale extrapolation:** The scale gradient (Figure implied by Table 3) shows F1 decreasing with model size. Can you fit a trend and estimate at what scale depth estimation drops to chance? Even a rough projection would help readers assess practical utility.

4. **Why Pythia-410M as default reference?** It shares architecture with 2 of 9 generators (Pythia family). The cross-reference experiment shows Qwen3-0.6B achieves +2.5pp higher F1. Is there a principled reason beyond experimental convenience?

5. **Class imbalance in practice:** The evaluation uses balanced classes. In a realistic corpus (e.g., 90% gen-0, 9% gen-1, 1% gen-2+), how would calibration and precision/recall trade-offs change?

---

## Missing Experiments or Analysis

Relative to the experiment plan, **all imagined experiments are covered**: feature ablation (plan_001), cross-generator LOGO (plan_002), paraphrastic comparison (plan_006), finer-grained ordinal (plan_009), end-to-end classifier (plan_012), three new families from plan-016 (Llama/Gemma/Mistral), cross-reference completion, and rp-LOFO diagnostics.

Additional experiments that would strengthen the paper:
- Mixed-depth corpus evaluation with realistic class imbalance
- Domain transfer beyond Wikipedia (news, social media, code)
- At least one frontier-scale generator (70B+) to characterize the scale ceiling
- Instruct-model depth estimation (even as a clearly negative result in the main text rather than only limitations)

---

## Minor Issues

- "LLM as Broken Telephone" citation appears incomplete (check bibliography entry)
- Table 3 caption says "Mean ± std" but the ± notation in the table body (0.77 ± 0.056) could be misread as a confidence interval rather than cross-generator std — clarify
- The paper could benefit from a figure showing the feature-depth trend lines (the "Figure 1" described in the experiment plan); only tables are present in the current version

---

## Overall Score: 4 — Weak Accept

**Justification:** The paper introduces a genuinely novel task (ordinal generation depth estimation) with careful experimental methodology, thorough multi-axis validation, and commendable intellectual honesty about limitations. The empirical breadth (9 generators, 6 families, 0.6B–7.6B scale) is substantial for this type of characterization study, and the differential depth response pattern is cleanly documented. The negative downstream-utility finding adds scientific value by establishing depth fingerprinting as diagnostic rather than curative.

However, three concerns prevent a stronger recommendation: (1) the practical scope is narrow (base models, continuation chains, English Wikipedia), creating a gap between the web-contamination motivation and actual applicability; (2) the core finding (location shift under recursive generation) is theoretically predictable rather than surprising; and (3) absolute performance (binary F1 = 0.73) and margins over baselines (+2–3pp) are modest.

The balance tips slightly positive because: the task formulation itself is a genuine contribution that could seed a research direction; the LOGO evaluation protocol is methodologically sound and reusable; the honest negative finding on downstream utility is valuable; and the paper is clearly written with well-organized experiments. A revised version that either (a) extends to instruct models even partially, or (b) provides stronger theoretical grounding for the location-shift model beyond empirical observation, would be considerably stronger.

## Confidence: 4/5

Familiar with AI-text detection, model collapse, and data curation literatures. Primary uncertainty is whether the community values novel task formulation sufficiently to offset the narrow practical scope — a judgment call on which reasonable reviewers may disagree.
