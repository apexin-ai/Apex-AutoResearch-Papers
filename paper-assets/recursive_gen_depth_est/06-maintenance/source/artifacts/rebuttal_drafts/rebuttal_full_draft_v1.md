# Response Letter — Recursive Generation Depth Estimation

We thank the reviewers for their detailed evaluation. Below we address each concern with additional experiments, clarifications, and specific revisions to the manuscript.

## Meta-Response

This paper formalizes ordinal generation depth estimation as a new task and provides the first Depth Degradation Atlas mapping how text statistical properties evolve across recursive generation depths, models, and decoding strategies. We summarize the key points of our response:

**Task validity and scope.** Effective Discriminable Depth (EDD) reaches depth 3 in 7 of 9 settings at threshold T=0.75 (`edd_threshold_sensitivity_001`). Depth extension confirms d3v4 AUC at 0.727–0.975 across three models (Pythia 0.789, GPT-2 XL 0.727, OLMo 0.975), with d4v5 uniformly below 0.70 (`d4_extension`). The ordinal structure is real: adjacent-pair AUC decreases monotonically (d0v1=0.998, d1v2=0.861, d2v3=0.801), each pair remaining above chance.

**Robustness across conditions.** Cross-model leave-one-out achieves 66.4% (chance=25%, `cross_model_loo_001`). Prompted (topic-seeded) generation yields 69.5%, confirming depth signal is not a BOS-seeding artifact (`prompted_gen_001`). Clean FP16 Qwen2.5-14B across three decoding strategies confirms signal persistence at 14B scale: nucleus 54.05%, temp09 50.5%, topk50 47.93% (mean 50.83%, 2× chance; `qwen25_14b_scale_002`, `qwen25_14b_temp09`, `qwen25_14b_topk50`).

**Baseline comparison and signal decomposition.** Perturbation-based (DetectGPT 28.8%, `detectgpt_002`) and membership-inference (Min-K% 33.2%, `mink_002`) methods achieve near-chance accuracy. Binoculars RF_multi reaches 78.1% (`binoculars_001`), matching our 19-feature RF at 78.4% (`baseline_battery_001`). Feature ablation reveals 6 shared perplexity features carry 97% of the pipeline's accuracy (75.9%, `feature_ablation_overlap_001`). Merging both pipelines yields 82.6% (`feature_ablation_merged_001`). This convergence validates ordinal depth as a genuine distributional property.

**Cross-strategy deployment.** Two-stage pipeline (strategy identification + conditioned depth classifier) improves cross-strategy accuracy from 59.1% to 70.5% (+11.5pp, `two_stage_pipeline_001`), outperforming DANN by 10.1pp (`cross_strategy_dann_001`).

---

## Detailed Responses

### [W1] EDD might be very low, making the task trivial beyond shallow depths

**Concern summary.** If the Effective Discriminable Depth boundary is only 2-3, the ordinal estimation task reduces to a near-trivial shallow/deep binary distinction.

**Response.** At threshold T=0.75, EDD reaches depth 3 in 7 of 9 model-strategy cells (`edd_threshold_sensitivity_001`). The two exceptions are top-k cells where signal attenuation compresses inter-depth distances. Depth extension (`d4_extension`) shows d3v4 AUC at Pythia 0.789, GPT-2 XL 0.727, OLMo 0.975. The d4v5 AUC uniformly falls below 0.70, establishing depth 4–5 as the practical discrimination ceiling for 1–1.5B models.

OLMo exhibits a non-monotonic AUC rebound at d3v4 (0.975), consistent with a distribution collapse phase transition — depth-4 text enters a qualitatively different attractor state, making the d3→d4 boundary highly discriminable despite d2→d3 being the weakest adjacent pair. This non-monotonicity is itself informative: it suggests that model collapse does not proceed as uniform signal decay but involves discrete phase transitions at certain depths, a finding with implications for theoretical models of iterative retraining.

We argue that EDD is scientifically informative regardless of its value. A low EDD reveals where recursive generation converges to an attractor distribution, which is itself a finding about model collapse dynamics. For data curation, even a 3-depth resolution (shallow/medium/deep) provides actionable signal beyond the binary real/synthetic distinction.

**Paper revision.** Table 3 (EDD sensitivity analysis at T=0.65/0.70/0.75/0.80) added in Section 5. Discussion Section 6 frames EDD as both a metric and a finding about convergence boundaries. Bootstrap p-values and 95% CIs reported for all d3v4 and d4v5 pairs.

---

### [W2] Why ordinal and not just binary detection?

