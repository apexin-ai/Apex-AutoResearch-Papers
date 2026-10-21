---
dream_id: dream_20260516T105318
tier: best
overall_score: weak reject
timestamp: 2026-05-16T11:40:57.180089+00:00
---

# Review Report: FREIGE — Faithful and Evidence-Grounded Document-Level Relation Extraction with LLMs

## Summary

This paper formalizes "evidence-grounded DocRE" — requiring LLMs to simultaneously generate relation triples and supporting evidence sentences — and systematically compares online RL (GRPO), offline preference optimization (DPO), and rejection sampling fine-tuning (RSFT). The central finding is a "decoupling spectrum": RL optimization pressure correlates with evidence-extraction decoupling severity, with GRPO+QLoRA causing catastrophic collapse (rel_F1 < 0.02) while RSFT avoids decoupling. The paper proposes CED (Contrastive Evidence Discrimination) as an NLI-based scoring function and EDCR as a diagnostic metric. Results are validated across model families (Qwen3, LLaMA-3.1), scales (1.7B–8B), and datasets (DocRED, Re-DocRED).

---

## Strengths

**S1. Well-motivated task formulation.** Formalizing evidence-grounded DocRE fills a genuine gap: generative LLMs for DocRE produce no verifiable evidence. The "evidence generation tax" (~7pp Ign-F1) is clearly quantified and provides an intuitive framing for the paper's central challenge. The distinction between evidence *retrieval* (encoder methods) vs. evidence *generation* (this work) is cleanly articulated.

**S2. Decoupling spectrum is a genuinely interesting finding.** The observation that RL optimization pressure monotonically correlates with decoupling severity — from RSFT (none) through GRPO-bf16 (mild) to GRPO-QLoRA (catastrophic) — is novel and practically important. The cross-family replication (Qwen3 rel_F1=1.38, LLaMA rel_F1=1.5) is compelling evidence that this is an optimization-dynamics phenomenon rather than a model-specific artifact. This insight has implications beyond DocRE for anyone applying RL to multi-objective structured prediction.

**S3. Impressive breadth of validation.** The paper validates claims along three orthogonal axes: cross-scale (1.7B/4B/8B), cross-dataset (DocRED/Re-DocRED), and cross-family (Qwen3/LLaMA). The test set results are obtained via official CodaLab submission, and the cross-dataset consistency table (Table 5) provides a clean summary. This level of thoroughness addresses common reviewer concerns about single-model/single-dataset generalization.

**S4. Human validation of EDCR.** The 100-sample annotation study with two annotators (ρ=0.78, κ=0.73) provides necessary grounding for EDCR as a diagnostic metric. The error analysis (Table 7) identifying multi-hop reasoning as the primary failure mode is informative and honest.

**S5. CED reranker is a practical contribution.** The training-free CED reranker achieving 46.5 Ign-F1 (only 0.2pp below no-evidence) with Evi-F1=81.2 is the most immediately deployable contribution. It elegantly sidesteps the evidence tax at inference time.

**S6. Clean paper structure.** The paper is concise (8 pages), well-organized, and the writing is clear. Tables are informative and consistently formatted.

---

## Weaknesses

**W1. DPO results are promised but absent (Major).** The abstract, introduction, and Section 1 all list DPO as one of three paradigms systematically compared. The abstract claims "DPO exhibits gradual decoupling across epochs." Yet no DPO results appear in any table. This is a significant gap: the decoupling spectrum narrative relies on a monotonic ordering (RSFT → DPO → GRPO-bf16 → GRPO-QLoRA), but the DPO data point is entirely missing from the paper. Without it, the "spectrum" is really just three points (RSFT, GRPO-bf16, GRPO-QLoRA), and the claim of monotonic progression is unsupported for the DPO → GRPO-bf16 transition. This needs to be either included or the framing should be revised.

**W2. EDCR adds limited information beyond rel_F1 (Major).** The paper reports ρ=−0.965 between EDCR and rel_F1 at the method level (Section 2.4). This extremely high correlation means EDCR and rel_F1 are near-perfectly redundant at the granularity where the paper's claims operate. The per-relation-level orthogonality (ρ=−0.064) is mentioned but not demonstrated with any downstream use case. The simple formula EDCR = 1 − rel_F1/evi_F1 mechanically approaches 1.0 whenever rel_F1 approaches 0 (as in catastrophic decoupling), which is trivially detectable from rel_F1 alone. The paper needs to demonstrate a concrete scenario where EDCR provides actionable information that rel_F1 alone does not — e.g., distinguishing between a model that is bad at extraction *and* evidence vs. one that is bad at extraction *but* good at evidence.

**W3. Unexplained 1.7B > 4B anomaly (Major).** In Table 3, Qwen3-1.7B SFT Ign-F1 = 47.86 substantially outperforms Qwen3-4B SFT Ign-F1 = 39.74. An 8pp advantage for a model with less than half the parameters is highly unusual and demands explanation. The paper mentions a "non-monotonic" pattern for the evidence tax but does not directly address why the smaller model is dramatically better at extraction. This could indicate confounds (different training hyperparameters, different LoRA configurations relative to model size, different effective trainable parameter ratios) that undermine the cross-scale comparison. Without explanation, the reader cannot distinguish genuine scale effects from experimental artifacts.

