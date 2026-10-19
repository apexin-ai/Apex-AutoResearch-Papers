---
dream_id: dream_20260514T075732
tier: worst
overall_score: weak reject
timestamp: 2026-05-14T08:44:44.239047+00:00
---

# Dream Review Report: "A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval"

**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-14
**Venue Standard**: Top ML venue, ~25% acceptance rate, 6-point scale

---

## Roundtable Summary

| Reviewer | Focus | Independent Score | Post-Discussion Score |
|----------|-------|:-:|:-:|
| R1 | Methods + Experiments | 4/6 (Weak Accept) | 3/6 (Weak Reject) |
| R2 | Novelty + Related Work | 3/6 (Weak Reject) | 3/6 (Weak Reject) |
| **Consensus** | | | **3/6 (Weak Reject)** |

**Confidence**: 4/5

---

## Step 1: Independent Reviews

### R1 (Methods + Experiments)

**Strengths identified:**
- 54 full-scale runs (9 seeds × 3 strategies × 2 encoders) far exceeds field standard of 1–3 seeds
- Negative result is genuine and well-powered: strategy deltas <1pp vs seed std ~3pp
- Comprehensive ablation coverage: temperature, hop distance, fusion head, dynamic mining, distance weighting, data size scaling
- Data pipeline audit (Table 9) responsibly rules out engineering bugs
- Bootstrap CIs and McNemar's test are appropriate statistical choices

**Major weaknesses:**
1. **Confounded pilot-to-full comparison**: The transition from pilot (2K, 8 repos) to full-scale (15K, 123 repos) changes data volume AND data distribution simultaneously (structural_rate 0.58→0.34, files/repo 45→185, large repos 30%→56%). Table 7's subsampling experiment draws from the full-scale distribution, so it cannot reproduce the pilot's distribution. The paper cannot distinguish "scale kills signal" from "distribution kills signal," yet the entire narrative rests on the scale interpretation.
2. **No mechanistic explanation**: Qwen's representation saturation (pos_sim=0.9855) exists at both pilot and full scale. If saturation explains when dataflow helps, why does the signal exist in pilot but not full? The paper diagnoses *what* happens but not *why*.
3. **Missing neg_difficulty quartile analysis**: Explicitly planned but absent. This analysis would directly reveal whether the pilot's difficulty distribution differs from full-scale, providing the missing mechanistic link.
4. **"Scaling law" overfit**: 4 data points (1K, 3K, 5K, 15K) with no confidence intervals, no cross-encoder validation (StarCoder scaling not shown), reported to 2 decimal places (-0.11pp/1K). Does not merit the term "law."

**Minor weaknesses:**
- Temperature ablation (Table 11): Random best at all τ, including τ=0.05 where hard negatives should matter most — contradicts the mechanistic story
- Failure analysis (Table 10) backfires: dataflow actually helped 2/50 but hurt 3/50 — net negative in its own target use case
- SWE-bench results (McNemar p=0.89) are completely null, adding length without evidence
- LocAgent comparison (26.2% vs ~19%) is unflattering and inadequately discussed
- Dataflow distance weighting (§6.5) has no table — just one sentence
- Qualitative examples from the experiment plan are entirely absent

**Initial score: 4/6** — The experimental scale and honest negative result reporting are above average, but the confounded comparison and incomplete mechanistic story prevent a clean accept.

---

### R2 (Novelty + Related Work)

**Strengths identified:**
- The specific demonstration that embedding mining benefit decays with data scale in code retrieval is a concrete, falsifiable observation
- 54-run comparison practices what the paper preaches about multi-seed evaluation
- Pilot vs full-scale distributional audit is methodologically instructive
- "Cautionary tale" framing is effective for a negative result paper

