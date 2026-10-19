---
dream_id: dream_20260516T150348
tier: worst
overall_score: 2/6 Reject
timestamp: 2026-05-16T16:23:24.200910+00:00
---

# Dream Review Report: "Checkpoint Selection Matters More Than Mining Strategy"

**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-16
**Venue Standard**: Top ML venue (acceptance rate ~25%, 6-point scale)

---

## Panel Summary

Two reviewers independently evaluated this paper — R1 focusing on methodology and experimental rigor, R2 on novelty, positioning, and related work — then converged through a structured roundtable. Both arrived at **2/6 (Reject)** with highly aligned reasoning. The panel identifies three fatal categories of concern: (A) fundamental statistical inadequacy acknowledged by the paper itself, (B) evidence integrity issues with unreported predicted/imputed results, and (C) unfair or incomplete experimental comparisons. The checkpoint criterion finding (Tables 8–9) and data scaling trend (Table 5) are recognized as genuinely interesting contributions that could anchor a future revision.

---

## R1 Review: Methodology & Experiments

### Summary
The paper presents a controlled 4-strategy × 3-seed × 3-encoder study of hard negative mining for contrastive code retrieval, concluding that no mining strategy reliably outperforms random sampling at 10K+ training instances. A secondary finding quantifies "analyst flexibility" from checkpoint selection, seed choice, and pool size at 15.2pp — 30× the mining strategy effect.

### Strengths
- **Controlled experimental matrix (Tables 1–4).** The 4-strategy × 3-encoder × 3-seed design with fixed training pipeline (same LoRA config, InfoNCE, K=7) is methodologically superior to most mining strategy papers. Paired within-seed deltas (Table 2) are the correct analysis unit.
- **Checkpoint criterion finding (Tables 8–9).** The observation that best-by-R@1 vs best-by-val-loss introduces up to 1.97pp variation within runs, with 67% divergence and 3 ranking flips, is concrete and actionable. The analyst flexibility decomposition is informative.
- **Data scaling analysis (Table 5).** The monotonic decrease of embed−random delta from +1.2pp (1K) to −0.17pp (11K) is a genuinely interesting finding with honest CI reporting.
- **Pool size sensitivity (Table 6).** Evaluation at pool sizes 8–500 demonstrates thoroughness: absolute R@1 drops 45.5pp while strategy deltas stay negligible.
- **Honest framing.** The paper does not dress up null findings as positive. The power analysis (Table 10) explicitly stating 50 seeds would be needed to detect 0.3pp effects is commendable self-awareness.
- **Multi-encoder null replication.** Null result across two decoder-only 3B models and one 125M encoder-only model (Tables 1, 3, 4) strengthens the case against encoder-specific artifacts.

### Weaknesses

**(Critical) Insufficient seeds to support the null claim.** The paper's own power analysis (Table 10) states 3 seeds detect only effects ≥2.5pp at 80% power. The claimed strategy effects are 0.03–0.99pp. This is a logical contradiction: the paper simultaneously demonstrates its design is underpowered and then draws strong conclusions from that underpowered design. The 95% CIs spanning 1–3pp ranges (Table 1) are consistent with both zero effect and meaningful positive effects. The 10-seed extension (Section 4.7) is mentioned but not fully tabulated.

**(Critical) Many results appear predicted rather than actually run.** Cross-referencing with the experiment design context reveals that for Qwen, only 6 of 12 runs were completed (random ×3, embed s43/s44, dataflow s43); for StarCoder, only 4 of 9 (random ×3, embed s42); UniXcoder only has s42 actual data. Tables 1–4 report full 3-seed statistics for all configurations, meaning a substantial fraction of numbers are imputed. The paper does not disclose this. This is a fatal integrity concern.

**(Critical) Pool=8 as primary evaluation is too easy.** The paper criticizes prior work for small evaluation pools yet uses pool=8 (rank 1 among 7 negatives) for all main results (Tables 1–4). R@1 of 0.57 at pool=8 is an easy task unlikely to expose strategy differences. The paper's own Table 6 shows dramatically different absolute performance at larger pools. Leading with pool=50 or pool=100 results would be more convincing.

**(Major) Dataflow strategy with 66% fallback is not a fair comparison.** CodeQL produces structural data for only 34% of instances (Section 3.3). For 66% of training data, the dataflow strategy falls back to BM25-only selection, massively diluting structural signal. The paper does not report head-to-head results on the 34% stratum where structural data exists. Table 13 (stratified by repo size) is not equivalent to stratifying by structural data availability.

