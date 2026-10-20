---
dream_id: dream_20260516T092241
tier: worst
overall_score: 3.0 — Findings-level (borderline Main reject)
timestamp: 2026-05-16T10:30:25.769048+00:00
---

# Dream Review Report — EMNLP 2026 Main Conference

**Paper**: "When Does Multi-Sample Selection Help Structured IE? A Diagnostic Study of Output Convergence"
**Venue**: EMNLP 2026 Main Conference
**Review Mode**: Full (2 Reviewers, 4-step roundtable)
**Date**: 2026-05-16

---

## Venue Calibration

Scoring follows the ACL Rolling Review / EMNLP 2026 scale:
- **Overall Assessment** (1–5): 5 = Award (top 2.5%), 4 = Main Conference, 3.5 = Main/Findings borderline, 3 = Findings, 2.5 = Findings borderline, 2 = Resubmit next cycle, 1 = Do not resubmit
- **Soundness** (1–5), **Excitement** (1–5), **Reproducibility** (1–5)
- EMNLP Main acceptance rate: ~22–25%

Sources: [ARR Review Form](http://aclrollingreview.org/reviewform), [ARR Reviewer Guidelines](http://aclrollingreview.org/reviewerguidelines), [EMNLP 2025 Reviewer Instructions](https://2025.emnlp.org/reviewer/instructions/)

---

## Final Consensus Scores

| Dimension | R1 (Methods) | R2 (Novelty) | Consensus |
|-----------|:---:|:---:|:---:|
| **Overall Assessment** | 3.5 | 3.0 | **3.0** |
| **Soundness** | 3.5 | 3.0 | **3.5** |
| **Excitement** | 3.0 | 2.5 | **2.5** |
| **Reproducibility** | 4.0 | 4.0 | **4.0** |

**Recommendation**: Findings-level paper. Solid empirical contribution with publishable insights, but falls short of the EMNLP Main novelty and impact bar.

---

## Roundtable Narrative

### Step 1: Independent Reviews

**R1 (Methods + Experiments)** scored 3.5/5, finding the experimental design competent with the LoRA rank ablation as a clean, well-controlled contribution. Key concerns centered on missing ablations (N, T, epoch, additional LoRA rank points), absence of aggregation baselines (MBR, majority voting), uncorrected multiple comparisons, and small practical effect sizes (Cohen's d ~ 0.15–0.17).

**R2 (Novelty + Related Work)** scored 3.0/5, identifying the QE-vs-selection decoupling as the strongest novel finding but judging overall novelty as incremental. The conditional answer ("selection depends on output diversity") is partially anticipated by Brown et al. (2024) and Snell et al. (2024). Prescriptive guidelines rest on only two positive data points. Related work misses mode collapse, diverse decoding, and LoRA theory literature.

### Step 2: Cross-Sharing

R1 flagged to R2 that the fixed N=8 and T=1.0 throughout all experiments is a notable gap given the paper's central thesis is about output diversity — one would expect ablations on exactly the parameters that control diversity (N, T). R2 flagged to R1 that the "regime-dependent" framing, while useful, is not deeply novel — the TTS literature already implicitly conditions on output diversity. Both agreed the paper's genuine contribution is the structured IE–specific diagnosis (degeneracy + LP compression mechanisms), not the high-level conditional framing.

### Step 3: Convergence

**Points of agreement:**
1. The LoRA rank ablation (Section 6.4) is the paper's strongest experiment and most convincing causal evidence
2. The QE-vs-selection decoupling (QE is signal-intrinsic, selection is regime-dependent) is the most novel insight
3. Prescriptive guidelines (Table 9) are under-supported — only 2 of 6 conditions show significant positive selection, and both are "mild FT" conditions
4. Effect sizes are small (d=0.15–0.17) and need explicit contextualization against the 8× inference cost
5. Statistical rigor has gaps: ~30 implicit comparisons without correction; Fisher combined p=0.085 is borderline
6. The paper is well-written, well-organized, and reproducibility is good
7. Scope is narrow for Main Conference: one primary model family (Qwen3), English only, LoRA-only fine-tuning

**Disagreement resolved:**
R1's initial 3.5 reflected appreciation for the experimental methodology; R2's 3.0 reflected the novelty ceiling. After cross-sharing, R1 acknowledged that the missing N/T ablations undercut the diversity thesis more than initially weighted, while R2 acknowledged the LoRA rank ablation is methodologically stronger than typical empirical studies. Both converged to 3.0 overall — a solid Findings paper that does not clear the Main Conference novelty + impact threshold.

### Step 4: Consolidated Assessment

---

## Strengths

**S1: Clean causal ablation via LoRA rank (Major).** The rank=16 vs. rank=8 comparison on SciERC is the paper's strongest contribution. Same model, same data, same training epochs — only the rank differs. This cleanly isolates fine-tuning intensity as a convergence driver: degeneracy drops from 21% to 5.2% while F1 decreases only 3.9pp. LP selection flips from non-significant (+0.6pp, p=0.39) to significant (+3.6pp, p=0.015). This is a well-controlled experiment rare in empirical NLP studies.

**S2: QE-vs-selection decoupling is a genuine insight.** The finding that SJ ρ is stable across rank configurations (0.360→0.378) while LP selection gap changes dramatically (+0.6→+3.6pp) is a crisp, previously unarticulated result. It implies that confidence signals are always useful for flagging uncertain instances (QE), even when they cannot improve selection — a practical distinction for system designers.

**S3: Systematic multi-signal, multi-dataset evaluation.** Five confidence signals × four NER datasets + one RE dataset × three model configurations, with cross-seed evaluation on SciERC and Few-NERD. The experimental matrix is broader than typical single-dataset studies. Cross-model validation (LLaMA-3.1-8B on CoNLL) and cross-scale validation (Qwen3-4B) add credibility.

**S4: Two well-characterized failure mechanisms.** Instance degeneracy (identical outputs across samples) and LP compression (compressed score ranges) are clearly defined, empirically grounded, and mechanistically interpretable. The free-form decoding ablation confirming LP compression is model-intrinsic (not a JSON artifact) is a nice control experiment.

**S5: Honest, well-organized presentation.** The paper clearly states five limitations, reports both positive and null results, includes p-values throughout, and provides prescriptive guidelines. The pivot from "universal failure" to "conditional effectiveness" is transparently presented. The paper is well-structured across 10 sections within the page limit.

## Weaknesses

**W1: No ablation on N or T — the parameters most relevant to the diversity thesis (Major).** The entire paper argues that output diversity determines selection effectiveness, yet N is fixed at 8 and T is fixed at 1.0 throughout. How does selection gain scale with N=2, 4, 16, 32? Does T=0.8 or T=1.2 shift the convergence regime? These are the most natural experiments given the paper's thesis, and their absence is conspicuous. The review context YAML shows no N or T ablation was even planned.

**W2: Prescriptive guidelines rest on thin evidence (Major).** Table 9's decision matrix — the paper's headline practical contribution — derives from only two statistically significant positive results: Few-NERD (+3.2pp, p=0.028) and SciERC rank=8 (+3.6pp, p=0.015). Both are "mild FT" conditions on the same model family (Qwen3-8B). The thresholds (degeneracy <10%, LP range >0.07 nats) are inferred from 4–6 data points with no held-out validation. This is insufficient to constitute reliable practitioner guidelines. The 10%/0.07 cutoffs look like they were reverse-engineered from the data rather than derived from principled analysis.

**W3: Multiple comparisons uncorrected (Moderate).** The paper tests ~30 signal×dataset×condition combinations. The two headline p-values (0.028, 0.015) are individually significant at α=0.05 but would not survive Bonferroni or even Benjamini-Hochberg correction across the full comparison family. Fisher combined p=0.085 for SJ>LP (NER) is borderline even without correction. The paper does not discuss this.

**W4: Small effect sizes vs. 8× inference cost (Moderate).** Cohen's d values of 0.152 (Few-NERD) and 0.168 (SciERC rank=8) represent small effects. The selection gains of 3–4pp come at the cost of generating 8 samples per instance (8× inference). The paper does not discuss this cost-benefit tradeoff. At what point does the marginal F1 gain justify the compute?

**W5: Limited novelty — conditional answer is partially anticipated (Moderate).** The finding that sample selection works when outputs are diverse is implicitly present in Brown et al. (2024) and Snell et al. (2024) for reasoning tasks. The paper's contribution is demonstrating this specifically for structured IE and diagnosing the mechanisms, but the high-level insight is not surprising. The QE-selection decoupling (S2) is more novel than the regime-dependent framing itself.

**W6: Missing aggregation baselines (Moderate).** Only best-of-N selection is evaluated. Majority voting adapted for structured outputs (e.g., entity-level voting), MBR decoding with set-valued utility functions, and union/intersection strategies are all natural alternatives. Without these, the paper cannot claim that "no unsupervised signal outperforms greedy" — only that no signal achieves it via the best-of-N paradigm.

**W7: Cross-model validation absent in the favorable regime (Minor).** Cross-model validation (LLaMA) is only performed on CoNLL (high-convergence regime where selection fails). There is no cross-model check in the low-convergence regime (Few-NERD or rank=8-equivalent), leaving open whether the positive selection results generalize beyond Qwen3-8B.

**W8: LoRA rank ablation covers only 2 points on 1 dataset (Minor).** Rank=16 vs. rank=8 on SciERC is a single comparison. Additional points (rank=4, 32, 64) and replication on another dataset would establish whether the degeneracy-rank relationship is monotonic and generalizable. An epoch ablation (1, 2, 3, 4, 5 epochs on SciERC at rank=16) would help disentangle epoch count from rank as convergence drivers.

**W9: Related work gaps (Minor).** Missing: (a) output diversity / mode collapse in LLMs (Holtzman et al. 2020; Kirk et al. 2024); (b) deeper engagement with MBR decoding beyond Eikema & Aziz 2022 (Freitag et al. 2023); (c) LoRA theory explaining why lower rank preserves diversity (Hu et al. 2022 analysis of rank and expressivity); (d) diverse decoding strategies (nucleus sampling variants, typical decoding) as alternatives to LoRA rank reduction for controlling diversity.

## Questions for Authors

**Q1.** Have you explored any N or T ablation? Even a small-scale experiment (e.g., N=2,4,8,16 on Few-NERD) would substantially strengthen the paper. If selection gain scales with N in the low-convergence regime but not in the high-convergence regime, this would be strong evidence for the regime-dependent thesis.

**Q2.** The prescriptive thresholds (10% degeneracy, 0.07 nats LP range) — how sensitive are results to these cutoffs? Have you considered a continuous model (e.g., predicting selection gain from degeneracy/LP range) rather than discrete bins?

**Q3.** For the LoRA rank=8 result: the greedy F1 drops from 0.664 to 0.625. With LP selection, it recovers to 0.661 — essentially matching rank=16 greedy. But practitioners who use rank=8 likely accept the lower greedy F1. Is the real recommendation "use rank=8 and multi-sample selection" or "use rank=16 and greedy"? The practical guidance seems ambiguous.

**Q4.** Why not evaluate majority voting or entity-level MBR? These aggregation strategies might outperform best-of-N selection, especially when individual samples have complementary strengths.

**Q5.** The SJ advantage over LP on SciERC NER is borderline (Fisher p=0.085). Yet the paper at times implies structural signals are clearly superior. Could you clarify the strength of this claim?

**Q6.** For Few-NERD's low degeneracy: you attribute this to 3 epochs (vs. 5 for SciERC) AND high entity density. Can you disentangle these? A 5-epoch Few-NERD run would isolate the epoch effect from the dataset-property effect.

## Experiment Coverage Assessment

Based on the review context YAML (imagined experiment list):

| Experiment | Status | Coverage in Paper |
|-----------|--------|------------------|
| exp-020: Few-NERD smoke | Done | Appendix D (brief) |
| exp-021: Few-NERD full | Done | Sections 4–6, Tables 4–6, 10 (thorough) |
| exp-022: 3rd seed SciERC | Done | Section 7.1, Tables 8, 11–12 (thorough) |
| exp-023: LoRA rank=8 ablation | Done | Section 6.4, Tables 4–5, 7 (thorough) |
| exp-024: claim audit | Done | Paper rewritten accordingly (narrative revised) |
| exp-017: LLaMA CoNLL | Done (registry) | Section 7.2 (brief) |
| exp-019: supervised verifier | **SKIPPED** | Mentioned in Limitations as future work |

**Coverage assessment**: The paper covers all executed experiments adequately. The skipped supervised verifier baseline (exp-019) is appropriately flagged as future work. However, the YAML reveals experiments not in the imagined list that would have been valuable: N ablation, T ablation, epoch ablation, and additional LoRA rank points. The experiment design was focused on breadth (datasets, models) rather than depth (parameter sweeps on the diversity-relevant dimensions).

## Detailed Comments

### On the Central Thesis
The paper's central claim — that selection effectiveness is regime-dependent, governed by output convergence rather than model capability — is well-supported within its experimental scope. The capability trap reinterpretation (R² dropping from 0.98 to 0.51 when Few-NERD is added, to 0.35 with the rank=8 data point) is convincing. However, the regime boundary is defined post-hoc from the same data used to establish it, creating a circularity concern. Independent validation of the 10%/0.07 thresholds on unseen datasets would be needed for the prescriptive guidelines to be trustworthy.

### On Statistical Methodology
The use of bootstrap with 1000 iterations is standard but the lack of multiple comparison correction across the full experimental matrix is a gap. The paper makes ~6 primary selection comparisons (Table 4), of which 2 are significant. Under Benjamini-Hochberg at α=0.05 with 6 tests, these would likely survive (adjusted p ≈ 0.045 and 0.084), but one becomes borderline. The Fisher combined p-values (Appendix C) are appropriate for the cross-seed analysis, though the SJ>LP result (p=0.085) should be more clearly marked as not significant at conventional thresholds.

### On the QE-Selection Decoupling
This is the paper's most elegant finding. Table 7 shows SJ ρ essentially unchanged (0.360→0.378) while LP selection gap changes from +0.6pp to +3.6pp across LoRA rank configurations. This cleanly disentangles two things that are typically conflated: can a signal estimate quality? (yes, robustly) vs. can a signal improve selection? (only when there's something to select among). This insight has implications beyond IE — it applies to any multi-sample strategy where fine-tuning compresses the output distribution.

### On Practical Impact
The prescriptive guidelines (Table 9) are the right idea but premature in their current form. Two positive data points do not a decision matrix make. The paper would be stronger if it presented these as "preliminary observations suggesting a regime boundary" rather than "prescriptive guidelines for practitioners." The cost-benefit analysis (8× inference for 3–4pp F1) is notably absent.

### On Presentation
The paper is well-written and well-organized. The progression from QE results (Section 4) → selection results (Section 5) → convergence diagnostics (Section 6) → robustness (Section 7) → guidelines (Section 8) is logical. Tables are informative and consistently formatted. The abstract accurately reflects the paper's findings without overclaiming.

### Comparison with Prior Work
Nédellec and Xia (2026) is the closest prior work — they study consistency–accuracy correlations for IE using surface-level string matching. This paper's contributions beyond theirs are: (a) structured matching (SJ via Hungarian algorithm), (b) evaluation of selection (not just correlation), (c) diagnosis of failure mechanisms, and (d) the fine-tuning intensity ablation. The differentiation is adequate but could be sharper.

## Summary

This paper conducts a systematic diagnostic study of multi-sample selection for structured information extraction. Its strongest contributions are the LoRA rank ablation establishing fine-tuning intensity as a controllable convergence driver, and the QE-vs-selection decoupling showing that quality estimation and selection effectiveness are governed by different factors. These are genuine empirical insights.

However, for EMNLP Main Conference, the paper faces challenges: (1) the high-level insight (selection works when outputs are diverse) is not deeply novel, (2) the prescriptive guidelines rest on only two positive results, (3) the most natural ablations (N, T) given the diversity thesis are absent, and (4) effect sizes are small relative to inference cost. The paper would be a strong candidate for Findings, where the systematic evaluation and diagnostic insights would be well-placed.

**Key revisions that would strengthen the paper:**
1. Add N ablation (N=2,4,8,16) in both high- and low-convergence regimes
2. Add T ablation (T=0.6, 0.8, 1.0, 1.2) on at least one dataset
3. Evaluate at least one aggregation alternative (entity-level majority voting or MBR)
4. Soften prescriptive guidelines to "preliminary observations" or validate on held-out data
5. Add multiple comparison correction discussion
6. Discuss cost-benefit tradeoff (F1 gain vs. inference cost)
7. Add epoch ablation to disentangle from LoRA rank effect

---

*Review conducted via 2-reviewer roundtable: R1 (Methods+Experiments), R2 (Novelty+Related Work). Full 4-step protocol: independent review → cross-sharing → convergence → synthesis.*