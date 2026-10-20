---
dream_id: dream_20260527T022433
tier: median
overall_score: 4 — reject
timestamp: 2026-05-27T03:37:08.678881+00:00
---

---
dream_id: dream_20260527T022433
tier: median
reviewer: R2 (Novelty + Related Work)
overall_score: 4 — reject
timestamp: 2026-05-27
---

# Reviewer R2: Novelty and Related Work

## Summary

This paper applies a battery of standard interpretability tools (layer-wise probes, attention head profiling, counterfactual perturbation, RSA, CKA) to three decoder-only VLA architectures across four LIBERO suites, discovering that VLM-to-VLA fine-tuning produces consistent exit-layer R² collapse while L1 attention routing is inherited from pretrained backbones. The experimental matrix is well-designed and the statistical methodology is careful, but the paper's own internal evidence systematically undermines its contributions: the most visually striking finding (L1 attention gradient) is shown to be a base-model artifact (D090), head ablation produces ΔMSE≈0 (no functional consequence), counterfactual sensitivity correlates perfectly with token overlap (surface-level), DINOv2 alone achieves R²=0.687 (challenging the premise that instruction routing matters for action prediction), and the CKA metric reverses the RSA ordering (metric dependence). The paper is essentially an honest autopsy of a research direction that did not yield actionable insights.

## Strengths

- **Cross-architecture factorial design is genuine.** Three backbone families (Llama-2, Phi-3, Qwen2.5-VL) with different attention mechanisms (MHA vs GQA), vision encoders, and training pipelines. The natural experiment exploiting VLA-to-VLA vs VLM-to-VLA reference baselines is a well-conceived design that most single-architecture studies lack.

- **NLP finetuning controls are well-chosen.** Three chat-finetuned models sharing backbones with the VLAs produce uniformly flat R² profiles (ΔR²=0.000), cleanly establishing that exit collapse is not a generic fine-tuning artifact. The control covers all three backbone families, which is thorough.

- **Statistical methodology exceeds the field norm.** Monte Carlo cross-validation (n=1000) with demo-level splitting, permutation tests, TOST equivalence testing, Bonferroni correction across 63 tests (40/45 survive), probe seed sensitivity analysis. This level of rigor is commendable and rare in VLA interpretability papers.

- **Unusually honest self-assessment.** The paper explicitly acknowledges metric incomparability (5/7 CF pairs), the CKA-RSA reversal, the non-significant behavioral correlation (ρ=0.583, p=0.10), the ad hoc Δ>0.10 threshold, and the failed closed-loop evaluation attempt (SR=0/3). This transparency is admirable.

- **Appropriate concurrent work engagement.** The paper differentiates itself from Fang et al. (2026), Buurmeijer et al. (2026), Swann et al. (2026), Grant et al. (2026), and Haon et al. (2025) in a substantive rather than perfunctory way.

## Weaknesses

### W1. [Critical] The paper's own evidence argues against its contributions

This is not a standard weakness — it is the paper's defining structural problem. Consider the cumulative weight of the paper's own findings:

(a) **D090 self-critique removes the most visually striking result.** The 0→9→24 L1 attention head gradient was the paper's most compelling figure. Section 4.4 reveals this is a base-model artifact: Phi-3-Vision allocates 32/32 instruction-dominant heads *before any VLA training*. The paper correctly reports this but does not sufficiently reckon with how much evidential weight this removes. What remains is exit collapse (descriptive) and counterfactual sensitivity (surface-level, see below).

(b) **ΔMSE≈0 from head ablation.** Ablating 24/32 "instruction-dominant" heads produces d=0.65 trajectory divergence but ΔMSE=-0.001 (p=0.52, n.s.) relative to ground truth. The "direction rather than precision" interpretation is post-hoc and unfalsifiable. The more parsimonious reading: these heads do not carry functionally important information for action quality. Combined with the 8% specificity gap (instruction-dominant d=0.65 vs random-24 d=0.60), the instruction-dominant classification has minimal functional meaning.

(c) **DINOv2 R²=0.687 challenges the premise.** A frozen self-supervised vision encoder with no language input and no action training achieves higher action prediction R² than the VLA's own trained readout (0.678). This directly challenges the premise that instruction routing matters for action prediction — vision alone is sufficient and even superior.

(d) **Counterfactual sensitivity is surface-level.** The Spearman ρ=1.0 between token overlap (Jaccard) and Cohen's d across perturbation conditions means CF sensitivity tracks lexical novelty perfectly. The ordering (empty > wrong > shuffled > paraphrased) follows token overlap monotonically, not semantic distance. The paper claims "VLAs encode instruction content beyond token-level matching" based on paraphrased having different d from shuffled, but shuffled has Jaccard=1.0 and paraphrased has Jaccard=0.533 — the d ordering simply follows overlap.

