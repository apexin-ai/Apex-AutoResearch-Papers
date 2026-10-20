---
dream_id: dream_20260514T140607
tier: best
overall_score: borderline accept
timestamp: 2026-05-14T15:02:57.842612+00:00
---

---
dream_id: dream_20260514T140607
tier: best
overall_score: borderline accept
timestamp: 2026-05-14
---

# R1 Review: Methods and Experiments

**Paper:** Ordinal Depth Estimation of Recursive LLM Generations via Contrastive Learning with Learnable Margins
**Venue:** EMNLP 2026 (ARR)
**Reviewer Focus:** Methods and Experiments

---

## Summary

This paper formalizes ordinal generation depth estimation — predicting how many recursive generation cycles (depth 0=human through depth 5) a text passage has undergone — and proposes DCOL, a DeBERTa-based contrastive ordinal learning method with three text-specific modifications (surprisal-augmented anchors, learnable non-uniform margins, strategy-aware conditioning). The paper also contributes a Depth Degradation Atlas characterizing how 19 statistical features evolve across 3 models x 3 decoding strategies x 6 depths, introducing the Effective Discriminable Depth (EDD) metric. DCOL achieves 72.2% six-class accuracy (chance=16.7%), outperforming CORAL-DeBERTa (62.1%) by 10.1pp. Experimental coverage is extensive: 14 experiments spanning generalization, ablation, granularity, downstream application, cross-scale transfer, and wild-data calibration.

---

## Strengths

- **Comprehensive and well-structured experimental design.** The paper covers 14 experiments addressing distinct validity questions: within-model accuracy (Table 3), depth extension and saturation (Table 4), main comparison against 7 baselines (Table 5), per-class breakdown (Table 6), feature-based vs. end-to-end (Table 7), cross-model LOO (Table 8), cross-strategy LOO (Table 9), cross-scale transfer (Table 10), ablation (Table 11), granularity analysis (Table 12), wild-data calibration (Table 13), and downstream curation (Table 14). This is unusually thorough for a single paper and preempts most natural reviewer questions.

- **Clean observation-to-design-to-validation loop.** The Atlas documents non-uniform inter-depth geometry (d0->1 gap is 2.83x the d3->4 gap); this directly motivates learnable non-uniform margins; the learned margin ratios (1.00, 0.68, 0.52, 0.41, 0.35) correlate with empirical distances (r > 0.95). This is a well-executed example of empirically motivated method design.

- **Strong and fair baseline battery.** Seven baselines spanning binary detector repurposing (DivEye, Binoculars), ordinal regression (CORAL), standard classification (CE-DeBERTa), direct regression (PPL), feature-based ordinal (RF+CORAL), and zero-shot prompting (GPT-4). Critically, CORAL-DeBERTa uses the same encoder as DCOL, isolating the contribution of the three modifications from encoder choice.

- **Convincing ablation study.** Each of the three components contributes independently (2.2-3.9pp). The sum of individual drops (9.2pp) slightly exceeds the joint drop (8.1pp), indicating 1.1pp of positive interaction — a plausible and well-analyzed result. The finding that "w/o all three" (64.1%) still outperforms CORAL (62.1%) cleanly separates the contrastive framework contribution from the modification contributions.

- **Atlas as independent scientific contribution.** The EDD metric, feature monotonicity analysis (var_surprisal at 0.961), identification of non-monotonic features (burstiness, type-token ratio), and the non-uniform geometry documentation have value for the model collapse community independent of DCOL. The finding that surprisal variance is a near-universal depth indicator is genuinely useful.

- **Statistical significance reported for key comparisons.** DCOL vs. CORAL tested via paired bootstrap (p < 0.001). Confidence intervals provided for main results ([71.0, 73.4] for 6-class accuracy). This exceeds the reporting standard of many EMNLP submissions.

- **Elegant granularity analysis result.** The finding that above-chance margin *increases* from 46.1pp (binary) to 55.5pp (6-class) is a genuinely surprising and informative result that justifies the ordinal framing beyond rhetorical argument.

---

## Weaknesses

### Major

1. **(M1) Loss formulation in Eq. 1 is incomplete or incorrectly presented.** The loss as written — L = sum max(0, ||f(xi) - f(xj)|| - m(delta_ij))^2 — only penalizes when embedding distance *exceeds* the margin. This is a ceiling/pull term with no repulsive mechanism. As stated, the loss is trivially minimized by mapping all inputs to a single point (embedding collapse). Standard contrastive ordinal losses include both attractive and repulsive terms, or use an N-pair formulation with positive/negative pairs. Either (a) the complete loss has additional terms not described, or (b) the formulation is genuinely flawed. This is the single most critical issue for reproducibility. The paper claims adaptation from CLOC (CVPR 2025), which uses a multi-margin N-pair loss — but the presented equation does not match that framework. Without the complete training objective, the method cannot be reimplemented.

