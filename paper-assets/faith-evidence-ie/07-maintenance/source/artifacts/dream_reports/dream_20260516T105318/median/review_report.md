---
dream_id: dream_20260516T105318
tier: median
overall_score: borderline reject
timestamp: 2026-05-16T11:43:11.230883+00:00
---

# FREIGE: Faithful Relation Extraction with Evidence Generation — Review Report

## Paper Summary

This paper proposes evidence-grounded DocRE as a new task requiring generative LLMs to jointly output relation triples and supporting evidence sentences. The framework (FREIGE) systematically compares GRPO, DPO, and RSFT for this joint objective. The central finding is the "evidence–extraction decoupling spectrum": RL optimization pressure correlates with the severity of a trade-off where evidence quality improves at the cost of extraction accuracy. RSFT with NLI-based scoring is identified as the only route avoiding decoupling. The paper also proposes EDCR, a simple ratio metric for decoupling diagnosis, validated against human judgments.

---

## Overall Assessment

**Score: 4 — Borderline Reject**

A thorough empirical study with a genuinely interesting observational finding (the decoupling spectrum), but the contributions do not reach the novelty/significance bar for a top ML venue. The task definition is a natural extension rather than a conceptual leap, the proposed metric (EDCR) is trivially simple, the flagship scoring method (CED) is statistically indistinguishable from a naive baseline, and the RSFT improvement is modest (+3pp on test). The paper's strength lies in its breadth of validation and scientific honesty, but it reads more as an empirical investigation report than a paper with a clear, impactful methodological contribution.

---

## Detailed Review

### Strengths

**S1: Well-structured empirical comparison across three optimization paradigms.**
The systematic comparison of GRPO (online RL), DPO (offline preference), and RSFT (rejection sampling) for a multi-objective generative task is thorough and well-executed. The paper tests each paradigm under multiple configurations (QLoRA vs bf16, different group sizes, epoch counts) rather than running a single configuration per method. This provides convincing evidence for the decoupling spectrum claim.

**S2: The decoupling spectrum is a genuinely interesting empirical finding.**
The observation that RL optimization pressure correlates with evidence–extraction decoupling severity, and that QLoRA amplifies this to catastrophic levels while bf16 shows only mild effects, is well-documented and informative. The distinction between intra-task decoupling and inter-task forgetting (Section 6) is a valuable conceptual contribution. The bf16 vs QLoRA comparison (GRPO bf16 −2pp vs QLoRA catastrophic collapse) effectively isolates quantization as an amplifier rather than root cause.

**S3: Breadth of validation is commendable.**
Two model families (Qwen3, LLaMA-3.1), three scales (1.7B, 4B, 8B), two datasets (DocRED, Re-DocRED), and multi-seed significance testing represent a thorough experimental design. The paper also honestly reports negative results (CED ≈ flat-NLI, dev→test degradation for RSFT).

**S4: Scientific honesty about CED vs flat-NLI.**
Rather than hiding the non-significance of CED vs flat-NLI (p=0.31), the paper openly reports it and adjusts claims accordingly. This is admirable and increases trust in the other reported results.

**S5: Human validation of EDCR, with detailed disagreement analysis.**
The 100-sample, 850-triple human annotation study with systematic disagreement categorization (partial evidence, multi-hop, implicit evidence) adds valuable grounding. The method-level correlation (ρ=0.82) supports EDCR's utility for coarse-grained diagnosis.

### Weaknesses

**W1 (Major): Limited methodological novelty.**
The paper's proposed methods are combinations of existing techniques: SFT with structured output (standard), RSFT with NLI scoring (STaR + off-the-shelf NLI), GRPO/DPO applied to a new task (standard application), and EDCR = 1 − rel_F1/evi_F1 (trivial ratio). The CED scoring function, which was the most novel component, turns out to be statistically indistinguishable from naive flat-NLI scoring (p=0.31). After this result, the paper's methodological contribution reduces to "use any NLI scorer to filter RSFT data with strict top-k=1 selection"—a practical recipe, but not a contribution that advances our understanding of how to solve this class of problems.

**W2 (Major): The task definition, while useful, is a straightforward extension.**
Evidence-grounded DocRE adds evidence generation to existing generative DocRE. The paper treats this as a novel task formulation, but the idea of producing justifications alongside predictions is well-established in explainable AI. The "evidence tax" (∼7.5pp) is quantified but not deeply analyzed—why does evidence generation cost this much? Is it inherent to sequence length, attention allocation, or output format? Without this analysis, the tax observation remains descriptive.

**W3 (Major): Modest improvement magnitudes and generalization concerns.**
- RSFT achieves only +3.0pp on the DocRED test set (narrowed from ∼+5pp on dev), with the paper acknowledging distribution shift sensitivity
- On Re-DocRED, the gain shrinks further to +2.0pp
- The CED reranker achieves 45.8 Ign-F1 vs 46.0 for no-evidence SFT—but the reranker requires generating multiple candidates at inference time, making it computationally expensive for a marginal benefit over simply not generating evidence
- The dev→test gap for RSFT (∼3.2pp) vs SFT (∼1.2pp) raises concerns about RSFT's robustness

**W4 (Major): Incomplete cross-family validation.**
The LLaMA-3.1-8B validation covers only the spectrum endpoints (RSFT: no decoupling; GRPO QLoRA: catastrophic). Without intermediate points (bf16 GRPO, DPO 1ep/3ep), the claim of a "spectrum" on LLaMA is not actually validated—only two discrete points are confirmed. The paper acknowledges this as a limitation, but it weakens claim C2's cross-family generalizability.

