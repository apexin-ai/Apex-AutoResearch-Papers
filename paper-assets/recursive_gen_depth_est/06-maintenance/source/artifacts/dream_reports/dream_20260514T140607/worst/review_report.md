---
dream_id: dream_20260514T140607
tier: worst
overall_score: 2.5 — Borderline Findings
timestamp: 2026-05-14T15:05:50.685819+00:00
---

# Dream Review Report — EMNLP 2026 Submission

**Paper**: "Measuring the Limits of Recursive Generation Depth Estimation: A Depth Degradation Atlas Across Models and Decoding Strategies"

**Venue**: EMNLP 2026 (via ACL Rolling Review)  
**Review Mode**: Full (2 Reviewers + Roundtable)  
**Scoring Rubric**: ARR 2025/2026 — Soundness/Excitement/Overall on 1–5 scale with half-point increments

---

## Paper Summary

This paper formalizes **ordinal generation depth estimation** — predicting how many recursive generation cycles (depth 0 = human through depth 5) a text passage has undergone. The benchmark spans 3 model families (Pythia-1.4B, OLMo-1B, GPT-2 XL) × 3 decoding strategies (nucleus, top-k, temperature) × 6 depths. Two primary contributions are claimed: (1) the **Depth Degradation Atlas**, a systematic mapping of how 19 statistical features evolve across recursive depths, and (2) the **Effective Discriminable Depth (EDD)** metric, defined as the maximum depth where adjacent-pair AUC exceeds 0.70. The headline finding is EDD = 2 in 7 of 9 model–strategy combinations, meaning reliable discrimination is limited to a ternary distinction: human-written vs. first-generation vs. deeply recursive text (73% accuracy). DCOL, a contrastive ordinal method adapted from CLOC, achieves 42% 6-class accuracy but does not significantly outperform CORAL (40%, p = 0.12). Cross-model transfer drops to 33%. The paper reframes depth estimation from a classification engineering problem to a measurement science problem.

---

## Reviewer 1 (R1): Methods + Experiments

### Strengths

- **Comprehensive experimental design.** 14 experiments addressing within-model estimation, cross-model/cross-strategy generalization, end-to-end vs. feature-based, granularity ablation, downstream curation, cross-scale transfer, and wild-data calibration. This covers virtually every natural follow-up question.
- **Convergent evidence for the signal-bottleneck thesis.** Multiple independent lines of evidence — DCOL ≈ CORAL (p = 0.12), end-to-end DeBERTa ≈ feature-based RF, DCOL ablation showing ≤1pp per component — all point to the same conclusion: the bottleneck is in feature discriminability, not learning methodology.
- **Honest negative-result reporting.** The paper does not try to hide that DCOL barely improves over CORAL, that cross-model transfer fails, that wild-data correlation is weak (ρ ≤ 0.21), or that graduated curation does not significantly beat binary filtering (p = 0.31). This transparency is commendable and scientifically valuable.
- **Strong baseline battery.** 7 baselines + DCOL evaluated under identical conditions (Table 5). The inclusion of zero-shot LLM prompting, binary cascade, and EditLens repurposed provides useful reference points.
- **EDD as an independent scientific contribution.** The metric is well-defined, intuitive, and directly actionable. The AUC > 0.70 threshold maps to a concrete operational meaning.
- **Clean granularity analysis.** The binary (94%) → ternary (73%) → 4-class (58%) → 6-class (42%) degradation curve (Table 10) directly supports the ternary recommendation and is elegantly presented.

### Weaknesses

