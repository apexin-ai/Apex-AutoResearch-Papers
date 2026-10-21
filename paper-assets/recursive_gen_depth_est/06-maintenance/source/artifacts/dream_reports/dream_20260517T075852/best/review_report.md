---
dream_id: dream_20260517T075852
tier: best
overall_score: borderline accept
timestamp: 2026-05-17T08:49:30.155888+00:00
---

# Dream Review Report — Ordinal Depth Estimation for Recursive LM Generations

**Venue:** EMNLP 2026 Main (ACL Rolling Review)
**Paper:** "Ordinal Depth Estimation for Recursive Language Model Generations: A Depth Degradation Atlas Across Scales and Strategies"
**Reviewers:** R1 (Method & Experiments), R2 (Novelty & Related Work)

---

## Scores (ARR 1–5 scale)

| Dimension | R1 | R2 | Final |
|-----------|----|----|-------|
| Soundness | 4 | 4 | **4** |
| Excitement | 3 | 3 | **3** |
| Overall Assessment | 3 | 3 | **3** |

**Disposition:** Borderline accept for EMNLP Main. Strong candidate for Findings.

---

## Experiment Coverage vs. Imagined Experiments

| Imagined Experiment | Plan ID | Paper Section | Status |
|---------------------|---------|---------------|--------|
| 13B Clean FP16 Scale Validation | plan_014 | Section 5.2, Table 2 | Fully covered |
| Prompted Generation Ecological Validity | plan_016 | Section 5.3, Tables 3-4 | Fully covered |
| Cross-Strategy Two-Stage Pipeline (Improved) | plan_017 | Section 5.4, Tables 5-6 | Fully covered |
| Wild-Data Calibration on RedPajama/Dolma | plan_015 | Section 5.5, Table 7 | Fully covered |

**Coverage: 4/4 (100%).** All imagined experiments are present in the paper with results matching expected ranges.

---

## R1 Review: Method & Experiments

### Strengths

1. **Clean task formalization.** The ordinal depth estimation problem is precisely defined (Eq. 1-2). The recursive generation chain formulation is unambiguous and creates a clear experimental protocol. The EDD metric (Eq. 2) naturally captures the "depth horizon" of discriminability and provides a useful single-number summary across configurations.

2. **Comprehensive benchmark design.** The 3-model x 3-strategy x 4-depth grid (9 configurations, 36 cells) is thorough for a first study. The choice of diverse model families (Pythia, OLMo, GPT-2 XL) with different architectures and training data strengthens generalizability claims. Extension to d=5 for limit analysis is appropriate.

3. **Fixed reference model design.** Using Pythia-1.4B as a fixed reference across all experiments is a key methodological insight. It ensures features reflect text properties rather than generator-reference alignment, and enables cross-model comparability. The 14B experiment validates this: Pythia-1.4B retains discriminative power on 14B-generated text with only 2-4pp degradation.

4. **Feature interpretability.** 19 features in 4 families (perplexity, surprisal, diversity, fluency) are transparent, reproducible, and computationally cheap. The finding that p90_ppl and var_surprisal are universal top-2 features across all 9 configurations, at 14B scale, and under prompted generation is a robust empirical result.

5. **Scale validation addresses the right concern.** Using Qwen2.5-14B in clean FP16 (no quantization) directly resolves the 7B QLoRA confound (U-shaped curves). The result (76.2%, within 1B range) falsifies the "small model artifact" hypothesis. Identifying the U-shape as quantization noise is a useful methodological finding.

6. **Ecological validity is statistically supported.** The prompted generation experiment (50 prompts, 5 domain clusters, 92.8% accuracy retention) with KS tests confirming feature distribution stability (p > 0.05 for all top-5 features) provides solid evidence. Cross-topic variance is small (std = 3.1pp), ruling out content domain as a confound.