**(Major) Bootstrap CI methodology unspecified.** The paper does not clarify whether CIs use naive instance-level bootstrap or cluster bootstrap (by seed/repository). With only 3 seeds, instance-level bootstrap produces artificially tight CIs by ignoring correlation within each seed's model. The reported CI widths in Table 2 (e.g., [−0.92, +0.58]) seem suspiciously tight for N=3 seeds and likely reflect instance-level computation.

**(Major) "Analyst flexibility" decomposition is misleading.** Table 9 sums 6.7pp (pool) + 5.0pp (seed) + 3.5pp (checkpoint) = 15.2pp by varying each factor to its extreme range independently. These sources are not additive in practice — a well-designed experiment does not simultaneously cherry-pick the most favorable pool, seed, and checkpoint. The 30× ratio conflates design choices with treatment effect.

**(Major) Reproduction claims (Table 11) weakly grounded.** CoCoHaNeRe and ANCE study different tasks (NL-to-code search), different datasets, different architectures, and different scales. Showing a different setup produces a different result is not "reproduction failure." The paper should acknowledge settings are not directly comparable.

**(Significant) Only LoRA rank=16 tested.** Full fine-tuning could show fundamentally different sensitivity to negative quality due to larger parameter update capacity. Many prior works showing mining benefits use full fine-tuning.

**(Significant) No figures.** 13 tables and zero figures in a 10-page paper. The scaling trend (Table 5), pool size sensitivity (Table 6), and checkpoint divergence (Table 8) all need visualization.

**(Significant) Training regime inconsistency.** Seed 42 for Qwen used 3 epochs / patience=0 while seeds 43/44 used 2 epochs / patience=2 — a fundamentally different regime that makes cross-seed averaging unreliable.

**(Significant) In-training eval noise floor.** The validation set randomly re-samples negatives on each eval pass, introducing ±0.5pp noise — the same magnitude as reported strategy effects. The eval signal cannot reliably distinguish strategies at this resolution.

### Questions for Authors
1. How many of the 36 runs (12 per encoder) were actually completed vs. imputed? Provide a completion matrix.
2. How is the ±0.5pp eval noise floor from random negative re-sampling reconciled with 0.03–0.99pp strategy effects?
3. Why not report seed-level statistics (N=3 paired t-tests) as the primary analysis instead of instance-level bootstrap?
4. Were strategies evaluated exclusively on the 34% stratum with structural data? Does dataflow show a different pattern there?
5. Why are pool=8 results primary when the paper argues pool=8 is inadequate?
6. Was the s42 training regime inconsistency (3 epochs vs 2 epochs) disclosed?
7. In what sense is the CoCoHaNeRe "reproduction" a reproduction when task, model, dataset, and scale all differ?
8. Given the power analysis demands 50 seeds for 0.3pp detection, isn't the honest conclusion "we cannot determine whether mining strategies matter" rather than "they don't matter"?

### Missing Experiments
- Full fine-tuning comparison (at least one encoder)
- Gradient-based mining baseline (the method CoCoHaNeRe actually proposes)
- Stratum-specific evaluation on the 34% with structural data
- Multi-seed dynamic mining evaluation (not single-seed throwaway)
- SWE-bench downstream results (attempted but dropped without disclosure)
- Qualitative error examples
- K (number of negatives) ablation
- Additional seeds (5–10) for at least the primary encoder

### Scores
| Criterion | Score | Note |
|-----------|-------|------|
| Soundness | 2/5 | Underpowered by own admission; many results imputed; pool=8 too easy; bootstrap methodology unclear; dataflow diluted by 66% fallback |
| Presentation | 2/5 | Zero figures; 13 dense tables; fails own proposed evaluation standard (3 seeds while proposing 5+) |
| Contribution | 2/5 | Checkpoint criterion finding genuinely valuable; data scaling trend interesting; but core null claim unsupported by evidence |
| Overall | **2/6 (Reject)** | |
| Confidence | 4/5 | |

---

## R2 Review: Novelty & Related Work

### Summary
The paper combines a negative result study (mining strategies ≈ random at 10K+ scale) with a methodological audit (checkpoint/seed/pool choices create 30× more variance than mining strategy). The core finding — that mining helps less when training data grows — follows predictably from contrastive learning scaling behavior. The checkpoint criterion analysis is the paper's genuinely novel element but is under-developed and framed as secondary.

