---
dream_id: dream_20260513T171200
tier: worst
overall_score: 4/10 — Weak Reject
timestamp: 2026-05-13T18:18:06.450185+00:00
---

# Dream Review Report — ContamCal (AAAI 2027)

**Dream ID:** 20260513T171200
**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)
**Target Venue:** AAAI 2027

---

## Paper Information

**Title:** ContamCal: Mapping the Possibility Frontier of Contamination-Aware Benchmark Calibration
**Pages:** 14 (11 main + 3 references)
**Claimed Contributions:** (1) Fisher Information identifiability analysis (AUC threshold 0.72), (2) Signal survival analysis across training regimes, (3) ContamCal framework (4PL+γ IRT with RRF signal fusion)

---

## Consolidated Assessment

| Dimension | R1 (Methods+Experiments) | R2 (Novelty+Related Work) | Consensus |
|-----------|--------------------------|---------------------------|-----------|
| Soundness / Originality | 2/4 (Fair) | 2/4 (Fair) | 2/4 |
| Significance | 2/4 (Fair) | 2/4 (Fair) | 2/4 |
| Clarity | 3/4 (Good) | 3/4 (Good) | 3/4 |
| Overall (1-10) | 4 (Weak Reject) | 4 (Weak Reject) | **4 (Weak Reject)** |
| Confidence | 4/5 (High) | 4/5 (High) | — |

---

## Summary

ContamCal augments 4PL Item Response Theory with a contamination covariate γ, fusing four detection signals (Embedding Retrieval, Min-K%++, ConStat, Self-Critique) via Reciprocal Rank Fusion into a Bayesian IRT model with credible intervals. The paper's central claim is establishing a "possibility frontier": practical identifiability requires detection signal AUC ≥ 0.72, a threshold current signals meet only under heavy SFT contamination of small models (≤1.5B parameters). The paper frames this as a "negative but informative" result, arguing it characterizes impossibility regions for any post-hoc calibration method.

The paper is intellectually honest and well-written, but the core method does not deliver: it is not significantly better than linear regression or DCR, the primary existing method. The "possibility frontier" framing, while creative, is ultimately post-hoc rationalization of a method that failed to achieve its original calibration goal. The novelty is limited — the core model is a direct application of item compromise IRT from educational measurement — and the practical utility is confined to a narrow regime (small, SFT-contaminated, open-weight models) that is arguably the least concerning for contamination scrutiny.

---

## Strengths (Consensus)

1. **Fisher Information identifiability analysis is a genuine theoretical contribution.** The derivation of a practical AUC threshold (0.72) via Cramér-Rao bounds gives the detection community a concrete, actionable target. No prior work has formally characterized when contamination calibration is feasible. (R1, R2)

2. **Signal survival analysis has independent empirical value.** The systematic 4-signal × 4-regime heatmap (Table 15) quantifies signal degradation patterns across training regimes. The finding that degradation is gradual (−0.035/step) rather than cliff-like refutes the assumption of clean regime boundaries. (R1, R2)

3. **Intellectually honest framing.** The paper does not hide negative results — it reports that calibration actively hurts in the RL regime (11.2pp vs 9.5pp uncalibrated, Table 18) and that the "calibration paradox" makes the most-scrutinized models the least calibratable. This transparency is uncommon and commendable. (R1, R2)

4. **Comprehensive experimental coverage.** 12 experiments spanning SFT injection, signal quality, aggregation, noise propagation, core calibration, scale bridging (0.5B–72B), signal survival, RL case study, multi-family validation, and closed-weight analysis. The experimental design is thorough. (R1)

5. **Well-grounded in psychometric theory.** The connection to item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004) demonstrates interdisciplinary sophistication. The measurement error model (Eq. 3) correctly propagates Stage 1 uncertainty. (R2)

6. **Good writing quality.** The two-stage pipeline is clearly presented. Mathematical exposition is clean. Tables are informative and well-labeled. (R1, R2)

---

## Weaknesses (Consensus)

### Major

**W1. Core method does not outperform simple baselines.** [R1, R2]
4PL+γ achieves 6.8pp MAE (Table 10), which is NOT significantly better than:
- Linear regression + CI: 6.2pp (p = 0.18)
- DCR (EMNLP 2025): 6.4pp (p = 0.35)