- **(Major) Zero figures in an "Atlas" paper.** The paper contains 13 tables and 0 figures. For a contribution framed as a "Depth Degradation Atlas" — a systematic visual mapping of how features evolve — the complete absence of visualizations is a critical presentation failure. The experimental design calls for feature trajectory plots, AUC decay curves, t-SNE embeddings, confusion matrices, heatmaps, and non-monotonicity illustrations. None are present. Tables alone cannot carry the Atlas narrative; readers cannot intuit multi-dimensional degradation trajectories from tabulated numbers.
- **(Major) EDD threshold lacks sensitivity analysis.** The AUC > 0.70 cutoff that defines EDD is stated without justification. At 0.75, several combos' EDD might drop to 1; at 0.65, some might rise to 3. The robustness of the headline EDD = 2 finding to threshold choice is undemonstrated. A sensitivity table (EDD at thresholds 0.60, 0.65, 0.70, 0.75, 0.80) is essential.
- **(Major) Incomplete statistical reporting.** Confidence intervals are missing for most metrics (AUC values in Tables 3–4, cross-model/cross-strategy transfer accuracy). P-values are reported only for DCOL vs. CORAL and graduated vs. binary curation. The paper should provide CIs on all headline numbers and pairwise significance tests in the baseline comparison (Table 5).
- **(Major) Sample sizes and dataset statistics unreported.** How many text passages per depth × model × strategy? What is the passage length distribution? How were seed texts selected? Without these, reproducibility is compromised and it is impossible to assess statistical power.
- **(Minor) Depth-0 confound in headline metrics.** The near-perfect d0/d1 AUC (0.982–0.998) means depth-0 classification is essentially binary human-vs-machine detection — a well-studied problem. Headline 4-class and 6-class accuracy numbers are inflated by this easy subproblem. A companion metric excluding depth 0 (d1–d5 only, or d1–d3 for 4-class) would isolate the genuine ordinal estimation contribution.
- **(Minor) DCOL loss function underspecified.** Section 5.2 describes DCOL's three modifications verbally but does not provide a complete mathematical formulation. The interaction between strategy-aware margins, surprisal anchors, and learnable margins is unclear. Is there a repulsive term? How are negative pairs sampled?
- **(Minor) Pythia MAE missing in Table 4.** The dash for Pythia's MAE is unexplained. If this is a reporting omission or a deliberate choice (e.g., Pythia was the development model), it should be stated.
- **(Minor) Learned margin analysis is thin.** The paper reports std = 0.08 for learned margins but does not show the actual margin profile (which margins are larger, how they correlate with empirical inter-depth distances). This is a missed opportunity to strengthen the signal-bottleneck argument.

### Questions for Authors

