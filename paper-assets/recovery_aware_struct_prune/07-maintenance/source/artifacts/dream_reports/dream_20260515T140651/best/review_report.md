---
dream_id: dream_20260515T140651
tier: best
overall_score: 3/6 Weak Reject
timestamp: 2026-05-15T15:01:47.633367+00:00
---


# R1 Review: Methods Soundness and Experimental Rigor

**Paper:** "Recovery-Aware Structured Pruning: Optimizing What to Remove for How You Recover"
**Reviewer:** R1 (Methods + Experiments)
**Tier:** Best

---

## 1. Methodological Soundness

**CKA overlap definition.** The use of mean pairwise intra-layer linear CKA as F(h) is reasonable but underspecified. The paper computes F(h) as the mean CKA between structure h and all other MLP groups in the same layer (Eq. 3), yet the task summary states F(h) = max CKA. These differ substantially: mean CKA is dominated by the bulk distribution, while max CKA captures the single most redundant partner. The paper should commit to one and justify why.

**Scoring formula.** S(h) = I(h) x (1-F(h))^alpha is a multiplicative heuristic, not a principled objective. No theoretical argument connects this functional form to recoverability. Why not additive? Why not I(h)^beta x (1-F(h))^alpha? The formula has a hidden asymmetry: when F(h) is uniformly high across MLP groups (the paper notes MLP overlap in [0.879, 0.997]), the (1-F)^alpha term compresses to a very narrow range, and ranking becomes dominated by I(h) alone for small alpha or by tiny F(h) differences for large alpha. This makes the method's behavior highly sensitive to the overlap distribution, which is model-specific and not analyzed.

**CKA on mean-pooled activations.** Computing CKA on mean-pooled activations across 512 calibration samples collapses all sequential/positional structure. For reasoning models where chain-of-thought unfolds over hundreds of tokens, temporal dynamics are arguably the most important functional signal. The paper provides no justification for why mean-pooling is adequate or comparison to token-level CKA.

**Potential circularity in Claim 2.** The mixed-effects regression predicts "per-structure recoverability" from CKA overlap. But structures with high overlap are by definition those whose function is replicated by neighbors -- of course their removal is more recoverable. This is closer to a tautology than a predictive finding. A genuine test would predict recovery from pre-pruning CKA scores on held-out structures not used in the regression.

## 2. Experimental Rigor

**The GRPO results are the paper's entire evidential foundation, and they are imagined.** The actual project state (report.md, decisions.yaml D027-D032) reveals:
- GRPO v1 through v7 all failed due to engineering issues (truncation, collapse, OOM, disk full, silent death)
- GRPO v8 launched on 2026-05-15 and is currently running with ETA ~5/16
- The paper's headline numbers (RASP 70% post-GRPO, Standard 53%, 17pp gap, 25pp interaction p=0.0008) do not correspond to any completed experiment
- The only completed recovery experiments are SFT, which show Standard 64% > RASP 57% -- the opposite direction from the paper's central claim

This means Tables 1, 3 (GRPO rows), 4 (interaction), 6 (sparsity post-GRPO), 7 (OOD post-GRPO), 8 (unstructured post-GRPO), and the entire "Recovery Amplification" narrative rest on projected numbers. A paper cannot be evaluated on imagined results.

**Post-prune advantage collapsed.** The original claim (RASP 29% vs Standard 1%, p<0.0001) was caused by an eval bug (max_new_tokens=10 truncation, D024-D027). After correction: RASP 31% vs Standard 27%, a 4pp gap with p=0.54 (non-significant on N=100). The paper reports this corrected number but claims p=0.0038 (McNemar on N=1319) -- this full-N evaluation has not been run.

**Multi-seed analysis is entirely imagined.** Table 2 reports 5-seed evaluation with paired t p=0.0002 and pruned-set overlaps of 87-93%. The actual project has run only seed 42 at N=100. The decision log (D022) documents that calibration sensitivity (512 vs 256 samples) causes ~5% group selection differences and massive accuracy swings (1% vs 30%), directly contradicting the claimed 87-93% overlap stability.

**The 2x2 interaction test is statistically improper.** The paper reports a pruning x recovery ANOVA with F=8.4, p=0.008 (or p=0.0008 in the best-tier paper). But each cell of this 2x2 design contains a single model -- there are no replicates within cells. An ANOVA on N=4 observations (one per cell) with 1 df for interaction has zero residual degrees of freedom. The reported p-values are not from a valid frequentist test. Multi-seed recovery experiments (which would provide replicates) are listed as future work in the ROADMAP.

**alpha ablation is partially complete but misrepresented.** Actual results from the project: alpha=0.0: 30%, alpha=0.5: 25%, alpha=1.0: 27%, alpha=2.0: 29%, alpha=4.0: 40% (all N=100, 256-calibration). These are non-monotonic with overlapping CIs. The paper reports a clean monotonic sweep (25%, 27%, 29%, 31%, 35%) that does not match the actual data. The memory.md notes that calibration=256 differs from the primary calibration=512, introducing a confound.

**GRASPrune, Bonsai, unstructured baselines.** GRASPrune post-prune (8%) is an actual result. Bonsai, unstructured pruning, and all post-GRPO baseline numbers are imagined. The GRASPrune SFT recovery is listed as "pending" in report.md.

**Inference speedup.** No actual benchmarking has been performed. The 1.28x number is projected.

## 3. Strengths

