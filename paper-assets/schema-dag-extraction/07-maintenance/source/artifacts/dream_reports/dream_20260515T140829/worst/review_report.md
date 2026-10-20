---
dream_id: dream_20260515T140829
tier: worst
overall_score: weak reject
timestamp: 2026-05-15T14:57:04.317896+00:00
---

# Dream Review Report: "One Size Does Not Fit All: Negative Results on Schema Decomposition for Training-Free LLM Information Extraction"

**dream_id:** 20260515T140829  
**Review mode:** full  
**Reviewers:** R1 (Methods + Experiments), R2 (Novelty + Related Work)  
**Consensus score:** 3 / 6 (Weak Reject)  
**Confidence:** 4 / 5 (High)

---

## 1. Paper Summary

The paper investigates why training-free LLM information extraction degrades on complex schemas. It proposes a two-channel degradation model (type count → recall loss; type confusability → type confusion) and develops SDGD (Schema DAG-Guided Decomposition), a graph-coloring-based schema decomposition framework with three variants (zero-shot, calibration-based, improved merge). Experiments span 3 IE tasks (NER/Few-NERD, ED/MAVEN, RE/DocRED), 2 LLMs (Qwen3-32B, LLaMA-3.3-70B), and 3 embedding spaces. All findings are negative: confusability is model-specific (r=0.156 for Qwen3 vs r=0.018 for LLaMA), SDGD consistently underperforms single-pass and random batching, and merge amplification is identified as a structural bottleneck. The paper is framed as negative results that reframe assumptions about schema decomposition.

---

## 2. Roundtable Process

### Step 1: Independent Reviews

**R1 (Methods + Experiments) — Score: 3, Confidence: 4**

**R2 (Novelty + Related Work) — Score: 3, Confidence: 4**

### Step 2: Cross-Sharing

R1's methodological concerns were shared with R2 and vice versa. Key cross-reactions:

- R2 agreed with R1 that the LLaMA scale confound (32B vs 70B) undermines the "model-specificity" claim. R2 noted this also weakens the novelty: if the null result is explained by model scale rather than model family, the finding is even less surprising.
- R1 agreed with R2 that the 6-reference related work is unacceptable and that LLM-PEE is the most critical missing comparison. R1 added that without LLM-PEE comparison, it is unclear whether SDGD-zero is even a novel algorithm or a reimplementation.
- Both reviewers converged on the view that merge amplification is the most interesting finding but is undersupported by the current evidence (only simple merge strategies tested, "perfect oracle" claim is extrapolation).

### Step 3: Convergence

**Areas of agreement:**
1. The multi-channel degradation framework (count vs confusability) is a genuine diagnostic contribution
2. Related work is severely inadequate (6 references for a venue paper)
3. Method development is insufficient to declare the decomposition direction dead
4. The LLaMA null result has an uncontrolled confound (model scale)
5. Merge amplification is interesting but the "irreducible" claim overstates the evidence
6. The paper is below Main threshold but has Findings potential with revisions

**Areas of disagreement (minor):**
- R1 was more concerned about statistical methodology (multiple comparisons, BCS p=0.054); R2 was more concerned about framing and positioning. These are complementary rather than contradictory.

### Step 4: Synthesis (below)

---

## 3. Strengths

**S1. Rigorous controlled experimental design.** The 2×2 factorial (count × BCS), systematic variation across 3 tasks / 2 models / 3 embeddings, and multi-level analysis (pairwise, per-type, batch) demonstrate strong methodological discipline. The controlled batch construction for isolating confusability is well-designed. [R1, R2 concur]

**S2. Merge amplification is a novel and actionable finding.** Identifying that decomposition is bottlenecked by the merge/reassembly step — with 42% merge conflict rate at per-type granularity and structural precision loss even after conflict resolution — is a genuinely useful insight. The observation that per-type splitting (which should eliminate within-batch confusion) still suffers precision collapse is informative. [R2 primary, R1 concurs]

**S3. Transparent reporting of negative results.** The paper does not hide failures. The 5-seed SDGD-zero vs random comparison (100% consistency, p=0.003), the progression from SDGD-zero → cal → v2 each failing to close the gap, and the honest LLaMA null are commendable. [R1, R2 concur]

**S4. Cross-task breadth.** Testing across NER (66 types), ED (168 types), and RE (96 types) with genuinely different schema structures (cross-domain vs same-domain, sentence-level vs document-level) goes beyond typical single-task evaluation. [R2]

**S5. Multi-model validation is attempted honestly.** Rather than reporting only the positive Qwen3 result, the authors test three embeddings on LLaMA to rule out embedding choice as an explanation. [R1]

---

## 4. Weaknesses

