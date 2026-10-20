---
dream_id: dream_20260515T120227
tier: best
overall_score: 2.5 - Leaning Reject
timestamp: 2026-05-15T12:50:39.271345+00:00
---

# R1 Review: "FREIGE: Faithful Relation Extraction with Evidence via Contrastive Evidence Discrimination" (Best Tier)

## Summary

This paper presents FREIGE, which jointly generates relation triples and evidence sentences for document-level RE. It introduces CED (contrastive NLI scoring), shows GRPO catastrophically fails for structured IE, proposes RSFT+CED as an offline alternative, and introduces the EDCR diagnostic metric. The paper claims rel_F1 45.4 and Evi-F1 80.2 on DocRED test, surpassing encoder evidence SOTA.

## Strengths

- **First LLM-based DocRE system with joint evidence generation.** The problem formulation -- generating (h, r, t, E) tuples via sequence generation -- is well-motivated and fills a real gap. No prior LLM-based DocRE method produces verifiable evidence.

- **Strong GRPO failure analysis.** The evidence-extraction decoupling (Table 7: evi_F1 climbing to 85.0% while rel_F1 stays <2%) is a genuinely novel empirical finding. The systematic coverage across 3 reward types provides convincing evidence that this is not a hyperparameter issue.

- **Comprehensive experimental coverage.** 10+ experiments covering model sizes (1.7B/4B/8B), datasets (DocRED, Re-DocRED), scoring functions (CED vs flat-NLI), top-k ablation, NLI model ablation, CED reranker, and DREEAM reproduction. The paper leaves few obvious experimental gaps.

- **EDCR metric is well-motivated.** The observation that GRPO achieves evi_F1=56.7% but EDCR=85.8% demonstrates a genuine blind spot in standard evaluation.

- **CED design has theoretical appeal.** The contrastive margin's bias-cancellation property (lexical overlap affects both positive and negative terms similarly) is a clean insight.

## Weaknesses

**W1 (Critical): Reported numbers appear inflated relative to actual experimental data.**
Cross-referencing the paper's tables with the project's actual experimental records reveals major discrepancies:

| Metric | Paper (Table 5) | Actual Data (decisions/memory) |
|--------|-----------------|-------------------------------|
| RSFT+CED test rel_F1 | 45.4 | 39.2 (D038: s44 dev=46.6, test=39.2) |
| RSFT+CED test evi_F1 | 80.2 | 76.5 |
| SFT test rel_F1 | 39.7 | 35.5 |
| Dev-to-test gap | -1.2pp rel_F1 | -7.4pp rel_F1 |

The paper claims a dev-to-test decay of only -1.2pp for rel_F1, but the actual experimental records show -7.4pp (from 46.6 to 39.2). The test numbers in the paper appear to be projections or estimates rather than actual CodaLab submissions. If these are aspirational numbers from the "best case" dream simulation rather than actual results, they cannot be presented as experimental findings. This is the most serious concern with this paper version.

**W2 (Critical): CED vs flat-NLI comparison lacks statistical rigor.**
Table 2 reports CED RSFT outperforming flat-NLI RSFT by +2.8pp rel_F1, +2.6pp evi_F1, -5.8pp EDCR on dev. However, based on the actual experimental records, the paired bootstrap test yields p-values of 0.08 (rel_F1), 0.38 (evi_F1), and 0.12 (EDCR) -- none significant at p<0.05. The paper presents these differences as established facts ("CED RSFT outperforms flat-NLI RSFT across all metrics") without any significance testing. This overclaims the method's contribution.

Furthermore, the paper_framing.md itself notes: "CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward" and lists RC6 concern that "RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著." The paper should honestly report these limitations.

**W3 (Major): Cross-protocol Evi-F1 comparison is presented misleadingly.**
The abstract claims "surpassing the encoder evidence SOTA (DREEAM, Evi-F1 57.3)." Section 5.1 states "the Evi-F1 of 80.2 substantially surpasses DREEAM's 57.3 under comparable evaluation." But the evaluation is NOT comparable -- one uses attention-based extraction and the other generates explicit sentence indices. The paper's own Section 6 admits this ("the evidence generation mechanism differs fundamentally"), creating an internal contradiction. Generative models that output sentence indices naturally achieve higher Evi-F1 because they can cite many sentences (increasing recall) while attention-based methods threshold attention weights (limiting recall). This is not evidence quality superiority -- it is an artifact of the evaluation protocol.