**Major weaknesses:**
1. **Novelty is thin**: The central message — small-scale evaluations are unreliable, hard negative mining has diminishing returns at scale — is established knowledge in ML. Henderson et al. (2018), Dodge et al. (2019), Bouthillier et al. (2021) make the same argument in other domains. DPR showed BM25 negatives matter less as training scales. The paper treats these as discoveries rather than connecting to established patterns.
2. **Related work severely insufficient**: 9 citations in 3 short paragraphs for a 10-page analysis paper. Missing entire categories:
   - Evaluation methodology: Henderson 2018, Dodge 2019, Bouthillier 2021, Lucic 2018
   - Hard negative theory: Robinson 2021, Kalantidis 2020, Chuang 2020
   - Contrastive learning foundations: SimCLR, MoCo, DPR
   - Code representation baselines: CodeBERT, CodeT5+, UniXcoder, StarCoder original paper
   - Structural code methods: RepoGraph, RANGER, GraphCoder, CodeGRAG
3. **CoCoHaNeRe critique unsubstantiated**: The paper's opening motivation claims CoCoHaNeRe "conflated BM25-proxy negatives with true embedding-distance negatives." This is asserted but never empirically verified — no BM25 baseline is run. For a paper whose motivation rests on "correcting" a prior work, this is a disqualifying gap.
4. **"Architecturally distinct" claim questionable**: Both Qwen2.5-Coder-3B and StarCoder2-3B are decoder-only transformers. They differ in pretraining data/procedure, not architecture. This weakens the generalization argument.
5. **14 tables, 0 figures**: The scaling law cries out for a line plot. Per-seed results need box plots. Failure taxonomy would benefit from a Sankey diagram. The all-tables presentation makes the paper dense and less compelling.
6. **Zero method contribution**: No new strategy, loss function, or technique is proposed. The CodeQL pipeline is engineering, and its value is undermined by the paper's own conclusion that structural negatives don't help.

**Minor weaknesses:**
- Pool size of 50 never discussed or ablated; strategy rankings may change at realistic pool sizes (hundreds of files)
- Checkpoint selection criterion unspecified; strategy rankings can reverse depending on best-loss vs best-R@1 selection
- 34% structural data coverage underreported as limitation — 2/3 of instances get no structural signal, making dataflow strategy a mixture of random + structural
- No learning curves or overfitting analysis despite apparent overfitting at step 1000
- Open-source CodeQL pipeline claim is undermined by the negative finding about structural negatives

**Initial score: 3/6** — Above-average experimental effort but thin novelty, severely insufficient related work, unsubstantiated motivating critique, and no method contribution.

---

## Step 2: Cross-Discussion

### Points of Agreement (both reviewers converge):

1. **"Scaling law" is overstated** — Both agree 4 data points without CIs cannot be called a "law." Should be "trend" or "observation."
2. **Missing experiments weaken the paper** — Neg_difficulty quartile analysis, qualitative examples, and tabulated distance-weighting results are all absent from what was planned.
3. **Experimental scale is genuinely impressive** — 54 runs is commendable and exceeds field norms.
4. **The negative result itself has value** — The community benefits from knowing pilot signals don't replicate at scale.

### R1 adjustments after seeing R2's review:

R1 acknowledges that the related work gap is more severe than initially assessed. For an analysis/empirical paper, the literature positioning is critical — the paper must show what is already known vs. what is new. With only 9 citations and missing the evaluation methodology literature, the paper fails to establish that its contribution is novel. R1 also agrees that the CoCoHaNeRe critique being unverified is a significant gap that weakens the paper's motivation.

R1 finds R2's point about "architecturally distinct" being misleading to be valid — both are decoder-only models, so the encoder diversity claimed is overstated.

R1 agrees the 0-figure presentation is a major weakness for this type of analysis paper.

**R1 adjusts score from 4/6 to 3/6**, primarily due to the related work insufficiency and unsubstantiated CoCoHaNeRe critique — issues R1 had not weighted heavily in the methods-focused review.

### R2 adjustments after seeing R1's review:

R2 agrees that the confounded pilot-to-full comparison is the paper's most critical methodological flaw and should be elevated in importance. The inability to distinguish scale effects from distribution effects undermines the paper's central narrative.

