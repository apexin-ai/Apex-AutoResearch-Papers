---
dream_id: dream_20260516T155803
tier: median
overall_score: 3/6 — Weak Reject
timestamp: 2026-05-16T16:28:23.794555+00:00
---


# Review Report: FREIGE — Faithful Evidence-Grounded Document-Level Relation Extraction via Generative LLMs

## 1. Summary

This paper formalizes **evidence-grounded DocRE** as a new task requiring LLMs to jointly produce relation triples and supporting evidence sentences. It presents FREIGE, comparing three training paradigms—GRPO (online RL), DPO (offline preference optimization), and RSFT (rejection sampling fine-tuning with NLI-based scoring). Two principal findings are reported: (1) a "decoupling spectrum" where RL optimization pressure correlates with evidence-extraction decoupling severity, and (2) a U-shaped scaling pattern for the evidence generation tax across model sizes (1.7B/4B/8B). RSFT with CED scoring emerges as the only viable route. The paper also proposes EDCR as a diagnostic metric (ρ=0.55 with human judgments) and validates across DocRED and Re-DocRED.

---

## 2. Strengths

**S1. Well-motivated task formulation.** The distinction between discriminative evidence *retrieval* (SAIS, DREEAM) and generative evidence *production* is clearly articulated. This is a meaningful research direction—LLM-based extractors currently provide no verifiable grounding, and the paper directly addresses this gap.

**S2. The decoupling spectrum is insightful (Table 3).** Showing that GRPO-QLoRA → GRPO-bf16 → DPO → RSFT forms a continuous decoupling gradient, and that this is an *intra-task* resource allocation phenomenon (not catastrophic forgetting, evidenced by bf16 GRPO retaining IE ability), is a genuinely interesting empirical finding.

**S3. Unusually honest and calibrated claims.** The paper explicitly acknowledges: the 12pp gap vs DREEAM in sentence-level alignment, EDCR's moderate (not strong) human correlation, the evidence tax, the post-hoc retrieval trade-off, and cross-dataset attenuation. This level of candor is commendable and strengthens credibility.

**S4. Comprehensive experiment coverage.** The paper includes test set evaluation, cross-dataset generalization (Re-DocRED), post-hoc retrieval baseline, EDCR human validation, NLI model ablation, and dev-to-test degradation analysis. All planned experiments from the design document are present.

**S5. The post-hoc comparison (Section 4.6) is valuable.** Rather than claiming end-to-end generation is strictly superior, the paper frames it as a trade-off (faithfulness vs. extraction accuracy), which is a more defensible and useful framing for practitioners.

---

## 3. Weaknesses

**W1. Very large absolute performance gap with encoder SOTA (Major).** RSFT CED achieves 42.5 Ign-F1 on DocRED test; DREEAM reports 61.7 on dev (test unavailable without CodaLab). Even accounting for dev-test degradation, this is a ~15-20pp gap. The paper frames generative and discriminative approaches as "different design points," but does not adequately address when a practitioner would choose a system at 42.5 F1. The practical utility argument is underdeveloped.

**W2. Limited methodological novelty (Major).** The paper explicitly positions RSFT as "a single-round variant of STaR with domain-specific NLI-based quality filtering" (Section 5). CED scoring is a straightforward application of NLI contrastive entailment. EDCR (Eq. 1) is simply the average NLI entailment probability. The contribution is primarily empirical analysis—valid, but the novelty bar for pure analysis papers at top venues is high, and the analysis rests on limited data points (see W4).

**W3. Post-hoc baseline undermines the core value proposition (Major).** Table 6 shows SFT+BM25 achieves *higher* rel_f1 (0.489 vs 0.468) with decent Evi-F1 (0.74 vs 0.82). The paper argues RSFT evidence is more "faithful" via EDCR (0.64 vs 0.58), but EDCR itself is only validated at ρ=0.55 with human judgments. Using a partially-validated metric to justify the main approach's advantage over a simpler baseline is partially circular. The CED reranker (Table 6, N=8) achieves 0.486 rel_f1 and 0.819 Evi-F1—comparable to RSFT on both axes at the cost of 8× latency—which further questions whether RSFT training is necessary vs. inference-time reranking.

**W4. U-shaped scaling claim rests on thin evidence (Moderate).** The "U-shaped pattern" is derived from 3 Qwen model sizes + 1 LLaMA cross-family point (Table 4). Three points within a single architecture family cannot robustly establish a U-shape—they could equally reflect idiosyncrasies of the Qwen family at these specific scales. The LLaMA-8B point (−0.7pp) is consistent but provides only one cross-family confirmation. The claim would benefit from at least 2-3 more scale points or additional model families.