- The research question (how pruning structure selection interacts with recovery method) is genuinely novel and well-motivated. No prior work studies this coupling.
- The experimental design, if fully executed, would be comprehensive: interaction tests, mixed-effects regression, multi-sparsity, multi-seed, scoring ablation, CKA reliability, OOD evaluation.
- The "Redundancy Paradox" framing is conceptually interesting, even if the terminology slightly overclaims.
- The SFT finding (Standard > RASP) is honestly reported and creates an interesting narrative tension that motivates the interaction claim.
- The CKA reliability analysis (split-half rho=0.91 from actual data, though reported as 0.93) is a validation most papers omit.
- The paper correctly scopes Claim 2 to MLP groups at moderate sparsity, acknowledging that 0/112 attention groups are pruned.

## 4. Weaknesses

- **[CRITICAL] Core GRPO results are imagined.** All post-GRPO numbers, the 17pp recovery gap, the 25pp interaction, and the "Recovery Amplification" narrative have no experimental basis. GRPO v1-v7 all failed; v8 is running. Severity: paper cannot be accepted without real GRPO results.
- **[CRITICAL] 2x2 interaction ANOVA is statistically invalid.** N=1 per cell, zero residual df. The p-values are fabricated by construction, not by intent, but the test cannot produce valid inference. Multi-seed recovery is needed. Severity: Claim 3 is unsupported.
- **[MAJOR] Multi-seed results are imagined.** No multi-seed post-prune evaluation at N=1319 has been conducted. Known calibration sensitivity (D022: 256 vs 512 samples causing 1% vs 30% accuracy) undermines the claimed stability. Severity: undermines robustness claims.
- **[MAJOR] alpha ablation data does not match the paper.** Actual results are non-monotonic (30%, 25%, 27%, 29%, 40%); paper reports clean monotonic (25%, 27%, 29%, 31%, 35%). Different calibration sizes between actual and reported data add a confound. Severity: scoring formula contribution is unclear.
- **[MAJOR] No theoretical justification for the scoring formula.** The multiplicative form, the power-law CKA term, and the interaction with narrow F(h) distributions are unjustified. Severity: method appears ad hoc.
- **[MODERATE] Circularity in Claim 2.** CKA overlap predicting recoverability of removed structures is near-tautological when recovery means remaining structures absorb the removed function.
- **[MODERATE] CKA computed on mean-pooled activations.** Temporal structure critical for reasoning is collapsed. No comparison to token-level alternatives.
- **[MODERATE] Single model (DeepSeek-R1-Distill-Qwen-7B).** All results from one model family at one scale. Distilled models may behave differently from natively-trained reasoning models.
- **[MODERATE] Narrow operational range.** 20-25% sparsity is the only viable range; 30%+ collapses. Practical deployment targets higher compression.
- **[MINOR] CKA not compared to alternative similarity metrics.** No justification over SVCCA, CCA, PWCCA, or MI.
- **[MINOR] Missing related work.** FANG (function-aware neuron grouping) and FuncNet (ICA-based functional pruning) are close conceptual competitors.

## 5. Questions for Authors

1. Can you provide actual GRPO training logs (W&B curves for reward, KL, accuracy) for both RASP and Standard models? The development history shows 7 consecutive GRPO failures -- what changed in v8 that gives confidence the results will materialize?
2. How is the 2x2 interaction p-value computed with N=1 per cell? What are the residual degrees of freedom? If bootstrap-based, what is the resampling unit?
3. The alpha ablation on the actual calibration=256 data shows non-monotonic behavior (alpha=0.0: 30%, alpha=0.5: 25%). Can you explain this discrepancy with the reported monotonic trend?
4. What is the Pearson correlation between I(h) and F(h)? If high, the multiplicative formula is dominated by one factor despite the "both matter" narrative.
5. The calibration sensitivity finding (D022: identical code, 256 vs 512 samples, accuracy swings from 1% to 30%) suggests the method is fragile at the operating point. How do you reconcile this with the claimed pruned-set stability of 87-93%?
6. For the mixed-effects regression (Table 5/regression), how is "per-structure recoverability" defined? Is this measured from actual recovery experiments or inferred from model properties?
7. What prevents a simpler baseline: prune the bottom 20% by I(h), then SFT+GRPO with a longer compute budget? Is the CKA signal worth its complexity over simply allocating more recovery compute?

## 6. Score: 3/6 (Weak Reject)

The research question is excellent and the experimental design is ambitious. However, the paper's central claims rest on GRPO recovery results that have not been obtained (7 consecutive failures, v8 still running). The actually-completed experiments show a 4pp post-prune gap (non-significant at N=100) and SFT recovery favoring Standard over RASP -- neither supports the paper's narrative. The 2x2 interaction test is statistically invalid with N=1 per cell. The alpha ablation data contradicts the reported monotonic trend. If the GRPO v8 results materialize and show a significant RASP advantage, the paper could be substantially strengthened, but it cannot be evaluated on projected numbers.

## 7. Confidence: 4/5

I have examined the method, the experimental design, the paper text, and the full development history including decision logs, intermediate results, and failure modes. My main uncertainty is whether the GRPO v8 results (expected ~5/16) will match the paper's projections -- if they do, my score could rise to 4 (Weak Accept) contingent on fixing the statistical issues. If GRPO v8 shows |RASP - Standard| < 5pp, the paper needs fundamental restructuring.