Only 2 of 7 baselines are significantly beaten (vanilla 4PL, Emperor mitigation) — both are trivially weak baselines that ignore contamination entirely. DCR actually outperforms ContamCal on MMLU (5.0 vs 5.2pp) and ARC-C (5.8 vs 6.2pp). The per-benchmark γ_k variant yields a negligible 0.3pp improvement and fails to converge on HumanEval (ESS=85, R̂=1.12).

**W2. RRF fusion degrades signal quality.** [R1, R2]
4-signal RRF AUC=0.68 is LOWER than the best single signal Embedding (0.71, Δ=−0.03, Table 7). Equal-weight rank fusion cannot downweight fundamentally weak signals (Self-Critique AUC=0.60). Calibrated weighted RRF (0.69) does not significantly improve (p > 0.10). The fusion component, which is presented as Stage 1 of the framework, actively harms downstream calibration.

**W3. Calibration actively hurts in the RL regime.** [R1, R2]
In the RL case study (Table 18), 4PL+γ MAE=11.2pp vs uncalibrated 9.5pp — a 1.7pp degradation. Expected regret is negative (−0.05 vs uncalibrated, −0.10 vs remove-rescore). The method "hallucinates" contamination effects from noise, overcorrecting false positives and undercorrecting true positives. 88% of γ CIs include zero.

**W4. "Possibility frontier" framing is post-hoc rationalization.** [R2, endorsed by R1]
The paper was originally conceived as "we solve contamination calibration" and reframed to "we map when calibration is possible" after the method failed to deliver. While the reframing is intellectually interesting, it does not change the underlying fact: the method does not work well enough for its intended purpose. The identifiability map, while useful, could be established through simulation analysis alone without the ContamCal framework.

**W5. Insufficient novelty for a top venue.** [R2]
- The 4PL+γ model is a direct application of item compromise IRT (Eckerly 2017, Sinharay 2017) with continuous rather than binary exposure — an incremental adaptation, not a methodological advance
- The Fisher Information analysis is a relatively straightforward calculation
- RRF is explicitly disclaimed as non-novel
- The measurement error model is standard Bayesian technique
- What remains genuinely new (signal survival heatmap, identifiability threshold) could be a workshop/short paper, not a full AAAI submission

**W6. The "calibration paradox" undermines practical value.** [R1, R2]
Calibration difficulty is positively correlated with model scale (MAE: 5.8pp at 0.5B → 8.2pp at 7B → 11.8pp at 72B). Signal AUC drops monotonically with scale (0.74 → 0.64 → 0.58). γ-θ posterior correlation increases (0.55 → 0.68). The framework is useful only for small, open-weight, SFT-contaminated models — precisely the regime where contamination is least concerning.

### Moderate

**W7. Systematic undercoverage or vacuously wide CIs.** [R1]
The default model achieves only 76% coverage at the 95% nominal level (Table 11). The measurement error model "fixes" coverage to 92% but at CI width of 22pp — a 60% accuracy model's CI would span [49%, 71%], rendering model selection impossible. No operating point achieves both nominal coverage AND practical width (<10pp).

**W8. γ-θ posterior confounding.** [R1]
The posterior correlation r=0.63 (Table 12 context) confirms identifiability breach — the model confounds "high ability" with "contaminated." This banana-shaped posterior causes sampling difficulty (2.8% divergences, ESS=210, R̂=1.06). At 7B scale, the correlation rises to 0.68.

**W9. Thin reference list and citation issues.** [R2]
22 references is below AAAI norms (30-40 typical). Missing: membership inference foundations (Carlini et al. 2021), IRT identifiability literature (San Martin et al. 2015 on 3PL/4PL), causal inference formalization (Pearl 2009), comprehensive contamination surveys, and key IRT textbooks (Embretson & Reise 2000). Self-Critique citation appears inconsistent across drafts.

**W10. Single model family + single seed for multi-family.** [R1, R2]
Controlled experiments use only the Qwen2.5 family. The Llama validation uses a single seed (no variance estimate) and shows a 3.3pp MAE gap vs Qwen, suggesting architecture-dependent effects that compromise generalizability claims.

