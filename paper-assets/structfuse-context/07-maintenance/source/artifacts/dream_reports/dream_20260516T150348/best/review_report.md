---
dream_id: dream_20260516T150348
tier: best
overall_score: 3/6 Weak Reject
timestamp: 2026-05-16T16:08:04.259095+00:00
---

# Dream Review Report: "What Makes Hard Negatives Work for Code Retrieval?"

**dream_id:** 20260516T150348 | **review_mode:** full | **Reviewers:** R1 (Methods+Experiments), R2 (Novelty+Related Work)

---

## Paper Summary

This paper presents a controlled comparison of four hard negative mining strategies (random, static embedding-distance, dataflow-aware structural, BM25-based) for contrastive code retrieval across two 3B-parameter encoders (Qwen2.5-Coder-3B, StarCoder2-3B) and one 125M encoder (UniXcoder). Three contributions are claimed: (1) static embedding-distance mining reliably improves retrieval (+1.4pp Qwen, +0.9pp StarCoder on held-out eval), refuting CoCoHaNeRe's negative result; (2) structure-grounded negatives interact with encoder representation geometry; (3) checkpoint selection criterion effects (up to +16.3pp) exceed mining strategy effects by 7×, revealing an evaluation methodology confound. The paper includes 14 tables, extensive ablations, and external validation on RepoBench-R.

---

## Roundtable Process

### Step 1: Independent Reviews

**R1 (Methods + Experiments): 3/6 (Weak Reject), Confidence 4/5**
**R2 (Novelty + Related Work): 3/6 (Weak Reject), Confidence 4/5**

### Step 2: Cross-Sharing Summary

After exchanging reviews, both reviewers noted complementary concerns:

- R1's statistical critique (instance-level bootstrap masking seed-level variance; only 3 seeds, with s42 Qwen requiring different training regime effectively reducing to 2 seeds for some comparisons) reinforces R2's practical significance concern about ~1pp effects.
- R2's novelty critique (core finding recapitulates ANCE applied to code) was acknowledged by R1 as outside their focus but reasonable — "well-designed study whose results turned out more modest than hoped."
- Both reviewers independently identified the same strongest contribution (checkpoint criterion finding) and the same weakest claim (representation geometry interaction).
- R2's observation about the dataflow strategy being confounded with BM25 ranking (negatives are structurally disconnected but ranked by BM25) was recognized by R1 as an important unaddressed confound.

### Step 3: Convergence

**Points of agreement (high confidence):**

1. **Checkpoint criterion finding is the paper's genuine insight.** Both reviewers consider the +16.3pp observation valuable, but both note the number is seed-specific (s43 outlier; s42 shows 0.0pp gap). The median criterion effect (~3.5pp) better represents the typical case. The 7:1 ratio is computed from the mean, which is skewed. Recommendation: reframe around median and variance, not max.

2. **Effect sizes are small and practically questionable.** +1.4pp (Qwen) and +0.9pp (StarCoder) R@1 on held-out eval, shrinking to +0.3pp and +0.6pp under standard eval. While statistically significant, no downstream task evaluation connects these R@1 improvements to practical value. The one attempt (SWE-bench) failed catastrophically.

3. **CoCoHaNeRe "refutation" is overstated.** No direct evidence is provided for the claimed BM25-proxy conflation. The paper cites CoCoHaNeRe as studying the same problem, but CoCoHaNeRe studies NL-to-code search (bimodal) while this paper studies code-to-code file retrieval (unimodal). The critique also omits gradient-based methods, which were CoCoHaNeRe's recommended alternative. A "correction in a different setting" framing would be more honest than "empirical refutation."

4. **"Representation geometry" (Contribution 2) is under-evidenced.** With n=2 encoders differing in pretraining data, tokenizer, objective, and model family, attributing differential dataflow effects to "representation geometry" is post-hoc rationalization. The stratified analysis (Q1: +0.6pp → Q4: +2.3pp) shows harder instances benefit more from harder negatives — this is a property of InfoNCE, not a discovery about geometry. Actual geometric analysis (isotropy, intrinsic dimensionality, uniformity/alignment) is absent. The title's "Representation Geometry" promise is not delivered.