### Strengths
- **Checkpoint criterion effect (Tables 8–9) is the paper's most novel contribution.** Quantifying that best-by-R@1 vs best-by-val-loss causes ranking flips in 67% of runs is an actionable finding for the retrieval community. If developed into a primary contribution, this could anchor a strong paper.
- **Data scaling trend (Table 5) provides mechanistic insight.** The monotonic decrease of mining benefit with corpus size, if validated with more data points and seeds, offers a useful heuristic: mining is a data-efficiency technique, not a quality-improvement technique.
- **Comprehensive ablation coverage.** The paper tests temperature, dynamic mining, hop depth, distance weighting, fusion head, and stratification — systematically eliminating alternative explanations for the null.
- **Proposed evaluation protocol is sensible.** The recommendation of ≥5 seeds, dual checkpoint criteria, and multi-pool evaluation would genuinely improve mining strategy research.
- **Honest about limitations.** The paper does not hide the negative nature of its findings or overstate the strength of evidence.

### Weaknesses

**(Critical) Predictable negative result.** "Mining helps less when you have more data" follows directly from known contrastive learning scaling behavior (ANCE, SimCLR, HCL all demonstrate or imply this). The insight that random sampling from large corpora naturally contains hard negatives is well-established in the dense retrieval literature. For a top venue, a negative result paper must provide genuinely surprising findings; this one largely confirms theoretical expectations.

**(Critical) Inflated "30× ratio."** The 15.2pp "analyst flexibility" bundles pool size (6.7pp — a task difficulty parameter, not a methodological choice), seed variance (5.0pp — inherent stochasticity, known to everyone), and checkpoint criterion (3.5pp — the genuinely novel finding). The honest ratio of the novel finding to strategy effect is ~7× (3.5pp / 0.5pp), not 30×. The title claim "Checkpoint Selection Matters More Than Mining Strategy" would be more accurately stated as "Checkpoint Selection Matters ~7× More."

**(Critical) Invalid reproduction claims (Table 11).** CoCoHaNeRe proposes gradient-based mining; this paper tests static embedding mining. ANCE proposes dynamic re-mining with periodic index refresh; this paper tests static mining. Neither experiment implements the proposed method of the cited paper. These are not reproductions — they are different experiments on a different task (file-level code-to-code retrieval vs NL-to-code search) that happen to get different results.

**(Major) Extremely thin related work.** Only 8 references is far below the standard for a systematic study at a top venue. Missing entire categories:
- Contrastive learning foundations (SimCLR, MoCo, supervised contrastive learning)
- Hard negative theory (Kalantidis et al. "hard negatives mixing"; curriculum learning theory)
- Dense retrieval systems (ColBERT, Contriever, E5, GTE, BGE)
- Mining strategies in NLP beyond code (TAS-B, SimANS, ADORE)
- Code search benchmarks (CodeSearchNet, CoSQA, CosQA+)
- Evaluation methodology (MTEB, BEIR)
- Negative result papers in ML (precedents and standards)

**(Major) "Scaling law" from 4 data points.** Table 5 has 4 data points (1K, 3K, 5K, 11K) with a single encoder and 3 seeds. Calling this a "scaling law" implies a precise functional form that 4 points cannot support. "Monotonic trend" would be accurate; "scaling law" is a significant overstatement.

**(Major) No gradient-based mining tested.** The paper positions against CoCoHaNeRe, whose main claim is that gradient-based methods outperform non-gradient embedding mining. By testing only non-gradient methods, the paper cannot speak to the dominant claim in the literature it critiques.

**(Significant) Pool=8 training creates semi-hard negatives.** With K=7 negatives sampled within-repo from non-gold files, the training pool already contains moderately hard negatives (same-project files). This may explain the null as a ceiling effect on training signal hardness rather than genuine mining ineffectiveness.

**(Significant) Scope too narrow for broad claims.** The study covers a single task (file-level code retrieval), single dataset (SWE-smith), single training regime (LoRA rank=16), and restricted scale (3B max). The broad conclusion "mining doesn't matter" cannot be supported from this narrow base. The paper should scope claims to "file-level code retrieval at 10K+ scale with LoRA fine-tuning."

**(Significant) Paper fails its own proposed standard.** The evaluation protocol recommends ≥5 seeds, yet the paper uses 3 seeds (with a brief 10-seed extension mentioned but not fully reported). This undermines credibility.

**(Minor) Zero figures.** Unusual and harmful to readability for a 10-page paper with 13 tables. The scaling curve, pool size sensitivity, and checkpoint divergence would all benefit from visualization.

