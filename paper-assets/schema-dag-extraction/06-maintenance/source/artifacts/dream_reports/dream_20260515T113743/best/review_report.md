---
dream_id: dream_20260515T113743
tier: best
overall_score: 3 — Reject
timestamp: 2026-05-15T12:29:44.942582+00:00
---


# Review: Pairwise Type Confusability Independently Predicts Extraction Degradation in Training-Free LLM Information Extraction

## Reviewer R1 — Methods and Experiments Focus

---

### 1. Summary

This paper studies why training-free LLM information extraction degrades on complex schemas, isolating "type confusability" (embedding cosine similarity between type pairs) from "type count" as independent degradation channels. The authors validate pairwise confusability correlations across NER (Few-NERD), ED (MAVEN), and RE (DocRED) with two LLMs, propose a multi-channel degradation model (count→omission, confusability→substitution), and present SDGD, a graph-coloring decomposition framework. The paper claims SDGD-zero yields +5.5 F1 on Few-NERD and +3.3 on MAVEN over single-pass extraction.

---

### 2. Strengths

- **Well-designed controlled experiments for Claims 1-2.** The pairwise SCS→confusion analysis is methodologically clean. Operating at the type-pair level avoids many aggregation confounds that plague batch-level analyses. The cross-task (NER/ED/RE) and cross-model (Qwen3/LLaMA) replication protocol is thorough.

- **Centrality confound analysis is a genuine methodological contribution.** The discovery that per-type BCS aggregation introduces a centrality confound on homogeneous schemas (MAVEN), with both embeddings showing positive correlations that contradict the hypothesis, is insightful and honestly reported. This finding has practical value for the community.

- **Error taxonomy provides mechanistic evidence.** The monotonic increase in type substitution errors from Q1 (6.2%) to Q4 (38.4%) across BCS quartiles, with a corresponding decrease in false negatives, cleanly supports the two-channel degradation model. The chi-squared test (p < 1e-16) is appropriate.

- **2x2 factorial design is well-constructed.** Crossing count × confusability with 10 batches per cell, finding significant main effects for both factors (F=14.2 and F=22.8) with a non-significant interaction, is clean evidence for the additive model.

- **Embedding ablation (2x3 matrix) is a useful practical contribution.** The finding that no single embedding universally captures confusability, with Qwen3 working for cross-domain and MiniLM for same-domain schemas, provides actionable guidance.

- **Transparent reporting of negative results in the analytical sections.** Qwen3 pairwise failure on MAVEN (r=-0.007, n.s.) and per-type positive correlations on MAVEN are honestly disclosed rather than buried.

---

### 3. Weaknesses

- **CRITICAL: SDGD results appear to be imagined/projected, not from actual experiments.** The project's own experimental log (memory.md, D014, experiment_plan.yaml) records that exp-008 SDGD-zero **actually produced F1=0.251, far below the single-pass baseline of 0.445** (a -19.4pp degradation, not a +5.5pp improvement). The experiment plan explicitly states "DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass baseline on Few-NERD." Decision D014 records "SDGD-zero 差于 baseline，Claim 3 需重大调整或放弃." The paper's SDGD numbers (F1=0.469 for SDGD-zero, 0.488 for SDGD-cal, etc.) appear in files labeled "imagined_experiments" within a "dream_reports" directory. **If these results have not been obtained from actual experiments, the entire Claim 3 and Section 6 must be withdrawn.** This is the single most serious issue with the paper.

- **Effect sizes for pairwise correlations are small.** r=0.12-0.16 means confusability explains only 1.4-2.4% of variance in pairwise confusion. While statistically significant due to large n (1,953-14,028 pairs), the practical predictive value is very limited. The paper acknowledges this in limitations but the abstract and introduction frame these as strong findings ("independently predicts extraction quality degradation").

- **Multiple comparisons not corrected.** The paper reports correlations across 2 embeddings × 3+ datasets × 2 analysis levels (pairwise/per-type) × 2 models, totaling ~20+ statistical tests. No Bonferroni, BH, or other correction is applied. Several results hover near conventional significance thresholds (e.g., LLaMA per-type p=0.041, MAVEN per-type Qwen3 p=0.021). After correction, some of these would likely become non-significant.

- **FewRel results are incomplete.** FewRel is mentioned as a key dataset in the framing document (Tier 2 evidence, "Δ=21-50pp") and in the paper_framing.md, but the paper body contains no dedicated FewRel section. The experiment (exp_fewrel_formal) is listed as still RUNNING. The extreme-batch comparison numbers (count_4: Δ=-20.9pp, count_8: Δ=-50.0pp) come from a pilot study, not a formal experiment with proper controls.

- **DocRED analysis appears shallow.** The paper claims DocRED pairwise r=0.095-0.108, but the experimental data suggests these come from the same "dream/imagined" pipeline. DocRED has no factorial analysis, no error taxonomy, no SDGD evaluation. It serves mainly as a third checkmark for "cross-task replication" without depth.

- **MAVEN extreme-batch results show high-BCS > low-BCS F1, contradicting the paper's framing.** Table in experiment_data.json shows count_6: high-BCS relaxed F1=0.218 vs low-BCS=0.098, and count_12: high-BCS=0.192 vs low-BCS=0.114. High-BCS batches perform BETTER, not worse. The paper's Section 5.3.1 reports this but frames it as supporting the confusability hypothesis through confusion rate ratios, without adequately addressing that the headline metric (F1) goes in the wrong direction on MAVEN.