5. **Bibliography is inadequate.** 7 references in the compiled paper. For a self-described "systematic study," this is critically thin. Missing: ANCE's full context (DPR, SimCLR, HCL, DCL, MoCHi, ProGCL, WCL), code retrieval baselines (CodeBERT, UniXcoder's original paper, RepoGraph), curriculum learning connections (CL-DRD, CAPSTONE), and sentence embedding foundations (SimCSE, Sentence-BERT). Multiple works mentioned in text (ARISE, RANGER, CodexGraph) lack bib entries.

**Points of disagreement (resolved):**

- R1 raised concerns about experiments being "imagined" vs. completed (placeholder markers in tex, some experiments queued). R2 did not flag this independently but agreed it is a serious concern if true. **Resolution:** This is a legitimate concern about manuscript maturity, but for the dream review we evaluate the paper as presented (all tables contain concrete numbers).

- R1 suggested the UniXcoder null result conflates scale with architecture. R2 agreed but rated this as a moderate rather than major issue. **Resolution:** The paper acknowledges this in limitations. It weakens the "scale boundary" claim but does not invalidate the null result itself. Rated as moderate.

**No score movement after cross-sharing.** Both reviewers maintain 3/6.

---

## Consolidated Review

### Strengths

1. **Well-controlled experimental design.** The 4-strategy × 2-encoder × 3-seed matrix with fixed training pipeline (same LoRA config, data, K=7) isolates the mining strategy variable cleanly. This is methodologically superior to most mining strategy papers.

2. **The BM25 vs. embedding-distance disentanglement is a useful empirical distinction.** Demonstrating that BM25 negatives consistently harm (−2.2 to −3.2pp) while true embedding-distance negatives consistently help (+0.9 to +1.4pp), with a 4-strategy ordering BM25 < random < dataflow ≤ embedding replicated across both encoders and RepoBench-R, is the paper's cleanest finding.

3. **Checkpoint criterion finding is genuinely surprising and practically valuable.** The observation that checkpoint selection methodology can introduce variation far exceeding the effect being measured is an important cautionary finding for the contrastive retrieval community.

4. **Comprehensive ablation suite.** Temperature (3 settings), pool size (4 settings), hop depth (3 settings), data scaling (3 sizes), fusion head, weighted vs. binary, static vs. dynamic mining, and UniXcoder scale boundary. The static vs. dynamic null result is particularly informative.

5. **Honest limitation disclosure.** SWE-bench OOD failure reported transparently. Effect sizes stated plainly. Dataflow result framed as exploratory. This builds credibility.

6. **Cross-benchmark validation.** RepoBench-R results with non-overlapping CIs confirm strategy ranking transfers beyond the training domain.

### Weaknesses

1. **(Major) Novelty below top-venue threshold.** The core recommendation — "use static embedding-distance negatives for contrastive retrieval" — recapitulates ANCE (Xiong et al., 2021) applied to code. The paper does not articulate what is fundamentally different about code that makes this finding non-obvious. Analysis papers at top venues deliver counterintuitive insights; "embedding negatives help for code too" does not meet that bar.

2. **(Major) Effect sizes are small and disconnected from practical impact.** +0.9–1.4pp R@1 on held-out eval, +0.3–0.6pp under standard eval. No downstream task evaluation. The paper's own Contribution 3 undermines Contribution 1: if evaluation methodology introduces 7× more variance than mining strategy, the practical takeaway is "fix evaluation, don't worry about mining" — making the mining comparison secondary.

3. **(Major) Statistical framework masks seed-level variance.** Instance-level bootstrap (10K resamples) produces tight CIs because N_instances is large, but this hides between-seed variance. With only 3 seeds (effectively 2 for some Qwen comparisons where s42 used a different training regime), seed-level effects are poorly characterized. The paper should report per-seed deltas alongside instance-level CIs.

