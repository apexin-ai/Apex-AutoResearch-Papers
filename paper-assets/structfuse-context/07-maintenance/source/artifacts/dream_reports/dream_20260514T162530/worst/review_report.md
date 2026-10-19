---
dream_id: dream_20260514T162530
tier: worst
overall_score: 3 — Weak Reject
timestamp: 2026-05-14T17:20:17.994148+00:00
---

# Dream Review Report — "Why Hard Negative Mining Strategies Don't Differentiate for Code Retrieval at Scale"

**dream_id**: 20260514T162530  
**Review mode**: full (2 Reviewers, complete roundtable)  
**Scoring**: 6-point scale, top ML venue standards (~25% acceptance)

---

## Reviewer Scores

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Methods + Experiments | 4 (Weak Accept) | 4/5 |
| R2 | Novelty + Related Work | 3 (Weak Reject) | 4/5 |
| **Consensus** | | **3 (Weak Reject)** | **High** |

---

## Paper Summary

A negative-result paper comparing 4 hard negative mining strategies (random, embedding-distance, dataflow-aware, BM25) for contrastive code retrieval across 2 decoder-only 3B encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 seeds per condition. Central finding: no strategy reliably outperforms random at full training scale (~44K instances). The paper proposes a "geometry equalizer" mechanism—fine-tuning collapses pretrained margin differences by 65–78%—and a scale ablation showing mining advantage vanishing from +1.3pp (1K) to +0.2pp (5K).

---

## Consolidated Strengths

1. **Statistical rigor above community standard.** 9 seeds per condition with paired t-tests, Bonferroni correction, and bootstrap CIs is exemplary. The paper consistently reports uncertainty, p-values, and acknowledges power limitations (e.g., SWE-bench N=300). Both reviewers praised this. (R1, R2)

2. **Geometry equalizer mechanism is the paper's strongest contribution.** The pre- vs. post-fine-tuning margin analysis (ratio collapse from 4.35→1.29 on Qwen, 2.90→1.28 on StarCoder) goes beyond "nothing works" to "here is why nothing should be expected." This distinction elevates the paper above a pure null-result report. (R1, R2)

3. **Pool size instability is a novel methodological contribution.** Kendall τ = 0.33 between pool-50 and pool-500 rankings warns the community that strategy comparisons are fragile under evaluation parameter variation. Both reviewers independently identified this as practically useful and generalizable beyond this paper. (R1, R2)

4. **Comprehensive ablation suite.** Temperature, dynamic mining, hop count, fusion head, and distance weighting ablations systematically close potential escape hatches. The dynamic mining result (+0.05pp at 3.4× cost) is particularly valuable for practitioners. (R1)

5. **Honest framing of limitations.** The paper acknowledges LoRA constraints, 34% structural coverage, SWE-bench power limitations, and 2-encoder scope. This transparency is appropriate for a negative-result paper. (R2)

---

## Consolidated Weaknesses

### Critical (both reviewers agree)

**W1. Single-seed scale ablation undermines the central narrative.** Table 8 (strategy effect vs. training set size) is the paper's most important evidence—the monotonic decrease from +1.3pp at 1K to +0.2pp at 5K carries the "scale substitutes for curation" claim. Yet it uses only 1 seed. The trend could be noise. The abstract and introduction present this as established, not preliminary. At minimum, 3 seeds at each scale point are needed with CIs. Without replication, the core narrative rests on an unreplicated single trajectory. *This is the paper's most fixable and most damaging gap.* (R1 identified; R2 agreed strongly)

**W2. Related work is critically underdeveloped.** Only 4 formal references for a venue submission is disqualifying. Major omissions include: SimCSE (dropout-based augmentation matches hard negative mining), E5 (large-scale embedding with mining that shows improvements at scale—potentially contradicts this paper), CodeSearchNet, UniXcoder, CodeT5+ (major code retrieval baselines), false negative decontamination literature (Qu et al., 2021), curriculum learning for negatives, in-batch negatives. GraphCodeBERT and CodeBERT are named but not cited. The CoCoHaNeRe work central to the paper's framing has no formal citation. For a paper whose contribution is positioning relative to prior work, this is a serious gap. (R2 identified; R1 agreed fully)

