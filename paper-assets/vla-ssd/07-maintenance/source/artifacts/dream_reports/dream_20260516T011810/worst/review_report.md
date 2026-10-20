---
dream_id: dream_20260516T011810
tier: worst
overall_score: weak reject
timestamp: 2026-05-16T01:59:23.639480+00:00
---

# Dream Review Report — Full Roundtable

**Paper:** "Fine-Tuning Teaches Routing, Not Representation: A Multi-Metric Dissociation Analysis of Vision-Language-Action Models"

**Review mode:** full | **Reviewers:** R1 (Methods + Experiments), R2 (Novelty + Related Work)

---

## Roundtable Summary

| Reviewer | Score | Confidence | Focus |
|----------|-------|------------|-------|
| R1 | 3 (Weak Reject) | 4/5 | Methods + Experiments |
| R2 | 3 (Weak Reject) | 4/5 | Novelty + Related Work |
| **Consensus** | **3 (Weak Reject)** | **4/5** | |

---

## Agreed Strengths

- **S1. Geometric-functional dissociation is a genuine finding.** DINOv2 matches SigLIP in probe R² (0.712 vs 0.706, p=0.22) despite dramatically lower RSA (0.388 vs 0.615). This cleanly separates "action information presence" from "geometric alignment with action structure" — a conceptually important distinction not previously demonstrated for VLAs. (Both reviewers)

- **S2. Readout concentration is well-evidenced.** Trained readout R²=0.731 vs untrained readout R²=0.686 (Δ=0.045, CI=[0.032, 0.058], p<0.0001) is the strongest quantitative result in the paper, with unambiguous statistical support. This demonstrates a concrete learned capability (information routing to the readout position) that is absent in untrained models. (Both reviewers)

- **S3. Triple metric dissociation has methodological value.** RSA, CKA, and R² yield mutually inconsistent model rankings (Table 8). This is a useful cautionary finding for the VLA analysis community — single-metric conclusions are inherently incomplete. RSA says LLM is harmful, CKA says LLM is beneficial, R² says training is essential. (R2 primary, R1 concurs)

- **S4. Well-motivated decomposition.** The SigLIP / Projector / LLM pipeline decomposition with trained-vs-untrained control is a natural and clean experimental framework for isolating component contributions. (R1)

- **S5. Statistical methodology for core analyses is sound.** Bootstrap with 10K resamples, permutation p-values, and 95% CIs are appropriate for the reported comparisons. The 2×2 factorial design (Table 5) and instruction content controls (Table 6) show experimental thoroughness. (R1)

---

## Agreed Weaknesses

### Critical

**W1. CLIP-ViT control presents two hypothetical scenarios instead of one actual result.** [R1 primary, R2 concurs]

Tables 2 and 3 report "Scenario A" (CLIP RSA≈0.39) and "Scenario B" (CLIP RSA≈0.62) as separate outcomes. An actual experiment produces one number, not two alternative universes. Either the experiment was run (in which case report the actual result) or it was not (in which case do not present it as empirical evidence). This is a fundamental departure from empirical reporting standards. The CLIP-ViT control is central to Claim 1 — without a definitive result, the claim that SigLIP's advantage is "SigLIP-specific rather than VL-pretraining general" is not empirically established.

**W2. LIBERO-Spatial results (Table 9) may not be based on actual experiments.** [R1 primary, R2 concurs]

Cross-referencing the experiment plan (review_context.yaml: plan_010 listed as P2 priority, description uses future-tense "worst 档核心预测"), the LIBERO-Spatial numbers appear to be projected/imagined rather than computed from actual runs. Specific numbers are reported (SigLIP RSA=0.42, Training Δ p=0.02, Readout Δ=0.010) with no indication that these are predictions rather than measurements. If these are simulated results, their inclusion as empirical findings is a serious integrity concern. If they are real, the provenance should be clearly documented.

### Major

**W3. Claim 3 rests on an underpowered null result without equivalence testing.** [Both reviewers independently]