2. **(M2) Circularity in surprisal-augmented anchors.** Section 4.3 states that token-level surprisal is computed "under a reference model" but never specifies which model. For Pythia-generated text evaluated using Pythia-1.4B's own surprisal, the signal conflates model identity with depth — the model's certainty about its own output is tautologically higher than about other models' output. This creates a potential confound in the cross-model experiments: when DCOL is trained on all three models but evaluated on a held-out model, is the reference model changed? If Pythia-1.4B is always the reference, the held-out OLMo text's surprisal under Pythia reflects both depth degradation AND model mismatch. The ablation shows surprisal anchors contribute 3.1pp, so this is not ignorable. The paper must specify: (a) which reference model is used, (b) whether it is the same for all text, (c) how this interacts with cross-model generalization.

3. **(M3) Depth-0 confound inflates headline numbers.** Depth 0 is human-written (Wikipedia); depths 1-5 are model-generated. The d0 vs. d1 AUC of 0.998 is essentially binary human-vs-machine detection, not depth estimation. Per-class accuracy confirms this: d0 achieves 91.2% while d5 achieves only 54.8%. The 72.2% headline is substantially boosted by near-perfect d0 classification. A fairer headline metric would be 5-class accuracy on d1-d5 only (pure depth estimation among synthetic text), which I estimate at approximately 64-65% based on the per-class numbers. This metric is never reported. The binary detection result (96.1%) further confirms the d0 signal is dominated by the human-vs-synthetic distinction rather than depth structure. The paper should prominently report d1-d5 accuracy alongside the 6-class number.

4. **(M4) k-NN inference is underspecified.** Section 4.5 states DCOL uses "a k-nearest-neighbor classifier in the learned embedding space" at inference, but provides no k value, no distance metric specification, no sensitivity analysis, and no justification for choosing k-NN over a learned classification head. If performance is sensitive to k, this is a hidden hyperparameter that could undermine the reported numbers. For a method paper, the inference procedure must be fully specified.

5. **(M5) No figures in a paper titled "Atlas."** The paper contains 14 tables and zero figures. The experiment design (per the imagined_experiments.yaml) envisions confusion matrix heatmaps, Atlas heatmap grids, AUC decay curves, t-SNE visualizations, waterfall charts, feature importance comparisons, and inter-depth distance scatter plots — none of which appear. For a paper whose second major contribution is a "Depth Degradation Atlas" — a term that evokes visual cartography — the complete absence of any visualization is a serious presentation failure. Tables 1 and 2 convey the Atlas findings but do so in a way that is far less interpretable than the equivalent heatmaps and curves would be. An Atlas without maps is a contradiction.

### Minor

6. **(m1) Cross-scale evaluation is limited and incomparable.** The 8B probe (Table 10) uses only 3-class (depth 0-2), making it incomparable to the 6-class main results. Only one larger model (Llama-3.1-8B) is tested, only to depth 2. The claim "depth signals transfer across model scales" (Section 5.5) is stronger than this evidence supports. The 13.3pp transfer gap is substantial. A more measured claim would be appropriate.

7. **(m2) Downstream curation lacks task-based evaluation.** Table 14 reports only held-out perplexity on RedPajama. PPL improvement could reflect distributional matching rather than genuine quality improvement. No evaluation on standard benchmarks (MMLU, reasoning tasks, etc.) is provided. Additionally, the comparison is not volume-controlled: binary filtering retains 71.6% of data while graduated retains 92.3%. Part of the PPL improvement may simply come from having 20% more training data. A fair comparison would include a volume-matched binary baseline retaining ~92% of data.

8. **(m3) EDD threshold sensitivity not analyzed.** EDD is defined with a fixed AUC >= 0.75 threshold (Section 3.3). No sensitivity analysis is provided. Several entries in Table 2 (e.g., d3-d4 AUCs in the 0.77-0.80 range) are close to the threshold. If the threshold were 0.80, multiple EDD values would drop by 1, changing the median from 4 to ~3. The paper should discuss threshold choice or provide EDD as a function of threshold.

9. **(m4) No error analysis or confusion matrix.** The paper states that "misclassifications concentrate at +/-1 depth" (Table 6 caption) but never shows a confusion matrix. Without this, we cannot verify whether errors are indeed ordinal or whether specific depth pairs have pathological confusion patterns. An error analysis examining what textual properties make depth estimation harder would strengthen the paper.

10. **(m5) Wild-data calibration has no ground truth.** Correlations with PPL and AlignScore (Table 13) are suggestive but could mean DCOL is simply learning a perplexity proxy. The partial correlation (rho = -0.198) partially mitigates this, but the correlation is weak. Without ground-truth depth labels on wild data, this experiment provides only indirect evidence of ecological validity.

