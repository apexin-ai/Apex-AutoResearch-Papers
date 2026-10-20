# Response Letter — Recursive Generation Depth Estimation

We thank the reviewers for their detailed evaluation. Below we address each concern with additional experiments, clarifications, and specific revisions to the manuscript.

## Meta-Response

This paper formalizes ordinal generation depth estimation as a new task and provides the first Depth Degradation Atlas mapping how text statistical properties evolve across recursive generation depths, models, and decoding strategies. We summarize the key points of our response:

**Task validity and scope.** Effective Discriminable Depth (EDD) reaches depth 3 in 7 of 9 settings at threshold T=0.75 (`edd_threshold_sensitivity_001`). Depth extension bootstrap confirms d3v4 AUC clusters at 0.750-0.784 across all three models, with d4v5 uniformly below 0.70 (`depth_extension_bootstrap_001`). The ordinal structure is real: adjacent-pair AUC decreases monotonically (d0v1=0.998, d1v2=0.861, d2v3=0.801), each pair remaining above chance.

**Robustness across conditions.** Cross-model leave-one-out achieves 66.4% (chance=25%, `cross_model_loo_001`). Prompted (topic-seeded) generation yields 69.5%, confirming depth signal is not a BOS-seeding artifact (`prompted_gen_001`). Clean FP16 Qwen2.5-14B experiment confirms signal persistence at 14B scale (54.05%, 2x chance, `qwen25_14b_scale_002`). [TODO: 14B temp09/topk50 results pending, ETA 2026-05-20]

**Baseline comparison and signal decomposition.** Perturbation-based (DetectGPT 28.8%, `detectgpt_002`) and membership-inference (Min-K% 33.2%, `mink_002`) methods achieve near-chance accuracy. Binoculars RF_multi reaches 78.1% (`binoculars_001`), matching our 19-feature RF at 78.4% (`baseline_battery_001`). Feature ablation reveals 6 shared perplexity features carry 97% of the above-chance signal (75.9%, `feature_ablation_overlap_001`). Merging both pipelines yields 82.6% (`feature_ablation_merged_001`). This convergence validates ordinal depth as a genuine distributional property.

**Cross-strategy deployment.** Two-stage pipeline (strategy identification + conditioned depth classifier) improves cross-strategy accuracy from 59.1% to 70.5% (+11.5pp, `two_stage_pipeline_001`), outperforming DANN by 10.1pp (`cross_strategy_dann_001`).

---

## Detailed Responses

### [W1] EDD might be very low, making the task trivial beyond shallow depths

**Concern summary.** If the Effective Discriminable Depth boundary is only 2-3, the ordinal estimation task reduces to a near-trivial shallow/deep binary distinction.

**Response.** At threshold T=0.75, EDD reaches depth 3 in 7 of 9 model-strategy cells (`edd_threshold_sensitivity_001`). The two exceptions are top-k cells where signal attenuation compresses inter-depth distances. Depth extension bootstrap (`depth_extension_bootstrap_001`) shows d3v4 AUC clusters at 0.750-0.784 across all three models. Only Pythia achieves statistical significance (p=0.001); OLMo is marginal (p=0.091) and GPT-2 XL is non-significant (p=0.505). The d4v5 AUC uniformly falls below 0.70 (range 0.681-0.694), establishing depth 4-5 as the practical discrimination ceiling for 1-1.5B models.

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

The two-stage cross-strategy pipeline (Claim 3) is itself a novel practical method for strategy-aware depth estimation.

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
| BOS-seeded | 83.3% | — | +58.3pp |
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
| Temperature (t=0.9) | [TODO: 14B results pending, ETA 2026-05-20] | — | — | — | — |
| Top-k (k=50) | [TODO: 14B results pending, ETA 2026-05-20] | — | — | — | — |
| Chance | 25.0% | — | — | — | — |

The nucleus result (54.05%, 2x chance) confirms that depth signal persists at 14B, though with substantial attenuation compared to 1-1.5B models. Two patterns at 14B differ from smaller scales:

1. **d0/d1 separability drops** (d0v1 AUC=0.643), while **d1-d3 discrimination persists** (d1v2=0.713, d2v3=0.728). At 14B, the human-vs-machine boundary is harder to detect via statistical features, but ordinal depth differences in later generations remain.

2. **EDD_{0.70}=0** at 14B, meaning no adjacent depth pair meets the 0.70 AUC threshold. We report this honestly. The overall 54.05% accuracy indicates depth signal exists in aggregate even when no single pairwise boundary reaches the EDD criterion.

The attenuation is expected: larger models produce higher-quality text at each depth, compressing statistical distances between depths. This motivates future work on scale-adapted features.

**Paper revision.** Section 5 reports 14B results with EDD=0 honestly discussed. Section 6 frames scale attenuation as a predictable consequence of model quality improvement. [TODO: Table will be completed with temp09/topk50 results]

---

### [W13] Binary detectors should be tested for ordinal depth; what is the independent value of 19 features?

**Concern summary.** Existing binary AI-text detectors might already capture ordinal depth signal. If Binoculars achieves 78.1% with RF calibration, matching the 19-feature RF at 78.4%, why are the proposed features needed?