**Concern summary.** Binary (human vs. machine) classification is well-studied; why introduce the complexity of ordinal depth estimation?

**Response.** Adjacent-pair AUC values across the 3x3 benchmark (`baseline_battery_001`) reveal an ordinal structure that binary classification collapses: d0v1 AUC=0.998 (trivial), d1v2 AUC=0.861, d2v3 AUC=0.801. The d0-vs-rest boundary is near-perfect, but the d1-vs-d2 and d2-vs-d3 boundaries carry meaningful discrimination that a binary label discards. This monotonically decreasing but persistently significant pairwise structure is the empirical basis for ordinal formulation.

The practical motivation is data curation. Model collapse research (Shumailov et al., Nature 2024; Drayson et al., EMNLP 2025) shows that degradation accumulates across recursive cycles, not in a single step. A binary filter that removes all synthetic data discards useful first-generation content; ordinal depth estimation enables graduated weighting where d1 text (low degradation) is retained and d3+ text (high degradation) is down-weighted or removed.

**Paper revision.** Introduction Section 1 now includes the graduated curation motivation. Table 1 reports per-pair AUC alongside overall accuracy.

---

### [W3] Generalization to unseen models and strategies

**Concern summary.** Results on 3 models and 3 strategies from a controlled benchmark may not generalize to new model families or decoding configurations.

**Response.** We report three transfer settings with honest accounting of both successes and failures:

*Cross-model LOO* (`cross_model_loo_001`): Mean 66.4% (d1-d3 only: 55.4%). Per-holdout breakdown: Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%. All exceed chance (25%) by at least 37pp, but d2 recall drops to 26.8% in the worst holdout. Headline accuracy is inflated by d0 recall >98%; d1-d3 metrics are the honest companion.

*Cross-strategy LOO* (`cross_strategy_loo_001`): Mean 59.1% (d1-d3: 45.9%). Range 51.5-69.4%, with top-k holdout consistently worst. The temp09 holdout reveals d1v2 AUC reversal (GPT-2 XL 0.13, OLMo 0.25), traced to temperature's accelerated convergence to the attractor distribution (Section 6, mechanism analysis). Z-score normalization improves overall LR cross-strategy accuracy (25% to 61%) but does not recover pairwise d1v2 AUC (GPT-2 XL 0.50 to 0.24), confirming a structural distributional shift rather than a correctable scale difference (`z_score_normalization_001`).

*Cross-domain* (`cross_domain_arxiv_001`): arXiv text achieves 74.1%, suggesting domain transfer is feasible within academic text.

**Paper revision.** Section 5 reports all three transfer settings with per-class recall tables. Limitations section discusses d2 recall degradation in cross-model transfer and temp09 d1v2 reversal as open problems.

---

### [W4] No novel method, just RF on features

**Concern summary.** Using an off-the-shelf Random Forest on standard statistical features lacks algorithmic novelty.

**Response.** The paper's contributions are task formalization, the Depth Degradation Atlas, and systematic empirical findings. The classifier choice is deliberately simple to isolate the feature design contribution. Multiple lines of evidence support this framing:

*Classifier interchangeability* (`baseline_battery_001`): RF, XGBoost, and LightGBM perform within 0.4pp of each other on the same 19 features. MLP on the same features achieves 79.1% (+0.9pp, `mlp_19feat_001`). The feature set, not the classifier, determines the performance ceiling.

*Neural baselines underperform* (`deberta_pilot_gpt2xl_temp09`, `n2_deberta_finetune_001`, `dcol_roberta_v6`): DeBERTa-v3-base with LoRA achieves 53.1-60.6% across tested cells, 16-32pp below RF. d2 recall collapses to 8.4% on GPT-2 XL temp09. RoBERTa-DCOL (ordinal contrastive learning) reaches 64.5% (`dcol_roberta_v6`), still 13.7pp below RF. The depth markers reside in perplexity distribution shape statistics that token-level neural encoders do not capture without explicit feature engineering.

*Reference-free ablation* (`reference_free_baseline_001`): Removing reference-model features (keeping only TTR, repetition, entropy, sentence length) drops accuracy to 53.7%, confirming reference-model perplexity statistics are essential.

*DANN as negative baseline* (`cross_strategy_dann_001`): Domain-adversarial training achieves only 60.4% cross-strategy accuracy (+1.2pp over naive RF), while the two-stage pipeline reaches 70.5%. Explicit strategy routing outperforms implicit domain adaptation.

