---
dream_id: dream_20260514T203201
tier: median
overall_score: weak reject
timestamp: 2026-05-14T21:29:57.517670+00:00
---

# Dream Review Report: Structural Consistency for Confidence Estimation in LLM-Based Information Extraction

**Paper**: "Structural Consistency for Confidence Estimation in LLM-Based Information Extraction: A Systematic Comparison and the Correlation-Selection Gap"
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-14

---

## Paper Summary

The paper systematically compares five unsupervised confidence signals for LLM-based information extraction (NER and RE): sequence log-probability, exact match rate (EM), Fleiss' Kappa (FK), soft Jaccard similarity (SJ), and entity-level majority voting confidence. Evaluated on SciERC and CoNLL-2003 with Qwen3-8B and LLaMA-3.1-8B. Three claims: (1) structural consistency signals (voting, SJ) are the strongest quality estimators, substantially outperforming logprob (ΔAUROC up to +0.17); (2) a "correlation-selection gap" exists — strong instance-level quality estimation (ρ≈0.50) does not translate to effective best-of-N selection; (3) compound error propagation in RE degrades all signals, with dramatic per-relation heterogeneity (ρ=0.545 on HYPONYM-OF to ρ=0.004 on FEATURE-OF).

---

## Reviewer 1 (R1): Methods + Experiments

**Soundness**: 3/5 | **Overall**: 4/6 (Weak Accept) | **Confidence**: 4/5

### Strengths
- Comprehensive signal comparison under a unified evaluation protocol (ρ, τ, AUROC, best-of-N F1) produces a directly comparable picture the field lacks
- The correlation-selection gap is genuine and underappreciated — ρ≈0.50 yet no signal beats greedy on NER despite +16.9pp oracle headroom
- Per-relation heterogeneity (Table 8) is the most diagnostic finding; ρ from 0.545 to 0.004 reveals signal collapse invisible in aggregate metrics
- OOD analysis (Table 9) showing logprob sign inversion (ρ: +0.14 → −0.20) is a strong argument for structural signals in deployment
- Decision flowchart in Section 6 maps findings to concrete design choices
- Seed-level variance reporting (SD=0.025 across 3 seeds) adds credibility

### Weaknesses
- **W1 (Major)**: Best-of-N oracle gap not explained mechanistically. Oracle reaches +0.169 above greedy on NER, yet every signal plateaus within +0.003. The paper documents the gap without investigating whether it arises from signal ranking errors, score distribution collapse, or greedy already being near the top of the sample distribution. This is the paper's central tension and it remains unresolved.
- **W2 (Moderate)**: N=8/T=1.0 primary configuration not justified. No principled argument for why N=8 is the evaluation point; practitioner-relevant regime may be N=2 or N=4. N-scaling analysis (Table 6) uses a different setup.
- **W3 (Moderate)**: CoNLL-2003 coverage is asymmetric. Table 4's 2×2 matrix covers NER only. No CoNLL RE experiment. The "consistent across models" claim rests on a narrow cross-section.
- **W4 (Moderate)**: WNUT-17 abandonment (54% F1=0) mentioned in Section 4 but unacknowledged in the paper's claim scope or limitations. This weakens OOD generalization claims.
- **W5 (Moderate)**: SciERC label quality not discussed. FEATURE-OF's ρ_SJ=0.004 may reflect annotation inconsistency rather than signal collapse. Confounding is unaddressed.
- **W6 (Minor)**: Ensemble analysis (Table 7) lacks feature importance ablation — which features contribute to the logistic ensemble?
- **W7 (Major)**: Confidence intervals on ρ missing in main tables (Tables 1–4). Given SciERC RE n≈397, differences of Δρ≈0.05–0.10 may not be statistically significant. Only Table 6 reports seed variance.
- **W8 (Minor)**: No comparison to calibration baselines (temperature scaling, Platt scaling on logprob). These standard post-hoc methods could narrow the logprob/SJ AUROC gap without multi-sample generation.

### Key Questions
- Q1: Top-1 accuracy — what fraction of time does the signal's top-ranked sample have strictly higher F1 than greedy? Distinguishes ranking errors from greedy near-optimality.
- Q2: WNUT-17 — what specifically failed (parsing, model performance, signal degeneration)?
- Q3: FEATURE-OF ρ=0.004 — annotation noise, floor effect, or genuine signal collapse?
- Q4: OOD setup details — which dataset constitutes OOD? What kind of shift?
- Q5: Temperature below T=0.5 — at very low T, structural signals should converge and lose discriminative power.

---

## Reviewer 2 (R2): Novelty + Related Work

**Novelty**: 2/5 | **Significance**: 3/5 | **Overall**: 3/6 (Weak Reject) | **Confidence**: 4/5

