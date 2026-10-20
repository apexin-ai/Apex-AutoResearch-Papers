---
dream_id: dream_20260513T081242
tier: worst
overall_score: Reject (2/6)
timestamp: 2026-05-13T09:11:29.697687+00:00
---

# Dream Review Report — "Why Cross-Method Circuit Consensus Fails: An Empirical Analysis"

**dream_id:** 20260513T081242 | **Review mode:** full | **Date:** 2026-05-13

---

## Consolidated Review Summary

This paper introduces Cross-method Structural consensus Scoring (CSS), a binary consensus framework applied to K=3 circuit discovery methods (EAP-IG, EP, ACDC) across 3 tasks on GPT-2 Small and 2 tasks on Qwen-2.5 0.5B. The headline finding is negative: CSS fails in 4/5 configurations, and the sole positive case (IOI on GPT-2) is confounded by ACDC isinf binarization and zero-ablation size bias. The paper identifies three structural failure causes: inter-method correlation, binarization pathologies, and combinatorial dilution at scale.

Both reviewers independently scored the paper **Weak Reject (3/6)** in initial assessment. After cross-sharing, R1 revised to **Reject (2/6)** while R2 maintained **Weak Reject (3/6)**.

**Consensus overall score: 2–3/6 (Reject to Weak Reject)**

---

## R1: Methods and Experiments

### Strengths
- Clean CSS formulation: the scoring framework is simple, well-defined, and easy to reproduce
- Honest negative reporting: the paper does not oversell; Arithmetic and SVA failures are transparently presented
- The ablation method comparison (§4.3) is a useful methodological contribution — showing IOI advantage drops from +0.080 (zero) to +0.003 (resample) is informative for the broader circuit evaluation community
- Top-k sensitivity sweep demonstrates CSS stability across k, cleanly ruling out binarization threshold as the failure cause
- CIRCUS comparison (§6) is well-designed and the "both methods fail" conclusion is more honest than selectively framing CSS as better
- Multi-seed bootstrap on SVA (Table 1) is a positive methodological choice, though only applied to one task

### Weaknesses
- **W1 (No statistical testing on primary claim):** The central claim — CSS=1.0 CPR > best single method CPR — is reported as bare point estimates without bootstrap confidence intervals or permutation tests. On IOI, the advantage is Δ=+0.080 (zero ablation) from a single seed, or Δ=+0.003 (resample) which is indistinguishable from noise. No p-values are provided for any CPR comparison except the SVA bootstrap.
- **W2 (Unfair size comparison):** CSS=1.0 produces 7 edges (IOI) while single methods use 50–100 edges. CPR naturally differs for circuits of different sizes. The paper never tests a size-controlled baseline (e.g., top-7 edges from the best single method). The IOI "advantage" may simply reflect that 7 random high-quality edges outperform 100 edges that include noise — this is a sparsification artifact, not a consensus benefit.
- **W3 (IOI dominance):** The sole positive result comes from one task (IOI) on one model (GPT-2 Small). All claims about "when consensus works" rest on this single confounded data point. The paper acknowledges this but still gives it 1.5 pages of discussion.
- **W4 (Qwen results are degenerate, not informative):** On Qwen-2.5 0.5B, CSS=1.0 is empty (0 edges) on both tasks. These are not "negative results" — they are trivial outcomes where the method produces no output. They add scale coverage on paper but zero analytical value beyond confirming that Jaccard≈0 → empty intersection.
- **W5 (Missing experiments):** Gemma-2 2B and Llama-3.1 8B were not attempted. Qwen Arithmetic appears projected from IOI patterns rather than independently verified. The factual recall experiment was abandoned, leaving only 3 completed GPT-2 conditions. For a paper claiming to analyze "why consensus fails," the empirical base is thin.
- **W6 (Jaccard correlation on n=3):** Section 7 presents Spearman ρ=-0.50, p=0.67 on 3 valid data points and 2 degenerate points. This is not a finding — it is an observation on insufficient data. Promoting the "Goldilocks zone" to the abstract on this basis overstates the evidence.

### Questions for Authors
- Q1: What is the CPR of the top-7 edges from EAP-IG alone on IOI? If comparable to CSS=1.0's 0.109, the consensus has no value.
- Q2: Why was multi-seed bootstrap analysis applied to SVA but not IOI or Arithmetic?
- Q3: The Qwen top-0.3% threshold was chosen to match GPT-2's ratio. Did you try absolute thresholds (e.g., top-100 edges on both models)?

