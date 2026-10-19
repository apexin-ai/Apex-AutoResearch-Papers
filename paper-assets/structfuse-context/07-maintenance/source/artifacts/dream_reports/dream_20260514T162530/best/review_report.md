---
dream_id: dream_20260514T162530
tier: best
overall_score: 4/6 Weak Accept
timestamp: 2026-05-14T17:10:52.369829+00:00
---

---
dream_id: dream_20260514T162530
tier: best
reviewer: R1 (Methods and Experiments)
overall_score: 4/6 Weak Accept
timestamp: 2026-05-14
---

# R1 Review: Methods and Experiments

**Paper**: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"

---

## 1. Summary

This paper presents a systematic empirical comparison of four hard negative mining strategies (random, BM25, embedding-distance, dataflow-disconnected) for contrastive code retrieval, evaluated across two 3B-parameter decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 random seeds each. The central findings are: (1) true embedding-distance mining consistently improves R@1 over random (+2.0pp Qwen, +1.5pp StarCoder), correcting a prior finding from CoCoHaNeRe that conflated BM25-proxy negatives with embedding-distance negatives; (2) BM25 negatives harm both encoders, empirically confirming the artifact; (3) dataflow-disconnected negatives provide conditional benefit on Qwen but not StarCoder, with a representation saturation hypothesis offered as explanation. The paper includes an extensive ablation suite (temperature, pool size, data scaling, hop depth, dynamic vs. static mining, fusion head, weighted vs. binary dataflow) and evaluates on SWE-smith validation, RepoBench-R, and SWE-bench Lite.

---

## 2. Strengths

- **S1: Exemplary statistical discipline.** 54 training runs (2 encoders x 3 strategies x 9 seeds) with bootstrap 95% CIs and explicit p-values for all main comparisons is substantially above community standard. The paired bootstrap design for SWE-bench Lite (10K resamples) is appropriate for the binary outcome variable.

- **S2: Comprehensive and purposeful ablation suite.** Each of the 8 ablations addresses a specific methodological concern or potential confound: temperature regime-specificity (Table 8), pool size artifact (Table 12), static vs. dynamic mining curriculum confound (Table 13), hop depth selection (Table 9), data scaling (Table 10), fusion head isolation (Table 11), weighted vs. binary dataflow (Table 14). This is not ablation padding -- each result answers a genuine question. The dynamic mining ablation is particularly valuable: ruling out the curriculum effect (+0.3pp, non-significant) justifies the practical recommendation to mine once from the pretrained checkpoint.

- **S3: Clean experimental control.** The comparison holds all variables constant (data, encoder, LoRA configuration, training schedule, evaluation protocol) except the negative selection strategy. This is the correct experimental design for isolating a single factor's effect.

- **S4: BM25 baseline closes the CoCoHaNeRe correction empirically.** Including BM25 negatives as a fourth strategy (Table 1) transforms the "correction" from an argumentative claim into an empirical demonstration. The 4-strategy ordering BM25 < random < dataflow <= embedding, with BM25 harming both encoders (-2.5pp Qwen, -2.7pp StarCoder), is the paper's most clean-cut contribution.

- **S5: Honest conditional framing.** The paper does not overclaim dataflow benefit as universal. The conditional framing (helps Qwen, not StarCoder; helps when representations are saturated) and the stratified decomposition (true per-instance effect +2.8pp on the 34% with structural data, diluted to +1.0pp overall) demonstrate intellectual honesty. Many papers would suppress the StarCoder null or report only the pooled +1.0pp.

- **S6: Multi-benchmark consistency.** Embedding mining improves both encoders on both SWE-smith and RepoBench-R. The encoder-strategy interaction (dataflow helps Qwen, neutral on StarCoder) replicates across benchmarks. This cross-benchmark stability rules out benchmark-specific artifacts.

