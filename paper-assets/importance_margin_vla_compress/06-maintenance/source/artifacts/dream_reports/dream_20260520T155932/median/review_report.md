---
dream_id: dream_20260520T155932
tier: median
overall_score: borderline reject (5/10)
timestamp: 2026-05-20T16:52:37.136501+00:00
---

# Dream Review Report: "Why Token Pruning Crashes Some Robot Policies but Not Others"

**Dream ID:** 20260520T155932  
**Venue:** CoRL 2026  
**Review Mode:** Full (2 Reviewers, 4-step roundtable)

---

## Paper Summary

The paper presents the first systematic cross-architecture analysis of vision token pruning robustness in VLA models. Testing 5 models (π0, X-VLA, OpenVLA, OpenVLA-OFT, SmolVLA) spanning 3 vision connector families on LIBERO, the authors identify a four-class taxonomy of pruning sensitivity: immune (pure linear, CV=0.038), threshold-graded (linear+BART, CV=0.151), smooth graded (MLP, CV=0.215), and catastrophic (pixel-shuffle, CV=0.314). The coefficient of variation (CV) of token importance scores serves as a zero-cost predictor. For pixel-shuffle's catastrophic failure, Vision Token Re-encoding (VTR, ~22M params) recovers 0%→60%+ SR at 75% compression. VTR fails on MLP-projector models (0% SR), reinforcing connector-dependency as the core finding.

---

## Venue Standards (CoRL 2026)

Rating scale: 1-10 (1=strong reject, 5=borderline reject, 6=borderline accept, 8=strong accept). Acceptance rate ~25-30%. Evaluation criteria: significance and novelty of results, relevance to robot learning, degree to which results are objectively established, potential for scientific and technological impact.

---

## R1 Review: Methods and Experiments

### Strengths
1. **SmolVLA cliff-edge ablation is thorough and convincing.** Seven pruning configurations (random, ACIS, ToMe, Sobel × multiple k values) all producing 0% SR, verified on official checkpoint and across suites, comprehensively rules out confounds.
2. **π0-OpenVLA controlled comparison is the paper's strongest methodological contribution.** Same token count (256), same SigLIP lineage, different connector → 63pp gap at k=0.1.
3. **VTR mechanism isolation is rigorous.** Three independent lines of evidence (M=128 passthrough, MLP adapter control at p=0.15, flat M-curve) converge to isolate re-encoding as the causal mechanism.
4. **Extended training control** (45.0% vs 44.8%, p>0.9) rules out the alternative hypothesis that VTR gains come from additional optimization.
5. **Transparent negative result reporting** — VTR on OpenVLA yielding 0% SR is honestly reported and reframed as evidence.
6. **Per-task breakdowns** enable assessment of whether aggregates mask heterogeneous behavior.

### Weaknesses
1. **Heterogeneous pruning methods across models undermine the unified taxonomy.** OpenVLA uses random removal (harder), X-VLA uses L2-norm (easier), SmolVLA uses both. The "strengthens findings" framing is post-hoc. The L2-norm vs random comparison on OpenVLA (Δ<3pp) may be based on still-running experiments.
2. **π0 "immune" classification rests entirely on offline single-step loss.** The paper's own Section 5.4 shows offline metrics underestimate closed-loop degradation by up to 77pp (X-VLA). The taxonomy's left anchor has the weakest evidence.
3. **OpenVLA main degradation curve is single-seed.** The 6-point curve defining "smooth graded" uses a single seed with 500 episodes per k. Seed replications at k=0.7 and k=0.5 may still be running.
4. **X-VLA seed replication at cliff point shows concerning variance.** Seed42=56.2% vs seed43 reportedly ~68.3% (12pp gap), yet reported std is 1.6pp — discrepancy needs clarification.
5. **OFT contributes almost nothing** — only an entropy measurement (0.667) due to confirmed eval bug. Could be demoted to footnote.
6. **VTR on OpenVLA failure is under-investigated.** 20K steps vs SmolVLA's 100K. Was training loss still decreasing? Were other durations attempted?
7. **No pairwise VTR comparison survives Bonferroni correction** at n=3 seeds.