7. **Two-stage pipeline shows systematic problem-solving.** The v1 (57.5% strategy clf) to v2 (81.2%) progression with principled feature additions targeting strategy-discriminative signals is well-motivated. The oracle analysis (78.4% ≈ within-strategy 78.2%, gap = 0.2pp) confirms the architecture ceiling and localizes remaining error to strategy misclassification.

8. **Honest limitations.** Five specific limitations clearly described. Wild-data temporal analysis appropriately caveated ("does not constitute causal evidence"). Reference model circularity discussed with two mitigating observations.

### Weaknesses

1. **No neural classifier baselines.** Only RF (500 trees) and LR are evaluated. Even a simple MLP on the 19 features, or a fine-tuned probe (BERT/DeBERTa on raw text), would contextualize whether hand-crafted features capture the full depth signal. The machine-generated text detection field has moved toward neural methods; ignoring them entirely is a gap. This is particularly important because the low d2 recall (26.8-63%) suggests current features may be insufficient for middle depths.

2. **Sample sizes not clearly reported.** The paper never explicitly states how many passages are generated per depth per model-strategy configuration. For 5-fold stratified CV, total N per class directly affects CI width and the reliability of the reported accuracies. This is a significant reproducibility concern.

3. **d2 recall is problematically low.** Per-class recall for d2 ranges from 26.8% to 63.0% across configurations. The 14B confusion matrix (Figure 3) shows d2 recall of 0.58 with 25% of d2 classified as d3. For practical data curation, graduated decisions at middle depths are exactly the advertised use case. This undermines the practical contribution.

4. **Single 14B data point for "scale robustness."** The claim that the signal persists "at the 14B scale" rests on one experiment with one model (Qwen2.5-14B) and one strategy (nucleus). No 30B+ or 70B+ experiments. A single supporting data point does not establish "scale robustness" as a general finding.

5. **LoRA-only fine-tuning.** All recursive chains use LoRA. Full fine-tuning, continued pretraining, or other adaptation methods (prefix tuning, adapters) could produce different depth signatures. The paper doesn't discuss whether LoRA's low-rank constraint specifically shapes the distributional shift pattern.

6. **No held-out test set.** 5-fold stratified CV means every data point participates in training at some point. A proper train/dev/test split would provide stronger accuracy claims, especially for the headline numbers.

7. **Wild-data FPR estimation is assumption-dependent.** The FPR estimates assume web corpora are "predominantly human-written," but without ground-truth labels this is an assumption. The gradient (WikiText 0% to web crawl 15-20%) could also reflect stylistic differences (template content, SEO text) unrelated to recursive generation. The paper acknowledges this but treats the gradient as confirmatory evidence.

8. **No systematic error analysis.** Beyond per-class recall and per-topic accuracy (Table 4, prompted generation only), there is no analysis of what text characteristics predict misclassification. Text length, domain, lexical complexity, etc. would help understand failure modes.

### Questions for Authors
1. How many passages per depth per model-strategy configuration? Total dataset size?
2. What is the performance of a simple MLP or fine-tuned LM probe on this task?
3. Has any reference model other than Pythia-1.4B been tested? How sensitive are results to reference model choice?
4. What is the computational cost of the full 28-feature extraction pipeline per passage?
5. How was the pre/post-2023 timestamp determined in the RedPajama temporal analysis? Are there content-type confounds (e.g., increased SEO content)?

---

## R2 Review: Novelty & Related Work

### Strengths

1. **Genuinely novel task formulation.** No prior work formalizes the problem of estimating recursive generation depth from text alone. The gap identification is clean: model collapse studies know depth (they control the pipeline), binary detectors discard depth information. Ordinal depth estimation fills a real methodological hole.

2. **The Depth Degradation Atlas is a valuable empirical contribution type.** The systematic mapping of feature behavior across models, depths, and strategies, revealing non-obvious patterns (trajectory reversal, universal markers), aligns well with EMNLP's emphasis on empirical methods. This is not "just experiments" but a structured empirical investigation that produces reusable findings.