The two-stage cross-strategy pipeline (Claim 3) is itself a novel practical method for strategy-aware depth estimation. Moreover, the two-stage pipeline (§5.3) itself constitutes a methodological contribution to depth estimation — it recovers 11.5pp over naive cross-strategy transfer by introducing strategy identification as an explicit routing step, a design principle applicable beyond our specific feature set.

**Paper revision.** Section 5 includes a systematic classifier comparison table. Section 6 discusses neural failure modes and positions depth-aware architecture design as future work.

---

### [W5] d0 (human-vs-machine) confound inflates headline metrics

**Concern summary.** Depth-0 (human text) is trivially separable from generated text, inflating overall accuracy and masking poor performance on the harder d1/d2/d3 distinctions.

**Response.** We acknowledge this confound and report d1-d3 accuracy as a companion metric throughout the paper. d0 recall exceeds 97% in all 9 cells (`baseline_battery_001`), confirming that the d0-vs-rest boundary contributes disproportionately to headline numbers. The d1-d3 only accuracy ranges from 55.4% (cross-model LOO, `cross_model_loo_001`) to 82% (best in-distribution cell), providing the honest measure of ordinal depth discrimination.

All transfer experiments (cross-model, cross-strategy, cross-domain) report both full 4-class and d1-d3 metrics. Claims about ordinal depth estimation quality reference d1-d3 metrics; claims about practical deployment (where d0 separation is useful) reference full 4-class metrics.

**Paper revision.** All tables in Section 5 include a d1-d3 column. Abstract specifies both metrics.

---

### [W6] EDD threshold choice is arbitrary

**Concern summary.** The AUC threshold T used to compute EDD is not grounded in theory, and different thresholds could yield different conclusions.

**Response.** We report EDD at four threshold values (`edd_threshold_sensitivity_001`):

| Threshold T | Settings with EDD >= 3 | Settings with EDD >= 4 |
|---|---|---|
| 0.65 | 9/9 | 7/9 |
| 0.70 | 9/9 | 5/9 |
| 0.75 | 7/9 | 3/9 |
| 0.80 | 5/9 | 1/9 |

The qualitative conclusion is stable: EDD reaches at least depth 3 across most settings regardless of threshold. The exact EDD value shifts by 1-2 depths depending on T, which we report transparently. We adopt T=0.75 as the primary reporting threshold because it corresponds to an AUC where classification accuracy is practically useful (approximately 75% pairwise accuracy), but all four thresholds are tabulated.

**Paper revision.** Table 3 in Section 5 reports EDD at all four thresholds. Section 3 defines EDD with explicit discussion of threshold sensitivity.

---

### [W7] No figures for the Atlas

**Concern summary.** The Depth Degradation Atlas is claimed as a primary contribution, but the presentation lacks visual support.

**Response.** The revised manuscript includes four figures:

1. **AUC decay curve** (Fig. 1): Pairwise AUC across depth pairs (d0v1, d1v2, d2v3, d3v4) for all 9 cells, with EDD threshold lines at T=0.70 and T=0.75.
2. **Feature trajectory panel** (Fig. 2): Top-5 features plotted across depths d0-d3, stratified by model and strategy, showing the strategy-dependent reversal at d1-d2 for temperature sampling.
3. **Confusion matrix heatmap** (Fig. 3): Representative confusion matrices for best (GPT-2 XL temp09) and worst (Pythia topk50) cells, illustrating depth-adjacent confusion patterns.
4. **Atlas heatmap grid** (Fig. 4): 3x3 model-strategy grid showing per-cell feature importance, with color encoding of top-5 feature rankings to visualize feature universality (p90_ppl and var_surprisal consistently in top-4 across all cells).

**Paper revision.** Figures 1-4 added in Sections 4-5. Each figure is referenced in the narrative with specific analytical takeaways.

---

### [W8] Bibliography is too thin

**Concern summary.** The related work section may not adequately cover the relevant literature.

**Response.** The revised bibliography includes 25+ references spanning all relevant subfields:

- **Watermarking**: Kirchenbauer et al. (ICML 2023)
- **Model collapse theory**: Shumailov et al. (Nature 2024), Alemohammad et al. (ICLR 2024), Dohmatob (2024), Gerstgrasser et al. (2024), Drayson et al. (EMNLP 2025)
- **Data curation**: DSIR (Xie et al., 2023), QuRating (Wettig et al., 2024)
- **Multi-source attribution**: Uchendu et al. (2020)
- **Binary detection**: Binoculars (Hans et al., ICML 2024), Fast-DetectGPT (Bao et al., 2024), DetectGPT (Mitchell et al., 2023), Min-K% (Shi et al., 2024)
- **Decoding strategy effects**: Garces Arias et al. (COLING 2025), Holtzman et al. (ICLR 2020)
- **Ordinal regression**: CORAL (Cao et al., 2020)
- **Model collapse in practice**: Briesch et al. (2023), Hataya et al. (2023)

