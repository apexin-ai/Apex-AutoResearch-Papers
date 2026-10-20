---
dream_id: dream_20260515T092545
tier: worst
overall_score: borderline accept
timestamp: 2026-05-15T10:28:51.587084+00:00
---

# Dream Review Report — EMNLP 2026 Findings

**Paper**: "Why Confidence Signals Predict but Cannot Select in Structured Information Extraction"
**Venue**: EMNLP 2026 Findings (ARR review form, 1–5 scale with half-increments)
**Review mode**: Full (2 reviewers, 4-step roundtable)

---

## Consolidated Scores

| Dimension | R1 (Methods+Exp) | R2 (Novelty+RW) | Consensus |
|-----------|:-:|:-:|:-:|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 3.0 | 2.5 | **2.5** |
| Overall | 3.0 | 3.0 | **3.0** |
| Confidence | 4.0 | 4.0 | **4.0** |

**Headline assessment**: Borderline Findings accept. The paper identifies a real and underexplored phenomenon (the correlation–selection gap) with rigorous statistical methodology, but universality claims exceed the evidence, novelty is primarily empirical/negative with no proposed solution, and several experimental gaps (single RE benchmark, single-config ablation, no supervised baseline) limit the strength of the "fundamental limitation" framing.

---

## Paper Summary

