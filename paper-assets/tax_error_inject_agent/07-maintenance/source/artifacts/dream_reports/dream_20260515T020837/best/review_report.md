---
dream_id: dream_20260515T020837
tier: best
overall_score: weak reject (2/5)
timestamp: 2026-05-15T03:08:03.813201+00:00
---

## R1 Review: Methods + Experiments

### Summary
The paper investigates whether taxonomy-guided error injection (TaxEI), which produced large gains in tool-use domains (PALADIN on ToolBench), transfers to embodied planning (ALFWorld). Using a 4-operator error taxonomy, the authors train Qwen3-8B under three conditions (Vanilla, TaxEI, Random) and report that TaxEI degrades performance while increasing variance. The paper claims two separable effects: a shared threshold-plateau in dose-response and a constant ~6.4pp taxonomy penalty, supported by training dynamics analysis, qualitative failure analysis, WebShop replication, and scale ablation.

### Strengths
- S1: **Well-motivated negative result with clear practical value.** Testing whether error injection transfers across agent domains is a natural and important question. The negative finding, if properly supported, would save the community from pursuing a dead-end in planning domains.
- S2: **Clean experimental isolation of the taxonomy label variable.** The v4 same-source dual-formatting design (TaxEI and Random differ only in the error tag text, using identical injected trajectories) is methodologically sound and eliminates confounds from injection point selection, recovery content, or data volume.
- S3: **The per-operator locality gradient (Table 8) is the paper's most compelling finding.** The monotonic relationship between error locality (C4 local -> P2 global) and TaxEI advantage (+6.1pp -> -8.4pp) provides a micro-level mechanism that bridges the macro tool-use/planning contrast. This is genuinely insightful.
- S4: **Dose-response protocol with fixed total data size** is a well-designed ablation that controls for data volume confounds. The seed=42 dose-response data (Table 2) appears to be grounded in actual experiments.
- S5: **Transparent statistical reporting.** The paper reports both significant and non-significant tests (e.g., paired t-test p=0.18 NS alongside pooled permutation p=0.031), and the discussion of the asymmetry between mean and variance effects is honest.

### Weaknesses
- W1: **Critical data integrity concern -- Table 1 numbers do not match the project's actual experimental results.** The actual 3-seed results (from the project's ROADMAP and decisions log) are: Vanilla 65.3%±3.3pp (61.7/68.1/66.0), TaxEI 56.7%±8.6pp (61.7/46.8/61.7), Random 63.1%±7.0pp (66.0/55.3/68.1). However, Table 1 in the paper reports Random as 70.9%±3.3pp (68.1/74.5/70.2) and TaxEI as 64.5%±3.3pp (61.7/68.1/63.8), with all three methods having identical SD=3.3pp. These numbers appear to come from the "imagined experiments" (Multi-Seed Dose-Response at 10% injection), not from the actual core evaluation. This is a fundamental problem.

- W2: **The "constant ~6.4pp taxonomy penalty" claim is acknowledged as a discretization artifact in the project's own analysis notes.** The project's memory file explicitly states: "per-task cross-analysis confirms that the 3 dose points have almost entirely different penalty tasks. Tasks appearing in all 3 dose points = 0. The ~6.4pp corresponds to exactly 3/47 tasks = 6.38pp, which is coincidence, not systematic penalty." The paper nevertheless presents this as a central finding ("remarkably stable gap," "systematic additive bias"). This contradicts the authors' own analysis.

- W3: **Multiple experiments appear to be simulated rather than actually conducted.** The multi-seed dose-response replication (Table 3), WebShop validation (Tables 4-5), scale ablation (Table 6), training dynamics with gradient cosine similarity (Table 4 in paper), qualitative failure analysis (Table 7), and few-shot recovery prompting (Table 8) are all present in the "imagined_experiments.yaml" file with pre-specified expected results. The project registry shows no corresponding completed experiments for WebShop, scale ablation at 25K/50K, multi-seed dose-response, or gradient cosine computations. If these are projections rather than actual results, the paper cannot present them as empirical findings.

- W4: **Statistical methodology is problematic.** (a) Pooling 3 seeds x 3 doses x 47 tasks to get N=423 "independent" observations is incorrect -- the dose-response conditions within a seed share the same model initialization and much of the same training data, violating independence. The inflation from N=141 to N=423 artificially reduces p-values. (b) Paired t-tests with n=3 seeds have essentially no power (the paper acknowledges this for TaxEI vs Vanilla, p=0.18, but then routes around it via pooling). (c) The F-test for variance ratio with df=(2,2) is extremely unreliable.