(e) **Metric dependence.** CKA reverses the RSA ordering (Table in appendix). The "non-monotonic refinement" finding is metric-specific and cannot be treated as a robust result.

When a paper's central findings are: a base-model artifact (L1), a descriptive pattern without functional significance (exit collapse + ΔMSE≈0), surface-level perturbation sensitivity (ρ=1.0 with token overlap), and metric-dependent geometry — the cumulative picture is that the research question did not yield findings commensurate with a CoRL publication.

### W2. [Major] Novelty is limited to systematic application of existing methods

Every analytical method in this paper is standard in the NLP interpretability toolkit:
- Layer-wise probing: Alain & Bengio (2017), Belinkov (2022)
- RSA: Kriegeskorte et al. (2008)
- CKA: Kornblith et al. (2019)
- Attention head profiling: Clark et al. (2019), Michel et al. (2019)
- Counterfactual perturbation: adapted from NLP probing literature

The contribution is applying these methods to VLAs. This places the entire burden on empirical findings — and as detailed in W1, those findings are primarily descriptive, partially undermined by the paper's own controls, and lack functional significance. The "first systematic VLA profiling toolkit" framing overstates the novelty: assembling standard tools does not constitute a toolkit contribution unless the combination reveals something that individual tools cannot.

### W3. [Major] Related work has significant gaps

The paper's related work section is well-organized but misses several literatures that would either strengthen or contextualize its findings:

- **Neural collapse / representation collapse** (Papyan et al. 2020, Jing et al. 2022): The exit-layer R² decline is reminiscent of neural collapse phenomena where final-layer representations converge to class means. This literature could provide theoretical grounding for *why* VLM→VLA produces exit collapse.

- **Logit lens / tuned lens** (nostalgebraist 2020, Belrose et al. 2023): These works established that intermediate layers often contain more task-relevant information than exit layers in language models. The exit collapse finding is essentially a VLA instantiation of this known phenomenon.

- **Fine-tuning representation distortion** (Kumar et al. 2022 is cited, but Merchant et al. 2020, Mosbach et al. 2020 are absent): These NLP studies documented that fine-tuning concentrates task information in later layers while disrupting general representations — directly paralleling exit collapse.

- **Layer-wise probing in NLP** (Tenney et al. 2019, Jawahar et al. 2019, Rogers et al. 2020): Canonical references establishing the methodology the paper adapts. Their absence makes the paper appear less aware of the probing tradition it builds on.

- **Attention head pruning and specialization** (Voita et al. 2019): Directly relevant to the L1 attention analysis and the ablation experiments. Voita et al. showed that most attention heads can be pruned without loss — consistent with the paper's ΔMSE≈0 finding.

- **Feature reuse in fine-tuning** (Chizat et al. 2019 on lazy training): Could explain why VLA→VLA shows minimal representational change.

Without engaging these literatures, the paper misses the opportunity to connect its VLA-specific findings to broader, well-established phenomena in representation learning. The exit collapse finding may not be novel at all — it may be a well-known fine-tuning effect instantiated in a new domain.

### W4. [Major] Exit collapse has not been distinguished from format specialization

When a VLM is first trained to produce discrete action tokens, the exit layer must adopt a format compatible with the action head's tokenization scheme. An MLP probe operating on intermediate layers is format-agnostic, but exit-layer representations may be in an action-head-specific format that the probe cannot decode. This would produce the observed ΔR² pattern without any genuine "information loss."

The project notes indicate an action_head_decoding experiment was conducted (applying the frozen action head layer-by-layer), and the result was "negative" — meaning the action head *does* show exit-peaking R², which directly supports format specialization as the explanation for probe-measured exit collapse. That this experiment is excluded from the paper is a significant omission. Format specialization is the most parsimonious alternative explanation and it has not been ruled out.

### W5. [Major] The premise is questionable given the paper's own evidence

The paper studies "instruction routing" in VLAs, but its own evidence suggests instruction routing may not matter:

- **DINOv2 R²=0.687**: Vision alone predicts actions better than the VLA's trained representations.
- **Grant et al. (2026), cited by this paper**: Visual dominance — VLAs underweight instructions.
- **Haon et al. (2025), cited by this paper**: Instruction underutilization in deployment.
- **ΔMSE≈0 from head ablation**: Removing instruction-routing heads does not degrade action quality.
- **Instruction invariance**: Image-token RSA is identical with and without instructions (Δρ<0.006).