### Strengths
- Clean, reproducible experimental setup (two models, two datasets, controlled temperature sweep)
- Per-relation-type heterogeneity is genuinely novel and points to a structural property of RE not previously documented
- OOD logprob inversion is the most novel empirical finding — practically important for deployed IE systems
- Temperature sensitivity analysis distinguishing SJ (robust, Δρ=±0.01) from FK (sensitive, Δρ=±0.06) is methodologically useful
- Decision flowchart synthesizes findings into actionable guidance
- 2×2 cross-validation matrix strengthens structural > logprob claim for NER

### Weaknesses
- **W1 (Major)**: Scope insufficient for a top venue. 2 datasets, 2 models, 1 task family, 5 pre-existing signals. Comparable empirical papers at ACL/NeurIPS cover broader ranges of tasks, model scales, or include mechanistic ablations. No signal is introduced by this paper; a pure benchmarking paper must clear a higher bar of scope or surprise.
- **W2 (Major)**: The correlation-selection gap is reframed prior knowledge. The gap between AUROC-based evaluation and downstream selection improvement is well-studied in selective prediction (Geifman & El-Yaniv 2017), conformal prediction, and uncertainty-aware generation. The paper names and documents a known phenomenon in a new domain but presents it as a discovery.
- **W3 (Major)**: Best-of-N NER failure is underanalyzed. The analysis stops at documenting the gap — no investigation of whether it's a diversity problem (samples cluster near greedy), a scoring problem (all samples score similarly), or a model collapse problem.
- **W4 (Major)**: Only 8B instruction-tuned models tested. Logprob calibration is known to differ substantially between base models (better calibrated) and RLHF-tuned models (distorted). The finding that logprob is weak may not generalize.
- **W5 (Moderate)**: SJ sensitivity to parsing errors not characterized. When the LLM produces malformed outputs (missing brackets, wrong delimiters), SJ may degrade gracefully or catastrophically depending on parsing fallback.
- **W6 (Major)**: Statistical significance underreported throughout. AUROC differences of 0.17 and ρ differences of 0.10–0.20 are point estimates without confidence intervals or permutation tests.
- **W7 (Moderate)**: "First systematic empirical comparison" claim needs qualification given Xiong et al. 2024 and Geng et al. 2025 conduct broad surveys of LLM confidence signals.

### Missing Related Work
- Conformal prediction for structured outputs (Angelopoulos et al., Fisch et al.) — closely related to abstention use case
- Prompt robustness for IE (LLM-IE, GOLLIE lines) — relevant to interpreting what structural consistency actually measures
- CISC (Huang et al. 2025) overlap not clearly differentiated from entity-level voting confidence
- CRF marginals and structured prediction uncertainty — underengaged despite direct relevance to NER

### Positioning Concerns
- **Overclaiming**: "First systematic comparison" is too strong; "correlation-selection gap" is presented as a discovery rather than domain-specific documentation of a known effect
- **Underclaiming**: OOD logprob inversion and per-relation heterogeneity are the paper's strongest contributions but are underemphasized relative to the correlation-selection gap framing

---

## Roundtable: Cross-Sharing and Convergence

### Points of Strong Agreement
1. **Per-relation heterogeneity** is the most diagnostic finding (R1: "most diagnostic"; R2: "genuinely informative")
2. **OOD logprob inversion** is the most novel empirical result (both independently highlight)
3. **Decision flowchart** is practically useful (both independently praise)
4. **Best-of-N NER failure** needs mechanistic explanation, not just documentation (R1-W1, R2-W3)
5. **Statistical reporting** is insufficient for a quantitative empirical paper (R1-W7, R2-W6)

### Points of Disagreement
1. **Correlation-selection gap novelty**: R1 accepts as "genuine and underappreciated"; R2 pushes back as reframed prior knowledge. Converged view: the domain-specific documentation has value, but the framing as a discovery is overclaiming.
2. **Overall scope**: R1 does not contest scope (focuses on execution gaps); R2 raises scope as a major concern. Converged view: scope is sufficient for the claims if properly framed, but the "systematic" qualifier is oversold.

### Converged Strengths (Ranked)
1. OOD logprob inversion — most novel, practically important, not previously documented in IE
2. Per-relation heterogeneity analysis — challenges monolithic signal recommendations
3. Correlation-selection gap empirical documentation — genuine and practically relevant even if conceptually known
4. Unified evaluation protocol enabling fair signal comparison
5. Decision flowchart providing actionable practitioner guidance