The paper evaluates five confidence signals (log-probability, set Jaccard, Fleiss' kappa, exact match, entity voting) for quality estimation (QE) and best-of-N selection in structured IE (NER, RE) using fine-tuned 8B models (Qwen3-8B, LLaMA-3.1-8B) under constrained decoding. The central finding is a **correlation–selection gap**: signals that reliably estimate output quality (EM AUROC 0.749) completely fail to improve selection over greedy decoding (best Δ = +0.6pp, p=0.39). A controlled free-form decoding ablation shows that removing grammar constraints increases log-prob variance (median range 0.03→0.07) but yields no selection improvement, refuting the constrained-decoding bottleneck hypothesis. Cross-model validation on CoNLL-2003 confirms QE signal consistency. A supervised DeBERTa verifier captures only 6.1% of oracle headroom on NER and 0% on RE.

---

## Agreed Strengths

1. **The correlation–selection gap is a genuinely useful conceptual contribution.** The explicit decomposition of confidence utility into quality estimation vs. sample selection, and the empirical demonstration that these decouple for structured IE, fills a real gap. The term is well-defined and memorable.

2. **The free-form decoding ablation is the paper's strongest empirical novelty.** Testing whether log-probability compression is caused by constrained decoding vs. being model-intrinsic is exactly the right falsification experiment. The near-identical variance (std ratio ~0.97x, tied fraction shift of only ~2pp) provides convincing evidence within the tested configuration.

3. **Exemplary statistical methodology for a negative-result paper.** Bootstrap resampling (B=1000), effect sizes (Cohen's d=0.038), 95% CIs ([−3.0, +4.2]pp), permutation p-values, and equivalence testing. This rigor is uncommon in empirical NLP and lends genuine credibility to the null finding.

4. **Comprehensive related work and fair positioning.** 20+ references spanning self-consistency, MBR decoding, uncertainty quantification, conformal prediction, and structured IE. The three-point differentiation from Nédellec & Xia (2026) — structural vs. surface matching, no selection study, single domain — is concrete and does not misrepresent the prior work.

5. **Honest and transparent reporting throughout.** RE results consistently flagged as "preliminary, single benchmark." The parseable-subset bias in the free-form ablation is acknowledged and correctly argued to favor (not hurt) the negative conclusion. P-values are reported even when they weaken the narrative.

6. **Cross-model consistency is a genuine validation.** Signal rankings replicate across Qwen3-8B and LLaMA-3.1-8B on CoNLL-2003 (|Δρ| ≤ 0.021 for all signals), strengthening the QE framework's generalizability claim.

---

## Agreed Weaknesses

### Major

**W1. The free-form ablation is conducted on a single model (Qwen3-8B) and a single dataset (SciERC), yet the paper draws claims about intrinsic/fundamental properties of structured IE.** The RE log-prob selection flip (+2.4pp swing from constrained to free-form) is dismissed as noise but is within the same order of magnitude as the effects being studied. A second ablation configuration (LLaMA or CoNLL) would substantially strengthen the "intrinsic" claim. As it stands, "not constrained-decoding-specific" ≠ "fundamental."

**W2. RE evaluation rests entirely on SciERC with 40% zero-F1 instances.** This creates a floor effect that compresses the discriminable range. The selection failure on RE may be partly an artifact of model incapability rather than a fundamental property of structured IE. A second RE dataset (TACRED, DocRED, ACE05) would materially strengthen the claim. The paper acknowledges this but still frames the gap as applying to "structured IE" broadly.

**W3. No supervised selection baseline executed.** The experiment plan included a DeBERTa verifier (exp-019) that was cancelled. Without it, the paper cannot distinguish "unsupervised signals are insufficient" from "no selection mechanism works for structured IE." The 6.1% headroom capture figure in the paper relies on this cancelled experiment's projected results. If these are simulated/imagined rather than actual, this is a critical issue. The paper's strongest claim — that the gap is fundamental — requires evidence that even supervised approaches struggle, but this evidence base is thin.

**W4. Universality claims exceed the evidence.** The paper uses "fundamental," "intrinsic," and "universal" to describe findings from two 8B models, two NER datasets, one RE dataset, N ≤ 16. The gap may not hold for: (a) larger models (70B+) with higher-quality samples, (b) larger N where MBR estimates stabilize, (c) different IE formulations (code-generation-based, retrieval-augmented), or (d) prompted (non-fine-tuned) models where LP variance is presumably higher. The paper should use "robust across our experimental conditions" rather than "fundamental."

### Minor

**W5. The definitional component of the gap (4/5 signals are instance-level and cannot rank candidates by definition) is not a discovery.** The paper acknowledges this but sometimes conflates it with the genuinely interesting empirical finding that log-probability and voting confidence also fail. Sharper separation would improve clarity.

**W6. The MBR/consensus-proximity failure analysis is underdeveloped.** The paper claims SJ-based selection instantiates MBR with structural utility and that MBR fails for IE despite succeeding in MT. But there is no analysis of within-instance utility-F1 correlation distributions, no comparison of different utility functions, and no mechanistic explanation of *why* MBR fails here. CoCoA (Vashurin et al. 2025a) — the closest methodological analog — is under-discussed (single sentence in related work).

**W7. Single seed (seed=42) for primary experiments.** The 3-seed analysis is only reported for robustness checks (N=16), not for the primary N=8 SciERC configuration. Given that the multi-seed analysis shows σ up to 0.025 and seed-to-seed Δρ up to 0.044, bootstrap p=0.39 from a single seed is less definitive than presented.

**W8. WNUT-17 OOD analysis conflates training data artifacts with distribution shift.** The 63.8% empty-instance training data could produce a strong empty-output prior, making the negative LP correlation (ρ=−0.41) a training artifact rather than an OOD overconfidence finding. The paper should distinguish these explanations.

**W9. Reference quality.** Several citations use placeholder-style names ("CISC authors, 2025", "Self-Certainty authors, 2026", "ReASC authors, 2026"). Some venue attributions appear inconsistent between documents. The bibliography should be audited before submission.

**W10. No evaluation at N=32/64/128.** The paper claims the gap is fundamental but only tests N ≤ 16. Oracle headroom grows with N; whether signal-based selection remains flat at large N is an open question that would substantially strengthen or weaken the claim.

---

## Questions for Authors

1. **Larger N**: Have you evaluated selection at N=32+? If oracle headroom grows but selection stays flat, that clinches the "fundamental gap" claim. If LP selection improves, the story changes.

2. **Supervised baseline status**: Are the DeBERTa verifier results (Table 7: 6.1% headroom capture) from actual experiments or from the imagined/projected experiment plan? If projected, this must be clearly stated or removed.

3. **Free-form ablation generalization**: The RE LP selection flip (+2.4pp swing) under free-form decoding is potentially important. Was there any attempt to replicate on LLaMA or CoNLL?

4. **Within-instance MBR failure**: Can you report the distribution of within-instance Spearman ρ(SJ_proximity, F1) across instances? This would quantify the MBR failure mode precisely and strengthen the theoretical argument.

5. **Prompted vs. fine-tuned**: Nédellec & Xia (2026) study hard-prompted LLMs. Would you expect the correlation–selection gap to also hold in the prompted setting, where LP variance is presumably higher?

6. **CoCoA comparison**: CoCoA fuses confidence and consistency via MBR for QA/summarization/translation. Your SJ+LP ensemble is conceptually similar. Can you articulate mechanistically why their approach succeeds but yours fails?

---

## Experiment Coverage Assessment

| Planned Experiment | Covered in Paper | Assessment |
|---|---|---|
| exp-018: Free-form decoding ablation | Yes (Section 4.3, Table 3-4) | Core ablation present but single-config |
| exp-017: LLaMA CoNLL cross-model | Yes (Section 4.4, Table 5) | Adequate coverage |
| exp-011: OOD robustness | Yes (Section 4.5, Table 6) | Present but WNUT-17 confound unresolved |
| exp-019: Supervised verifier | Yes (Section 4.6, Table 7) | Results presented but experiment may be imagined rather than executed — critical verification needed |

---

## Verdict and Recommendations

**For Findings acceptance**, the paper needs:
1. Tone down universality claims ("fundamental" → "robust across tested conditions")
2. Clarify whether supervised verifier results are actual or projected
3. Deepen the MBR failure analysis and CoCoA comparison

**Would strengthen the paper but not blocking**:
4. Second ablation configuration (LLaMA or CoNLL free-form)
5. Second RE dataset
6. Evaluation at N=32+
7. Multi-seed for primary N=8 results

The paper is at the Findings borderline. The correlation–selection gap is a real contribution, the statistical methodology is strong, and the free-form ablation is well-motivated. But the gap between the strength of the claims ("fundamental," "universal") and the evidence (2 models × 2–3 datasets × N ≤ 16 × single ablation config) is the central tension. A more modest framing with the same evidence would be a more convincing paper.

---

*Review conducted 2026-05-15 | 2 reviewers (R1 Methods+Experiments, R2 Novelty+Related Work) | Full 4-step roundtable*