**W5 (Moderate): No comparison with encoder-based or other generative DocRE methods.**
The paper positions evidence-grounded DocRE as a new task but provides no comparison with encoder-based evidence retrieval methods (SAIS, DREEAM) on comparable metrics. Even an approximate comparison would contextualize the absolute performance level of the proposed approach. Similarly, there is no comparison with other generative DocRE methods (DocKS-RAG, LMRC mentioned in related work) to establish where FREIGE stands in the non-evidence setting.

**W6 (Moderate): Thin related work section.**
Only 9 references. Missing important related work: (1) Faithful generation / hallucination detection literature, which directly relates to evidence faithfulness; (2) Multi-objective RL literature, which would provide theoretical grounding for the decoupling phenomenon; (3) Other rejection sampling approaches for LLMs (e.g., ReST, RAFT); (4) QuRL, which is cited by name but not in the reference list; (5) GenRES, cited in Limitations but not in references. The related work also does not discuss the growing body of work on LLM self-verification and chain-of-thought faithfulness.

**W7 (Minor): EDCR has limited discriminative power at fine granularity.**
Method-level ρ=0.82 with only n=8 methods has wide confidence intervals. Per-relation ρ=0.58 and per-triple ρ=0.51 suggest the metric has limited diagnostic value beyond coarse method-level comparisons, yet the paper positions it as a reusable diagnostic tool.

**W8 (Minor): Statistical concerns with the cross-scale experiment.**
Three data points (1.7B, 4B, 8B) are insufficient to draw conclusions about scaling behavior. The 1.7B > 4B anomaly is hand-waved as "Qwen3's progressive training strategy" without evidence. The non-monotonic evidence tax pattern is acknowledged as an observation, but these observations collectively suggest the scaling results are unreliable for generalizable conclusions.

**W9 (Minor): The GRPO bf16 Ign-F1 > F1 anomaly is insufficiently explained.**
Table 1 shows GRPO bf16 with Ign-F1=43.8 > F1=42.0, which is unusual (Ign-F1 ≤ F1 by definition in standard DocRED evaluation since Ign-F1 removes shared train-dev triples). The paper attributes this to "train-triple filtering effects" but does not elaborate. This warrants detailed explanation since it could indicate an evaluation bug.

### Questions for Authors

1. Why is GRPO bf16 Ign-F1 (43.8) higher than F1 (42.0) on the test set? This violates the expected Ign-F1 ≤ F1 relationship. Please provide a detailed explanation.
2. Have you analyzed which relation types benefit most from RSFT vs SFT? A per-relation-type breakdown would help understand when evidence-aware training helps.
3. What is the inference cost of the CED reranker (number of candidates generated, latency)? If it requires generating 8 candidates per document, the practical benefit over no-evidence SFT (45.8 vs 46.0) seems marginal.
4. Can you provide confidence intervals for the ρ=0.82 method-level EDCR correlation? With n=8, bootstrapped CIs may be wide.
5. The paper claims RSFT avoids decoupling because it uses "static filtered data without online optimization pressure." But isn't this also true of standard SFT? What specifically about NLI-filtered RSFT prevents decoupling compared to unfiltered RSFT or differently-filtered RSFT?

### Experiment Coverage Assessment

Comparing against the experimental design document, all planned experiments are represented in the paper:

| Planned Experiment | Paper Coverage | Notes |
|---|---|---|
| Test Set Evaluation | Table 1 | ✓ Complete |
| Model Size Ablation (1.7B/8B) | Table 4 | ✓ Complete |
| Re-DocRED Cross-Dataset | Table 5 | ✓ Complete |
| NLI Model Ablation (DeBERTa base/large) | Appendix A, Table 8 | ✓ Complete |
| EDCR Human Annotation Validation | Table 6, Appendix B | ✓ Complete |
| LLaMA-3.1-8B Cross-Family | Table 7 | Partial (only endpoints) |
| CED vs flat-NLI 5-Seed Test | Table 3, Appendix C | ✓ Complete |

Coverage is comprehensive. The LLaMA partial coverage is acknowledged and is consistent with the experimental plan's GPU budget constraints.

### Minor Issues

- Appendix C header exists but appears to contain only Table 10 with no accompanying text
- QuRL and GenRES are cited by name but not in the reference list
- The paper would benefit from an explicit comparison table against prior generative DocRE methods
- Table 1 mixes test set (Ign-F1, F1) and dev set (Evi-F1, EDCR) metrics without visual separation

---

## Scoring Summary

| Criterion | Score (1-6) | Justification |
|---|---|---|
| Novelty | 3 | Task extension is natural; EDCR is trivial; CED ≈ flat-NLI removes the most novel component |
| Soundness | 4 | Experiments are well-executed with proper significance testing; some concerns (Ign-F1 > F1 anomaly, n=8 for method-level correlation) |
| Significance | 3 | Decoupling spectrum is informative but primarily observational; modest improvement margins; limited practical impact given CED reranker ≈ no-evidence SFT |
| Clarity | 5 | Well-written, clearly structured, honest about limitations |
| Reproducibility | 4 | Sufficient detail for main experiments; code not mentioned |
| **Overall** | **4** | **Borderline Reject** |

### Recommendation

The decoupling spectrum finding is the paper's strongest contribution and is genuinely informative for the community. However, the combination of (1) limited methodological novelty after CED ≈ flat-NLI, (2) modest improvement margins that shrink on test and cross-dataset settings, (3) incomplete cross-family validation, and (4) thin related work situating suggest the paper is not ready for a top venue in its current form. A revised version that (a) provides deeper theoretical analysis of why decoupling occurs, (b) completes the LLaMA spectrum, (c) compares against encoder-based methods, and (d) substantially expands the related work could be competitive.
