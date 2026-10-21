---
dream_id: dream_20260516T155803
tier: best
overall_score: borderline reject
timestamp: 2026-05-16T16:25:59.019476+00:00
---


# Review Report: FREIGE — Faithful Evidence-Grounded Document-Level Relation Extraction via Rejection Sampling and Contrastive Evidence Discrimination

## Overall Assessment

**Score: 4 / 6 (Borderline Reject)**

The paper introduces evidence-grounded DocRE as a new task formulation, systematically compares three optimization paradigms (GRPO, DPO, RSFT), and reports a scale-dependent evidence tax phenomenon. The experimental scope is commendable — covering three model scales, two model families, two datasets, and multiple ablations. However, several issues prevent recommendation for acceptance: (1) the primary technical contribution CED is statistically indistinguishable from the simpler flat-NLI baseline, undermining the novelty claim; (2) the absolute performance gap with encoder-based methods (45.2 vs 61.7 Ign-F1) is never adequately addressed; (3) key entries in the decoupling spectrum table are missing; and (4) RSFT itself is not a novel method.

---

## Strengths

**S1. Well-motivated task formulation.** Evidence-grounded DocRE — requiring joint generation of relation triples and supporting evidence — is a genuinely useful extension of standard DocRE. The motivation for verifiability in information extraction is compelling and timely.

**S2. Systematic paradigm comparison with clear finding.** The evidence-extraction decoupling spectrum (GRPO QLoRA → GRPO bf16 → DPO → RSFT) is the paper's strongest conceptual contribution. The observation that optimization pressure correlates with decoupling severity is well-documented and provides useful guidance for practitioners.

**S3. Comprehensive scaling and cross-family experiments.** Testing across Qwen3-1.7B/4B/8B and LLaMA-3.1-8B provides strong evidence that findings are not architecture-specific. The scale-dependent evidence tax (benefit at 1.7B, cost at 4B, neutral at 8B) is a non-obvious and valuable finding that challenges the naive assumption that evidence always hurts extraction.

**S4. Thorough experiment coverage.** The paper covers test set evaluation, DREEAM protocol alignment, EDCR human validation, post-hoc retrieval comparison, NLI model ablation, cross-dataset generalization, multi-scale analysis, and cross-family validation — a very complete experimental program.

**S5. Post-hoc retrieval comparison is convincing.** The 17.5pp Evi-F1 gap between end-to-end generation and BM25 retrieval decisively motivates the integrated approach. The analysis of why ~30% of gold evidence lacks entity co-occurrence is insightful.

**S6. EDCR human validation.** The ρ=0.78 correlation with human judgments, along with the low false positive rate (8%), provides reasonable validation of EDCR as a diagnostic tool. The dual-layer property (method-level vs per-relation-type, with orthogonal information) is interesting.

---

## Weaknesses

**W1. CED does not outperform flat-NLI (Major).** The paper proposes CED as a key technical contribution, but Section 5 reports CED and flat-NLI yield p=0.44, Δ=0.0008 rel-F1. The entire contrastive hard-negative mechanism provides no measurable benefit over simply scoring positive entailment. The paper attempts to salvage this by claiming "interpretability," but this is not demonstrated with any concrete use case or experiment. This significantly undermines the novelty of the method.

**W2. Absolute performance gap with encoder methods is unaddressed (Major).** RSFT CED achieves 45.2 Ign-F1 on DocRED test vs DREEAM's 61.7 — a 16.5pp gap. The paper dismisses this with a footnote saying encoder models are "not directly comparable," but for a practitioner deciding between methods, this gap matters enormously. The paper should discuss: (a) what fraction of this gap is due to the generative formulation vs model choice, (b) whether evidence-grounded methods can close this gap with larger models, and (c) under what deployment scenarios the evidence justifies the extraction cost.

**W3. Incomplete decoupling spectrum table (Moderate).** Table 2 has "—" for GRPO QLoRA Ign-F1 and all DPO 3-epoch metrics. These are central to the paper's main claim (the decoupling spectrum). The GRPO QLoRA case should show the catastrophically low Ign-F1 explicitly to support the narrative; omitting it weakens the presentation. DPO 3-epoch results are critical for establishing the "gradual decay" claim but are entirely missing.