### Score: 2/6 (Reject)
### Confidence: 4/5

---

## R2: Novelty, Significance, and Related Work

### Strengths
- The paper's pivot from "method paper" to "analysis paper" is the right call — negative results honestly reported are more valuable than positive results oversold
- ACDC isinf binarization analysis (§4.1) is a genuine methodological contribution: demonstrating that default ACDC thresholding creates extreme sparsity artifacts (14 edges vs 100) that inflate apparent method diversity is useful for anyone working with ACDC
- Combinatorial dilution (§5.3) is conceptually important: the observation that edge-level Jaccard decays superlinearly with edge space size (0.307→0.042 over 5.5× scaling) is a structural insight relevant to the scalability of all edge-level circuit analysis
- Writing is generally clear and well-organized; tables are informative; the paper reads efficiently

### Weaknesses
- **W1 (Straw man problem):** Binary majority voting is the simplest possible consensus mechanism. Its failure is predictable from first principles: if three methods each select top-k edges with pairwise Jaccard J, the expected three-way intersection scales roughly as J². With J=0.3, the expected three-way overlap is ~9% of the union — which is approximately what the paper finds (7 edges). The paper never engages with why binary voting was worth testing at length, nor does it test any more sophisticated consensus mechanism (score fusion, rank aggregation, weighted voting, node-level consensus). A negative result about an obviously weak approach is less informative than a negative result about a plausible one.
- **W2 (Narrow experimental scope):** The paper effectively has 3 completed conditions on GPT-2 Small (117M parameters) plus 2 degenerate conditions on Qwen-2.5 0.5B where the method produces empty output. No medium-scale model (350M–2B) bridges the gap between "works on one task" and "fails completely." The scaling narrative rests on exactly 2 data points (GPT-2 and Qwen).
- **W3 (Thin related work):** 9 references is unusually sparse for a 2026 mechanistic interpretability paper. Conspicuously absent:
  - Marks et al. (2024) — Sparse Feature Circuits, directly relevant as an alternative circuit representation
  - Lieberum et al. (2023/2024) — on scaling challenges in circuit analysis
  - Kramár et al. (2024) — AtP*, a refined attribution patching method
  - Neel Nanda's work on various circuit analyses
  - Goldowsky-Dill et al. (2023) — localizing model behavior with path patching
  - Zhang & Nanda (2024) — on circuit discovery methodology comparisons
  The absence of these references means the paper doesn't adequately position itself against the state-of-the-art or acknowledge that some of its "discoveries" (e.g., method correlation, binarization sensitivity) may already be known.
- **W4 (Goldilocks zone is unfalsifiable):** The Goldilocks zone hypothesis — that consensus works only when Jaccard is in a specific range — is presented with n=3 valid data points, a non-significant Spearman ρ, and one confounded supporting data point. It cannot be tested, falsified, or used prescriptively. Elevating it to the abstract and giving it a full section (§7) is disproportionate to the evidence.
- **W5 (Negative result about a predictable failure):** The core contribution — "binary voting doesn't work for circuit consensus" — is closer to a sanity check than a research finding. The more interesting questions (Does soft consensus work? Does node-level consensus survive scaling? Can you calibrate scores across methods?) are raised in the Discussion but never tested. The paper identifies the right research agenda but stops before the interesting work begins.
- **W6 (Framing inconsistency):** Table 3 reports IOI with zero ablation but SVA/Arithmetic with mean ablation. Section 4.3 then shows IOI's advantage is ablation-dependent. The reader must reconcile these scattered pieces to realize the paper's sole positive result is fragile — the presentation could be more forthright about this upfront.
- **W7 (CIRCUS comparison is unfair):** CIRCUS is a within-method approach not designed for cross-method consensus. Comparing it directly to CSS (a cross-method approach) is comparing across different problem formulations. The comparison would be more meaningful if both methods were applied to the same input (e.g., both applied cross-method or both within-method).

### Questions for Authors
- Q1: Have you considered testing weighted consensus (e.g., using normalized scores from each method rather than binary membership)? This would address the straw-man concern.
- Q2: The combinatorial dilution analysis extrapolates from 2 data points (GPT-2 and Qwen). Have you tried node-level (attention head) consensus to test whether dilution is specific to edge-level analysis?
- Q3: Why were no medium-scale models (GPT-2 Medium 345M, Pythia 410M) tested to characterize the scaling transition more precisely?