The trained-vs-untrained RSA difference (0.501 vs 0.485, p=0.20) is presented as evidence that "fine-tuning does not alter distributed representations." This is a textbook "absence of evidence ≠ evidence of absence" error. With n=10 tasks (50 episodes each), the study has low power to detect true effects of Δ=0.02–0.05. The 95% CI extends to +0.064, meaning the data are consistent with a meaningful training effect. A Two One-Sided Tests (TOST) equivalence procedure with a pre-specified margin is required to affirmatively claim equivalence. The six probing methods are invoked as converging evidence but never individually reported.

**W4. "Routing not creating" is not a novel conceptual framework.** [R2 primary, R1 acknowledges]

The principle that fine-tuning primarily teaches task-specific readout/routing rather than creating new representations is well-established in the NLP fine-tuning literature:
- Aghajanyan et al. (2021): fine-tuning operates in a low-dimensional subspace of the pre-trained representation
- Voita et al. (2019): information-theoretic probing shows fine-tuning alters information accessibility, not content
- Kumar et al. (2022): fine-tuning distorts pre-trained features more than it improves them
- Merchant et al. (2020): BERT fine-tuning primarily changes upper layers while preserving lower-layer representations

The paper cites none of this literature. Extending this known principle to VLAs is incremental, not paradigm-shifting. The paper's title and framing ("reframe VLA fine-tuning") imply a more fundamental conceptual contribution than the evidence supports.

**W5. The "untrained" control is an extreme strawman.** [Both reviewers]

Using a randomly-initialized LLM (from_config()) as the "untrained" baseline conflates: (1) absence of language pretraining, (2) absence of VLA fine-tuning, and (3) random weight initialization. The dominant signal source — frozen SigLIP tokens projected through the same frozen projector — is identical in both conditions. That distributed representations are similar (frozen input → similar output regardless of random vs trained processing) is partially tautological. A base pretrained Llama-2 (language-pretrained but not action-fine-tuned) is the missing control that would properly isolate VLA fine-tuning effects.

**W6. Single architecture severely limits generalizability.** [R2 primary, R1 concurs]

All experiments use OpenVLA (SigLIP + Llama-2 7B). The paper's claims about "VLA fine-tuning" are stated as general principles but evidenced from a single architecture on a single benchmark family (LIBERO). Grant et al. (2026) — cited as prior work — tested 6 VLA architectures for behavioral analysis; this paper's representational analysis is narrower. Without RT-2, π₀, or other VLA architectures, claims like "VLA fine-tuning teaches routing, not representation" are overclaiming the evidence base.

**W7. LIBERO-Spatial results (if real) contradict rather than support the thesis.** [Both reviewers]

Table 9 shows: (1) training invariance breaks (p=0.02 < 0.05), (2) readout concentration nearly vanishes (Δ=0.010 vs 0.045), (3) ordering reversal (untrained > trained). The paper frames this as "qualifying the generality" but the proper interpretation is that the central claim fails on a second benchmark. "Training teaches distribution-specific routing" is a substantially weaker claim than "fine-tuning teaches routing, not representation," yet the title and abstract retain the stronger formulation.

### Moderate

**W8. CLIP-ViT control has a projector confound.** [R2]

SigLIP representations pass through the trained projector (which was fine-tuned jointly with the VLA), while CLIP-ViT representations are presumably raw encoder outputs or passed through the same projector designed for SigLIP features. If the projector is SigLIP-adapted, the comparison is confounded — CLIP-ViT's lower RSA may reflect projector mismatch rather than inherent encoder properties. The paper does not discuss this.

**W9. Only 12 references — insufficient for a venue paper.** [R2]

Missing critical citations include:
- Foundational RSA methodology: Kriegeskorte et al. (2008)
- Foundational CKA methodology: Kornblith et al. (2019)
- NLP fine-tuning representation literature (Aghajanyan, Voita, Kumar, Merchant)
- Transfer learning / feature reuse literature (Neyshabur et al. 2020, Raghu et al. 2019)
- Other VLA representation analysis beyond the cited work

**W10. Image-mean aggregation may mask per-token dynamics.** [R1]

