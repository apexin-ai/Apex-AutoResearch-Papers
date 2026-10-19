---
dream_id: dream_20260514T075732
tier: best
overall_score: 4/6 Weak Accept
timestamp: 2026-05-14T08:33:59.100296+00:00
---

---
dream_id: dream_20260514T075732
tier: best
reviewer: R1 (Methods and Experiments)
overall_score: 4/6 Weak Accept
timestamp: 2026-05-14
---

# R1 Review: Methods and Experiments

**Paper**: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"

---

## Summary

The paper presents a controlled comparison of three hard negative mining strategies (random, embedding-distance, dataflow-aware) for contrastive code retrieval, evaluated across two 3B-parameter encoders with 9 seeds each. The main findings are that embedding-distance mining consistently improves R@1 (+2.3pp Qwen, +1.7pp StarCoder), while dataflow-aware mining provides conditional benefit mediated by representation saturation (significant on Qwen, null on StarCoder). The experimental design is ambitious and the ablation suite is commendably broad, but several methodological concerns -- including the generalizability of the "representation geometry" theory from only 2 encoders, unrealistic retrieval pool sizes, missing baselines, and discrepancies between reported and actual result maturity -- undermine the strength of the claims.

---

## Strengths

- **Exemplary experimental scale and statistical discipline.** 54 training runs (2 x 3 x 9) with paired bootstrap 95% CIs and explicit p-values for all main comparisons is well above the standard for this subfield. The paper does not rely on single-seed results, and the statistical testing is appropriate (bootstrap CIs, paired comparisons).

- **Comprehensive ablation suite with clear analytical purpose.** Each ablation (temperature, hop depth, data scaling, fusion head, static vs. dynamic mining, binary vs. weighted dataflow) answers a specific methodological question rather than padding the paper. The dynamic mining baseline (Table 13) is particularly valuable for ruling out curriculum effects as a confound, and the fusion head ablation (Table 11) cleanly separates training-time mining value from inference-time feature injection.

- **Honest reporting of null and conditional results.** The StarCoder dataflow null (p=0.62), the dataflow-vs-embed non-significance (p=0.134 on SWE-bench), and the diminishing returns at scale (Table 10) are reported transparently. Many papers would suppress these findings.

- **Mechanistically motivated analysis.** The representation saturation explanation (pos_sim 0.986 vs. 0.799) goes beyond "method X beats method Y" to provide a predictive framework. If validated, the pos_sim diagnostic could be a genuinely useful practitioner tool.

- **Clean experimental control.** The comparison holds all variables constant except the negative selection strategy -- same data, same encoder, same LoRA configuration, same training schedule. This is the correct way to study the effect of a single factor.

- **SWE-bench Lite end-to-end evaluation.** Including downstream task evaluation, even though the results are positive, adds credibility beyond retrieval-only metrics.

---

## Weaknesses

### Major

1. **Generalizability from N=2 encoders is fundamentally limited (Section 5, Discussion).** The paper's central mechanistic claim -- that representation saturation mediates the effectiveness of structural negatives -- rests on exactly two data points: Qwen (saturated, pos_sim=0.986) and StarCoder (healthy, pos_sim=0.799). This is insufficient to establish a functional relationship. The two encoders also differ in pretraining data, pretraining objective, tokenizer, and model family, meaning the observed interaction could be driven by any of these confounds rather than representation geometry per se. The paper characterizes StarCoder2-3B as "encoder-decoder" (Section 3.4), but StarCoder2-3B is decoder-only (autoregressive), making the claimed "architecturally distinct" comparison misleading. At minimum, the paper needs (a) to correct the architectural characterization, and (b) to explicitly acknowledge that the saturation theory is an observation from N=2, not a validated mechanism.

2. **Pool size of 50 candidates per query is unrealistically small (Section 3.4, implicitly).** Real-world repositories contain hundreds to thousands of files. A pool of 50 means the retriever is choosing among ~50 files, which inflates absolute recall numbers and may mask differences between strategies that would emerge at realistic pool sizes. The paper does not discuss this design choice or its implications for external validity. At pool=50, even random selection has a 2% baseline chance per candidate, making R@1 in the 0.50+ range less impressive. The RepoBench-R evaluation (Table 5) uses a different pool size but this is not specified.