**W1 (Major). Related work is drastically inadequate.** Six references for a paper targeting a top venue is far below standard. Critical omissions include:
- **LLM-PEE** (Zhang et al.): essentially the same algorithm as SDGD-zero (embedding-similarity-based type partitioning for LLM event extraction). This is the single most important missing comparison.
- **Multi-agent IE:** CROSSAGENTIE (Lu et al. 2025, ACL Findings), CMAS-NER (2025, TheWebConf) — directly address type confusion through alternative mechanisms.
- **Zero-shot IE baselines:** GoLLIE (ICLR 2024), GLiNER (NAACL 2024), IEPile (ACL 2024), KnowCoder (ACL 2024) — none cited.
- **Embedding geometry:** Ethayarajh (2019), Cai et al. (2021) on representation anisotropy — directly relevant to the centrality confound finding.
- **Schema decomposition:** PARSE, DEE, SPT, DLISC — all recent schema-aware IE approaches.
A paper claiming to "reframe assumptions" cannot do so while citing only 6 papers. The related work reads as if no literature review was conducted. [R2 primary, R1 concurs]

**W2 (Major). "Structural" merge amplification claim is insufficiently supported.** The paper declares merge amplification "irreducible" and "fundamental" after testing only three simple merge strategies (naive union, confidence-weighted dedup, type-priority). The "perfect merge oracle yields ~0.35 F1" claim is an extrapolation from the observation that merge conflicts account for ~40% of precision loss, not a formal derivation. More sophisticated approaches (LLM-based re-ranking, iterative refinement, constrained decoding, span-level voting with learned weights) are acknowledged in Limitations but not attempted. Declaring a direction dead after minimal method development is premature. [R1 primary, R2 concurs]

**W3 (Major). LLaMA null result conflates model scale with model family.** Qwen3-32B vs LLaMA-3.3-70B differs in both architecture family and parameter count (2.2× scale difference). The larger model plausibly has better type discrimination capacity independent of confusability sensitivity. The paper cannot distinguish "model family effect" from "model scale effect." Testing another ~32B model (e.g., Mistral-32B, or a smaller LLaMA variant) would be necessary to support the "model-specific" claim. [R1 primary, R2 concurs]

**W4 (Major). Novelty of negative findings is questionable.**
- "Confusability is model-specific": that different models exhibit different confusion patterns is expected given different architectures and training regimes. This is predictable, not surprising.
- "SDGD underperforms single-pass": splitting extraction into batches and merging results loses information — this is a well-known challenge in any decompose-and-merge pipeline.
- "Merge amplification is structural": the underlying phenomenon (independent classifiers disagree on ambiguous instances) has been studied for decades in ensemble methods.
The specific instantiation in LLM IE is new, but the general principles are not novel. [R2]

**W5 (Moderate). Batch size confound in SDGD evaluation.** SDGD's graph coloring may produce highly unbalanced batches (e.g., [18,12,11,7,7,5,3,3] types). Small batches (3 types) likely over-predict while large batches (18 types) under-predict. The paper does not control for batch size distribution — SDGD-zero's inferior performance may be driven by unbalanced batch sizes rather than by confusability-aware grouping being inherently harmful. [R1]

**W6 (Moderate). Small effect sizes undermine the confusability contribution.** Pairwise r=0.156 explains only ~2.4% of confusion variance. The paper leverages statistical significance inflated by large sample sizes (n=1,953 pairs). A statistically significant but practically negligible correlation does not constitute strong evidence for confusability as a meaningful degradation channel. There is also a rhetorical asymmetry: r=0.156 is presented as "significant evidence for confusability" in §4.3, while the nearly identical ρ=0.18 is presented as "explains only ~3% of variance" in §4.4 when evaluating the proxy. [R1, R2]

**W7 (Moderate). BCS effect is borderline and no multiple-comparison correction is applied.** The BCS main effect in the 2×2 factorial is p=0.054 — not significant at α=0.05. The paper tests pairwise correlations across 3 embeddings × 2 models × 2+ datasets, plus per-type correlations, batch-level effects, and factorial effects. No Bonferroni or FDR correction is applied. [R1]

**W8 (Minor). Missing mechanistic evidence.** The paper lacks an error taxonomy analysis binned by BCS level (what fraction of errors are substitutions vs omissions in high-BCS vs low-BCS batches). This would directly test HOW confusability causes errors and strengthen the multi-channel claim. FewRel results (which reportedly show stronger BCS effects: -9.1pp at 16-rel, -31.2pp at 80-rel) are also absent, which is puzzling given they would strengthen the narrative. [R1]