R2 finds R1's observation about the temperature ablation (random best at τ=0.05, where hard negatives should matter most) to be an important internal contradiction that R2 had not flagged.

R2 also agrees the failure analysis backfiring (hurt 3 > helped 2) deserves more prominent framing.

**R2 maintains score at 3/6** — R1's observations reinforce rather than mitigate the weaknesses already identified.

---

## Step 3: Convergence

### Consensus Score: 3/6 (Weak Reject)

### Agreed Major Issues (ranked by severity):

1. **Confounded pilot-to-full comparison** — The paper cannot separate scale from distribution shift. This undermines the central "scale kills signal" narrative and the claimed scaling law. The subsampling experiment (Table 7) partially addresses this but draws from the full-scale distribution, not the pilot distribution.

2. **Related work critically insufficient** — 9 citations for a 10-page analysis paper at a top venue is far below expectations. Missing evaluation methodology literature (Henderson, Dodge, Bouthillier), hard negative theory (Robinson, Kalantidis), contrastive learning foundations (SimCLR, MoCo, DPR), and code representation baselines. Without positioning against existing knowledge, the paper's novelty cannot be assessed.

3. **CoCoHaNeRe critique unverified** — The paper's opening motivation asserts a flaw in CoCoHaNeRe without running a BM25 baseline to demonstrate it. The entire "correcting a misconception" framing collapses without empirical verification.

4. **"Scaling law" overstated** — 4 data points, no CIs, single encoder, no theoretical backing. Should be "trend" or "observation" with appropriate caveats.