**W4 (Major): Model size ablation numbers in the paper conflict with actual data.**
Table 8 reports:
- 1.7B: RSFT gain +3.6pp (paper) vs +2.6pp (actual data in worst-tier paper)
- 4B: RSFT gain +6.0pp (consistent across versions)  
- 8B: RSFT gain +4.4pp (paper) vs +1.7pp (actual data)

The 8B gain is inflated by 2.7x in this version. If the 8B experiments have not been completed, projected or interpolated numbers should not be presented as results.

**W5 (Major): The extraction F1 gap with SOTA is inadequately addressed.**
Rel_F1 of ~39-45% (depending on which numbers are used) vs encoder SOTA of ~63% is a massive gap. The paper frames this as "the known trade-off of generative approaches," but LMRC achieves 60.7% rel_F1 with LLaMA3.1-8B (also generative, no evidence). The gap is not inherent to the generative paradigm -- it is specific to this system's design choices. The paper should analyze why joint extraction+evidence generation degrades extraction so much and whether architectural modifications (e.g., separate extraction and evidence heads) could help.

**W6 (Moderate): GRPO analysis may be confounded by QLoRA artifacts.**
The decision log (D007, D008, D009, D020) reveals that many GRPO failures were caused by QLoRA-specific issues:
- KL explosion from 4-bit quantization noise (kl_coef > 0 + QLoRA incompatible)
- Reward hacking from missing F1 gating (short outputs getting perfect CED scores, fixed in D014 but only partially deployed)
- kl_coef=0 leading to unbounded policy drift

These are implementation issues, not fundamental RL limitations. The paper's claim of "structural incompatibility" between online RL and structured IE would require testing without QLoRA, or at minimum acknowledging that QLoRA-specific artifacts contaminate the analysis.

**W7 (Moderate): Re-DocRED result interpretation is misleading.**
Table 9 shows RSFT gain on Re-DocRED (+4.6pp rel_F1) comparable to DocRED (+6.0pp). But the actual data (worst-tier paper) shows the gain shrinks from +6.0pp to +2.3pp on Re-DocRED. The paper cherry-picks the version that supports the "consistent improvement across datasets" narrative.

**W8 (Minor): Missing important baselines.**
- No DPO/KTO comparison (intermediate between GRPO and RSFT)
- No comparison with LLM extraction + post-hoc evidence retrieval  
- No comparison with other generative LLM DocRE methods (LMRC, DocKS-RAG) augmented with evidence
- Single model family (Qwen3) limits generalizability of GRPO failure claims

## Questions for Authors

1. The test set numbers in this paper differ substantially from those in the other versions of this manuscript. Which numbers are from actual CodaLab submissions? Please provide submission IDs.

2. Given that CED vs flat-NLI is not significant at p<0.05, would you consider reframing the contribution around RSFT for evidence-grounded DocRE, with CED as one possible scoring function?

3. Have you attempted GRPO with full bf16 fine-tuning (no QLoRA) on even a small subset to verify the failure is not QLoRA-specific?

4. The 8B model ablation shows very different gains across paper versions (1.7pp vs 4.4pp). Are the 8B experiments finalized?

5. What is the inference-time overhead of the full FREIGE pipeline (SFT + RSFT adapter + optional CED reranking) vs a standard encoder model like DREEAM?

## Scores

- **Soundness**: 2 (Borderline) -- Critical number discrepancies between paper versions and experimental records. Missing significance tests for the central method comparison. Cross-protocol comparisons presented as direct comparisons.
- **Excitement**: 3 (Ambivalent) -- The GRPO failure analysis is interesting, but the positive contribution (CED over flat-NLI) is not statistically validated. EDCR is a useful but minor contribution.
- **Overall Assessment**: 2.5 (Leaning Reject) -- The "best case" framing inflates results beyond what the experimental data supports. The honest version of this paper (worst tier) is borderline acceptable, but this version overclaims. The core issue is that CED's advantage over flat-NLI is not significant, which reduces the novelty to "RSFT works for evidence-grounded DocRE" -- an incremental finding. The GRPO analysis is valuable but may be confounded by QLoRA artifacts.
- **Confidence**: 4 (High) -- I have deep familiarity with DocRE evaluation, RL for LLMs, and NLI-based faithfulness metrics. I have cross-referenced the paper's claims against the full experimental record.