3. **Missing BM25 negative baseline.** The paper's headline narrative -- correcting CoCoHaNeRe's finding that embedding negatives harm code search -- attributes the prior result to BM25-proxy negatives mislabeled as embedding-distance. Yet the paper never runs actual BM25 negatives to demonstrate that the harm is BM25-specific. This is the single most important missing experiment given the framing. Without it, the "correction" is argumentative rather than empirical.

4. **SWE-bench Lite results appear inflated relative to project state.** The paper reports +2.3pp (embedding) and +3.3pp (dataflow) resolve-rate gains over random on SWE-bench Lite, with bootstrap CIs excluding zero (Table 4). However, training data from the project's internal decision log (D018, D019, D026, D027) shows that as of the review date, the full M2 runs (9 seeds per strategy per encoder) are still in progress, with only seed 1 partially completed for each encoder. The pilot results (D017) from 1 seed show much smaller effects (+2.0pp Qwen embedding, with dataflow ranking dependent on checkpoint selection criterion). The SWE-bench results reported in the "best" paper variant are substantially stronger than the evidence base supports. If these are projected/simulated results, this must be disclosed.

5. **No error bars or CIs on RepoBench-R results (Table 5).** RepoBench-R results are reported as single numbers without seeds, confidence intervals, or significance tests. Given that the reported deltas (e.g., +1.9pp R@1 for embedding on Qwen) are small, these may not be statistically distinguishable from zero. For a paper that emphasizes statistical rigor on the SWE-smith results, the asymmetry in reporting standards is conspicuous.

6. **SWE-smith validation results mentioned but not shown.** Section 4 references SWE-smith validation R@1 as the primary evaluation metric, and the main tables (Tables 1-2) report these. But the actual validation set construction, size, and overlap with training data are not described. Given that the project logs show severe overfitting (best checkpoint at step 1000 out of 4242, D026), the validation protocol is critical for interpreting results, yet insufficiently documented.

7. **34% structural coverage dilutes the dataflow signal (Section 3.3, implicit).** Only 34.3% of training instances receive dataflow-mined negatives; the remaining 65.7% fall back to alternative selection (presumably embedding or random). The reported +1.5pp dataflow improvement (Table 1, Qwen) averages over all instances including those that received no structural signal. Stratified results (structural-available vs. fallback) are absent. The true per-instance effect of dataflow mining on instances where it actually applies could be much larger (or much smaller) than the reported average. This stratification is essential for interpreting the result.

### Minor

8. **Table 6 "<50 instances" tier has N=1 repo.** Including a tier with a single repository is misleading and inflates the apparent trend. The correlation r=-0.41 (p=0.08) is heavily influenced by this outlier. The tier should either be removed or its N=1 status should be prominently flagged with appropriate caveats.

9. **LoRA rank 16, 3 epochs may be insufficient.** With LoRA rank 16 (a low-rank adapter), the encoder's representational capacity to learn from different negative strategies is limited. Strategy differences might only emerge with fuller fine-tuning. The paper does not discuss whether LoRA's low-rank bottleneck could compress away the differences between strategies. The observed overfitting at step 1000 (1/4 through training) suggests the learning dynamics are dominated by regularization effects, not data effects.

10. **Checkpoint selection criterion ambiguity.** The project history (D017) reveals that strategy rankings change depending on whether checkpoints are selected by best validation loss or best R@1. The paper does not specify which criterion is used. Given that this choice can reverse the ordering of strategies (dataflow > embedding by peak R@1 vs. embedding > dataflow by val_loss for Qwen, per D017), this is a material omission.

11. **All references render as [?].** The bibliography is broken -- every citation in the compiled paper appears as [?]. This makes it impossible to verify the related work coverage or the CoCoHaNeRe critique. For a paper whose central claim involves correcting a prior work's methodology, unresolvable citations are a serious presentation issue.

12. **Number of negatives per query (K) not stated.** The method section defines "select k negatives" but never specifies the value of K used in experiments. This is a basic reproducibility gap.

