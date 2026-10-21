# Paper Framing — contamcal-irt-calibration

## Target Venue
- Primary: AAAI 2027 (expected deadline: Jul-Aug 2026)
- Secondary: ICLR 2027 (expected deadline: Sep 2026)
- ~~EMNLP 2026 ARR May 25~~ (dropped, D001)

## Core Insight
When benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.

## Core Claims (3 条)

1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B), 2+ model families, and 4 benchmarks.

2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.

3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.

## Contributions (Hierarchical)

### Core
1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals
2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)
3. Dual-track validation: controlled SFT injection across multiple model families (internal validity) + ecological RL case study (external validity)

### Supporting
4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds
5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology

## Story Spine
- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
- **Our framing**: ContamCal is a "statistical safety net" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).
- **Headline result template**: "On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage."

## Venue Fit Risks
- **AAAI**: Strong fit for Bayesian/probabilistic methods + empirical ML evaluation. Risk: reviewers less familiar with NLP contamination literature. Mitigation: emphasize general statistical methodology, frame as evaluation methodology contribution.
- **ICLR**: Strong fit for ML methodology + LLM evaluation. Risk: may expect stronger RL validation than observational case study. Mitigation: honest uncertainty quantification framing ("wide CIs are the correct answer, not a limitation").
- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as "new algorithm" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.
- **RL limitation**: RL models get wide CIs. This is honest — frame as "calibration is only as good as its inputs." Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).

## Anticipated Reviewer Concerns & Defenses

| # | Concern | Defense | Experiment |
|---|---------|---------|------------|
| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |
| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |
| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is "best-available proxy", acknowledged as limitation | exp-006, exp-009 |
| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |
| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |
| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |
| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |
| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |
| 9 | Single global γ misspecified? | Per-benchmark γ_k model variant as ablation; report both global and per-benchmark results | exp-006 |
| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |
| 11 | Single model family? | Multi-family validation: Qwen2.5 + at least one additional family (Llama/Pythia) | exp-014 |
| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |

## Evaluation Protocol (5 Metrics)
1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage

## Benchmarks (4)
1. **MMLU** — knowledge-intensive multiple-choice (14K items)
2. **GSM8K** — mathematical reasoning free-form (~1.3K items)
3. **ARC-Challenge** — science reasoning multiple-choice
4. **HumanEval** — code generation with execution evaluation (N=164, noted as potential limitation for 4PL estimation)
- Day-8 contingency: reduce to MMLU + GSM8K

## Baselines (7)
0. **Raw (no adjustment)** — report original benchmark scores as anchor
1. **Remove-and-rescore** — drop flagged items, rescore on remaining
2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT
3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)
4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)
5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)
6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare

## Local Independence Discussion
Standard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.

## Citation Requirements (30+ minimum)
Must include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.