3. **Strategy-dependent feature trajectory reversal is a genuinely surprising finding.** Temperature sampling reversing feature trajectories at the d1/d2 boundary, causing naive cross-strategy AUC to drop to 0.13 (worse than random), is non-trivial. The mechanistic explanation (uniform logit scaling accelerates convergence to attractor distribution) is plausible and connects to Holtzman et al.'s observations about decoding strategy effects.

4. **Strong narrative structure.** The paper follows a clear arc: problem definition, benchmark construction, Atlas findings, practical pipeline, real-world calibration. Each section builds on the previous. Contributions are clearly stated and each is supported by specific sections and tables. The Introduction effectively motivates why ordinal depth is more useful than binary labels.

5. **Positioning against binary detectors is effective.** The argument that first-generation synthetic data may be useful (cite Gunasekar et al.) while deeply recursive text is degraded provides a compelling reason to move beyond binary classification to ordinal estimation.

6. **Limitations are honest and thorough.** No over-claiming. Five specific limitations are described with appropriate caveats. This builds trust in the empirical findings.

### Weaknesses

1. **Methods are not novel.** RF/LR on 19 hand-crafted statistical features is a straightforward application of standard tools. The novelty is entirely in the problem formulation and empirical findings, not in algorithmic contribution. For EMNLP Main, reviewers may expect methodological innovation alongside empirical contribution.

2. **Related Work is somewhat thin.**
   - ~22 references is below typical EMNLP density for a paper spanning model collapse, text detection, decoding effects, attribution, data curation, and watermarking. Papers in this space typically cite 30-40 works.
   - Missing: RAID benchmark (Dugan et al., 2024) for machine text detection evaluation; multi-class/multi-source detection methods; LLM-generated text quality evaluation frameworks; more recent 2025 model collapse works.
   - No discussion of how depth estimation relates to text quality scoring beyond the brief mention of QuRating/DSIR.

3. **Section 6 "Atlas Visualizations" is vestigial.** A single sentence ("We present four key visualizations that constitute the empirical core of the Depth Degradation Atlas") followed by figures. This section should be integrated into Section 4 with per-figure analysis, or expanded with substantive discussion. As written, it reads like a placeholder.

4. **Two-stage pipeline is obvious engineering.** Given that cross-strategy transfer catastrophically fails, "identify strategy first, then route to strategy-specific classifier" is the natural and expected response. The contribution is in execution and demonstration, not in conceptual innovation.

5. **Gap between experimental setup and motivating scenario.** The paper motivates ordinal depth estimation for web-crawled training data contamination, where frontier models (GPT-4, Claude, etc.) generate text via API calls. But experiments use LoRA fine-tuning on small models (1-14B). Real-world recursive contamination likely involves heterogeneous models, strategies, and human editing at each depth. The prompted generation experiment (Section 5.3) partially bridges this gap but does not close it.

6. **Minor writing issues.**
   - Abstract last sentence ("confirming ecological relevance and scale robustness") reads like a conclusion stamp rather than a result.
   - Section 4.2 reports multiple p-values inline without multiple testing correction.
   - Using "Atlas" as a proper noun throughout feels slightly self-aggrandizing for a systematic empirical study.
   - Some sentences are dense with inline metrics, reducing readability (e.g., Section 5.2 paragraph listing all AUC values and CIs).

7. **Practical impact is uncertain.** The 15-20% FPR on web data, combined with ~58% d2 recall, means the tool would produce many false positives and miss many intermediate-depth texts. The paper proposes ensemble voting as mitigation but doesn't test it.

### Questions for Authors
1. How does the approach handle mixed-depth text (e.g., human text revised by an LLM, or LLM text with human edits)?
2. Is there a plan to release the benchmark dataset and code for community use?
3. How would the approach generalize to non-English text, or to text from frontier-scale models (70B+)?
4. Could the Atlas be made extensible (e.g., a framework/toolkit for adding new models/strategies)?
5. What is the authors' view on the gap between the LoRA experimental setup and API-based text generation in the wild?

---

## Roundtable Step 2: Cross-Sharing Summary