- **The "multi-channel degradation model" is descriptive, not predictive.** The paper presents post-hoc categorization of errors into channels but does not demonstrate that the model predicts degradation on held-out schemas, new tasks, or different prompt designs. The R² of 0.38-0.39 (from the task brief's factorial analysis) is modest and the additive vs. multiplicative distinction is practically nil (0.38 vs 0.39).

- **SCS proxy validation numbers are suspiciously strong in the paper vs. the task brief.** The paper reports Qwen3 SCS vs empirical ρ=0.584 with 85% top-20 overlap, while the task brief states ρ=0.35 and 50% top-10 overlap. These are substantially different numbers that need reconciliation.

- **Sample sizes for the factorial design are small.** 10 batches per cell in the 2×2 factorial (40 total observations) provides limited statistical power. The interaction effect (p=0.087) is "marginally significant" -- with proper power analysis this design may be underpowered for detecting interactions.

---

### 4. Questions to Authors

1. **Can you clarify the provenance of SDGD results?** The experimental logs indicate SDGD-zero produced F1=0.251 on Few-NERD (below baseline 0.445), yet the paper reports F1=0.469 (+5.5pp). Are the paper's numbers from a different run with the "v2" merge strategy? If so, has this v2 actually been executed on GPU, or are these projected/simulated results?

2. **Why does the MAVEN extreme-batch comparison show higher F1 for high-BCS batches?** If confusability degrades extraction, high-BCS batches should have lower F1. The reversal needs more explanation than "confusion rate ratios" -- it suggests a fundamental confound where semantically coherent (high-BCS) batches provide better extraction context.

3. **How do you reconcile the SCS proxy validation numbers?** The paper reports ρ=0.584 and 85% top-20 overlap for Qwen3 SCS vs empirical confusion, but earlier analyses showed ρ=0.35 and 50% top-10 overlap. Which is correct?

4. **Have you considered that the pairwise SCS→confusion correlation might be partially tautological?** If the LLM uses internal representations similar to the embedding model's representations, then pairs that are close in embedding space may be close in the LLM's representation space, making confusion a trivial consequence of representation geometry rather than a schema-design insight.

5. **What is the within-count BCS analysis on MAVEN?** The task brief mentions r=0.12, p=0.18 at count 6, which is not significant. This seems to undercut the claim that pairwise confusability "independently predicts" degradation on MAVEN when count is controlled.

6. **For the error taxonomy, how were "type substitution" errors operationally defined?** Specifically, how do you distinguish a type substitution (correct span, wrong type) from a case where the model genuinely believes the span is the predicted type rather than being "confused" between two types?

7. **Why is there no multiple comparison correction across the ~20+ statistical tests reported?**

---

### 5. Minor Issues

- The abstract claims results across "three IE tasks" but the paper's actual experimental depth varies dramatically: Few-NERD has full analysis, MAVEN has partial analysis with contradictory directions, DocRED is shallow, and FewRel is missing.
- Table 2 (pairwise cross-task) reports n=14,028 for MAVEN but the paper says 168 types, which gives 168*167/2 = 14,028 pairs. However, many of these pairs will have zero confusion observations, inflating n and making p-values misleadingly small.
- The Related Work section is thin (3 short paragraphs, 6 references total). For a venue like EMNLP, this needs substantial expansion covering label confusion in classification, schema complexity in IE, prompt engineering for structured extraction, and embedding-based similarity measures.
- "Relaxed F1" for MAVEN (ignoring trigger boundaries) is a non-standard metric that makes results difficult to compare with prior work.
- The paper does not report confidence intervals for any of the key effect size estimates.
- Wall-clock times are reported but hardware specs are not mentioned in the paper body.
- Reference [2] (MAVEN) has year 2023 in the cite key but 2020 in the text.

---

### 6. Preliminary Score: 3 (Reject)

**Justification:**

The analytical contributions (Claims 1-2) represent solid empirical work with a genuine methodological insight (centrality confound). However, the paper has a fatal flaw: the SDGD results (Claim 3) -- which constitute the paper's primary method contribution and occupy a significant portion of the paper -- appear to be projections from a "dream/best-case" simulation rather than actual experimental results. The real experiment (exp-008) produced results showing SDGD-zero *degrading* performance by 19.4 F1 points below baseline, the opposite of the claimed +5.5pp improvement.

Even setting aside the SDGD integrity concern: the pairwise effect sizes are small (r=0.12-0.16, ~2% variance explained); multiple comparisons are uncorrected; FewRel results are missing; the MAVEN extreme-batch F1 goes in the wrong direction; and the SCS proxy validation numbers are inconsistent across documents. The paper would need Claims 1-2 to stand on their own as a purely analytical contribution, which is a harder sell at a top venue without a convincing practical application.

If the SDGD results are confirmed to be from actual experiments (with the v2 merge fix validated on GPU), and the inconsistencies in reported numbers are resolved, the score could rise to 4-5. But as submitted, the evidentiary basis for the paper's central method claim is not established.

---

### 7. Confidence: 4 (High)

I have carefully cross-referenced the paper's claims against the project's experimental logs, decision records, and experiment plan. The discrepancy between reported SDGD results and actual experimental outcomes is well-documented in the project's own records. My assessment of the analytical contributions (Claims 1-2) is based on thorough examination of the statistical methodology and effect sizes. I am less certain about whether there might be additional experimental runs not captured in the files I examined, which is why confidence is 4 rather than 5.