5. **No mechanistic explanation** — The paper shows *what* (signal vanishes) but not *why* (the saturation argument doesn't explain pilot-vs-full differences). The missing neg_difficulty quartile analysis would have been the key mechanistic evidence.

6. **Presentation: 14 tables, 0 figures** — Dense, hard to skim, and fails to leverage visual communication for key findings.

### Agreed Minor Issues:

7. Two "architecturally distinct" encoders are both decoder-only transformers — overstated diversity claim.
8. Dataflow distance weighting (§6.5) deserves a table, not one sentence.
9. Qualitative examples are entirely absent.
10. Pool size of 50 never discussed; may affect strategy rankings.
11. Checkpoint selection criterion unspecified.
12. 34% structural data coverage means dataflow strategy is 2/3 random fallback — understated limitation.
13. Temperature ablation (random best even at τ=0.05) contradicts the mechanistic story but is not discussed.
14. Failure analysis shows net negative impact (hurt 3 > helped 2) for dataflow in its own target use case.

---

## Step 4: Consolidated Assessment

### Summary

This paper presents a large-scale negative result study (54 training runs) showing that hard negative mining benefits observed at pilot scale (~2K instances) for contrastive code retrieval do not replicate at full scale (15K instances, 9 seeds). The experimental effort is genuine and above field norms. The negative result itself is informative: strategy-level R@1 deltas (<1pp) are dwarfed by seed variance (~3pp), and no strategy achieves statistical significance over random sampling (bootstrap p ≥ 0.68).

### Strengths

- **Experimental scale**: 54 runs (9 seeds × 3 strategies × 2 encoders) with bootstrap CIs is well above the 1–3 seed standard in code retrieval.
- **Honest negative result reporting**: The paper does not oversell null findings and includes a thorough data pipeline audit ruling out engineering errors.
- **Comprehensive ablations**: Temperature, hop distance, fusion head, dynamic mining, distance weighting, and data size scaling are all tested and reported.
- **Scaling trend**: The observation that embedding benefit decays with data size (from +1.3pp at 1K to -0.2pp at 15K) is a concrete and useful finding, even if "scaling law" overstates it.
- **Failure taxonomy**: The manual analysis of 50 retrieval failures provides useful error categorization for the community.

### Weaknesses

- **Confounded central comparison**: The pilot-to-full transition changes both data volume and distribution. The paper's central narrative ("scale kills mining benefit") cannot be distinguished from "distribution shift kills mining benefit" without a controlled experiment.
- **Critically thin related work**: 9 citations in 3 paragraphs, missing evaluation methodology, contrastive learning theory, and code representation baselines. Novelty cannot be assessed without proper positioning.
- **Unsubstantiated motivation**: The CoCoHaNeRe critique is asserted without empirical verification (no BM25 baseline).
- **Overstated "scaling law"**: 4 data points, no confidence intervals, single encoder — should be "trend."
- **No method contribution**: Tests existing methods and finds they fail. CodeQL pipeline's value is undermined by the negative finding.
- **0 figures in 10 pages**: Dense table-only presentation fails to communicate key findings visually.
- **Missing planned experiments**: Neg_difficulty quartile analysis, qualitative examples, and tabulated distance-weighting results are absent.

### Recommendation

**Weak Reject (3/6)**. The paper demonstrates above-average experimental discipline and reports a genuine negative result, but it falls short of top-venue standards due to: (1) confounded central comparison that undermines the claimed mechanism, (2) critically insufficient related work that prevents novelty assessment, (3) unsubstantiated motivating critique of prior work, and (4) overstated "scaling law." The paper reads as a thorough project report rather than a paper with sufficient insight density for a top ML venue.

### Path to Revision

1. **Deconfound scale vs distribution**: Run a controlled experiment with pilot-distribution subsamples at increasing sizes (1K, 3K, 5K from pilot-like repos only) AND full-distribution subsamples at pilot size (2K from 123 repos). This isolates the two effects.
2. **Expand related work to 25+ citations**: Add evaluation methodology (Henderson 2018, Dodge 2019, Bouthillier 2021), hard negative theory (Robinson 2021, Kalantidis 2020), contrastive learning foundations (SimCLR, MoCo, DPR), code baselines (CodeBERT, CodeT5+, StarCoder), and structural methods (RepoGraph, RANGER).
3. **Add BM25 negative baseline**: Empirically verify the CoCoHaNeRe critique.
4. **Rename "scaling law" to "scaling trend"**: Report with CIs and cross-encoder validation.
5. **Add 3–4 key figures**: Scaling trend line plot, seed-variance box plots, failure taxonomy Sankey, stratified heatmap.
6. **Include neg_difficulty quartile analysis**: This is the missing mechanistic link.
7. **Stratify by structural data availability**: Report results separately for the 34% of instances with structural data vs the 66% without.

### Experiment Coverage Assessment

| Planned Experiment | Coverage | Notes |
|---|:-:|---|
| M2 Full Qwen 9×3 | ✅ Complete | Table 1 |
| M2 Full StarCoder 9×3 | ✅ Complete | Table 2 |
| SWE-bench Lite | ✅ Complete | Tables 3–4 |
| RepoBench-R | ✅ Complete | Table 5 |
| Stratified Analysis | ⚠️ Partial | Repo-size done (Table 8), neg_difficulty quartile missing |
| Hop-Distance Ablation | ✅ Complete | Table 12 |
| Data Size Scaling | ✅ Complete | Table 7 |
| Fusion Head Ablation | ✅ Complete | Table 13 |
| Dataflow Distance Weighting | ⚠️ Partial | One sentence in §6.5, no table |
| Failure Analysis 50 cases | ✅ Complete | Table 10 |
| Qualitative Examples | ❌ Missing | Entirely absent |
| Temperature Ablation | ✅ Complete | Table 11 |
| Dynamic vs Static Mining | ✅ Complete | Table 14 |
| Bootstrap CI SWE-bench | ✅ Complete | Table 4 |
| Inference-Time Comparison | ✅ Complete | Table 6 |
| Data Pipeline Audit | ✅ Complete | Table 9 |

**Coverage**: 12/16 complete, 2/16 partial, 1/16 missing. The missing/partial items (neg_difficulty quartile, qualitative examples, distance weighting table) would have meaningfully strengthened the analysis.

---

*Review conducted by R1 (Methods + Experiments) and R2 (Novelty + Related Work) with full roundtable protocol.*