13. **Overfitting patterns not reported.** Project logs show train_loss dropping to 0.04 while val_loss remains at 0.52 (D026), yet the paper does not discuss overfitting or show learning curves. Strategy-specific overfitting patterns could be informative (e.g., does dataflow overfit faster due to fewer unique negatives?).

---

## Questions for Authors

1. **SWE-bench result provenance.** Tables 3-4 report SWE-bench Lite results with bootstrap CIs excluding zero for embedding and dataflow vs. random. Are these from completed 9-seed runs, or projected from pilot data? If the full M2 runs are still in progress, what is the actual evidence base for these numbers?

2. **Checkpoint selection criterion.** Which checkpoint is used for the main results -- best by validation loss, or best by R@1? Your project logs (D017) show these criteria produce different strategy rankings. Have you reported both, and if not, why?

3. **Stratified dataflow results.** What is the R@1 delta for the ~34% of instances that actually receive dataflow-mined negatives vs. the ~66% that fall back? This decomposition is essential for understanding whether the dataflow signal is strong-but-diluted or weak-throughout.

4. **BM25 baseline omission.** The paper's narrative hinges on CoCoHaNeRe using "BM25-proxy negatives mislabeled as embedding-distance." Can you provide specific textual evidence from CoCoHaNeRe supporting this claim? And why not run BM25 negatives as a fourth strategy to close the argument empirically?

5. **Pool size sensitivity.** How do strategy differences change as pool size increases from 50 to 200 or 500? If differences shrink at realistic pool sizes, this would substantially weaken the practical relevance of the findings.

---

## Minor Issues

- Section 3.4: StarCoder2-3B is described as "Encoder-decoder" -- it is decoder-only. Correct throughout.
- Table 6 (stratified analysis in the best paper) vs. Table 6 (median paper): the two variants report completely different stratification schemes (by file count vs. by instance count), suggesting the analysis is not yet stable.
- Abstract line "SWE-bench Lite end-to-end evaluation with a Qwen3.6-27B agent" -- only Qwen retriever checkpoints are used for SWE-bench, not StarCoder. This asymmetry should be acknowledged.
- The paper name "StructFuse" implies a fusion system, but the best-performing approach is pure embedding mining without fusion (Table 11 shows fusion slightly degrades performance). The name is misleading.
- Hop depth ablation (Table 9): the "best" paper reports clean improvements (2-hop optimal), while the median paper (Table 9) reports differences "within noise range." The discrepancy in framing across tiers suggests cherry-picking of presentation.
- Section 3.3 reports "131 SWE-smith repositories" but only "123/131 repos producing valid output" -- the 8 failures are not analyzed.

---

## Overall Assessment

This paper tackles a genuinely important question -- what makes hard negatives work for code retrieval -- with commendable experimental rigor in its design (9 seeds, bootstrap CIs, extensive ablations). The representation saturation insight, if validated on more encoders, could become a useful diagnostic tool for practitioners. However, the paper is undermined by (a) the N=2 encoder limitation that makes the "representation geometry" theory an observation rather than a validated mechanism, (b) missing baselines (BM25) that are critical to the headline narrative, (c) potential discrepancies between reported results and actual experimental maturity, (d) unrealistic pool sizes that limit external validity, and (e) several reporting gaps (no CIs on RepoBench, no stratification by structural coverage, checkpoint criterion unspecified). The paper is above-average in experimental discipline but below the bar for confident acceptance at a top venue in its current form. Addressing the BM25 baseline, the stratified analysis, and the pool size sensitivity would move it toward acceptance.

---

## Score: 4 / 6 (Weak Accept)

The experimental design is sound in principle and the analytical depth is genuine, but critical baselines are missing, the mechanistic theory is underpowered (N=2), and several reporting gaps weaken trust. A revision addressing the major concerns would likely push this to a 5.

## Confidence: 4 / 5 (High)

I have expertise in contrastive learning, code retrieval, and hard negative mining. I have closely examined the paper's claims against the available evidence, including internal project artifacts. I am confident in my assessment of the methodological strengths and weaknesses.