### Converged Weaknesses (Ranked by Severity)
1. **(Severe) Best-of-N selection failure mechanism unexplained**: The paper's central tension (high ρ, no selection gain on NER) is documented but not analyzed mechanistically. Score distribution analysis, ranking collision rates, or within-instance variance decomposition could address this.
2. **(Severe) Overclaiming scope**: "First systematic comparison" not defensible without engaging conformal prediction, selective prediction, and CISC literature. Requires reframing.
3. **(Major) Statistical reporting gap**: No confidence intervals on ρ, no significance tests on selection accuracy differences. Undermines empirical credibility of point estimates that are the paper's primary evidence.
4. **(Major) Model and task coverage bounded without adequate acknowledgment**: 8B instruction-tuned models only; logprob conclusions may not transfer to base/larger models. Must be foregrounded as a scope limitation, not buried in limitations list.
5. **(Major) Missing related work engagement**: Conformal prediction for structured outputs, selective prediction literature, CISC differentiation all underengaged. Affects positioning and novelty claims.
6. **(Moderate) Dataset coverage gaps**: WNUT-17 abandonment unacknowledged; CoNLL-2003 asymmetric coverage (NER only, Qwen-only in Table 2). RE claims rest on SciERC alone.
7. **(Moderate) N/T configuration not justified**: N=8/T=1.0 primary configuration lacks sensitivity analysis for practitioner-relevant regimes (N=2,4).
8. **(Minor) SJ parsing error sensitivity and FEATURE-OF annotation noise undercharacterized**
9. **(Minor) No calibration baselines (temperature/Platt scaling on logprob)**
10. **(Minor) Ensemble feature importance ablation absent**

### Experiment Coverage Assessment
Comparing against the imagined experiment list (review_context.yaml):
- **Well covered**: baseline_logprob, baseline_exact_match, baseline_entity_voting, evaluation_metrics_expansion, ner_conll2003, ner_multi_model, ner_llama_conll, ner_n16_scierc, adaptive_compute_demo, signal_ensemble_analysis, selection_curves, re_diagnostic_analysis, temperature_sensitivity_analysis, capability_stratification
- **Partially covered**: re_n16_confirmation (merged into Table 6), ner_ood_robustness (appendix only)
- **Acknowledged gap**: ner_wnut17 (abandoned, mentioned in Section 4)
- Coverage rate: ~15/17 experiments reflected in the paper. Good overall coverage.

---

## Consolidated Assessment

### Overall Score: 3/6 (Weak Reject)

**Rationale**: The paper addresses a real and underserved problem — confidence estimation for LLM-based structured IE. The experimental execution is clean and covers the planned experiment matrix well. Two findings genuinely advance the field: the OOD logprob inversion (structural signals maintain positive correlation while logprob inverts under domain shift) and the per-relation heterogeneity analysis (ρ ranging 100× across relation types). The decision flowchart is a practical artifact the community could use.

However, the paper falls below the acceptance bar at a top-25%-acceptance venue for three converging reasons:

1. **The central contribution is underanalyzed.** The correlation-selection gap — the paper's titular finding — is documented but not explained. Why does ρ≈0.50 fail to produce selection gains when oracle headroom is +16pp? Without a mechanistic hypothesis supported by analysis (score distributions, ranking collision rates, within-instance variance), this remains a labeled observation, not a understood phenomenon.

2. **Overclaiming meets insufficient novelty defense.** "First systematic comparison" and "identification of the correlation-selection gap" both overclaim. The former ignores prior surveys and related confidence estimation work for structured prediction. The latter names a known phenomenon (selective prediction literature) without acknowledging precedent. The individually novel findings (OOD inversion, per-relation heterogeneity) are underemphasized while the less novel framing occupies the title and abstract.

3. **Statistical rigor below the bar for a purely empirical paper.** A paper whose primary contribution is empirical comparison must report uncertainty. Point estimates of ρ without confidence intervals, selection accuracy differences within noise (Δ=+0.003 on NER) claimed as evidence, and missing significance tests weaken the evidentiary foundation.

### Key Conditions for Acceptance (Revision Guidance)

**Mandatory for acceptance**:
1. Add bootstrap CIs to all ρ estimates in main tables; add significance tests to key comparisons (structural vs logprob, selection vs greedy). This is straightforward with existing data.
2. Provide mechanistic analysis of the best-of-N NER failure: score distribution plots, ranking collision analysis, or within-instance quality variance decomposition.
3. Reframe "first systematic comparison" — engage conformal prediction for structured outputs, selective prediction (Geifman & El-Yaniv 2017), and differentiate from CISC. Position contribution as domain-specific characterization within 8B instruction-tuned LLMs.

**Strongly recommended**:
4. Explicitly scope all conclusions to "8B instruction-tuned models" in abstract and conclusion.
5. Foreground OOD logprob inversion and per-relation heterogeneity as headline contributions (these are the genuinely novel findings).
6. Acknowledge WNUT-17 failure and CoNLL asymmetry in limitations with explicit claim scoping.

**Optional but impactful**:
7. N∈{2,4,8} sensitivity curve for practitioner relevance.
8. One base model or larger model experiment to test logprob conclusion generalizability.
9. Brief calibration baseline comparison (Platt scaling on logprob).

### Venue Recommendation
In current form: **Findings/workshop track** at ACL/EMNLP. With mandatory revisions 1–3 addressed: competitive for **main conference** at a top ML/NLP venue.