**R1 to R2:** Key experimental concerns are (1) d2 recall critically low for practical use, (2) sample sizes unreported, (3) no neural baselines to determine if 19 features suffice, (4) wild-data FPR estimates rest on untested assumptions. The methodology is sound but narrow in scope.

**R2 to R1:** Key positioning concerns are (1) methods are standard, novelty is purely task/empirical, (2) Section 6 is vestigial, (3) ~22 references is thin for this breadth, (4) gap between experimental setup (LoRA, ≤14B) and motivating scenario (frontier model web contamination) is large. Writing quality is generally good but has minor issues.

## Roundtable Step 3: Convergence

Both reviewers converge on these points:

**Agreements:**
- Task novelty is the paper's strongest asset. Ordinal depth estimation is genuinely new, well-motivated, and fills a real gap between model collapse studies and binary detectors.
- Experimental comprehensiveness is impressive for a first paper on a new task. The 3x3x4 benchmark + 14B + prompted + wild-data + two-stage pipeline represents substantial work.
- The Atlas findings (feature universality, monotonic AUC decay, trajectory reversal) are scientifically interesting and reusable.
- Standard methods (RF/LR) are the weakest dimension. For EMNLP Main, stronger methodological contribution is expected.
- Scope limitations (model scale, LoRA-only, English-only) are appropriate for a first paper but constrain significance claims.
- Practical utility remains unproven given d2 recall and FPR issues.

**Disposition consensus:** The paper is a solid empirical contribution that opens a new task. It is above the bar for EMNLP Findings but borderline for Main conference. The gap to Main acceptance could be closed by: (1) adding neural classifier baselines, (2) demonstrating practical utility in a downstream curation task, or (3) extending to frontier-scale models.

## Roundtable Step 4: Consolidated Assessment

### Overall Verdict: Borderline Accept (3/5)

This paper makes a genuine contribution by formalizing ordinal generation depth estimation as a new task and providing the first comprehensive empirical investigation (the Depth Degradation Atlas). The task is novel, timely, and well-motivated by the growing concern over recursive synthetic contamination in training data.

**What pushes toward acceptance:**
- Novel task with clear gap identification
- Comprehensive Atlas covering scales, strategies, and generation modes
- Non-obvious finding (temperature trajectory reversal) with mechanistic explanation
- Thorough limitations section
- 100% coverage of planned experiments

**What pushes toward rejection:**
- Standard methods (RF/LR) with no neural baselines
- Limited model scale (max 14B, single data point)
- Low d2 recall undermines practical utility claims
- Thin related work (~22 references)
- Gap between experimental setup and real-world motivating scenario

**Recommendation for authors:**
1. **Priority 1:** Add at least one neural baseline (MLP on features, or fine-tuned LM probe) to determine if the feature bottleneck explains low d2 recall
2. **Priority 2:** Report sample sizes clearly and add a held-out test evaluation
3. **Priority 3:** Expand Related Work to ~30-35 references, including RAID, multi-source detection, and 2025 model collapse works
4. **Priority 4:** Merge Section 6 into Section 4 with per-figure analysis
5. **Priority 5:** If feasible, add one 70B experiment to strengthen scale claims

### Final Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | **4** (Strong) | Experimental methodology is rigorous within its scope. Statistical analysis is appropriate (CV, CIs, AUC, KS tests). Limitations are honestly discussed. The main concern is scope (model scale, classifier type) rather than correctness. |
| Excitement | **3** (Good) | Task is novel and timely. Atlas findings (especially trajectory reversal) are interesting. But methods are standard, model scale is limited, and practical impact is uncertain given d2 recall and FPR issues. |
| Overall | **3** (Good) | Solid empirical paper that opens a new task. Appropriate for EMNLP Findings. Borderline for Main. The paper defines the problem well and establishes baselines, but lacks the methodological innovation or demonstrated practical impact typically expected for Main conference acceptance. |

**Confidence:** 4/5 (fairly confident, but acknowledge that task novelty could justify Main acceptance if area chairs value problem formulation contributions).