1. How many text passages are there per condition (depth × model × strategy)?
2. What is the seed text source and selection procedure?
3. How sensitive is EDD to the AUC threshold? Report at 0.65, 0.70, 0.75, 0.80.
4. What is the d1–d5 only accuracy (excluding depth 0)?
5. What is the complete DCOL loss function, including negative pair handling?
6. Were there data contamination controls (ensuring seed texts are not in models' training data)?

### R1 Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 3.0 | Main claims are supported by convergent evidence, but statistical reporting has significant gaps (missing CIs, missing sample sizes, incomplete p-values). The EDD threshold is unjustified. |
| Excitement | 3.0 | The Atlas concept and EDD metric are interesting. The signal-bottleneck finding is informative. But zero figures undermine the Atlas contribution, and the lack of any method that pushes the EDD boundary limits excitement. |
| Overall | 2.5 | Borderline Findings. Thorough experiments and honest reporting, but critical presentation gaps (no figures, no sensitivity analysis) and incomplete statistical rigor prevent a confident Findings recommendation. |
| Confidence | 4/5 | |

---

## Reviewer 2 (R2): Novelty + Related Work

### Strengths

- **Task formalization is genuinely novel and timely.** No prior work has formalized recursive generation depth estimation as a standalone prediction task. The insight that binary detection discards actionable ordinal information is simple, important, and well-articulated. This is a real conceptual contribution bridging AI-generated text detection and model collapse research.
- **EDD is a useful scientific metric.** Defining the Effective Discriminable Depth as the maximum depth where adjacent-pair AUC > 0.70 gives the community a concrete, measurable boundary for a previously vague question: "how deep can we see into recursive generation?"
- **Atlas systematizes and extends prior characterization.** Shumailov et al. (2024) showed collapse happens; Drayson et al. (EMNLP 2025) characterized degradation in Pythia. This paper extends to three architectures, three strategies, and formalizes findings via monotonicity scores, feature importance divergence, and the non-monotonic degradation observation. This is more than replication.
- **Model-specificity as a discovery, not a limitation.** The reframing of cross-model transfer failure (33%) as a scientific finding — revealing that depth signatures are fundamentally shaped by training distribution, architecture, and tokenizer — is intellectually honest and generates a concrete research direction (model fingerprinting).
- **Practical recommendations are well-grounded.** The ternary granularity recommendation, the model-fingerprinting prerequisite, and the "binary filtering captures most benefit" conclusion all follow directly from the evidence.

### Weaknesses

- **(Major) Critically thin bibliography — 9 references for an EMNLP submission.** A typical EMNLP paper cites 30–50 works. Nine references makes proper positioning impossible and signals insufficient engagement with the literature. Entire directly relevant subfields are absent:
  - **Watermarking** (Kirchenbauer et al., ICML 2023): a direct alternative to post-hoc depth estimation for provenance tracking. The paper never discusses why statistical depth estimation is needed when watermarking exists.
  - **Data curation/filtering** (DSIR, QuRating, D4, FineWeb): the downstream curation experiments (§6.8) position depth-weighting as a curation strategy but ignore the extensive data selection literature.
  - **Model collapse theory** (Alemohammad et al., ICLR 2024; Dohmatob et al., 2024; Gerstgrasser et al., 2024): the Atlas findings should be discussed against theoretical predictions for *why* distributions collapse.
  - **Multi-source attribution** (Uchendu et al., 2020): distinguishing text from multiple generators is adjacent to depth estimation.
  - **Training data attribution / membership inference** (Carlini et al., 2023; Shi et al., 2023): related provenance problems.
  - **Additional binary detectors**: Binoculars (Hans et al., 2024), LOKI, etc. — some appear as baselines in the experiments but lack bibliographic entries.
- **(Major) DCOL is an incremental adaptation of CLOC, not a novel framework.** The three modifications (strategy-aware margins, surprisal anchors, learnable margins) are individually standard techniques in metric learning. The ablation confirms their combined contribution is ~2pp over CORAL — statistically insignificant (p = 0.12). The paper should honestly position DCOL as "CLOC adapted for text depth estimation" rather than implying a new learning framework.
- **(Major) "Measurement science" framing, while intellectually honest, weakens the contribution profile for EMNLP.** The paper explicitly states it characterizes limits rather than pushing them. While this is scientifically valid, EMNLP reviewers typically expect either methodological advance or substantial new empirical insight. The Atlas provides the latter, but the zero-figures presentation undermines it. The EDD = 2 finding is important but can be stated in a single table (Table 1). The paper needs to provide richer Atlas content (visualizations, deeper analysis) to justify the "Atlas" framing.
- **(Minor) The paper title promises more than it delivers.** "Depth Degradation Atlas" evokes a rich, visual, multi-faceted empirical resource. The paper delivers 13 tables and summary statistics. Without feature trajectory visualizations, the Atlas is an index, not a map.
- **(Minor) Related work structure is too compressed.** Three short paragraphs (§2) cannot adequately survey the relevant landscape. Missing discussion threads: watermarking vs. depth estimation, connections to data quality estimation, distribution shift detection, theoretical grounding for the observed saturation.
- **(Minor) "First systematic empirical map" claim needs qualification.** Shumailov et al. (2024) and Drayson et al. (2025) both provide systematic empirical characterizations of recursive degradation. The genuine novelty is the ordinal estimation framing, EDD metric, and multi-model/multi-strategy coverage — not being "first" to characterize degradation empirically.

### Missing Related Work (Specific)

1. Kirchenbauer et al. (ICML 2023) — watermarking for LLMs
2. Alemohammad et al. (ICLR 2024) — self-consuming generative models
3. Dohmatob et al. (2024) — theoretical model collapse
4. Gerstgrasser et al. (2024) — model collapse in LLMs
5. Xie et al. (ICLR 2023) — DSIR data selection
6. Wettig et al. (2024) — QuRating
7. Uchendu et al. (2020) — authorship attribution for neural text
8. Hans et al. (ICML 2024) — Binoculars (used as baseline but uncited)
9. Carlini et al. (2023) — training data extraction
10. Shi et al. (2023) — detecting pretraining data

### Questions for Authors

1. Why are only 9 works cited? Were references omitted for page constraints or anonymity?
2. How does depth estimation relate to watermarking-based provenance tracking? Under what conditions is each approach preferable?
3. What is the 5-class (d1–d5 only) accuracy, excluding the near-trivial depth-0 classification?
4. Can the authors engage with model collapse theory to explain *why* EDD = 2? Is there a theoretical prediction for the saturation depth?
5. Has graduated curation been compared against volume-matched binary filtering (same data retention rate) to isolate the weighting effect from the data volume effect?

### R2 Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 3.0 | Task formalization and Atlas are sound. Experimental coverage is thorough. But the 9-reference bibliography undermines scholarly rigor, and DCOL's contribution over CORAL is not statistically significant. |
| Excitement | 2.5 | The task and EDD concept are genuinely interesting. But the execution gaps (no figures, thin bibliography) and incremental methodology dampen excitement. The Atlas *concept* is exciting; the Atlas *as delivered* is not. |
| Overall | 2.5 | Borderline Findings. Novel task formalization + thorough experiments, but critically thin bibliography, zero figures for an "Atlas" paper, and incremental method. Fixable issues, but significant revision needed. |
| Confidence | 4/5 | |

---

## Roundtable Discussion

### Step 2: Cross-Sharing

**R1 → R2**: The 14-experiment coverage is genuinely impressive and addresses most validity threats. The convergent evidence for the signal bottleneck (DCOL ≈ CORAL ≈ E2E DeBERTa) is the paper's strongest scientific argument. However, statistical rigor is below EMNLP standards — missing CIs, incomplete p-values, unreported sample sizes.

**R2 → R1**: The 9-reference bibliography is the paper's most glaring weakness. Missing engagement with watermarking, data curation, model collapse theory, and multi-source attribution leaves the paper poorly positioned. DCOL contributes essentially nothing beyond CLOC — the paper's value lies entirely in the task formalization, Atlas, and EDD, not in the method.

### Step 3: Convergence

**Points of agreement:**

1. **Task formalization is the strongest contribution.** Ordinal generation depth estimation is a genuinely novel, well-motivated task that bridges AI-text detection and model collapse research. Both reviewers recognize this as a real conceptual contribution.

2. **Atlas and EDD have scientific value.** The EDD = 2 finding, supported by convergent evidence from multiple experiments, is informative and actionable. The systematic multi-model, multi-strategy characterization extends prior work meaningfully.

3. **DCOL is not a significant methodological contribution.** The ~2pp advantage over CORAL (p = 0.12) is not statistically significant. Both reviewers agree DCOL should be honestly positioned as "one method we tried" rather than a primary contribution.

4. **Critical presentation failures undermine the paper.**
   - Zero figures in an "Atlas" paper is indefensible.
   - 9 references is far below EMNLP standards.
   - Statistical reporting is incomplete.

5. **Depth-0 confound inflates headline metrics.** Both reviewers flag the need for d1–d5 companion metrics.

6. **Model-specificity is a genuine discovery.** The cross-model transfer failure (33%) and feature importance divergence (Kendall's τ = 0.52) constitute a real finding with practical implications.

7. **Experimental coverage is a strength.** All 14 planned experiments are reflected in the paper.

**Point of mild disagreement:**

- R1 rates Excitement at 3.0 (acknowledging the Atlas concept); R2 at 2.5 (penalizing the gap between concept and execution). **Resolution**: 2.5 — the Atlas concept is interesting but the execution (tables-only, no visualizations) significantly reduces its impact as delivered.

### Step 4: Consolidated Assessment

**Consolidated Scores:**

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | **3.0** | Acceptable. The main claims (EDD = 2, signal bottleneck, model-specificity) are supported by convergent evidence from comprehensive experiments. But significant gaps in statistical reporting (missing CIs, incomplete p-values, unreported sample sizes), unjustified EDD threshold, and underspecified DCOL formulation prevent a higher rating. |
| **Excitement** | **2.5** | Between "Potentially Interesting" and "Interesting." The task formalization and EDD concept are genuinely interesting contributions to the NLP community. However, the execution fails to deliver on the Atlas promise (no visualizations), the bibliography is too thin to properly contextualize the work, and DCOL provides no methodological advance. The paper characterizes a limit but does not push it. |
| **Overall** | **2.5** | **Borderline Findings.** The paper introduces a legitimately novel task, provides a useful metric (EDD), and backs its claims with thorough experiments. These are real contributions. But three critical issues prevent a confident Findings recommendation: (1) zero figures in a paper whose primary contribution is an empirical "Atlas"; (2) only 9 references, missing engagement with watermarking, data curation, model collapse theory, and multi-source attribution; (3) DCOL provides no statistically significant improvement over existing ordinal methods. All three issues are fixable in revision. |

---

## Actionable Revision Recommendations

### Must-fix (for Findings acceptance)

1. **Add 4–6 key figures**: (a) Adjacent-AUC decay curve across all 9 combos with 0.70 threshold line marking EDD; (b) Feature trajectory panel (top-5 features × depth, stratified by model); (c) Feature importance rank divergence visualization across models; (d) Non-monotonicity illustration (GPT-2 XL × temperature); (e) Granularity vs. accuracy plot with chance baselines.

2. **Expand bibliography to 25+ references**: Must cover watermarking (Kirchenbauer et al.), model collapse theory (Alemohammad et al., Dohmatob et al.), data curation (DSIR, QuRating), multi-source attribution (Uchendu et al.), and properly cite all baselines used in experiments.

3. **Report d1–d5 accuracy** as a companion metric to isolate ordinal depth estimation from binary human-vs-machine detection.

4. **EDD sensitivity analysis**: Report EDD at thresholds 0.65, 0.70, 0.75, 0.80 to demonstrate robustness.

5. **Complete statistical reporting**: Add 95% CIs on all headline metrics; add pairwise significance tests for Table 5; report dataset sizes per condition.

### Should-fix (for stronger positioning)

6. **Rebalance framing**: Lead with Atlas + EDD as primary contributions; demote DCOL to "one approach evaluated" rather than a co-primary contribution.

7. **Expand §7 Discussion**: Engage with model collapse theory to explain *why* EDD = 2; discuss watermarking as a complementary approach; discuss implications for data curation pipeline design.

8. **Provide DCOL mathematical formulation**: Complete loss function with negative pair handling, margin parameterization, and training details.

---

## Experiment Coverage Assessment

Compared against the full experiment design (14 planned experiments):

| Experiment | Plan ID | Covered? | Notes |
|------------|---------|----------|-------|
| OLMo-1B recursive chain | plan_002 | ✅ | §6.1, Table 4 |
| GPT-2 XL recursive chain | plan_003 | ✅ | §6.1, Table 4 |
| DCOL training (DeBERTa) | plan_004 | ✅ | §5.2, §6.2, Table 5 |
| Leave-one-model-out | plan_005 | ✅ | §6.5, Table 8 |
| Atlas + EDD computation | plan_006 | ✅ | §4, Tables 1–3 |
| Leave-one-strategy-out | plan_007 | ✅ | §6.6, Table 9 |
| DeBERTa E2E classifier | plan_008 | ✅ | §6.4, Table 7 |
| Baseline battery | plan_009 | ✅ | §6.2, Table 5 |
| DCOL component ablation | plan_010 | ✅ | §6.3, Table 6 |
| Depth extension to 5 | plan_011 | ✅ | §4.4, Table 3 |
| Granularity ablation | plan_012 | ✅ | §6.7, Table 10 |
| Downstream curation | plan_013 | ✅ | §6.8, Table 11 |
| 7B cross-scale probe | plan_014 | ✅ | §6.9, Table 12 |
| Wild-data calibration | plan_015 | ✅ | §6.10, Table 13 |

**Coverage: 14/14 (100%).** All planned experiments are reflected in the paper with results matching the experimental design. However, the rich visualizations specified in the experiment plans (violin plots, trajectory panels, t-SNE, heatmaps, Sankey diagrams, AUC curves, attention maps) are entirely absent — replaced by summary tables only.

---

## Meta-Assessment

This paper has the skeleton of a solid Findings-track contribution: a novel task, a well-defined metric, and thorough experiments. The core scientific insight — that recursive depth estimation hits a fundamental signal barrier at EDD = 2 — is worth communicating to the community. However, the current manuscript reads as a first draft: it reports results comprehensively in tables but fails to present them compellingly (no figures), fails to contextualize them adequately (9 references), and elevates an incremental method (DCOL) to co-primary status it does not merit. A focused revision addressing the five must-fix items above could bring this to a solid Findings acceptance within one ARR cycle.