**W3. SWE-bench evaluation is underpowered and over-interpreted.** With 300 instances, bootstrap CI width ~5pp, and all deltas ≤0.67pp, the experiment cannot distinguish "no effect" from "effect too small to detect." The paper states "no downstream signal" but the correct statement is "insufficient power to detect plausible effect sizes." The discussion then leans on downstream results as meaningful validation despite this limitation. (R1 identified; R2 agreed)

**W4. Narrow architectural scope undermines generality claims.** Two 3B decoder-only models with similar architectures (both FIM-pretrained) limit the generalizability of the geometry convergence claim. Encoder-only models (CodeBERT-family), larger models (7B+), or encoder-decoder models may behave differently. The geometry mechanism is inferred from exactly 2 data points—attribution to pos_sim saturation is post-hoc with n=2. (R1 and R2 both identified independently)

### Significant

**W5. K=3 negatives is below standard practice.** Most contrastive retrieval work uses K=7–15 hard negatives per query. With K=3, the discrimination signal from mining is inherently weak, potentially biasing toward the null result. No justification is provided, and a K=7 ablation would be a cheap experiment that could substantially strengthen (or weaken) the paper's claims. (R2 identified; R1 agreed)

**W6. BM25-embedding equivalence uninformative without overlap analysis.** The paper reports ~60% overlap between BM25 and embedding top-K negatives, yet treats BM25≈embedding as evidence of "strategy invariance." Two strategies selecting largely the same negatives producing the same result is evidence of strategy equivalence for a specific pair, not general invariance. The paper should measure pairwise Jaccard overlap across all strategy pairs and condition the null result on overlap magnitude. Additionally, the paper simultaneously claims BM25 and embedding are "equivalent" while framing CoCoHaNeRe's BM25-based harm as a distinct phenomenon—these positions are in tension. (R1 identified; R2 agreed)

**W7. CoCoHaNeRe framing is structurally risky.** The paper builds its central narrative around "contextualizing" CoCoHaNeRe's -27pp finding, but: (a) CoCoHaNeRe is not formally cited, making verification impossible; (b) the paper's own BM25 result is inconclusive; (c) the paper acknowledges it "cannot fully disentangle the confounds." The framing carries narrative weight but delivers no conclusive scientific claim. (R2 identified; R1 partially agreed)

### Minor

- **W8.** The Bonferroni correction for stratified analysis (10 strata, α_adj=0.005) is overly conservative for exploratory analysis. FDR (Benjamini-Hochberg) would be more appropriate for a paper whose purpose is to find where effects might exist. (R1)
- **W9.** Failure analysis (n=50) lacks CIs and inter-annotator agreement. The 10% "structural fix possible" has a 95% Clopper-Pearson CI of approximately [3%, 22%]. (R1)
- **W10.** "At scale" in the title is debatable—44K training instances and 5K in the scale ablation are modest by current standards (DPR ~60K, ANCE >100K). Consider qualifying as "at moderate scale." (R2)
- **W11.** RepoBench-R evaluation (Table 4) describes "inconsistent sign across encoders" verbally but should report actual signs and CIs in the table. (R1)
- **W12.** "Decoder-only encoders" is a confusing term; clarify as "decoder-only models used as encoders." (R2)

---

## Questions for Authors (prioritized)

1. **Can you provide the scale ablation (Table 8) with ≥3 seeds at each data size?** If the monotonic trend holds with CIs, this substantially strengthens the paper. This is the single highest-impact revision.

2. **What is the pairwise Jaccard overlap of top-K negatives across all four strategies?** If BM25 and embedding share 80%+ negatives, the BM25≈embedding finding is mechanistically trivial. If random and embedding have <20% overlap yet produce the same R@1, that is genuinely informative.

3. **What happens with K=7 or K=15 negatives per query?** This tests whether the null result is specific to the low-K regime.

4. **Is CoCoHaNeRe a published, peer-reviewed work?** If not, the paper needs to reframe its central narrative target.

5. **Have you measured the false negative rate per strategy?** Embedding-distance mining at high recall may select actual positives as negatives, masking its benefit.

6. **For the geometry convergence (Table 10), does margin collapse precede or follow loss plateau?** This would clarify whether the equalizer is a cause or consequence of training dynamics.

7. **Does the null result hold at R@5 and R@10?** Strategy effects invisible at R@1 may appear at other cutoffs if strategies affect ranking depth differently.

---

## Experiment Coverage Assessment

Comparing against the full experiment design reference:

| Experiment | Covered? | Notes |
|-----------|----------|-------|
| M2 Full Qwen 9-seed | ✓ Table 1 | Complete |
| M2 Full StarCoder 9-seed | ✓ Table 1 | Complete |
| SWE-bench Lite | ✓ Table 3 | Complete but underpowered |
| RepoBench-R | ✓ Table 4 | Complete |
| Stratified 5-stratum | ✓ Table 5 | Complete |
| Temperature ablation | ✓ Table 11 | Complete |
| Dynamic mining | ✓ Table 12 | Complete |
| BM25 baseline | ✓ Table 2 | Missing overlap analysis |
| Pool size sensitivity | ✓ Tables 6-7 | Complete |
| Hop count ablation | ✓ Table 13 | Complete |
| Training scale ablation | ✓ Table 8 | **Single seed — critical gap** |
| Fusion head ablation | ✓ Table 14 | Complete |
| Distance weighting ablation | ✓ Table 15 | Complete |
| Bootstrap CIs for SWE-bench | Partial | Mentioned in text, no dedicated table |
| Failure analysis (50 cases) | ✓ Table 9 | Lacks CIs/IAA |
| Qualitative examples | Partial | Mentioned briefly, no figures |
| Inference-time comparison | ✓ §5 | Discussion only, adequate |
| Geometry convergence | ✓ Table 10 | Complete |

**Coverage**: 15/18 experiments fully covered, 3 partially covered. The paper has strong experimental breadth. The critical gap is statistical: the scale ablation's single-seed design undermines the most important claim.

---

## Roundtable Dynamics

**Step 1 (Independent):** R1 scored 4 (Weak Accept), emphasizing experimental rigor and geometry mechanism. R2 scored 3 (Weak Reject), emphasizing predictability of the result and citation gaps.

**Step 2 (Cross-sharing):** R1 agreed with R2 on related work deficiency and K=3 concern, partially agreed on CoCoHaNeRe framing risk, partially disagreed on "5K ≠ at scale" (arguing scale is domain-relative). R2 agreed strongly with R1 on single-seed scale ablation as the most damaging gap, agreed on SWE-bench power limitation, and noted the single-seed concern reinforced their existing skepticism.

**Step 3 (Convergence):** Neither reviewer changed their score. The core disagreement is whether the geometry convergence mechanism provides sufficient novelty to elevate a predictable-in-principle negative result to venue quality. R1 says yes (narrowly); R2 says no (the mechanism is descriptive, not predictive, and the SimCLR precedent reduces novelty).

---

## Meta-Review and Recommendation

**Overall Score: 3 (Weak Reject)**

This is a well-executed experimental study with commendable statistical rigor (9 seeds, proper corrections, honest uncertainty reporting) and a useful mechanistic contribution (geometry equalization). The pool size instability finding alone would make a useful workshop paper.

However, the paper has several issues that place it below the acceptance bar for a top ML venue:

1. **The most important piece of evidence (scale ablation) is unreplicated.** The "scale substitutes for curation" claim—which drives the paper's title, abstract, and central narrative—rests on a single-seed trajectory. This is the gap between a borderline and a clear accept.

2. **The related work is inadequate for a venue submission.** Four references for a paper whose contribution is positioning relative to prior work is insufficient. Key baselines (SimCSE, E5, CodeSearchNet) that could either support or contradict the claims are absent.

3. **The novelty is limited.** That contrastive learning converges regardless of negative sampling strategy is expected from SimCLR-era understanding. The code-domain-specific instantiation of this finding, while useful, is incremental. The geometry convergence explanation is descriptive (documents convergence after the fact) rather than predictive (does not predict convergence rate or critical scale threshold).

4. **Narrow experimental scope** (2 decoder-only 3B models, K=3 negatives, LoRA only) limits the generality of claims stated broadly in the title and abstract.

**Path to acceptance:** (a) Multi-seed scale ablation — highest priority, (b) expand related work to ≥20 references with proper contextualization, (c) test K=7/15, (d) add 1 encoder-only model, (e) verify and cite CoCoHaNeRe or reframe. If the scale ablation replicates with CIs, the related work is expanded, and K sensitivity is addressed, this could reach Accept at revision.

**Key takeaway for the research direction:** The negative result itself is credible and the experimental apparatus is strong. The paper's weakness is presentation and scope, not fundamental methodology. The geometry convergence finding and the pool-size instability finding are both publishable contributions that need better framing and broader validation.