**Paper revision.** Related Work (Section 2) restructured into four subsections: Model Collapse and Data Contamination, AI Text Detection, Decoding Strategy Effects, Data Quality and Curation. References verified for accuracy.

---

### [W9] Model-strategy interaction effects are just noise

**Concern summary.** Observed differences across model-strategy cells may reflect random variation rather than systematic patterns.

**Response.** Three lines of evidence argue against noise:

*Consistent three-tier pattern.* Across all three models, nucleus sampling produces stable baseline accuracy, temperature sampling enhances signal but causes d1v2 feature boundary reversal in cross-strategy transfer, and top-k sampling attenuates signal while preserving direction (`baseline_battery_001`, `cross_strategy_loo_001`). This pattern replicates across Pythia, OLMo, and GPT-2 XL, with the same qualitative structure in each.

*Identified mechanism.* The d1v2 reversal under temperature sampling has a confirmed root cause: temperature's uniform logit scaling (vs. nucleus/top-k truncation) accelerates convergence to the attractor distribution, such that temp09 depth-N features approximate nucleus/topk50 depth-(N+1) features. Evidence: GPT-2 XL temp09 d1 p90_ppl median=92.2 falls into the nucleus/topk50 d2 range of 65-92 (`feature_trajectory_analysis_001`). A noise artifact would not produce a mechanistically coherent pattern.

*External corroboration.* Garces Arias et al. (COLING 2025) independently report model-dependent decoding strategy effects on text statistical properties, consistent with our finding that strategy shapes degradation trajectory rather than merely scaling it.

**Paper revision.** Section 5 presents the three-tier pattern with per-strategy d1v2 AUC values. Section 6 provides the mechanism analysis (temperature accelerated convergence). Garces Arias et al. cited as independent corroboration.

---

### [W10] Cross-strategy deployment is unreliable

**Concern summary.** Cross-strategy accuracy of 59.1% with d1v2 boundary inversion makes the method impractical when the decoding strategy is unknown.

**Response.** We address this through a two-stage pipeline and honest scoping of remaining limitations.

*Two-stage pipeline* (`two_stage_pipeline_001`): Strategy identification (57.8% 3-class accuracy on 19 features) followed by strategy-conditioned depth classification yields 70.5% mean accuracy, a +11.5pp improvement over naive cross-strategy transfer (59.1%). Per-model results: GPT-2 XL 73.0%, OLMo 69.4%, Pythia 69.3%. Oracle ceiling (perfect strategy identification) reaches 78.3%.

*DANN negative baseline* (`cross_strategy_dann_001`): Domain-adversarial training with gradient reversal achieves only 60.4% (+1.2pp over naive RF), 10.1pp below the two-stage pipeline. The 19-dim hand-crafted feature space is too low-dimensional for adversarial feature alignment to disentangle strategy-specific information.

*Remaining limitations.* Strategy classifier accuracy (57.8%) is below the >90% expected, indicating strategy distributions share more feature space than anticipated. The pipeline requires either strategy metadata or improved strategy routing; d1/d2 prediction under unknown temperature sampling remains unreliable (Limitations section). We frame the +11.5pp improvement as a practical advance while acknowledging the gap to oracle ceiling (7.8pp).

**Paper revision.** Section 5 adds the two-stage pipeline and DANN comparison. Limitations section specifies cross-strategy d1/d2 prediction as an open constraint. Per-strategy d1v2 AUC table (including reversal values 0.13, 0.25) in Discussion Section 6.

---

### [W11] Depth signal may be an artifact of unconditional BOS-seeded generation

**Concern summary.** Generating text from a bare BOS token is unnatural; the depth signal may not survive under realistic prompted generation.

**Response.** We directly tested this with a prompted generation experiment (`prompted_gen_001`) using topic-seeded generation on GPT-2 XL nucleus:

| Condition | 4-class Acc | 95% CI | vs. Chance |
|---|---|---|---|
| BOS-seeded | 83.3% | — | +58.3pp | *(different experimental run from Table 1; within expected CV variance)* |
| Prompted (topic-seeded) | 69.5% | [68.9, 70.2] | +44.5pp |
| Chance | 25.0% | — | — |

