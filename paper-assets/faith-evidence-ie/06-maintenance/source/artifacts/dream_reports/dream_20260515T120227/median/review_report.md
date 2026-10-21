---
dream_id: dream_20260515T120227
tier: median
overall_score: 3.0 - Borderline
timestamp: 2026-05-15T12:49:42.079796+00:00
---

# R1 Review: "FREIGE: Faithful Evidence-Grounded Document-Level Relation Extraction via Contrastive Evidence Discrimination" (Median Tier)

## Summary

This paper presents FREIGE, the first LLM-based DocRE system that jointly generates relation triples and evidence sentences. The key contributions are CED (a contrastive NLI scoring function), RSFT with CED-based filtering, a cautionary analysis of GRPO failure, and the EDCR diagnostic metric. On DocRED test, FREIGE achieves rel_F1 42.8--43.8% and evi_F1 78.3--78.9%.

## Strengths

- **Well-structured experimental pipeline.** The paper presents a clean progression: SFT baseline -> GRPO failure -> RSFT success, with CED as a composable module applicable at training-time (RSFT filtering) and inference-time (reranking). The composability result (Table 5, RSFT+CED+reranker achieving EDCR 58.5%) is a nice practical finding.

- **Thorough GRPO failure documentation.** The three-reward-type analysis with trajectory data (Table 6) convincingly demonstrates systematic GRPO failure. The evidence-extraction decoupling (evi_F1 85.0% while rel_F1 <2%) is a genuinely novel empirical finding.

- **Honest evaluation protocol discussion.** Section 5.5 and the baseline comparison table clearly flag the fundamental protocol difference between generative evidence (explicit sentence indices) and attention-based evidence (DREEAM/SAIS). The paper avoids claiming direct superiority despite the large Evi-F1 gap.

- **Comprehensive ablation coverage.** CED vs flat-NLI, top-k selection, NLI model capacity, model size (1.7B/4B/8B), Re-DocRED extension, CED reranker -- all contribute to understanding the method's properties.

- **DREEAM reproduction** with <0.5pp gap validates the evaluation pipeline.

## Weaknesses

**W1 (Major): Inconsistencies in reported numbers across tables.**
The paper reports different numbers for the same configuration across tables. For example:
- Table 1 reports SFT test rel_F1=38.6, but the dev-to-test table (Table 2) shows SFT dev=40.6, test=38.6 -- a 2.0pp gap. However, the actual experimental data shows SFT test rel_F1=0.355 (35.5%), not 38.6%. 
- RSFT CED (s44) test rel_F1 is reported as 43.8 in Table 1, but actual data shows 0.392 (39.2%).
- The dev-to-test gap is reported as 2.1--2.8pp, but based on actual dev numbers (0.466) and actual test (0.392), it should be 7.4pp.

These discrepancies between the paper's tables and the underlying experimental data suggest either (a) multiple evaluation runs with different configurations, or (b) errors in number transcription. The authors must clarify and ensure all numbers are traceable to specific experiments.

**W2 (Major): CED vs flat-NLI advantage is modest and potentially not significant.**
Table 3 shows CED RSFT outperforming flat-NLI RSFT by +0.7pp rel_F1, +1.4pp evi_F1, and -2.4pp EDCR. No significance tests are reported for this comparison. Given that the "worst" tier paper (which appears to use the actual experimental data) reports p-values of 0.08/0.38/0.12 for the CED vs flat-NLI comparison -- none significant at p<0.05 -- this undermines the paper's central claim that "CED provides consistent improvement over flat-NLI scoring."

**W3 (Major): The generative approach's extraction F1 is substantially below state-of-the-art.**
Rel_F1 of 42.8--43.8% (test) is 20pp below DREEAM (63.3%) and even further below recent LLM methods like DocKS-RAG (63.6%). The paper positions evidence generation as the primary contribution, but if the extraction quality is too low for practical use, the evidence is of limited value. The paper should discuss whether the rel_F1 gap is inherent to joint extraction+evidence generation or specific to the Qwen3-4B + LoRA setup.

**W4 (Moderate): GRPO exploration may be insufficient to claim "structural incompatibility."**
The paper tests 3 reward types x 2 learning rates x limited KL configurations, all with QLoRA 4-bit quantization on Qwen3 only. Known issues with QLoRA + RL (quantization noise in KL computation, limited LoRA expressivity) could explain the failures without invoking "structural incompatibility between online policy optimization and compositional structured outputs." Missing explorations:
- Full fine-tuning or fp16 LoRA (isolates QLoRA artifacts)
- Higher LoRA rank (r=128 or r=256)
- DPO as an intermediate approach
- Reward decomposition (separate extraction and evidence rewards with independent weighting)

**W5 (Moderate): EDCR correlation analysis is statistically underpowered.**
The Pearson r=-0.42 between Evi-F1 and EDCR is computed across only 4-5 data points (methods), making this correlation estimate highly unreliable (confidence interval likely spans from -0.9 to +0.3). The claim that "EDCR captures a distinct failure mode" would be better supported by per-document or per-relation-type analysis with sufficient sample size.

**W6 (Moderate): Missing comparison with post-hoc evidence retrieval.**
A natural baseline for "LLM extraction + evidence" is to run an LLM extraction model (e.g., LMRC) and then retrieve evidence sentences using BM25 or sentence similarity. This would provide a fairer comparison for the evidence quality of the joint generation approach.

**W7 (Minor): The relation-type EDCR analysis (Table 7) uses suspiciously round numbers.**
The EDCR values by relation type are all integers (85.0, 83.0, 80.0, etc.) with CED improvements that are exactly 5.0 or 6.0pp for every relation type. This suggests either binning/rounding or synthetic data. The authors should provide exact values.

**W8 (Minor): Single model family limits generalizability.**
All experiments use Qwen3. The GRPO failure claim would be substantially stronger with replication on LLaMA or Mistral.

## Questions for Authors

1. Can you provide exact p-values for the CED vs flat-NLI comparison? If they are not significant, how do you justify framing CED as the key contribution rather than RSFT itself?

2. The relation-type EDCR analysis (Table 7) shows identical improvement magnitudes (5-6pp) across all relation types. Is this an artifact of rounding? Please provide exact values.

3. Have you tried running GRPO without QLoRA quantization? The decision log suggests many failures were related to QLoRA-specific issues (KL explosion from 4-bit quantization noise).

4. What is the output truncation rate at max_new_tokens=1024? Your experimental notes mention 37% truncation for SFT. Does RSFT reduce this?

5. The RSFT+CED+reranker combination (Table 5) achieves the best EDCR (58.5%) but at 8x inference cost. Have you measured the actual latency overhead per document?

## Scores

- **Soundness**: 3 (Acceptable) -- Experimental design is generally sound but number inconsistencies and missing significance tests weaken confidence.
- **Excitement**: 3 (Ambivalent) -- The GRPO failure analysis is interesting but the positive contribution (CED) may not be significant over simpler alternatives.
- **Overall Assessment**: 3.0 (Borderline) -- A competent empirical study with interesting negative results, but the method contribution needs statistical validation and the number inconsistencies must be resolved.
- **Confidence**: 4 (High) -- Familiar with DocRE, RL for LLMs, NLI-based evaluation, and the specific experimental challenges of this setup.