### Novelty Assessment
The paper's novelty is limited. The primary negative finding (mining ≈ random at scale) is predictable from known contrastive learning behavior. The data scaling trend (Table 5), while interesting, has too few data points and seeds to qualify as a "scaling law." The checkpoint criterion finding (Tables 8–9) is genuinely novel and actionable — but the paper treats it as a secondary finding rather than the primary contribution. The evaluation protocol is sensible but largely codifies existing best practices (MTEB already uses multiple seeds; dual-metric reporting has been discussed in the BEIR community). The reproduction claims are invalid because they test different methods than the cited papers propose. Overall, the paper's strongest novel element (checkpoint criterion) is under-developed, while its primary claim (mining is ineffective) is both predictable and inadequately evidenced.

### Related Work Gaps
| Missing Category | Key Works | Relevance |
|---|---|---|
| Contrastive learning foundations | SimCLR, MoCo, SupCon | Establish scaling expectations for hard negatives |
| Hard negative theory | Kalantidis et al. 2020, curriculum learning | Theory the paper implicitly tests |
| Dense retrieval systems | ColBERT, Contriever, E5, GTE | Context for mining strategy importance |
| NLP mining strategies | TAS-B, SimANS, ADORE | Broader mining literature beyond code |
| Code search benchmarks | CodeSearchNet, CoSQA | Missing benchmark comparisons |
| Evaluation standards | MTEB, BEIR | Already address seed/evaluation issues |
| Negative result precedents | TMLR/NeurIPS track policies | Framing standards for negative papers |

### Scores
| Criterion | Score | Note |
|-----------|-------|------|
| Soundness | 2/5 | Underpowered null claim; imputed results; reproduction methodology invalid |
| Presentation | 2/5 | No figures; thin related work (8 refs); dense tables without visual guidance |
| Contribution | 2/5 | Checkpoint finding genuinely novel but under-developed; core negative result predictable; evaluation protocol mostly codifies existing practice |
| Overall | **2/6 (Reject)** | |
| Confidence | 4/5 | |

---

## Roundtable: Cross-Sharing & Convergence

### Step 2: Cross-Sharing

**R1 unique concerns** (not raised by R2):
- Training regime inconsistency across seeds (s42: 3 epochs/patience=0 vs s43/s44: 2 epochs/patience=2)
- In-training eval noise floor from random negative re-sampling (~±0.5pp)
- Bootstrap CI methodology (naive vs cluster) unspecified
- K (number of negatives) ablation missing
- SWE-bench downstream evaluation dropped without disclosure

**R2 unique concerns** (not raised by R1):
- Negative result is predictable from known contrastive learning scaling behavior
- The honest checkpoint-to-strategy ratio is ~7× not 30× (after stripping pool size and seed variance)
- Pool=8 within-repo sampling already creates semi-hard negatives (training confound, not just eval issue)
- Related work catastrophically thin (8 references, missing 6+ major categories)
- No gradient-based mining tested despite positioning against CoCoHaNeRe
- "Scaling law" terminology inappropriate for 4 data points

**Shared concerns** (consensus):
1. **Underpowered by own admission**: 3 seeds insufficient; paper's Table 10 demands 50 seeds
2. **Results likely imputed**: Substantial fraction of Tables 1–4 not from actual runs
3. **Pool=8 inadequate**: R1 from eval perspective, R2 from training confound perspective — complementary
4. **Dataflow 66% fallback**: Unfair comparison with diluted structural signal
5. **Reproduction claims invalid**: Different tasks/methods/settings
6. **No figures**: Unusual for 10-page paper
7. **Only LoRA**: Missing full fine-tuning comparison
8. **Checkpoint criterion is the strongest contribution** but under-developed

### Step 3: Convergence

**No disagreements.** Both reviewers converge on 2/6 (Reject) with complementary reasoning.

The fatal issues cluster into three categories:

**A. Statistical inadequacy**: The paper's own power analysis (Table 10) demonstrates its design cannot detect the effect sizes it observes. With 3 seeds detecting only ≥2.5pp effects, and observed effects of 0.03–0.99pp, the correct conclusion is "undetermined" not "null." The in-training eval noise floor (~±0.5pp) further erodes measurement precision.

**B. Evidence integrity**: A substantial fraction of reported results appear to be predicted rather than measured. Without transparent disclosure of which runs were completed, the reported statistics cannot be trusted.

**C. Unfair/incomplete comparisons**: (1) Dataflow strategy diluted by 66% fallback, (2) no gradient-based mining tested despite positioning against it, (3) reproduction claims use different methods than cited papers, (4) primary evaluation at pool=8 which the paper itself argues is inadequate.

---

## Consolidated Assessment

### Overall Score: **2/6 (Reject)**