4. **(Major) CoCoHaNeRe refutation lacks direct evidence.** No specific passage from CoCoHaNeRe is cited to support the "BM25 proxy" claim. The tasks differ (NL-to-code vs. code-to-code). Gradient-based methods (CoCoHaNeRe's recommended approach) are excluded from comparison. "Refutation" should be downgraded to "complementary finding in a different setting."

5. **(Major) "Representation Geometry" claim is unsupported.** Two-encoder observation of different dataflow responses attributed to "geometry" without any geometric analysis (isotropy, intrinsic dimensionality, uniformity/alignment). The stratified Q1→Q4 pattern is a consequence of InfoNCE mechanics, not a geometry discovery. The title overpromises.

6. **(Major) Bibliography critically inadequate.** 7 references for a "systematic study" paper is below the minimum for any ML venue. Key missing citations span contrastive learning foundations, code retrieval baselines, and curriculum learning connections.

7. **(Significant) Scope insufficient for "systematic study" claim.** Python-only, one primary training dataset (SWE-smith), two effective encoders (both 3B decoder-only), zero gradient-based mining baselines. The title claims comprehensiveness the experiments don't deliver.

8. **(Significant) Checkpoint criterion finding is seed-specific.** The headline +16.3pp is from seed 43. Seed 42 shows 0.0pp. The median is ~3.5pp. The 7:1 ratio uses the mean, heavily skewed by s43. The finding is real but the headline number overstates its typicality.

9. **(Moderate) Dataflow strategy is confounded with BM25.** Dataflow negatives are structurally disconnected files *ranked by BM25*. When dataflow underperforms, it's unclear whether structural filtering is unhelpful or whether BM25 ranking within the filtered set introduces the same harmful lexical-overlap bias identified for pure BM25.

10. **(Moderate) No K ablation.** K=7 negatives is fixed. Given K directly controls the hardness-to-noise ratio in InfoNCE, this is a meaningful omission for a "systematic study."

### Questions for Authors

1. Can you provide per-seed embedding-vs-random deltas for the main Table 2 comparisons? How variable is the effect across seeds?

2. What specific CoCoHaNeRe methodology passage supports the "BM25 proxy" claim? Do you acknowledge they study bimodal NL-to-code search?

3. How does this differ from applying ANCE to code? What code-specific property makes static embedding-distance mining non-obvious?

4. The checkpoint criterion effect ranges from 0.0pp to 16.3pp. What determines whether a seed exhibits this divergence? Is s43's 16.3pp a pathological training run?

5. Why are gradient-based mining methods excluded despite framing against CoCoHaNeRe's gradient-based approach?

6. Have you computed geometric measures (isotropy, uniformity/alignment) to substantiate the "representation geometry" claim?

7. The dataflow strategy uses BM25 for ranking within structurally disconnected files. Have you tested dataflow with random or embedding-distance ranking instead to isolate the structural filtering contribution?

8. How do you reconcile that under standard evaluation (Table 1), dataflow *hurts* both encoders (Qwen −1.1pp, StarCoder −0.7pp)?

---

## Scores

| Reviewer | Score | Confidence |
|----------|-------|------------|
| R1 (Methods+Experiments) | 3/6 (Weak Reject) | 4/5 |
| R2 (Novelty+Related Work) | 3/6 (Weak Reject) | 4/5 |
| **Consensus** | **3/6 (Weak Reject)** | **4/5** |

## Meta-Review Assessment

The paper tackles an important and under-studied question with commendable experimental rigor. The controlled 4-strategy comparison and the checkpoint criterion finding are genuine contributions to the community's understanding. However, three fundamental issues prevent acceptance:

1. **Novelty:** The core finding recapitulates established text retrieval knowledge (ANCE) applied to code without identifying code-specific insights that would surprise the community.

2. **Effect magnitude vs. claims:** The ~1pp mining strategy effects are dwarfed by the paper's own evaluation methodology finding (7:1 ratio), creating an internal tension where Contribution 3 undermines Contribution 1's significance.

3. **Claim calibration:** "Representation Geometry" in the title, "empirically refuting" CoCoHaNeRe, and "systematic study" all overpromise relative to what the evidence supports.

**Recommendation:** The paper would benefit from (a) reframing Contribution 3 (evaluation methodology) as the primary contribution with mining comparison as supporting evidence, (b) adding gradient-based mining baselines to substantiate the CoCoHaNeRe critique, (c) expanding the bibliography and related work substantially, (d) reporting per-seed statistics alongside instance-level bootstrap, and (e) either conducting proper geometric analysis or removing "Representation Geometry" from the title. With these changes, this could be a solid contribution to a software engineering venue (ICSE, ASE, MSR) or an NLP workshop. For EMNLP Main at the current state, the novelty and insight depth are insufficient.

**Overall: 3/6 (Weak Reject)**