**W4. Missing CED vs. flat-NLI ablation (Moderate).** The paper's methodological contribution is the *contrastive* design of CED (Eq. 1) — subtracting the best hard-negative NLI score from the gold evidence score. However, no ablation compares CED to a non-contrastive ("flat") NLI baseline, e.g., simply using P_NLI(entail | E, r) without the contrastive term. The NLI model ablation (Table 8) varies model size but does not isolate the contrastive mechanism. Without this ablation, we cannot determine whether the contrastive design is the key ingredient or whether any NLI-based scoring would suffice.

**W5. Severely under-cited (Moderate).** The paper has only 4 references. DocKS-RAG and LMRC are discussed but not cited. GRPO is used extensively but not cited. Key DocRE baselines (KD-DocRE, JEREX, etc.) are not mentioned. The framing around RL for IE and catastrophic forgetting references "recent work" without citation. For a top venue, this is far below expected scholarly contextualization. The related work section reads as a sketch rather than a thorough survey.

**W6. Incomplete cross-family spectrum (Moderate).** Table 2 shows GRPO-bf16 only for Qwen3-4B, not for LLaMA-3.1-8B. The claim that the decoupling spectrum is "validated across model families" is therefore incomplete — we only see the catastrophic extreme for LLaMA but not the mild-decoupling (bf16) middle point. Similarly, DPO is tested for neither family (see W1). The Qwen3-4B spectrum has more conditions than LLaMA, making the cross-family validation asymmetric.

**W7. Single-seed for key experiments (Minor).** Table 3 notes Qwen3-4B uses 5-seed mean, but 1.7B and 8B use a single seed (s42). Given the anomalous 1.7B > 4B result (W3), single-seed numbers for 1.7B and 8B are insufficient to establish reliable cross-scale trends. A single bad/good seed could shift results by 2–3pp in LoRA fine-tuning.

**W8. No direct comparison with encoder-based SOTA (Minor).** The paper mentions DREEAM achieving ~61.7 Ign-F1 but never includes encoder baselines in its tables. The best generative result (CED reranker 46.5) is ~15pp below encoder SOTA. While the paper positions evidence generation as a different paradigm, including encoder results in at least one table would help readers calibrate the absolute performance level and understand the practical gap.

---

## Experiment Coverage Assessment

Compared to the full experiment design, the paper covers all six planned experiments:
- ✅ Test set evaluation (CodaLab) — Table 1
- ✅ Cross-scale ablation (1.7B/4B/8B) — Table 3
- ✅ Re-DocRED cross-dataset — Table 4
- ✅ LLaMA cross-family decoupling — Table 2
- ✅ EDCR human validation — Table 6
- ✅ NLI model ablation — Table 8

The primary coverage gap is DPO, which is *described* as part of the systematic comparison but has no experimental results.

---

## Questions for Authors

1. Can you provide the DPO results that the abstract and introduction promise? Specifically, training curves showing "gradual decoupling across epochs."
2. Why does Qwen3-1.7B substantially outperform Qwen3-4B on SFT? What are the LoRA rank/alpha settings for each scale? Are trainable parameter ratios comparable?
3. Can you demonstrate a use case where EDCR provides actionable diagnostic information that raw rel_F1 does not?
4. Have you run a flat-NLI baseline (no contrastive term) through the full RSFT pipeline? What is the Ign-F1 difference?
5. What is the inference cost multiplier for the CED reranker (G=8 samples + NLI scoring)?

---

## Minor Issues

- Table references "Tables 6 and 7" in Section 3.6 but there is no table numbered as such in the expected position — the numbering appears shifted.
- The CED score in Section 2.3 is described as "combining extraction F1 and evidence quality," but Eq. 1 defines CED as purely NLI-based. Clarify how extraction F1 enters the RSFT scoring.
- The paper describes RSFT as "Offline RL" in the introduction bullet list, but RSFT is not typically categorized as RL. This may confuse readers familiar with the RL literature.

---

## Overall Assessment

The paper addresses a meaningful and well-motivated problem — evidence-grounded DocRE — and the decoupling spectrum is a genuinely interesting finding with implications beyond the specific task. The experimental breadth (3 scales × 2 datasets × 2 families) is commendable and addresses common generalization concerns.

However, several issues reduce confidence below the acceptance threshold for a top ML venue:
- The most critical gap is the missing DPO experiments that the abstract explicitly promises — this undermines the "systematic comparison of three paradigms" narrative.
- EDCR's near-perfect redundancy with rel_F1 at the method level weakens Contribution 3.
- The unexplained 1.7B > 4B anomaly raises questions about experimental controls in the cross-scale analysis.
- The paper is severely under-cited, which is unusual for a venue submission.

The work has a solid foundation and the direction is promising. A revision that (a) includes DPO results or reframes the paper's scope, (b) explains the scale anomaly, (c) adds a CED vs. flat-NLI ablation, and (d) substantially expands the reference list could move this to an accept.

**Score: 3 — Weak Reject**

**Confidence: 4 — High** (familiar with DocRE literature and RL fine-tuning methods)