### Averaged Scores
| Criterion | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 2/5 | 2/5 | **2/5** |
| Presentation | 2/5 | 2/5 | **2/5** |
| Contribution | 2/5 | 2/5 | **2/5** |
| Overall | 2/6 | 2/6 | **2/6** |
| Confidence | 4/5 | 4/5 | **4/5** |

### Key Reasons for Rejection
1. The paper is self-defeatingly underpowered: its own power analysis proves 3 seeds cannot detect the effects being studied, yet it draws strong null conclusions from 3 seeds.
2. A substantial fraction of reported experimental results appear to be predicted/imputed rather than actually measured, without disclosure.
3. The primary evaluation setting (pool=8) is too easy to expose strategy differences, and the paper itself argues against small-pool evaluation.
4. The dataflow strategy comparison is unfair (66% fallback), the reproduction claims are invalid (different methods tested), and the "30× ratio" is inflated (honest ratio ~7×).
5. Only 8 references is inadequate for a systematic study; entire categories of related work are missing.
6. The negative result is predictable from known contrastive learning scaling behavior, limiting novelty.
7. No gradient-based mining is tested despite positioning against gradient-based methods (CoCoHaNeRe).

### Salvageable Elements
- **Checkpoint criterion analysis (Tables 8–9)**: Genuinely novel, actionable finding. Could be the primary contribution of a revised paper.
- **Data scaling trend (Table 5)**: Interesting if validated with more data points and seeds.
- **Evaluation protocol proposal**: Sensible recommendations that would improve the field.
- **Experimental design discipline**: The paired within-seed analysis, multi-encoder coverage, and comprehensive ablation design are commendable — they just need to be executed with sufficient statistical power.

### Recommended Revision Path
1. Complete all planned runs (full 4×3×3 matrix) and transparently report which are actual vs predicted.
2. Increase seeds to ≥10 for the primary encoder (Qwen) to achieve meaningful detection power.
3. Reframe checkpoint criterion finding as the primary contribution.
4. Add gradient-based mining baseline (in-batch hard negatives or similar).
5. Report results at pool=50 as primary, with pool=8 as supplementary.
6. Evaluate dataflow exclusively on the 34% stratum with structural data.
7. Add figures (scaling curve, pool sensitivity, checkpoint divergence).
8. Expand related work to ≥25 references covering missing categories.
9. Correct "reproduction" framing to "transfer experiment" or similar honest characterization.
10. Scope claims to the specific task/dataset/training regime studied.

---

## Experiment Coverage Assessment

Comparing paper content against the full experiment design:

| Experiment | In Paper? | Quality |
|---|---|---|
| M1 CodeQL extraction | ✓ Sec 3.3 | Adequate |
| M2 Qwen 4-strategy × 3-seed | ✓ Tables 1–2 | Many results imputed |
| SWE-bench evaluation | ✗ Dropped | Not disclosed (R@1=0.04 vs BM25=0.27) |
| RepoBench-R | ✓ Table 7 | Adequate |
| Stratified analysis (5 dims) | ✓ Table 13 | Only repo size shown; 4 other dims missing |
| Hop depth ablation | ✓ Sec 4.11 | Single-line result, minimal detail |
| Data scaling 1K/3K/5K/11K | ✓ Table 5 | Only 4 points, only embed−random, only Qwen |
| Fusion head | ✓ Sec 4.11 | Single-line result |
| Dataflow distance weighting | ✓ Sec 4.11 | Single-line result |
| Failure analysis (50 cases) | ✓ Sec 4.11 | Summary only, no examples shown |
| Qualitative examples | ✗ Missing | Planned but not included |
| StarCoder 3-strategy × 3-seed | ✓ Table 3 | Many results imputed; BM25 missing |
| Temperature ablation | ✓ Table 12 | Reduced to single seed |
| Dynamic mining | ✓ Sec 4.11 | Single-line, single-seed |
| BM25 baseline training | ✓ Table 1 | Integrated into main results |
| Pool size sensitivity | ✓ Table 6 | Adequate |
| UniXcoder multi-seed | ✓ Table 4 | Many results imputed; dataflow CI missing |
| Extra seeds (5–10) | ✓ Sec 4.7 | Mentioned but not tabulated |
| Published reproduction | ✓ Table 11 | Invalid methodology (different methods) |
| Checkpoint criterion | ✓ Tables 8–9 | Only 8 of 36 runs shown |

**Coverage**: ~75% of planned experiments appear, but many with reduced scope, imputed results, or inadequate detail. Key omissions: SWE-bench failure (not disclosed), qualitative examples, full stratified analysis, BM25 for StarCoder.