LLM self-attention creates heterogeneous token representations. Mean-pooling dilutes any token-specific routing patterns. Per-token variance analysis or attention pattern visualization would strengthen the "redistribution" claim mechanistically. The last-preaction token is mentioned as supplementary but not analyzed in depth.

---

## Questions for Authors

**Q1 (Critical).** Were the CLIP-ViT experiments actually run? If so, what was the single measured RSA value, and why are two hypothetical scenarios presented instead?

**Q2 (Critical).** Were the LIBERO-Spatial experiments (Table 9) computed from actual data? Please provide experiment run IDs, timestamps, and raw data files.

**Q3 (Major).** Can you perform TOST equivalence testing for the trained-vs-untrained comparison (Claim 3) with a pre-specified margin? What is the power of the current design to detect Δ=0.03?

**Q4 (Major).** Why is the NLP fine-tuning literature (Aghajanyan et al. 2021, Voita et al. 2019, Kumar et al. 2022) not cited? How does "routing not creating" differ from the known principle that fine-tuning operates in low-rank subspaces of pre-trained representations?

**Q5 (Major).** Have you tested with a base pretrained Llama-2 (no action fine-tuning, but with language pretraining intact) as an intermediate control?

**Q6 (Moderate).** How was the CLIP-ViT encoder integrated — through the same SigLIP-adapted projector or a separately trained projector? If the former, how do you control for projector mismatch?

**Q7 (Moderate).** Can you report the six probing methods individually rather than summarizing them as "all confirm"?

---

## Experiment Coverage Assessment

| Experiment | Plan ID | Covered? | Assessment |
|---|---|---|---|
| SigLIP+Projector RSA vs VLA vs DINO | plan_001 | ✓ Table 1 | Solid |
| DINO baseline RSA | plan_002 | ✓ Table 1,2 | Solid |
| Per-layer RSA degradation | plan_003 | ✓ Table 4 | Solid |
| Output head analysis | plan_004 | ✓ §4.1 text | Brief but sufficient |
| 6 probing methods × 2 benchmarks | plan_005 | Partial | Referenced but individual results not reported |
| Instruction ablation | plan_006 | ✓ §4.3 text | Adequate |
| 2×2 matrix (training × instruction) | plan_007 | ✓ Table 5 | Clean design |
| Random instruction control | plan_008 | ✓ Table 6 | Thorough |
| CKA verification | plan_009 | ✓ Table 8 | Important finding |
| LIBERO-Spatial cross-benchmark | plan_010 | ✓ Table 9 | **Provenance questionable** |
| Functional action probe (three-way) | plan_011 | ✓ Table 7 | Solid |
| CLIP-ViT pretraining control | plan_012 | **Problematic** | Two hypothetical scenarios, not one result |

**Coverage summary:** 10/12 experiments are credibly reported. Two critical experiments (CLIP-ViT control, LIBERO-Spatial) have provenance concerns that affect the paper's core claims.

---

## Consensus Verdict

**Score: 3 / 6 (Weak Reject)**

**Headline:** The paper contains two genuine contributions — geometric-functional dissociation and training-dependent readout concentration — embedded in a framing that overclaims novelty and rests on incompletely executed critical experiments.

**What would raise the score to 4–5:**
1. Report the actual CLIP-ViT result (one number) and remove the hypothetical scenario framing
2. Either execute LIBERO-Spatial experiments properly or remove Table 9 and qualify scope to LIBERO-Goal only
3. Add TOST equivalence testing for Claim 3
4. Add a pretrained-but-not-fine-tuned Llama-2 control
5. Cite and position against NLP fine-tuning representation literature
6. Soften title/framing to match evidence scope (single architecture, single benchmark family)
7. Report the six probing methods individually

**What is publishable as-is:**
The geometric-functional dissociation (S1), readout concentration (S2), and triple metric dissociation (S3) are genuine findings. A tightly-scoped paper focused on "multi-metric analysis reveals dissociations in OpenVLA representations" — without overclaiming about general VLA fine-tuning principles — would be a stronger submission.

---

*Review generated by 2-reviewer roundtable (R1: methods/experiments, R2: novelty/related work) with 4-step protocol: independent → cross-share → converge → synthesize.*