- W5: **The abstract and title are misleading relative to the actual evidence.** The abstract states specific numbers (SD 8.6pp vs 3.3pp, pooled permutation p=0.031, gradient cosine 0.28 vs 0.35, clean-sample loss inflation 16.6%) that, based on the project records, are either from imagined experiments or from incorrectly pooled statistics. The paper's framing has shifted from the project's own honest assessment ("injection is indistinguishable from noise in low-data embodied planning") to stronger causal claims about "structured gradient interference" and "taxonomy-operator replay."

### Questions for Authors
- Q1: Can you confirm that Table 1's per-seed numbers (particularly Random: 68.1/74.5/70.2 and TaxEI: 61.7/68.1/63.8) correspond to actual evaluation runs with checkpoints that can be inspected? The project registry shows quite different numbers.
- Q2: The multi-seed dose-response (Table 3) requires 12 additional training runs + 12 evaluations beyond the seed=42 dose-response. Were these actually conducted? If so, what are the experiment IDs and where are the logs?
- Q3: For the training dynamics analysis (Table 4), how was gradient cosine similarity between clean and injected samples computed? Was this done via actual gradient computation on saved checkpoints, or is it estimated?
- Q4: The WebShop replication requires building an entirely new taxonomy, collecting trajectories, and running training + evaluation in a new environment. Given that the ALFWorld pipeline alone required extensive engineering, can you provide details on the WebShop implementation?
- Q5: How do you reconcile the claim of a "constant ~6.4pp taxonomy penalty" with your own per-task analysis showing that the penalty tasks are entirely different across dose points?
- Q6: For the scale ablation to 25K and 50K, how were additional trajectories generated? The project notes that the base dataset is 501 GPT-5.2 trajectories producing 4,671 variants. Scaling to 50K would require ~5x more trajectory collection. Was this done?
- Q7: The qualitative failure analysis reports 24 cases (Table 7). Were these manually annotated from actual model outputs, and by how many annotators? What was the inter-annotator agreement?

### Detailed Comments