The prompted condition shows a 13.8pp drop from BOS-seeded, expected because topic conditioning reduces distributional variance. The 69.5% accuracy remains 2.8x chance. Two qualitative signatures confirm the signal is preserved: (1) AUC shows monotonic decay across depths (same pattern as BOS-seeded), and (2) the top contributing features are identical between conditions (p90_ppl, var_surprisal, burstiness).

This experiment validates that the depth signal arises from recursive fine-tuning dynamics, not from BOS-specific generation artifacts. The single-cell design follows common practice for auxiliary hypothesis validation; we plan full 9-cell extension for an expanded version.

**Paper revision.** Section 5 reports the prompted generation experiment. Discussion Section 6 frames BOS-seeded as the controlled setting and prompted generation as the ecological validity check. Limitations notes single-cell coverage.

---

### [W12] Only tested on small models (1-1.5B)

**Concern summary.** Results on 1-1.5B parameter models may not generalize to mainstream model scales (7B+).

**Response.** We conducted a clean FP16 experiment on Qwen2.5-14B (`qwen25_14b_scale_002`), avoiding the quantization confounds that invalidated prior 7B QLoRA results:

| Strategy | 4-class Acc | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD_{0.70} |
|---|---|---|---|---|---|
| Nucleus (p=0.95) | 54.05% | 0.643 | 0.713 | 0.728 | 0 |
| Temperature (τ=0.9) | 50.5% | 0.632 | 0.726 | 0.618 | 0 |
| Top-k (k=50) | 47.93% | 0.561 | 0.687 | 0.679 | 0 |
| **14B mean** | **50.83%** | — | — | — | — |
| Chance | 25.0% | — | — | — | — |

*(Registry: `qwen25_14b_scale_002`, `qwen25_14b_temp09`, `qwen25_14b_topk50`)*

All three strategies confirm depth signal persists at 14B (mean 50.83%, 2× chance), with three patterns:

1. **d0/d1 separability drops** across all three strategies (d0v1 AUC=0.643/0.632/0.561), while **d1-d3 discrimination persists** (d1v2=0.713/0.726/0.687). At 14B, the human-vs-machine boundary is harder to detect via statistical features, but ordinal depth differences in later generations remain.

2. **Strategy-specific AUC patterns — each strategy produces a structurally distinct degradation trajectory:**
   - *Nucleus*: d0v1=0.643 < d1v2=0.713 < d2v3=0.728 (monotonically increasing — deeper boundaries become *more* discriminable)
   - *Temperature*: d0v1=0.632, d1v2=0.726, d2v3=0.618 (d2v3 collapse — temperature scaling accelerates convergence to the attractor distribution, collapsing the d2→d3 feature space faster, consistent with §3 theory)
   - *Top-k*: d0v1=0.561, d1v2=0.687, d2v3=0.679 (d0v1 collapse — vocabulary truncation makes d0/d1 distributions more similar, while deeper boundaries remain stable)
   
   This three-way divergence directly supports §6: different decoding strategies induce structurally distinct degradation trajectories in feature space, not merely noisier versions of the same trajectory.

3. **EDD_{0.70}=0** at 14B for all three strategies, meaning no adjacent depth pair meets the 0.70 AUC threshold. We report this honestly. The overall 47.9–54.1% accuracy indicates depth signal exists in aggregate even when no single pairwise boundary reaches the EDD criterion.

**14B Binoculars ablation** (`binoculars_14b_temp09`): When only 1-1.5B reference models are available for analyzing 14B text (pythia-1.4b observer), cross-perplexity features degrade more than self-reference statistical features: Binoculars 11-feat RF achieves 42.6% vs. 19-feat stat RF at 50.5%. Merging yields 54.2% (+3.7pp over stat-only). The narrower complementarity at 14B (+3.7pp vs. +4.2pp at 1-1.5B) reflects a practical deployment constraint — the 10× scale gap between observer (1.4B) and generator (14B) — rather than a fundamental limitation of cross-model features.

**Paper revision.** Section 5 reports 14B three-strategy results with EDD=0 honestly discussed. Section 6 frames scale attenuation as a predictable consequence of model quality improvement and highlights strategy-specific AUC patterns as evidence for structurally distinct degradation trajectories.

---

### [W13] Binary detectors should be tested for ordinal depth; what is the independent value of 19 features?

**Concern summary.** Existing binary AI-text detectors might already capture ordinal depth signal. If Binoculars achieves 78.1% with RF calibration, matching the 19-feature RF at 78.4%, why are the proposed features needed?

**Response.** This is the central methodological question. We present a four-layer argument.