The cumulative picture is that instruction routing may be representationally present but functionally epiphenomenal in current VLAs. Studying the plumbing of a system that does not meaningfully use that plumbing is of limited scientific value.

### W6. [Moderate] N=2 independent VLM→VLA transitions

The exit collapse finding rests on two architectures (TracVLA, NORA). The permutation test (p=0.008) treats 9 architecture-suite cells as independent, but 4 TracVLA cells share weights and 2 NORA cells share weights — these are not independent observations. The effective N is 2, not 6 or 9. One counterexample from a third VLM→VLA architecture would break the pattern.

### W7. [Moderate] "Cross-architecture" diversity is narrower than framing suggests

All three architectures are:
- Decoder-only causal transformers
- Use frozen vision encoders
- Trained on LIBERO with autoregressive action token prediction
- Evaluated open-loop

Flow-matching (π₀), diffusion-based (Octo), encoder-decoder, and trainable-encoder VLA architectures are untested. The title "Cross-Architecture Analysis" overpromises relative to what is actually a cross-backbone analysis within a single architecture family.

### W8. [Minor] Instruction invariance at image tokens is architecturally guaranteed

The causal attention mask prevents image tokens from attending to instruction tokens. Reporting image-token RSA invariance to instruction content (Δρ<0.006) as an empirical finding inflates the apparent volume of results — it is an architectural tautology.

## Questions for Authors

1. **Format specialization**: The action_head_decoding experiment (applying the frozen action head layer-by-layer) reportedly showed exit-peaking R², directly supporting format specialization over information loss. Why was this excluded from the paper? If included, how would you reinterpret exit collapse?

2. **DINOv2 baseline**: DINOv2 achieves R²=0.687 with no language and no action training, exceeding the VLA's trained readout peak (0.678). Does this not suggest that the VLA's LLM backbone is *degrading* action-relevant information from the vision encoder, and that studying instruction routing is studying the wrong aspect of VLA failure?

3. **Functional significance**: Given ΔMSE≈0 from ablating 24/32 instruction-dominant heads, what concrete evidence supports the claim that these heads carry functionally important signals? What would falsify the null hypothesis that instruction routing is representationally present but computationally inert?

4. **Effective sample size**: The permutation test treats architecture-suite cells as independent, but cells from the same architecture share all model weights. With effective N=2, what is the actual statistical power of the exit collapse finding?

5. **Token overlap confound**: The ρ=1.0 Spearman correlation between Jaccard token overlap and Cohen's d across CF conditions suggests the model responds to lexical novelty, not semantic content. How do you distinguish instruction *understanding* from instruction *detection* in these perturbation experiments?

## Scores

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **Novelty** | **1/4** | No new methods, no new theoretical framework. Exit collapse may be a known fine-tuning effect (logit lens, representation distortion) in a new domain. The paper's own D090 finding and ΔMSE≈0 remove the most novel claims. |
| **Significance** | **1/4** | Findings are primarily descriptive, lack functional significance (ΔMSE≈0), and the paper's own evidence suggests the premise (instruction routing matters) is questionable. No actionable implications validated. |
| **Overall** | **4/10** | Below acceptance threshold. A competently executed study that honestly documents the failure of its own research premise. The transparency is commendable, but it does not compensate for the absence of findings that advance VLA understanding or design. |
| **Confidence** | **4/5** | I have read the paper and appendix thoroughly, am familiar with the interpretability methods used, and the paper's own evidence supports my assessment. |

## Recommendation: **Reject**

The paper is methodologically competent and admirably honest, but its contributions do not clear the CoRL acceptance bar. The exit collapse finding is the only surviving contribution after D090, and it is: (a) descriptive without mechanistic explanation, (b) not distinguished from format specialization, (c) lacking functional significance (ΔMSE≈0, non-significant behavioral correlation), (d) potentially a known phenomenon (logit lens / representation distortion) instantiated in VLAs, and (e) based on N=2 independent transitions. The paper's own evidence systematically undermines the premise that instruction routing is a productive research direction for current VLAs.

The authors should either: (1) pursue the format specialization explanation with the action_head_decoding data they already have, which would reframe exit collapse as a format-function dissociation finding; or (2) add behavioral validation demonstrating that exit collapse magnitude predicts task performance in a statistically powered comparison; or (3) connect to the representation distortion / logit lens literature and position exit collapse as a VLA instantiation of a known phenomenon, with the cross-architecture evidence as the specific contribution.