### Minor Issues
- "Parekh et al. 2026" — a 2026 arXiv preprint cited in a 2026 paper suggests possible self-citation or concurrent work; relationship should be clarified
- Table 3 mixes ablation methods across tasks without immediate flagging in the table caption
- Section 5.2 Qwen Arithmetic results read as projected rather than experimentally confirmed — the text should be explicit about this

### Score: 3/6 (Weak Reject)
### Confidence: 4/5

---

## Roundtable Convergence

### Areas of Agreement (both reviewers)
1. **Straw-man / naive baseline is the central flaw.** Binary majority voting's failure is mathematically predictable. The paper invests significant effort demonstrating the failure of an approach that was unlikely to succeed, without testing more plausible alternatives. Both reviewers agree this substantially limits the contribution.
2. **n=3 Jaccard-utility correlation is statistically vacuous.** The Goldilocks zone hypothesis is interesting conceptually but entirely unsupported by the evidence. It should be downgraded from a "finding" to a "speculation" and removed from the abstract.
3. **Narrow experimental scope.** Three completed conditions on one 117M model, plus two degenerate (empty-output) conditions on Qwen. No medium-scale bridge model. Scaling narrative rests on 2 data points.
4. **No statistical testing on primary claims.** CPR advantages reported as bare point estimates. Multi-seed bootstrap applied to SVA but not the sole positive case (IOI).
5. **IOI dominates all positive evidence.** One task, one model, two identified confounds. Not a robust foundation for any claim.
6. **Thin related work.** 9 references for a 2026 mechanistic interpretability paper is inadequate. Key recent work on circuit discovery methodology is missing.

### Areas of Genuine Contribution (acknowledged by both)
1. **ACDC isinf binarization analysis** — demonstrating that default thresholding creates extreme sparsity artifacts (14 vs 100 edges) that inflate apparent diversity. This is useful for practitioners.
2. **Combinatorial dilution observation** — edge-level Jaccard decays superlinearly with edge space size. This is a structural insight for scalability of circuit analysis.
3. **Ablation method sensitivity** — showing IOI advantage drops from +0.080 to +0.003 across ablation methods highlights a general confound in circuit evaluation.
4. **Honest negative reporting** — the paper does not oversell, which is commendable.

### Divergence
- R1 revised to 2/6 after agreeing with R2's straw-man critique, viewing the negative results as uninformative about a foreseeable failure. R2 maintained 3/6, finding the sub-contributions (isinf analysis, combinatorial dilution) carry some independent value even if the headline finding is weak.

---

## Final Consolidated Assessment

### Overall Score: 2/6 (Reject)

### Justification
The paper asks a reasonable question — does cross-method binary consensus improve circuit quality? — but answers it with the weakest possible consensus mechanism (binary majority voting), whose failure is predictable from the combinatorics of set intersection. The negative finding is thus less surprising and less informative than it could be. The sole positive case (IOI/GPT-2) rests on a confounded, non-size-controlled, single-seed comparison under a specific ablation method, and the Goldilocks zone hypothesis is statistically unsupported (n=3, p=0.67).

The paper does contain genuine nuggets: the ACDC isinf analysis, the ablation sensitivity finding, and the combinatorial dilution concept. However, these are individually small contributions that do not cohere into a paper-level contribution for a top ML venue. The experimental scope (3 tasks on one 117M model + 2 degenerate conditions) is insufficient, the related work is thin, and the paper stops before testing the interesting alternatives it identifies in the Discussion.

### Recommendation
The paper is below the acceptance threshold for a top ML venue. To strengthen it:
1. **Test non-trivial consensus mechanisms** — weighted score fusion, rank aggregation, or node-level consensus. The failure of these would be genuinely informative.
2. **Add size-controlled baselines** — compare CSS=1.0 (7 edges) against top-7 from each single method.
3. **Apply statistical testing uniformly** — multi-seed bootstrap on all tasks, not just SVA.
4. **Bridge the scaling gap** — test on GPT-2 Medium or Pythia 410M to characterize the transition point.
5. **Expand related work** — engage with Marks et al., Kramár et al., and other recent circuit methodology papers.
6. **Consider reformatting** as a shorter findings/workshop paper focused on the ACDC isinf binarization pathology and combinatorial dilution, which are the strongest standalone contributions.

### Scores Summary
| Reviewer | Initial | Post-Discussion | Confidence |
|----------|---------|----------------|------------|
| R1 (Methods + Experiments) | 3/6 | 2/6 | 4/5 |
| R2 (Novelty + Related Work) | 3/6 | 3/6 | 4/5 |
| **Consolidated** | — | **2/6** | **4/5** |