**W5. Cross-dataset generalization is weak (Moderate).** RSFT gains attenuate from +5.49pp (DocRED) to +2.2pp (Re-DocRED), a 60% reduction. CED selection rate drops from 12.4% to ~9%, and mean candidate F1 drops from 0.62 to 0.55. This suggests CED scoring's effectiveness is partially dataset-specific, weakening claims about the generality of the NLI-based scoring approach.

**W6. Statistical concerns (Moderate).**
- Seed variance: The review context indicates s42=43.63 vs s43=45.85 (2.2pp range), yet the paper reports "45.0" or "45.85" as the RSFT result without clearly reporting variance. A 2.2pp seed range is large relative to the claimed RSFT-vs-SFT improvement.
- CED vs flat-NLI are "statistically equivalent" (paired t-test p=0.44, Section 3.2). If the simpler flat-NLI scoring works equally well, the contrastive design of CED—a key design choice—has no demonstrated advantage, weakening the narrative around CED's importance.

**W7. Extremely thin related work (Minor).** Only 6 references. Multiple methods mentioned in the text are not cited: GenRES (mentioned in Limitations), DocKS-RAG, LMRC, ATLOP, DocuNet (mentioned in Related Work). A top-venue submission should properly engage with the literature.

**W8. EDCR metric design concerns (Minor).**
- Lower EDCR = higher decoupling is counterintuitive. EDCR=0.99 (GRPO-QLoRA) means near-perfect evidence but catastrophic extraction collapse. The metric name ("Completeness Ratio") suggests higher is better, but its diagnostic interpretation inverts this for the most interesting cases.
- The relationship between CED (training-time scorer) and EDCR (evaluation metric) is unclear—they appear to measure related but distinct things, yet share the NLI backbone. Potential confounding between training signal and evaluation metric is not discussed.

---

## 4. Questions for Authors

1. **Seed variance**: How many seeds were used for Table 1 results? What is the standard deviation? The 2.2pp range observed on dev suggests reported improvements may not be statistically significant.
2. **CodaLab submission**: Why not submit to CodaLab for a direct test-set comparison with DREEAM? This would substantially strengthen the paper.
3. **CED reranker as main method**: The CED reranker (N=8) in Table 6 achieves 0.486 rel_f1 + 0.819 Evi-F1—close to or better than RSFT on both metrics. What is the argument for RSFT training over inference-time reranking, beyond latency?
4. **Flat-NLI equivalence**: Given CED and flat-NLI are statistically equivalent (p=0.44), what justifies preferring CED and building the narrative around contrastive scoring?

---

## 5. Experiment Coverage Assessment

All 5 imagined experiments from the design document are present in the paper:

| Planned Experiment | Covered? | Section |
|---|---|---|
| Test Set Evaluation (RSFT CED + baselines) | ✓ | §4.2, Table 1 |
| Re-DocRED Cross-Dataset Pipeline | ✓ | §4.5, Table 5 |
| EDCR Human Annotation Validation | ✓ | §4.7, Table 7 |
| NLI Model Ablation (base vs large) | ✓ | §4.8, Table 8 |
| Post-hoc Evidence Retrieval Baseline | ✓ | §4.6, Table 6 |

Coverage is **complete**. Additionally, the paper includes the decoupling spectrum (Table 3), scaling analysis (Table 4), and dev-to-test degradation (Table 9) beyond the imagined experiments.

---

## 6. Minor Issues

- Table 1 footnote states DREEAM numbers are dev set, but the main text (Section 4.2) doesn't flag this prominently enough—readers may miss that the 61.7 vs 42.5 comparison is dev vs test.
- The DREEAM-protocol Evi-F1 comparison (Table 2) is the only apples-to-apples evidence comparison, yet it's presented as a secondary table rather than integrated into the main results.
- Section 4.9 (dev-to-test degradation) could note that RSFT's larger degradation (−3.35pp vs −1.86pp) suggests possible dev-set overfitting, not just distributional sensitivity.

---

## 7. Overall Assessment

**Score: 3 / 6 (Weak Reject)**

The paper addresses a meaningful problem and provides a thorough empirical investigation. The decoupling spectrum and scaling analysis are genuinely interesting findings. The writing is honest and well-calibrated.

However, three issues prevent acceptance: (1) the absolute performance gap with encoder SOTA is very large, making practical impact unclear; (2) methodological novelty is limited—RSFT/CED/EDCR are straightforward applications of existing ideas; (3) the paper's own post-hoc baseline and CED/flat-NLI equivalence results undermine key claims about the necessity and design of the proposed approach. The scaling analysis, while interesting, rests on too few data points to be a standalone contribution.

The paper would benefit from: additional model family/scale experiments to solidify the scaling claims, CodaLab test set submission for fair encoder comparison, and a clearer articulation of when practitioners should prefer end-to-end generation over simpler post-hoc retrieval.

**Confidence: 4/5** — I have carefully read the paper and understand the problem domain. My uncertainty is primarily around whether the analysis-focused contribution is sufficient for the target venue, which is a judgment call.