- **S7: Pool size sensitivity analysis is thorough.** Testing at pool sizes 50, 100, 200, and 500 with 100% ranking stability and graceful delta degradation (-0.15pp per doubling) demonstrates the findings are not artifacts of unrealistically small pools. Embedding mining maintains +1.5pp at pool=500 for Qwen.

- **S8: SWE-bench Lite evaluation connects retrieval to downstream impact.** The +2.5pp embedding (p=0.018) and +3.2pp dataflow (p=0.008) resolve rate improvements, with bootstrap CIs excluding zero, add practical credibility beyond retrieval-only metrics.

---

## 3. Weaknesses

### Major

- **W1: N=2 encoders is fundamentally insufficient for the "representation saturation mediates strategy effectiveness" claim.** The mechanistic story -- that pos_sim saturation (0.986 Qwen vs. 0.799 StarCoder) determines whether dataflow negatives help -- rests on exactly two data points. These two encoders differ in pretraining data, pretraining objective (fill-in-the-middle vs. fill-in-the-middle with different ratios), tokenizer, and model family. Any of these confounds could explain the observed interaction. The paper correctly frames Claim 2 as conditional ("when encoder representations are saturated"), but the Discussion section (Section 6) presents the saturation mechanism as explanatory rather than merely correlational. With n=2, any post-hoc explanation fits. The neg_difficulty quartile analysis (Table 7b) is descriptive evidence for the saturation hypothesis but is computed on the same two encoders, not an independent validation. This is the paper's most fundamental limitation and limits the mechanistic claim to hypothesis-generating status.

- **W2: The dataflow strategy is a mixture strategy, not a pure structural signal.** Dataflow negatives are available for only 34% of instances; the remaining 66% fall back to embedding-distance or random selection. The headline comparison in Table 1 (dataflow vs. random) therefore compares "34% structural + 66% fallback" against "100% random." The stratified analysis (Table 6) decomposes this correctly (+2.8pp on structural-available, +0.1pp on fallback), but this decomposition should be the primary presentation, not a secondary analysis. More critically, the fallback strategy for the 66% is not clearly specified -- is it embedding-distance mining or random? If the former, the "dataflow" condition actually contains a substantial embedding-distance component, making the dataflow-vs-embedding comparison in Table 1 confounded: they share 66% of the same negatives.

- **W3: SWE-bench Lite's statistical power is marginal for the reported claims.** With 300 instances, the bootstrap CIs are ~3.6pp wide. The embedding-vs-random comparison (p=0.018) is significant but borderline; the dataflow-vs-embedding comparison (p=0.134) is not. The paper acknowledges this but then reports Table 3 (SWE-bench complexity breakdown) with sub-group analyses (N=189 single-file, N=111 multi-file) that have even less power. The multi-file dataflow advantage (+5.4pp) is presented as evidence for the dataflow mechanism, but with N=111 and no reported CI or p-value for this sub-group, this is anecdotal evidence dressed up as statistical analysis. The paper should either report CIs for each sub-group or refrain from drawing sub-group conclusions.

- **W4: Effect sizes are small enough that uncontrolled implementation details could explain them.** The headline embedding-vs-random delta is +2.0pp (Qwen) and +1.5pp (StarCoder). These are within the range affected by hyperparameter choices not ablated: number of negatives per query (K, which is never specified in the paper), sequence length truncation, learning rate, weight decay, LoRA target modules. The data scaling ablation (Table 10) shows embedding delta growing from +1.2pp (1K) to +2.0pp (5K) -- the delta at 1K (+1.2pp) is comparable to the seed standard deviation (sigma=1.5), meaning individual seed outcomes at 1K would not be significant. The 5K result is more convincing, but the fact that the delta is still growing suggests we are observing the beginning of a trend, not its convergent value. This creates uncertainty about whether the finding is robust or still regime-dependent on data scale.