### R1 Scores
- Soundness: 3/4
- Empirical Rigor: 2.5/4
- Overall Recommendation: **5/10 (borderline reject)**
- Confidence: 4/5

---

## R2 Review: Novelty and Related Work

### Strengths
1. **The research question is genuinely novel and well-motivated.** No prior work asks "why does pruning work on some VLAs but not others?" at the right time when VLA architectures are proliferating.
2. **The connector-centric taxonomy is a real contribution.** The four-class spectrum with mechanistic explanations, especially the X-VLA "threshold-graded" nuance (effective pipeline vs nominal connector label), elevates beyond naive connector-type mapping.
3. **The π0-OpenVLA controlled comparison effectively rules out scale** as the explanatory variable (non-monotonic: 450M < 7B < 880M < 3.3B in pruning tolerance order).
4. **CV as a zero-cost single-forward-pass diagnostic** is actionable for practitioners deploying new VLAs.
5. **Related work is adequate and fairly positioned** — covers ViT pruning foundations, VLM extensions, VLA-specific methods, and concurrent work with fair positioning.
6. **VTR passthrough (M=128) and MLP adapter controls** are well-designed ablations isolating the causal mechanism.

### Weaknesses
1. **"First systematic analysis" claim is overstated.** "Don't Run with Scissors" (Jabbour et al., 2025) studies weight pruning fragility across VLA architectures. Claim should be scoped to connector-dependent *token* pruning.
2. **π0 offline-only evaluation** creates internal inconsistency (Section 5.4 shows offline metrics underestimate degradation by up to 77pp).
3. **Pruning method inconsistency** across models (random vs L2-norm) makes direct numerical comparison unreliable.
4. **VTR novelty is limited** — cross-attention pooling is Q-Former applied to a different input. The MLP adapter control further undercuts architectural novelty: "any learned re-encoding works" means VTR is not a method contribution but an observation.
5. **VTR practical scope is narrow** — works only for pixel-shuffle (1 of 4 classes). For MLP connectors, the framework reduces to "use existing pruning." For linear, no compression needed.
6. **SmolVLA baseline (44.8%) substantially below official (87.3%)**, and VTR on official checkpoint shows *regression* (59.2%→53.4%), weakening the method contribution.
7. **Single benchmark (LIBERO simulation)** — no real robot validation for a CoRL submission.

### R2 Scores
- Novelty: 3/4
- Significance: 3/4
- Related Work Coverage: 3/4
- Overall Recommendation: **6/10 (borderline accept)**
- Confidence: 4/5

---

## Roundtable Discussion

### Points of Agreement (Both Reviewers)
1. **Pi0 offline-only evaluation is the paper's most critical weakness** — the taxonomy's left anchor ("immune") has the weakest evidence, and the paper's own analysis shows offline metrics can diverge from closed-loop by 77pp.
2. **Heterogeneous pruning protocols** across models weaken the unified taxonomy claim.
3. **SmolVLA cliff-edge finding is thoroughly established** — the strongest experimental result in the paper.
4. **VTR mechanism isolation is rigorous** — M=128 passthrough, MLP adapter control, and flat M-curve are well-designed ablations.
5. **Research question is genuinely novel** and timely for the VLA community.
6. **VTR has limited novelty as a method** and limited practical scope (pixel-shuffle only).
7. **Single benchmark (LIBERO)** is a limitation for CoRL.
8. **OFT adds minimal value** to the paper.
9. **Some reported values may be predicted** rather than empirical (OpenVLA L2-norm, VTC-only experiments still running).

### Points of Disagreement
- **R1 (5/10) vs R2 (6/10):** R1 weighs empirical rigor more heavily and finds evidence insufficient for the strength of claims. R2 weighs the diagnostic contribution (novel question + taxonomy + CV predictor) and finds it sufficient despite experimental gaps.
- **Resolution:** The paper makes strong claims ("taxonomy," "first systematic analysis") that demand uniformly strong evidence. The pi0 gap and thin seed replication are addressable in revision, but in current form the evidence does not consistently support the claim strength.

