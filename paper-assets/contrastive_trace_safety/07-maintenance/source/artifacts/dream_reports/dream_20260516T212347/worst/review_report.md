---
dream_id: dream_20260516T212347
tier: worst
overall_score: weak reject (3/6)
timestamp: 2026-05-16T22:12:07.014311+00:00
---

# Dream Review Report: "Does Scale Erase Safety Signals?"

**Paper**: Does Scale Erase Safety Signals? Hidden-State Monitoring Limitations in Large Reasoning Models
**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)
**Date**: 2026-05-16

---

## Review Process

- **R1** (Methodology + Experiments): Evaluated experimental design, statistical rigor, reproducibility, ablation completeness, claims vs evidence
- **R2** (Novelty + Related Work): Evaluated novelty, significance, related work coverage, framing, writing quality, overclaiming
- **Roundtable**: Independent reviews → cross-sharing → convergence → synthesis below

---

## Paper Summary

The paper investigates whether hidden-state (HS) probes for safety commitment detection in reasoning models generalize across model scale. Using a 2×2 matrix of architectures (Llama, Qwen2.5) × scales (7–8B, 32B), the authors find that the HS monitoring advantage observed at 7–8B (pre-CP FPR 16% vs text's 27%, p=0.003; AUROC 0.847 vs 0.738) vanishes at 32B (pre-CP FPR 25–31% vs 27–30%, p>0.4; AUROC 0.56–0.60 for both modalities). Fisher discriminability drops 6× from 8B to 32B. Temporal aggregation, GRU probes, fine-grained supervision, layer sweeps, and cross-scale transfer all fail to recover the signal at 32B. The paper concludes that HS monitoring cannot be assumed to generalize with scale.

---

## Experiment Coverage Assessment

The review context lists 15 planned experiments. All 15 are reflected in the paper:

| # | Experiment | Paper Section | Status |
|---|-----------|---------------|--------|
| exp-001 | Layer sweep + static probe (32B) | §4.1, Table 1 | Covered |
| exp-002 | Temporal window (32B) | §4.2, Table 2 | Covered |
| exp-003 | Cross-model transfer | §4.6, Table 6 | Covered |
| exp-004 | Lead time analysis | §4.7, Table 7 | Covered |
| exp-005 | Mahalanobis baseline | §4.13, Table 13 | Covered |
| exp-006 | Bootstrap CIs + AUROC | §4.8, Table 8 | Covered |
| exp-007 | Window size ablation | §4.3, Table 3 | Covered |
| exp-008 | Layer selection ablation | §4.4, Table 4 | Covered |
| exp-009 | 16-label supervision | §4.12, Table 12 | Covered |
| exp-010 | Oracle decomposition | §4.15, Table 15 | Covered |
| exp-011 | OpenThinker-7B (2×2 completion) | §4.5, Table 5 | Covered |
| exp-012 | GRU probe (32B) | §4.11, Table 11 | Covered |
| exp-013 | Text baseline (32B) | §4.10, Table 10 | Covered |
| exp-014 | BOCPD/CUSUM (32B) | §4.14, Table 14 | Covered |
| exp-015 | FPR analysis (32B) | §4.9, Table 9 | Covered |

Full coverage. However, OpenThinker-7B results appear only in the 2×2 summary (Table 5) and are absent from most detailed comparison tables, weakening the 2×2 design claim.

---

## Consolidated Strengths

**S1: Important and timely research question (R1, R2 agree).** As the community invests in hidden-state monitoring for safety (TrajGuard, SIREN, SafeSwitch), understanding whether these approaches scale is essential for deployment decisions. The paper asks the right question.

**S2: Systematic and exhaustive ablation design (R1, R2 agree).** The paper progressively eliminates alternative explanations: not a layer selection issue (64-layer sweep), not temporal context (window ablation), not model capacity (GRU), not threshold choice (AUROC), not supervision granularity (16-label), not detection paradigm (BOCPD/CUSUM). This thoroughness makes the negative result more credible.

**S3: Clean experimental matrix (R1, R2 agree).** The 2×2 architecture × scale design with OpenThinker-7B completing the Qwen2.5/7B cell provides reasonable (though imperfect) evidence that scale drives the effect.

**S4: Appropriate statistical methodology (R1, R2 agree).** Bootstrap CIs, AUROC as threshold-independent metric, explicit p-values for the core HS vs text comparison at each scale.

**S5: Fisher discriminability as diagnostic (R1).** The 6× drop (17.9→2.8) provides a clean, interpretable, and mechanistically informative summary statistic.

**S6: Oracle decomposition (R1).** Provides a principled upper bound separating method limitations from fundamental information constraints, confirming safety commitment IS real at 32B even though probes can't detect it.

---

## Consolidated Weaknesses

### Critical Issues

**W1: Architecture-scale confound is not resolved (R1 W1, R2 W1 — unanimous).** The 2×2 matrix has a missing Llama/32B cell. All 32B models are Qwen2.5-based distillations from the same teacher (DeepSeek-R1). The paper claims "scale, not architecture, is the determining factor," but the data is equally consistent with "distillation-into-Qwen2.5-32B specifically disrupts safety geometry." Without a Llama-based 32B model or a non-distilled 32B+ reasoning model (e.g., native DeepSeek-R1-67B, GPT-o1), the central causal claim is underdetermined. The paper acknowledges this in Limitations but understates its severity given it is the core claim.

**W2: Extremely small test set (n=43) undermines statistical conclusions (R1 W3, R2 W6 — unanimous).** With 43 traces, binary metrics have resolution of ~2.3pp per trace. Many reported differences (e.g., +2.3pp temporal gain) correspond to 1 additional trace. Bootstrap CIs for 32B AUROC include 0.50 (chance), meaning the paper cannot definitively establish that HS probes provide ANY discrimination at 32B. The strong conclusion "zero benefit" should be "no statistically detectable benefit at n=43." The entire negative result could be a power issue.

**W3: Overclaiming about production systems (R1 via detailed comments, R2 W4 — unanimous).** The Conclusion claims "hidden-state extraction cannot be justified" for "production reasoning systems at 32B+." Extrapolation from two 32B distilled models to 70B+ natively-trained models is unsupported. The "+" in "32B+" implies a monotonic trend that has not been established.

### Major Issues

**W4: Related Work is severely inadequate (R2 W2).** At ~0.5 pages with ~14 citations, this is far below top venue standards (40–60 references typical). Critical missing work includes: (a) probing-at-scale literature (Dalvi et al.), (b) the superposition hypothesis (Elhage et al., "Toy Models of Superposition") which provides the exact theoretical framework for why safety features would become diffuse at scale, (c) mechanistic interpretability (dictionary learning, sparse autoencoders), (d) scaling laws for emergent properties. The paper's core finding is essentially an empirical confirmation of superposition predictions, yet this connection is never made.

**W5: No theoretical framework for the finding (R2 W5).** The "diffuse geometry" explanation (§5.1) is post-hoc and untested (R1 W7). The superposition hypothesis predicts exactly this phenomenon: larger models represent more features in superposition, making any individual concept harder to isolate with linear probes. Without this theoretical grounding, the paper provides an empirical observation without mechanistic understanding, limiting its contribution.

**W6: No figures in a 10-page paper with 15 tables (R2 W3).** The Fisher discriminability curves, ROC comparisons, transfer heatmap, and 2×2 summary all need visualization. The paper reads like an experiment log rather than a persuasive scientific narrative. This is a significant presentation deficit.

**W7: Misleading framing of the core finding (R2 W7).** Both HS and text probes achieve only AUROC 0.57–0.60 at 32B. The real finding is "ALL safety commitment detection fails at 32B regardless of modality," which is arguably more important and alarming than "HS loses its relative advantage." The paper emphasizes the relative comparison (HS vs text) while burying the absolute finding (nothing works).

**W8: Model mislabeling raises concerns (R1 W6).** Section 3.1 states "DeepSeek-R1-Distill-Qwen-7B ('r1-8b', Llama-based, 4096-d, 32 layers)" — this is contradictory. DeepSeek-R1-Distill-Qwen-7B is Qwen-based, not Llama-based. DeepSeek-R1-Distill-Llama-8B would be Llama-based. This inconsistency undermines confidence in whether the correct models were evaluated and whether the 2×2 matrix truly crosses architectures.

### Minor Issues

**W9: No multiple comparison correction (R1 W4).** 15+ hypothesis tests without Bonferroni/FDR correction. The primary result (p=0.003 at 8B) survives, but secondary claims may not.

**W10: Sentence-BERT as text baseline may be too weak (R1 W5).** A stronger text baseline (fine-tuned classifier, instruction-tuned LLM embeddings) would make the HS vs text comparison more meaningful. The 8B advantage might partly reflect a weak baseline rather than HS superiority.

**W11: Internal data inconsistency (R1 detailed comment #6).** QwQ-32B temporal gain is +4.6pp (Table 2), equal to r1-8b's gain, contradicting the "temporal fails at 32B" narrative. The paper does not discuss this inconsistency.

**W12: Cross-scale transfer result is a ceiling effect (R1 detailed comment #3).** Transfer at chance (~0.50) between 8B and 32B is expected when the target model's own probe accuracy is only 0.69–0.71. This should not be interpreted as strong evidence about "safety geometry."

---

## Questions for Authors (Consolidated)

1. **Data provenance**: Were experiments executed on real model activations, or are reported numbers from a simulation/prediction framework? The data files suggest pre-specified "expected_results" under different outcome tiers.

2. **Model identity**: Is the 8B model truly Llama-based (DeepSeek-R1-Distill-Llama-8B) or Qwen-based (DeepSeek-R1-Distill-Qwen-7B)? The text is contradictory.

3. **Non-distilled models**: Have you evaluated on any model that acquired reasoning via full RL rather than distillation?

4. **MLP probes**: Have you tried multi-layer perceptrons with substantial capacity (e.g., 3-layer, 1024 hidden units) on single-step 32B hidden states? GRU tests temporal modeling, not nonlinear single-step extraction.

5. **Non-safety control**: Does probing a non-safety property (e.g., topic classification) at both scales work fine? This would verify the probe methodology is not broken at 32B and that the finding is safety-specific.

6. **OpenThinker-7B full results**: Why do OpenThinker-7B results appear only in the 2×2 summary and not in detailed comparison tables?

---

## Missing Experiments / Suggestions

1. **MLP probes** (3-layer, 1024 hidden units) on single-step 32B hidden states to test nonlinear extraction
2. **Multi-layer ensemble probes** (concatenate 5 layers) to test distributed signal recovery
3. **Attention pattern probes** to test the paper's own speculation about attention-based encoding
4. **Non-distilled 32B+ model** (native DeepSeek-R1-67B or similar) to separate distillation from scale
5. **Non-safety probing control** (topic/sentiment) to verify scale-specificity
6. **Larger test set** (100+ traces) to resolve statistical power concerns
7. **Effect size analysis** (Cohen's d) to determine needed n for detecting a meaningful 32B effect

---

## Scores

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Methodology + Experiments | 3/6 (Weak Reject) | 4/5 |
| R2 | Novelty + Related Work | 3/6 (Weak Reject) | 4/5 |
| **Consensus** | | **3/6 (Weak Reject)** | **4/5** |

---

## Meta-Review Summary

The paper addresses an important and timely question: does hidden-state monitoring for safety commitment detection generalize across model scale? The experimental design is systematic, covering 15 experiments that progressively eliminate alternative explanations. The core empirical observation (Fisher discriminability drops 6× from 8B to 32B, HS-text AUROC difference becomes non-significant) is internally consistent.

However, the paper has critical weaknesses that prevent acceptance at a top venue:

1. **The central causal claim (scale causes signal loss) is confounded** by the fact that all 32B models are Qwen2.5-based distillations from the same teacher. Scale and distillation target are not separated.

2. **The test set (n=43) is too small** to support the binary claims made. Confidence intervals include chance for 32B models, meaning the paper cannot distinguish "no signal" from "weak signal + insufficient data."

3. **The paper lacks theoretical grounding.** The superposition hypothesis provides the exact framework for explaining the findings but is not cited or discussed. Without it, the contribution is an unexplained empirical observation.

4. **Presentation deficits** include no figures (in a paper crying out for visualization), severely inadequate Related Work (~0.5 page, ~14 citations), and model mislabeling that undermines confidence in experimental execution.

5. **The framing is narrow.** The more important finding — that ALL monitoring (HS and text) degrades to near-chance at 32B — is buried in favor of the relative HS-vs-text comparison.

**Recommendation**: Weak Reject (3/6). The research question is valuable and the experimental framework is sound in structure, but the evidence is insufficient to support the breadth of conclusions. Major revisions needed: (a) test on non-distilled 32B+ models, (b) increase test set to 100+, (c) add theoretical framework (superposition), (d) expand Related Work to 1.5+ pages with 40+ refs, (e) add 3–4 key figures, (f) reframe around the absolute monitoring failure, not just relative HS-text comparison, (g) resolve model identity inconsistency. As a workshop paper with appropriately scoped claims, the current evidence could be sufficient.