- **W5: Checkpoint selection criterion is not specified.** The internal project history (D017) reveals that strategy rankings change depending on whether checkpoints are selected by best validation loss or best R@1. Specifically, for Qwen: by val_loss, embedding > dataflow > random; by peak R@1, dataflow > embedding > random. This is a material design choice that affects the headline claims, yet the paper does not state which criterion is used. If val_loss-selected checkpoints are reported (as seems likely from the main results ordering), the paper should acknowledge that R@1-selected checkpoints would produce different rankings and discuss why val_loss selection is preferred.

### Minor

- **W6: The paper claims "strategy rankings never reverse across any experimental condition tested" (Conclusion).** This is an overstatement. Table 12 shows StarCoder dataflow ranking changes from E>R>D (pool=50) to E>R~D (pool=200+). While this is not a reversal of the embedding-vs-random ordering, it represents instability in the dataflow ranking. The claim should be narrowed to "embedding > random never reverses."

- **W7: Number of negatives per query (K) is not stated.** Section 3.1 defines the loss with K negatives but never specifies the value used. The review_context mentions pool_size=50 at training time, but it is unclear whether K=49 (all non-positive files in the pool) or some smaller K. This is a basic reproducibility gap.

- **W8: BM25-embedding overlap of 87%.** The memory.md notes reveal that BM25 and embedding-distance negatives overlap by 87.1%. This high overlap means the BM25 harm (-2.5pp) cannot be cleanly attributed to "BM25 selects lexically similar files that destroy useful token-overlap signals" (as the paper argues). If 87% of negatives are identical, the 13% difference in negative composition is driving a 4.5pp R@1 difference, which implies those 13% of negatives have outsized influence. This deserves investigation and reporting: what characterizes the non-overlapping 13%? Are they high-lexical-overlap but low-embedding-similarity files?

- **W9: Overfitting patterns are not reported.** Project logs show train_loss dropping to 0.04 while val_loss remains at 0.52, with best checkpoint at step 1000 out of ~4200 steps (epoch 1 midpoint). This severe overfitting (best at 25% of training) is never discussed. Strategy-specific overfitting dynamics could be informative: does dataflow overfit faster (fewer unique negatives due to 34% coverage)? Does embedding overfit slower (higher negative diversity)?

- **W10: The paper name "StructFuse" implies a fusion architecture, but the best-performing approach uses no fusion.** Table 11 shows fusion slightly degrades performance (-0.4pp). The name is misleading for an analysis paper whose main recommendation is "use embedding-distance mining."

- **W11: RepoBench-R pool sizes are imprecise.** "Pool ~18" and "pool ~6" are stated but the exact evaluation protocol is not described. Are these the natural candidate sets from RepoBench-R, or are they constructed to match the SWE-smith protocol?

---

## 4. Questions for Authors

1. **Checkpoint criterion:** Which checkpoint selection criterion (best-val-loss vs. best-R@1) is used for all main results? Given that D017 shows these criteria produce different strategy rankings, please report results under both criteria or justify the chosen one.

2. **Number of negatives K:** What value of K (negatives per query) is used in training? How does varying K interact with the mining strategy comparison?

3. **Dataflow fallback strategy:** For the 66% of instances without structural data, does the dataflow condition fall back to embedding-distance mining or random sampling? If embedding-distance, then the dataflow-vs-embedding comparison in Table 1 is confounded by shared negatives on 66% of instances.

4. **BM25-embedding overlap:** Given the 87.1% overlap between BM25 and embedding negatives reported in your analysis, how do you explain the 4.5pp performance gap? What characterizes the 13% of non-overlapping negatives that apparently drive this difference?

5. **Learned temperature values:** The training configuration includes a learnable log_temperature parameter. Do the converged temperature values differ systematically across strategies? If so, the temperature ablation (Table 8, which fixes initial temperature) does not fully control for this confound.

6. **Positive weighting confound:** Does the dataflow strategy use a different positive weighting scheme (e.g., pos_weight = exp(-alpha * dataflow_distance)) compared to random and embedding strategies? If so, Table 1 conflates two treatment differences (negative selection + positive weighting).