11. **(m6) Margin-geometry correlation is circular.** Reporting Pearson r > 0.95 between learned margins and empirical inter-depth distances is not a validation of the design principle — the margins were *trained* on the same data from which the Atlas distances were computed. They *should* correlate; this validates convergence, not correctness. A genuine validation would train margins on one model family and show they match the Atlas geometry of a held-out family.

12. **(m7) Related work is thin.** Only 10 references total. Notable omissions: watermarking-based provenance (Kirchenbauer et al. 2023), data quality/curation literature (DSIR, QuRating), multi-class synthetic attribution (Uchendu et al. 2020), additional model collapse theory (Alemohammad et al. 2023), and Fast-DetectGPT (Bao et al. 2024) which should be in the baseline battery.

13. **(m8) Monotonicity constraint implementation unspecified.** Section 4.2 states margins are subject to m1 >= m2 >= ... > 0, but does not describe how this is enforced (softmax reparameterization? projected gradient? penalty term?). This affects both reproducibility and understanding of optimization dynamics.

---

## Questions for Authors

1. **Provide the complete training objective** including the repulsive/floor term. Is this a standard N-pair contrastive loss with the margin function, or something else?
2. **Which reference model computes surprisal?** Is it the same model that generated the text? Is it the same for all three model families? How does this affect cross-model LOO results?
3. **What k is used in k-NN inference?** What distance metric? What is the sensitivity to k (e.g., k=1,3,5,10)?
4. **What is the 5-class (d1-d5 only) accuracy?** This would isolate pure depth estimation from the binary detection confound.
5. **How is the monotonicity constraint on margins implemented?** Softmax reparameterization, projection, or penalty?
6. **How is strategy conditioning handled at inference on wild data** where the decoding strategy is unknown? Is a default strategy embedding used? What is the sensitivity to misspecified strategy?
7. **Has depth-0 been tested with non-Wikipedia seed corpora?** The current setup conflates domain shift (Wikipedia vs. model output) with depth.
8. **Can you provide the confusion matrix** (6x6) for DCOL on the main benchmark?
9. **Can the margin-geometry correlation be validated on a held-out model family** not used in training?
10. **For the curation experiment**, what happens with volume-matched binary filtering (retaining ~92% of data)?

---

## Missing Experiments or Analyses

1. **5-class (d1-d5) accuracy** to isolate depth estimation from binary detection.
2. **Confusion matrix** for DCOL on the main benchmark.
3. **k-NN hyperparameter sensitivity** (k value, distance metric).
4. **EDD threshold sensitivity analysis** (EDD as a function of AUC threshold from 0.65 to 0.85).
5. **Volume-matched curation comparison** (binary filtering at ~92% retention).
6. **Figures**: At minimum, (a) an Atlas heatmap showing feature evolution across model x strategy x depth, (b) AUC decay curves across depth pairs, (c) a confusion matrix heatmap. These would transform the paper's readability.
7. **Statistical significance for ablation components** individually (are the 2-4pp drops significant, or within noise?).
8. **Per-model-strategy breakdown of DCOL performance** (9 combos) to identify whether the pooled number masks heterogeneity.

---

## Scores

**Soundness: 3.0 / 5**
Justification: The experimental design is thorough and well-structured, but the incomplete loss formulation (Eq. 1) is a critical gap that prevents reproduction. The surprisal circularity concern and depth-0 confound are substantive methodological issues. The k-NN inference underspecification adds uncertainty. The experimental results themselves appear internally consistent, and statistical testing is present for key comparisons.

**Excitement: 3.5 / 5**
Justification: The task formalization (ordinal depth estimation) is genuinely novel and timely. The Atlas and EDD contributions have independent scientific value for the model collapse community. The finding that above-chance margin increases with granularity is elegant. However, the methodological contribution (DCOL) is an incremental adaptation of CLOC with standard engineering modifications, and the complete absence of figures significantly dampens impact.

**Overall: 3.0 / 5 (Findings-track quality; borderline for main conference)**
Justification: The paper introduces a well-defined new task with a comprehensive benchmark and thorough experimental evaluation — these are genuine contributions. The Atlas is scientifically valuable. However, three issues prevent a confident accept: (1) the loss formulation gap makes the method unreproducible as written, (2) the headline 72.2% is inflated by the d0 confound without a complementary d1-d5 metric, and (3) the complete absence of figures in an "Atlas" paper is a presentation failure that undermines the contribution. If the authors address the loss formulation, report d1-d5 accuracy, and add key visualizations, this could reach a solid accept. The task and Atlas alone may justify publication at EMNLP Findings even with an incremental method.

**Confidence: 4 / 5**