**W11. Causal inference analogy is superficial.** [R2]
The paper repeatedly invokes the parallel to observational causal inference (adjusting for confounders rather than eliminating them) but never formalizes it. No DAG, no unconfoundedness discussion, no sensitivity analysis for unmeasured confounding. If the analogy is central, it needs formalization; if merely motivational, it should not be so prominent.

---

## Questions for Authors

1. **On identifiability threshold sensitivity:** The AUC threshold of 0.72 is derived under the 4PL+additive-γ model. How sensitive is this threshold to model specification? If contamination effects are multiplicative or interact with item difficulty, does the threshold change? A 2PL+γ comparison would help disentangle 4PL-specific identifiability issues from γ-specific ones.

2. **On practical deployment:** Given the narrow viability window (SFT regime, ≤1.5B models, open-weight, large benchmarks), who is the intended user? Can you provide a concrete scenario where ContamCal changes a practitioner's decision?

3. **On the RRF failure:** If 4-signal RRF (0.68) underperforms Embedding alone (0.71), why not simply use Embedding as the sole covariate? Have you evaluated a single-signal 4PL+γ model with Embedding scores directly?

4. **On causal formalization:** What is the contamination calibration analog of "no unmeasured confounders"? Is it plausible that training regime, data curation, and architecture do not confound the exposure-score relationship?

5. **On the comparison to linear regression:** Linear regression + CI achieves 6.2pp MAE (vs 6.8pp for 4PL+γ, p=0.18). Since linear regression is radically simpler, what justifies the complexity of the IRT approach? Is the theoretical interpretability of IRT parameters sufficient justification when the parameters themselves are poorly identified?

---

## Minor Issues

- Table numbering in the paper runs 1–20, which is very dense for 11 pages — consider consolidating
- Prior sensitivity analysis (Table 3) presented briefly but is important — deserves more discussion
- The SFT-Clean vs SFT-Contam AUC gap of only 0.02 (Table 15) implies signals detect "training change" broadly rather than contamination specifically — this methodological concern deserves more prominence
- The 144-condition simulation sweep parameters should be made available for reproducibility
- Eq. 2: the additive form θ_j + γ·τ_i − b_i implies contamination shifts the ability-difficulty difference equally for all items, which may not be realistic
- Local independence violation (35% item pairs with residual correlations > 0.05) needs discussion of remedies (testlet models, multidimensional IRT)

---

## Experiment Coverage vs. Design

All 12 imagined experiments from the experimental design are covered in the paper:
- exp-001 through exp-009, exp-012, exp-013, exp-014: all present
- Multi-family (exp-014) severely limited: single seed, partial dosage coverage, GPU budget exhaustion
- 72B (exp-012) observational only, no controlled ground truth
- Overall coverage is comprehensive in breadth but several experiments lack statistical power (multi-family, 72B observational)

---

## Overall Judgment

**Score: 4/10 — Weak Reject**

Both reviewers independently arrived at the same score with converging rationale. The paper tackles an important and timely problem (contamination calibration) with a principled approach grounded in psychometric theory, and it reports its findings with admirable honesty. However, three fundamental issues prevent acceptance:

1. **The method doesn't work well enough.** No significant improvement over linear regression or DCR, with RRF fusion actively degrading signal quality and calibration harming decisions in the RL regime.

2. **The novelty is limited.** The core model is an application of existing item compromise IRT. The Fisher Information analysis and signal survival heatmap, while useful, are insufficient for a full paper at AAAI.

3. **The practical value is confined to a narrow regime** (small, SFT, open-weight models) that is precisely where contamination scrutiny is least needed. The "calibration paradox" — where the most-scrutinized models are the least calibratable — is a fundamental structural limitation, not a correctable flaw.

**Recommendation for revision:**
- Consider submitting the Fisher Information identifiability analysis + signal survival heatmap as a focused empirical/analytical study (workshop or short paper)
- If pursuing a full paper, either (a) develop significantly stronger detection signals that cross the 0.72 AUC threshold, or (b) formalize the impossibility result with proper theoretical lower bounds rather than empirical non-significance
- Expand references to 35+, formalize the causal inference analogy, and resolve the Self-Critique citation
- Multi-family validation needs ≥3 seeds across ≥2 non-Qwen families