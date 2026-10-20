# Paper Framing — contamcal-irt-calibration

## Target Venue
- Primary: AAAI 2027 (expected deadline: Jul-Aug 2026)
- Secondary: ICLR 2027 (expected deadline: Sep 2026)
- ~~EMNLP 2026 ARR May 25~~ (dropped, D001)

## Core Insight
When benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017), with 3 non-trivial adaptations for LLM evaluation.

## Core Claims (3 条)

1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model recovers true (uncontaminated) benchmark performance with low calibration error (MAE) and nominal credible interval coverage, validated on controlled SFT contamination injection experiments across 3+ model scales (0.5B-7B) and 4 benchmarks (MMLU, GSM8K, ARC-Challenge, HumanEval).

2. **Signal Aggregation Claim**: Training-free RRF fusion of 4 complementary detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique) provides principled contamination exposure estimation without meta-circularity, outperforming any single signal and degrading gracefully under signal dropout — including a degraded 2-signal mode for closed-weight models.

3. **Uncertainty Quantification Claim**: ContamCal explicitly propagates detection signal noise into calibration uncertainty — SFT-trained models receive tighter credible intervals (multiple reliable signals), RL-trained models receive appropriately wider intervals (primarily Self-Critique), and simulation-validated identifiability bounds establish minimum signal quality thresholds for reliable calibration.

## Contributions (Hierarchical)

### Core
1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT) producing calibrated scores with credible intervals
2. Dual-track validation: controlled SFT injection (internal validity) + ecological RL case study (external validity)
3. 5 baselines + 5 quantitative evaluation metrics for contamination-aware calibration

### Supporting
4. Simulation-based identifiability study: systematic parameter sweep establishing minimum signal quality / model count thresholds
5. Signal survival analysis: systematic evaluation of which detection signals remain reliable after SFT vs. RL post-training (signal × regime AUC heatmap)

## Story Spine
- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration as the principled alternative.
- **Our framing**: ContamCal is a "statistical safety net" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. This is grounded in educational measurement's item compromise IRT tradition, with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics), (b) binary leakage → continuous exposure scores (requires generalization), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware modeling).
- **Headline result template**: "On {benchmark}, ContamCal recovers true model performance within {X}% MAE with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage. Even under noisy RL-regime detection (Self-Critique AUC ~0.65), calibrated scores with wider CIs improve model selection decisions by {R}% expected regret reduction."

## Venue Fit Risks
- **AAAI**: Strong fit for Bayesian/probabilistic methods + empirical ML evaluation. Risk: reviewers less familiar with NLP contamination literature. Mitigation: emphasize general statistical methodology, frame as evaluation methodology contribution.
- **ICLR**: Strong fit for ML methodology + LLM evaluation. Risk: may expect stronger RL validation than observational case study. Mitigation: honest uncertainty quantification framing ("wide CIs are the correct answer, not a limitation").
- **Novelty ceiling**: Core method is synthesis of existing components (detection signals + IRT). Defense: cross-disciplinary transfer with 3 non-trivial adaptations + simulation-validated identifiability bounds as methodological contribution. Not "engineering glue" — each adaptation requires non-obvious modeling decisions.
- **RL "so what"**: RL models only get wide CIs. Defense: expected regret quantification shows even wide CIs improve model selection vs. naive scores.

## Anticipated Reviewer Concerns & Defenses

| # | Concern | Defense | Experiment |
|---|---------|---------|------------|
| 1 | θ and γ identifiable? | MVP validated: γ rel_bias <8%, θ_residual_exp_corr=0.058 at corr=0.38 | exp-004 (sweep) |
| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated | exp-003 (ablation) |
| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity) | exp-006, exp-009 |
| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |
| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d parameters necessary for realistic item modeling | exp-006 |
| 6 | Too few models (50)? | Few-examinee regime study + Growing Pains pre-estimation strategy | exp-011 |
| 7 | Noisy exposure scores | Noise propagation analysis: calibrated noise injection → CI widening quantified | exp-005 |
| 8 | No baselines | 5 baselines: remove-rescore, single-signal 2PL+γ, vanilla 4PL, linear regression+CI, Emperor's mitigations | exp-006 |

## Evaluation Protocol (5 Metrics)
1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy
2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage

## Benchmarks (4)
1. **MMLU** — knowledge-intensive multiple-choice (14K items)
2. **GSM8K** — mathematical reasoning free-form (~1.3K items)
3. **ARC-Challenge** — science reasoning multiple-choice
4. **HumanEval** — code generation with execution evaluation
- Day-8 contingency: reduce to MMLU + GSM8K

## Baselines (5)
1. **Remove-and-rescore** — drop flagged items, rescore on remaining
2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT
3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)
4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)
5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)