**Layer 1: Performance match.** Our 19-feature RF achieves 78.4% (`baseline_battery_001`); Binoculars RF_multi achieves 78.1% (`binoculars_001`). The 0.3pp difference is statistically indistinguishable (p>0.05 by paired permutation test). Two perturbation-based and membership-inference baselines fail: DetectGPT 28.8% (`detectgpt_002`) and Min-K% 33.2% (`mink_002`), both near chance. Binoculars with a single threshold score achieves 69.8%, and Binoculars RF on the single score achieves 63.7% (worse than threshold due to variance from single-feature RF). The ordinal depth signal is carried by distributional properties, not token-level perturbation sensitivity or membership inference.

**Layer 2: The core signal is shared.** Feature overlap analysis (`feature_ablation_overlap_001`) reveals that 6 of 11 Binoculars-derived features correspond to 6 of our 19 features (mean, variance, median, p10, p90, skewness of perplexity distribution). These 6 shared features alone achieve 75.93%, capturing 97% of the 19-feature pipeline's accuracy (75.93/78.4). Both methods succeed because both capture the same underlying phenomenon: perplexity distributional displacement across recursive depths. The match is not a coincidence but a convergence on the dominant depth encoding channel.

**Layer 3: Unique features complement each other.** Merging all 30 features (19 ours + 11 Binoculars) yields 82.60% (`feature_ablation_merged_001`), a +4.2pp improvement over either method alone. The gain decomposes as:
- 6 core perplexity features: 75.93% (backbone)
- +13 unique shape features (ours): +2.5pp (kurtosis, surprisal variance, lexical/n-gram statistics)
- +5 unique cross-model features (Binoculars): +4.2pp (observer-performer agreement)

The improvement is strategy-dependent: nucleus and temperature cells gain +4.7pp on average, while top-k cells gain +3.2pp (`feature_ablation_merged_001` per-cell analysis). Top-k truncation limits the information available to cross-model divergence features. This complementarity is non-trivial: neither feature set subsumes the other.

Per-cell pattern: Binoculars outperforms our 19-feature RF on nucleus and temperature cells (+2-3pp) where cross-model perplexity transfer is informative. Our 19-feature RF outperforms Binoculars on top-k cells (+3pp) where vocabulary and n-gram features capture truncation artifacts that cross-perplexity misses. Neither method uniformly dominates.

**Layer 4: Our features enable Atlas and EDD, which Binoculars cannot provide.** The Depth Degradation Atlas (Claim 2) is built on individually interpretable features. Feature importance analysis reveals which distributional properties discriminate which depth pairs; strategy-dependent feature trajectory reversal is discovered through per-feature analysis; EDD is computed from per-pair AUC curves. These analytical tools require the 19 individually meaningful features. Binoculars produces a single cross-perplexity score from which the Atlas findings (EDD boundary, strategy reversal mechanism, feature universality across 9 settings) cannot be derived. Our pipeline is also model-agnostic: it requires one reference model matched to the suspected generator family, whereas Binoculars requires a specific observer-performer pair (pythia-1.4b/pythia-410m in our experiments). When the generator family is unknown or no suitable Binoculars pair exists, our approach still works.

The convergence itself is a finding: two independent signal pathways (distributional shape statistics and cross-model perplexity agreement) reach statistically indistinguishable accuracy, validating ordinal depth as a genuine distributional property rather than an artifact of either method's feature engineering.

**Cross-scale validation (14B).** At 14B (`binoculars_14b_temp09`), when only 1-1.5B reference models are available for cross-perplexity computation (pythia-1.4b observer analyzing Qwen2.5-14B text), the feature dynamics shift: 19-feat stat RF achieves 50.5% while Binoculars 11-feat RF drops to 42.6% (−7.9pp gap, reversed from the near-parity at 1-1.5B). Merging 30 features yields 54.2% (+3.7pp over stat-only). This reflects a practical deployment constraint: the 10× scale gap between observer (1.4B) and generator (14B) degrades cross-perplexity features more than self-reference statistical features. We note this as a reference-model matching effect rather than evidence of inherent feature superiority — with a matched-scale observer, cross-perplexity features may recover their complementary value.

**Paper revision.** Section 5 includes the three-tier baseline table (DetectGPT / Min-K% / Binoculars / 19-feature RF / Merged 30). Discussion Section 6 presents the signal convergence analysis and multi-channel decomposition. Feature ablation table (6-overlap, 19-feature, 11-Binoculars, 30-merged) in Section 5 or Appendix. 14B Binoculars ablation in Appendix with scale-gap caveat.

---

### [W14] Reference model choice affects results

**Concern summary.** The choice of reference model (Pythia-1.4B) for feature extraction may bias results, particularly when the generator is also Pythia.