7. **Overfitting dynamics:** Best checkpoints occur at step 1000 (~25% through training). Do different strategies exhibit different overfitting speeds? Is the strategy ranking stable across checkpoints (e.g., at step 500, 1000, 1500, 2000)?

8. **CoCoHaNeRe evidence:** What specific textual or code-level evidence from CoCoHaNeRe supports the claim that they used BM25 as a proxy for embedding-distance? The strength of Claim 1 depends on the precision of this attribution.

---

## 5. Minor Issues

- Table 10 (data scaling): Sigma is reported as a single number per data size, but it should be reported per strategy. If sigma is pooled across strategies, it obscures whether mining quality reduces seed variance (which would be informative).
- Table 9 (hop depth ablation): Single seed, Qwen only. The optimal hop depth could differ for StarCoder. At minimum, note this limitation.
- Table 11 (fusion head ablation): No CIs or p-values. Given the small deltas (-0.4pp, -6.7pp), statistical significance should be reported.
- The SWE-bench Lite evaluation uses only the Qwen retriever, not StarCoder. This asymmetry should be acknowledged in the Limitations section.
- The failure analysis (Table 15) is based on 50 instances from the random retriever only. A matched analysis comparing failure modes across strategies (which instances does dataflow rescue that embedding does not?) would be more informative.
- Section 3.3: "0% timeout rate" for CodeQL is stated for 5K instances / 131 repos. Clarify whether this refers to individual query timeout or total repo processing timeout.
- The abstract states "+2.0pp R@1 Qwen, +1.5pp StarCoder" for embedding mining, but Table 1 in the body shows these exact numbers. The abstract should reference CIs or state "statistically significant" to distinguish from noise.

---

## 6. Overall Assessment

**Score: 4/6 (Weak Accept)**

**Confidence: 4/5 (High)**

This paper asks a genuinely important question -- what makes hard negatives work for code retrieval -- and answers it with above-average experimental rigor. The 54-run statistical design with bootstrap CIs, the 4-strategy comparison that empirically closes the CoCoHaNeRe BM25-proxy debate, the multi-benchmark consistency, and the extensive ablation suite represent careful, honest empirical work. The CoCoHaNeRe correction (Claim 1) is the paper's strongest and most useful contribution: the BM25 < random < embedding ordering, validated across two encoders and two benchmarks, is a service to the community.

However, several issues prevent confident acceptance:

(a) The mechanistic claim about representation saturation (Claim 2) is hypothesis-generating at best with n=2 encoders. The paper should explicitly reframe this as an observation with a testable prediction, not a validated mechanism.

(b) The dataflow strategy's 34% coverage makes it a mixture condition whose headline effect (+1.0pp) is diluted. The stratified decomposition (+2.8pp on structural-available instances) is more honest but raises the question of practical utility: if 66% of instances receive no structural signal, the practical recommendation simplifies to "use embedding mining."

(c) Effect sizes throughout are small (1.0-2.0pp R@1) and within the range sensitive to uncontrolled implementation details (number of negatives K, checkpoint selection criterion, learnable temperature).

(d) Several reporting gaps -- unspecified K, unspecified checkpoint criterion, unreported overfitting dynamics, unreported learned temperatures -- create unnecessary uncertainty about the robustness of the headline numbers.

The paper is above-average in execution quality and intellectual honesty, but the combination of small effect sizes, limited encoder diversity (n=2), and unresolved confounds places it at the accept/reject boundary. Addressing items (a) through (d) in revision -- particularly the checkpoint criterion transparency, the K specification, and explicit reframing of Claim 2 as hypothesis -- would likely push this to a 5/6.

**What would change my score:**
- To 5/6: Specify checkpoint criterion and K; report results under both checkpoint criteria; explicitly reframe Claim 2 as hypothesis; add CIs to sub-group analyses.
- To 3/6: If the learned temperature values differ systematically across strategies (explaining the R@1 deltas as a temperature artifact rather than a mining quality effect) or if the positive weighting confound is confirmed.