**W9 (Minor). No decomposed evaluation metrics.** The paper uses aggregate F1/P/R but never separates span detection accuracy from type classification accuracy. The count channel should manifest in span detection; the confusability channel should manifest in type classification given correct spans. This decomposition would directly validate the two-channel model but is absent. [R1]

---

## 5. Questions for Authors

**Q1.** How are "low BCS" and "high BCS" batches constructed in the 2×2 factorial? If by extremal selection, the effect sizes are inflated. Report the BCS distribution of random batches and where selected batches fall.

**Q2.** Was SDGD-zero's batch size distribution controlled (e.g., min_batch_size constraint) before the results in Table 7? If not, re-run with balanced batches to isolate confusability-aware grouping from batch size effects.

**Q3.** How many test instances per evaluation? Dataset splits and test set sizes are not reported.

**Q4.** The graph coloring threshold τ — was it fixed a priori or tuned? No sensitivity analysis is presented.

**Q5.** For SDGD-cal with 5 examples per type and 66 types, how are type pairs with zero calibration co-occurrence handled in the confusion matrix?

**Q6.** How does the paper relate to LLM-PEE, which performs essentially the same embedding-similarity-based type partitioning for LLM event extraction?

**Q7.** LLaMA's non-monotonic count curve (F1 rises from 0.275 at count=22 to 0.395 at count=44) is striking. Is this reproducible across seeds? Does prompt format change at different count levels?

---

## 6. Experiment Coverage Assessment

All 10 imagined experiments are represented in the paper:

| Experiment | Coverage | Assessment |
|---|---|---|
| exp-005 DocRED | §4.6 | Adequate |
| exp-006 2×2 Factorial | §4.2 | Adequate |
| exp-009 SDGD-zero MAVEN | §4.5.2 | Adequate |
| exp-010 SDGD-cal Few-NERD | §4.5.1 | Adequate |
| exp-011 SDGD-cal MAVEN | §4.5.2 | Adequate |
| exp-012 LLaMA validation | §4.3 | Strong |
| exp-013 Random ablation | §4.5.1 | Adequate (5 seeds) |
| exp-014 Per-type splitting | §4.5.1 | Adequate |
| exp-015 SCS proxy | §4.4 | Adequate |
| exp-008-v2 SDGD v2 | §4.5.1 | Adequate |

**Notable gaps in coverage:**
- No error taxonomy analysis (substitution vs omission by BCS level) — a significant mechanistic omission
- No FewRel sentence-level RE results, which would show stronger BCS effects and strengthen the confusability claim
- No embedding ablation table (2×3 cross-embedding matrix for Qwen3 extractions)
- No Qwen3 count curve (only LLaMA's is shown)

---

## 7. Consolidated Assessment

### What works
The paper asks the right question (what drives schema-induced degradation in training-free LLM IE?) and uses the right methodology (controlled factorial experiments). The multi-channel degradation framework is a genuine analytical contribution. The merge amplification finding, while undersupported, identifies a real and underappreciated problem. The cross-task and cross-model breadth is commendable.

### What doesn't work
The paper's three headline contributions are each undermined:
1. **"Confusability is model-specific"** — confounded by model scale (32B vs 70B), small effect size (r=0.156), and is arguably an expected finding.
2. **"SDGD fails"** — after insufficient method development (only simple merge strategies), with an uncontrolled batch size confound.
3. **"Merge amplification is irreducible"** — based on extrapolation, not formal analysis, after testing only three simple strategies.

The related work section with 6 references is the most immediately disqualifying issue — it misses the most important comparison point (LLM-PEE) and fails to situate the work in the rapidly growing LLM IE landscape.

### Recommendation

**Score: 3 / 6 (Weak Reject)** for a top ML venue Main track.

The analytical contributions (multi-channel degradation model, centrality confound, merge amplification diagnosis) are solid material for a **Findings** paper with revisions:
1. Comprehensive related work (20-25 refs minimum, with LLM-PEE comparison)
2. Control for batch size distribution in SDGD evaluation
3. Test a ~32B model from a different family to separate scale from family effects
4. Either develop merge strategies further or provide formal analysis of decomposition limits
5. Add error taxonomy analysis and decomposed evaluation metrics
6. Apply multiple-comparison correction

The paper would also benefit from reframing: shift emphasis from "SDGD failed" (weak negative result) to "here is a diagnostic framework for schema complexity, and here is why naive decomposition cannot work" (stronger methodological contribution).

---

## 8. Individual Reviewer Scores

| Reviewer | Focus | Score | Confidence |
|---|---|---|---|
| R1 | Methods + Experiments | 3 (Weak Reject) | 4/5 |
| R2 | Novelty + Related Work | 3 (Weak Reject) | 4/5 |
| **Consensus** | | **3 (Weak Reject)** | **4/5** |