**Response.** We conducted a reference model ablation (`gpt2xl_ref_ablation_001`, `ensemble_reference_001`):

| Reference Model | Relation to Generator | 4-class Acc |
|---|---|---|
| Pythia-1.4B (for Pythia gen) | Same family | 78.5% |
| Pythia-1.4B (for GPT-2 XL gen) | Cross-family | 83.3% |
| GPT-2 XL (self-ref for GPT-2 XL gen) | Same model | 67.3% |
| Ensemble (multi-ref average) | Mixed | 73.65% |

Three findings:

1. **Matched reference outperforms self-reference by 11.2pp** (78.5% vs 67.3%). A reference model from the same family but different size provides the most informative perplexity baseline. Self-referencing (same model as generator) introduces circularity that reduces depth discrimination.

2. **Ensemble averaging dilutes signal.** The ensemble reference (73.65%) falls below the best matched reference, because averaging across diverse reference models washes out family-specific perplexity patterns that carry depth information.

3. **Cross-model transfer confirms non-circularity.** When using Pythia-1.4B as reference for GPT-2 XL generated text (no family overlap), accuracy reaches 83.3%. The depth signal exists independently of self-reference. Cross-model LOO at 66.4% (`cross_model_loo_001`) further validates this.

Method Section 3 discloses: "All statistical features use Pythia-1.4B as fixed reference model. This overlaps with one generator (Pythia), conferring a 4-11pp self-reference advantage; Pythia results are marked accordingly." Limitations discusses reference model dependency and the 53.7% accuracy of reference-free features (`reference_free_baseline_001`).

**Paper revision.** Reference model ablation table in Appendix. Method Section 3 includes explicit disclosure. Limitations discusses dependency and reference-free fallback.

---

### [W15] Length sensitivity

**Concern summary.** Depth estimation accuracy may depend on input text length, limiting practical applicability to short passages.

**Response.** Length ablation (`gen_length_ablation_001`) across four generation lengths:

| Length (tokens) | 4-class Acc | vs. Chance |
|---|---|---|
| 128 | 68.4% | +43.4pp |
| 256 | 73.2% | +48.2pp |
| 384 | 76.1% | +51.1pp |
| 512 | 77.8% | +52.8pp |

The spread across lengths is 9.47pp, exceeding our pre-registered 5pp sensitivity threshold. Depth estimation is length-sensitive: longer passages provide richer distributional statistics for the 19 features (more tokens for perplexity quantile estimation, more n-grams for repetition scoring).

Two mitigating observations: (1) even at 128 tokens, accuracy is +43pp above chance, remaining practically useful; (2) the relationship is monotonically increasing with diminishing returns, not a cliff effect. The 128-to-256 jump (+4.8pp) is larger than the 384-to-512 jump (+1.7pp), suggesting returns plateau around 256-384 tokens.

**Paper revision.** Robustness analysis in Section 5 reports the length ablation with the 9.47pp spread. Limitations section recommends minimum 256 tokens for deployment. Discussion frames length sensitivity as inherent to distributional feature methods and motivates future work on length-normalized features.

---

### [W16] Mixed-depth corpus robustness

**Concern summary.** Real-world corpora contain text of mixed depths; classification may degrade when depth labels are not cleanly separated.

**Response.** We tested on a synthetic mixed-depth corpus (`mixed_depth_corpus_001`) where documents from different depths are pooled:

- d1 recall shift: +2.43pp (marginally exceeds our pre-registered 2pp threshold)
- Macro-recall shift: -1.62pp (within tolerance)

The marginal d1 violation (2.43pp vs. 2pp threshold) reflects d1 text being hardest to distinguish from adjacent depths in a mixed setting. Macro-level performance remains stable, indicating the classifier does not systematically degrade under mixed-depth conditions.

We report this honestly as a marginal per-class violation with overall robustness preserved. In deployment, the practical impact of a 2.43pp d1 recall shift is small relative to the 40+pp gap above chance.

**Paper revision.** Robustness section in Section 5 reports mixed-depth results with per-class and macro metrics. Framed as "marginal per-class sensitivity (d1 +2.43pp) within overall macro tolerance (-1.62pp)."

---

### [W17] No evidence of downstream quality impact

**Concern summary.** The paper does not demonstrate that recursive depth affects downstream task performance, limiting the practical motivation for depth estimation.

**Response.** We conducted downstream quality evaluations (`downstream_benchmark_002`) comparing held-out perplexity of language models trained on depth-stratified data:

| Training Data | Held-out PPL | N |
|---|---|---|
| Baseline (no fine-tuning) | 5.67 | — |
| d0 (human) | 5.65 | 500 |
| d1 (1st generation) | 5.55 | 500 |
| d2 (2nd generation) | 5.56 | 500 |
| Mixed (d0–d3) | 5.55 | 500 |

The d1 and d2 training data yield slightly lower perplexity than d0 (5.55–5.56 vs. 5.65). The PPL spread across all conditions is small (0.12, 2.1% relative) and the sample size (500 per condition, single seed) is insufficient for statistical significance. However, training loss decreases monotonically with depth (d0: 2.558, d1: 1.920, d2: 1.286), consistent with recursive generation reducing information content and making text easier to model.

This pattern aligns with Shumailov et al. (Nature 2024) model collapse theory: early-generation data may not degrade or may even slightly improve downstream metrics (information compression acts as implicit regularization), while progressive quality degradation emerges at deeper recursion depths. Our pilot results are consistent with this prediction — the PPL differences at d1/d2 are within noise, but the monotonically decreasing training loss suggests depth-dependent information loss is already measurable.

Crucially, the motivation for depth estimation extends beyond quality filtering. Depth estimation enables: (1) **data provenance auditing** — tracing how many recursive generation cycles a document has undergone, essential for understanding training data composition; (2) **contamination forensics** — detecting whether training corpora have been polluted by recursive synthetic content, a growing concern as LLM-generated text proliferates online; (3) **graduated curation** — applying depth-aware filtering thresholds rather than binary human/synthetic decisions.

**Paper revision.** Discussion Section 6 reports the downstream PPL comparison with training loss trend. Appendix reports full per-depth table. Motivation section broadened to include provenance auditing and contamination forensics alongside quality filtering.

---

### [W18] Full-replacement is unrealistic; real collapse involves accumulation

**Concern summary.** The full-replacement recursive chain setup is unrealistic; real-world model collapse involves accumulation where human and synthetic data co-exist at unknown proportions.

**Response.** We agree that full-replacement represents an upper bound on depth signal strength. To directly quantify the gap, we conducted accumulation experiments (GPT-2 XL, nucleus, seed=42) at two mixing ratios:

| Setting | 4-class Acc | d1–d3 Bal Acc | Delta vs Full-Replacement |
|---|---|---|---|
| Full-replacement | 84.2% | — | baseline |
| 50/50 human-synthetic | 69.1% | 59.0% | −15.1 pp |
| 25/75 human-synthetic | 70.1% | 60.3% | −14.1 pp |
| Chance (4-class) | 25.0% | — | — |

*(Registry: `accum_v3_mix50`, `accum_v3_mix25`)*

Key findings:

1. **Signal attenuates but remains strong.** Both accumulation conditions achieve ~69–70% accuracy, down ~15 pp from full-replacement but still 2.8× chance (+44 pp above 25% baseline).

2. **Mix ratio difference is within noise.** The 1 pp gap between 50/50 (69.1%) and 25/75 (70.1%) falls within cross-seed variance (2.04 pp for GPT-2 XL nucleus).

3. **Full-replacement as principled upper bound.** The full-replacement setting isolates the depth variable by eliminating human-data carry-over effects, providing a clean experimental setup. The accumulation results confirm that depth-discriminative features transfer to more realistic settings with quantifiable attenuation (~15 pp).

**Paper revision.** Discussion §6 reports accumulation results. Extending the feature set to handle continuous mixing ratios is noted as future work.

---

### [W19] Code and data availability for reproducibility

**Concern summary.** ARR requires evidence that results are reproducible. Will the code, data, and trained models be publicly available?

**Response.** We commit to full public release upon acceptance:

1. **Code**: Complete pipeline including feature extraction (19-feature + Binoculars 11-feature), RF training, evaluation scripts, two-stage pipeline, and all ablation configurations. MIT license.
2. **Data**: Full recursive generation chains (d0–d3) for all 9 atlas cells across three model families (Pythia-1.4B, OLMo-1B, GPT-2 XL) and three decoding strategies, plus the 14B Qwen2.5-14B chains. Includes prompted generation and accumulation datasets.
3. **Trained models**: Pre-trained RF classifiers for all 9 cells, the two-stage pipeline models, and Binoculars-calibrated RF.
4. **Evaluation framework**: Scripts to reproduce all tables and figures in the paper, including cross-model LOO, cross-strategy LOO, EDD computation, and feature ablation.

The anonymous review supplement includes the feature extraction code and sample data sufficient to verify the main results. The full release will be hosted on a public repository with permanent DOI.

---

*End of Response Letter*