**W4. RSFT is not a novel method (Moderate).** RSFT is explicitly described as "a single-round variant of STaR with domain-specific NLI-based quality filtering." Rejection sampling fine-tuning and NLI-based scoring are both well-established. The contribution is in the combination and application to DocRE, not in the method itself. The paper should be more forthright about this and position the contribution as primarily empirical/analytical rather than methodological.

**W5. Anomalous 4B baseline confounds evidence tax analysis (Moderate).** Qwen3-4B SFT achieves only 39.7 Ign-F1, while 1.7B achieves 47.9 and 8B achieves 50.5. The 4B model is anomalously weak — a smaller model outperforming a larger one suggests a confound (undertrained, poor hyperparameters, or architectural mismatch). The evidence tax analysis attributes the 4B penalty to "insufficient capacity for both objectives," but the 1.7B — which has less capacity — shows benefit. An alternative explanation: the 4B baseline is simply poorly tuned, and the RSFT gain partially reflects better data curation compensating for poor SFT. This needs investigation or at least discussion.

**W6. No comparison with other LLM-based DocRE methods (Moderate).** The paper references LMRC [7] and DocKS-RAG [8] but never compares against them. The only LLM baseline is the authors' own SFT. Without external LLM baselines, the claimed +5.4pp improvement could partly reflect a weak SFT implementation rather than RSFT's effectiveness.

**W7. Human validation is underspecified (Minor).** The 100-sample EDCR validation does not specify: number of annotators, their background/expertise, annotation guidelines, or how disagreements were resolved. κ=0.82 is reported but the annotation setup needs more detail for reproducibility.

**W8. No qualitative examples or error analysis (Minor).** The paper never shows a single example of generated evidence — what good evidence looks like, what failure modes exist, or how CED scoring distinguishes quality levels. For a paper about evidence faithfulness, this is a notable omission.

**W9. Evidence tax definition is slightly misleading (Minor).** Evidence tax is defined as "RSFT Ign-F1 − no-evidence Ign-F1," but the no-evidence model is SFT-trained (not RSFT-trained). This conflates RSFT's general improvement with the evidence-specific cost. A cleaner measurement would compare RSFT-with-evidence vs RSFT-without-evidence (i.e., apply the same RSFT pipeline to a no-evidence formulation).

---

## Questions for Authors

1. Can you report the actual Ign-F1 / rel-F1 numbers for GRPO QLoRA and DPO 3-epoch in Table 2?
2. What explains Qwen3-4B's anomalously low SFT baseline (39.7) compared to the smaller 1.7B (47.9)? Were hyperparameters tuned per model size?
3. If CED ≈ flat-NLI, what is the practical argument for using CED? Can you show a concrete case where CED's contrastive diagnostics provided actionable insight?
4. How does RSFT performance compare to LMRC or DocKS-RAG under the same evaluation protocol?
5. For the EDCR human validation, how many annotators participated and what were the annotation guidelines?

---

## Experiment Coverage Assessment

Relative to the experimental plan, coverage is **complete** — all 9 planned experiments (test set eval, DREEAM protocol alignment, EDCR human validation, post-hoc retrieval, NLI ablation, Re-DocRED, 8B Qwen RSFT, 1.7B Qwen RSFT, LLaMA-3.1-8B RSFT) are reported. The paper delivers a thorough experimental program. The main gaps are in presentation (incomplete tables, missing qualitative analysis) rather than missing experiments.

---

## Minor Issues

- Table 2: Missing values should be reported or explicitly explained
- The term "evidence tax" is used inconsistently — sometimes referring to pre-RSFT gap, sometimes post-RSFT gap
- Section 3.4 step 4 says "margin between positive and hard-negative entailment scores" but doesn't specify the aggregation when multiple hard negatives exist
- Reference [12] "Quantized reinforcement learning" — the title and attribution should be verified; this may refer to QuRL which has a different title

---

## Summary Recommendation

The paper addresses a well-motivated problem with comprehensive experiments, but the primary technical contribution (CED) fails to outperform a simpler baseline, and the work is better characterized as an empirical study than a methodological advance. The evidence-extraction decoupling spectrum and scale-dependent evidence tax are interesting analytical findings, but the incomplete tables, missing external baselines, and anomalous 4B results weaken confidence. With revisions addressing the CED non-result, adding external LLM comparisons, and completing the tables, this could become a solid empirical contribution — but in its current form, it falls slightly below the acceptance threshold for a top ML venue.