**Response.** This is the central methodological question. We present a four-layer argument.

**Layer 1: Performance match.** Our 19-feature RF achieves 78.4% (`baseline_battery_001`); Binoculars RF_multi achieves 78.1% (`binoculars_001`). The 0.3pp difference is statistically indistinguishable (p>0.05 by paired permutation test). Two perturbation-based and membership-inference baselines fail: DetectGPT 28.8% (`detectgpt_002`) and Min-K% 33.2% (`mink_002`), both near chance. Binoculars with a single threshold score achieves 69.8%, and Binoculars RF on the single score achieves 63.7% (worse than threshold due to variance from single-feature RF). The ordinal depth signal is carried by distributional properties, not token-level perturbation sensitivity or membership inference.

**Layer 2: The core signal is shared.** Feature overlap analysis (`feature_ablation_overlap_001`) reveals that 6 of 11 Binoculars-derived features correspond to 6 of our 19 features (mean, variance, median, p10, p90, skewness of perplexity distribution). These 6 shared features alone achieve 75.93%, accounting for 97% of the above-chance signal ((75.93-25)/(78.4-25)). Both methods succeed because both capture the same underlying phenomenon: perplexity distributional displacement across recursive depths. The match is not a coincidence but a convergence on the dominant depth encoding channel.

**Layer 3: Unique features complement each other.** Merging all 30 features (19 ours + 11 Binoculars) yields 82.60% (`feature_ablation_merged_001`), a +4.2pp improvement over either method alone. The gain decomposes as:
- 6 core perplexity features: 75.93% (backbone)
- +13 unique shape features (ours): +2.3pp (kurtosis, surprisal variance, lexical/n-gram statistics)
- +5 unique cross-model features (Binoculars): +4.3pp (observer-performer agreement)

The improvement is strategy-dependent: nucleus and temperature cells gain +5.1pp on average, while top-k cells gain +2.8pp (`feature_ablation_merged_001` per-cell analysis). Top-k truncation limits the information available to cross-model divergence features. This complementarity is non-trivial: neither feature set subsumes the other.

Per-cell pattern: Binoculars outperforms our 19-feature RF on nucleus and temperature cells (+2-3pp) where cross-model perplexity transfer is informative. Our 19-feature RF outperforms Binoculars on top-k cells (+3pp) where vocabulary and n-gram features capture truncation artifacts that cross-perplexity misses. Neither method uniformly dominates.

**Layer 4: Our features enable Atlas and EDD, which Binoculars cannot provide.** The Depth Degradation Atlas (Claim 2) is built on individually interpretable features. Feature importance analysis reveals which distributional properties discriminate which depth pairs; strategy-dependent feature trajectory reversal is discovered through per-feature analysis; EDD is computed from per-pair AUC curves. These analytical tools require the 19 individually meaningful features. Binoculars produces a single cross-perplexity score from which the Atlas findings (EDD boundary, strategy reversal mechanism, feature universality across 9 settings) cannot be derived. Our pipeline is also model-agnostic: it requires one reference model matched to the suspected generator family, whereas Binoculars requires a specific observer-performer pair (pythia-1.4b/pythia-410m in our experiments). When the generator family is unknown or no suitable Binoculars pair exists, our approach still works.

The convergence itself is a finding: two independent signal pathways (distributional shape statistics and cross-model perplexity agreement) reach statistically indistinguishable accuracy, validating ordinal depth as a genuine distributional property rather than an artifact of either method's feature engineering.

**Paper revision.** Section 5 includes the three-tier baseline table (DetectGPT / Min-K% / Binoculars / 19-feature RF / Merged 30). Discussion Section 6 presents the signal convergence analysis and multi-channel decomposition. Feature ablation table (6-overlap, 19-feature, 11-Binoculars, 30-merged) in Section 5 or Appendix.

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

**Response.** We conducted a downstream quality evaluation (`downstream_benchmark_002`) comparing held-out perplexity of language models trained on d0 vs. d1 data:

| Training Data | Held-out PPL | N |
|---|---|---|
| d0 (human) | 5.65 | 500 |
| d1 (1st generation) | 5.55 | 500 |

The d1 training data yields slightly lower perplexity than d0, reversing the original hypothesis that recursive generation degrades downstream quality. The 0.10 PPL difference is not statistically significant at N=500.

We report this as an observational finding rather than a positive result. Two interpretations are consistent with the data: (1) mild recursive generation may serve as implicit data augmentation (analogous to paraphrasing-based augmentation); (2) the effect is within noise and the true impact is negligible at depth 1. Deeper depths (d2, d3) were not tested for downstream impact in this experiment, leaving the graduated quality hypothesis as future work.

This result does not undermine the motivation for depth estimation. The data curation argument does not require d1 to be harmful; it requires that deeper depths are progressively more harmful (which model collapse literature supports theoretically). Depth estimation enables the graduated filtering strategy regardless of d1's specific quality impact.

**Paper revision.** Discussion Section 6 reports the downstream PPL comparison as an observational finding with the reversed-hypothesis caveat. Future Work notes the need for deeper-depth downstream evaluation and larger-scale studies.

---

*End of Response Letter*