**Section 3 (Method):** The experimental design is sound in principle. The same-source dual-formatting (D004/D006 decisions) that makes TaxEI and Random differ only in the error tag is a strong methodological choice. The 4-operator taxonomy (P1, P2, C1, C4) covers a reasonable space. However, the paper does not justify why only 4 operators (vs. PALADIN's 7), nor does it discuss whether the taxonomy's coverage is comparable.

**Section 4.1 (Core Results):** The numbers in Table 1 are inconsistent with the project's actual experimental records. The real data shows TaxEI mean=56.7% with individual seeds 61.7/46.8/61.7, not 64.5% with seeds 61.7/68.1/63.8. The variance gradient claim (Vanilla SD 3.3pp < Random 7.0pp < TaxEI 8.6pp) is supported by the actual data, but the paper reports all SDs as 3.3pp, which contradicts the variance gradient that is supposed to be the paper's primary finding.

**Section 4.2 (Dose-Response):** The seed=42 dose-response data (Table 2) appears genuine and is the paper's strongest empirical contribution. The threshold-plateau pattern (10% -> 25% drop of 12.8pp, then plateau at 50%) is interesting. However, the claimed constant taxonomy penalty of ~6.4pp has been identified in the authors' own notes as a discretization artifact of 47-task granularity. The paper should either acknowledge this or provide evidence that the same tasks are responsible across dose points (which the authors' own analysis shows is not the case).

**Section 4.3 (Multi-Seed Dose-Response):** If Table 3 is based on imagined rather than actual experiments, this section must be removed entirely. The suspiciously uniform taxonomy penalty (6.4pp at every single seed x dose combination except one at 6.3pp) is more consistent with a constructed table than empirical data, which would show natural variation.

**Section 4.4 (Training Dynamics):** The gradient cosine similarity metric (0.28 vs 0.35) would be a strong mechanistic finding if actually computed. However, computing per-sample gradient cosine similarity requires saving and comparing full gradient vectors, which is computationally expensive and not a standard training logging output. The project records do not show evidence of this computation being performed.

**Section 4.5 (Qualitative Failure Analysis):** Analyzing 24 cases is a small sample. The categorization into "operator replay," "action sequence disorder," etc. requires clear operational definitions and ideally multiple annotators. The claim that 25% show "operator replay" is interesting but needs better grounding.

**Section 4.6 (WebShop):** Only 2 seeds are used, which is insufficient to compute meaningful variance estimates. The cross-environment comparison table (Table 5) is appealing but requires that the WebShop experiments were actually conducted with comparable rigor.

**Section 4.7 (Scale Ablation):** Single-seed results at 25K and 50K. If these are projections rather than actual experiments, they cannot be included.

**Section 4.8 (Few-Shot Recovery):** The comparison between SFT-based injection and inference-time recovery prompting is conceptually valuable. The finding that P2 (sub_goal_deletion) shows zero few-shot gain while C4 (observation masking) shows +8.5pp aligns well with the locality hypothesis. But again, the provenance of these numbers needs verification.

**Statistical Analysis (Section 4.9):** The "Original" vs "Updated" framing in Table 9 creates an impression of progressive evidence accumulation, but the "Updated" statistics pool non-independent observations. The effective N of 423 assumes that a seed=42 model at 10% injection and the same seed=42 model at 25% injection provide independent evidence, which they do not (same initialization, overlapping training data).

### Missing Experiments
1. **More than 3 seeds for the core comparison.** The paper argues that single-seed evaluation is unreliable, yet uses only 3 seeds -- barely above the minimum for computing a standard deviation. Five or more seeds would provide meaningful statistical power.
2. **Controlled cross-domain experiment.** Running the same method on both ToolBench and ALFWorld with the same base model would be the definitive test of the task-structure hypothesis. The paper acknowledges this but doesn't attempt it.
3. **Hyperparameter sensitivity analysis.** Only one learning rate and one epoch count (3) are used. The interaction between injection ratio and learning rate could be important -- perhaps TaxEI needs a lower learning rate to avoid overfitting to error patterns.
4. **Multiple base models.** Only Qwen3-8B is tested. The findings might not generalize to other architectures or model sizes.
5. **Larger test set or cross-validation.** 47 test tasks is very few. Each task counts as ~2.1pp, making fine-grained comparisons unreliable.
6. **Verification that the training dynamics, WebShop, scale ablation, and qualitative analysis experiments were actually conducted,** with corresponding logs and checkpoints.

### Minor Issues
- The paper title in the .tex file ("Error Injection Helps Tool-Use but Hurts Planning") differs from the title referenced in the review task summary ("Seed Variance Dominates Error Injection Signal in Low-Data Embodied Planning SFT"). This discrepancy suggests the paper went through significant framing changes. The current title makes a stronger claim ("hurts planning") than the evidence supports.
- Section numbering: the paper uses \section for Method and Experiments but subsections are not numbered in a way that matches the review task's references.
- Table 1 caption says "Clean task success rate" but should clarify these are from the full 9,029-sample training runs (not dose-response).
- The bibliography entries use inconsistent formatting (some "et al." have first names, others don't).
- The PALADIN citation uses arXiv ID 2509.25238 -- this should be verified as the correct identifier.
- "760 base trajectories x operators" in Section 3.1 seems inconsistent with "501 GPT-5.2-generated successful trajectories" mentioned earlier in the same paragraph.

### Scores
- Soundness: 2/5
- Excitement: 3/5
- Overall Recommendation: 2/5
- Confidence: 4/5 (I have carefully cross-referenced the paper's claims against the underlying project data)

### Justification
The core research question is well-motivated and the negative result, if properly supported, would be a valuable contribution to the Insights from Negative Results workshop. The experimental design (same-source dual-formatting, dose-response protocol) is sound. The per-operator locality gradient is a genuinely interesting finding.

However, I have serious concerns about data integrity. The numbers in Table 1 do not match the project's actual experimental results. Multiple experiments (multi-seed dose-response, WebShop, scale ablation, training dynamics gradient analysis, qualitative failure analysis) appear in the project's "imagined experiments" file with pre-specified outcomes, raising questions about whether they were actually conducted. The central claim of a "constant ~6.4pp taxonomy penalty" is contradicted by the authors' own per-task analysis. The statistical methodology inflates significance by pooling non-independent observations.

The paper as written makes strong empirical claims that are not adequately supported by the available evidence. A revised version that (1) reports only actually-conducted experiments with verifiable results, (2) correctly reports the core multi-seed numbers, (3) reframes the taxonomy penalty as a discretization artifact rather than a systematic bias, and (4) uses appropriate statistical methods would be a much stronger submission. The underlying research direction remains promising for this venue.