### Key Questions for Authors (Prioritized)
1. Can you provide closed-loop pi0 evaluation at any retention ratio? Even a small-scale test would dramatically strengthen the taxonomy.
2. Which OpenVLA L2-norm values in Table 3 are empirical vs. predicted from still-running experiments?
3. What are the exact X-VLA per-seed SR values at k=0.7? The reported std (1.6pp) seems inconsistent with the seed42-seed43 gap.
4. VTR on OpenVLA used 20K steps vs SmolVLA's 100K — what does the training loss trajectory look like?
5. VTR on official SmolVLA checkpoint (59.2%→53.4%) shows degradation. Is VTR only useful when the base model is undertrained?
6. Is CV predictive or tautological? It is computed from the connector's output tokens — does it measure anything beyond the same property that causes pruning sensitivity?

---

## Consolidated Assessment

### What This Paper Does Well
- Asks the right question at the right time
- Provides a useful conceptual framework (four-class taxonomy + CV diagnostic)
- Thoroughly establishes the SmolVLA catastrophic cliff finding
- Rigorously isolates the VTR re-encoding mechanism
- Transparently reports negative results (VTR on OpenVLA)

### What Needs Improvement
- Pi0 closed-loop evaluation (taxonomy's left anchor)
- Unified pruning protocol across all models (at least at key comparison points)
- Multi-seed replication for OpenVLA main curve
- Clarification of which results are empirical vs. predicted
- Additional benchmark beyond LIBERO
- VTR practical utility remains unclear (fails on official checkpoint, fails on MLP projectors)

### Experiment Coverage vs. Design
The review_context.yaml describes 13 imagined experiments. The paper covers most but several appear to be still running:
- OpenVLA L2-norm full sweep: partially in paper, status unclear
- OpenVLA VTC-only M=32/64/96: in Table 6, but listed as RUNNING
- X-VLA seed44 replications: in Table 4, but listed as RUNNING
- OpenVLA random seed43 replications: mentioned in text, RUNNING
- RoboFlamingo: correctly noted as future work
Coverage is adequate for the claims made, **provided** the still-running experiments produce results consistent with the reported/predicted values.

---

## Final Scores

| Dimension | Score |
|-----------|-------|
| Novelty (research question) | 3/4 (genuinely novel) |
| Novelty (method/VTR) | 2/4 (limited — Q-Former variant, narrow scope) |
| Soundness | 2.5/4 (strong on SmolVLA/VTR, weak on pi0/cross-model protocol) |
| Empirical Rigor | 2.5/4 (heterogeneous protocols, thin seeds, some predicted values) |
| Significance | 3/4 (useful diagnostic framework for growing VLA community) |
| Related Work | 3/4 (adequate and fairly positioned) |
| Presentation | 3/4 (well-written, clear taxonomy, good tables) |
| **Overall** | **5/10 (borderline reject)** |

### Recommendation Rationale
The paper addresses a genuinely novel and important question for the robotics community — why does token pruning behave so differently across VLA architectures? The four-class taxonomy and CV diagnostic are real contributions. However, the evidence does not uniformly match the claim strength: (1) the taxonomy's left anchor (pi0 "immune") relies on offline-only evaluation contradicted by the paper's own analysis, (2) heterogeneous pruning protocols prevent clean cross-model comparison, (3) key results may be predicted rather than empirical, and (4) VTR's practical utility is undermined by its failure on the official SmolVLA checkpoint and on MLP-projector models. For CoRL, single-benchmark (simulation-only) evaluation is also a concern.

A revision addressing pi0 closed-loop evaluation, unified pruning protocol at key comparison points, and multi-seed OpenVLA curves would likely push this to a borderline accept (6). The diagnostic contribution is lasting; the evidence needs to catch up.
