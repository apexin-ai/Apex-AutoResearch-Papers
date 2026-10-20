---
dream_id: dream_review_r1
tier: best
overall_score: 4/6 Weak Accept
timestamp: 2026-05-15T10:04:59.280488+00:00
---

## Reviewer 1 (R1): Methods & Experiments Focus

### Summary
This paper studies per-head mixed-precision KV cache quantization on hardware-aligned bit-widths {2,4,8,16} across five 7-9B architectures. It identifies that unconstrained MCKP/greedy solvers fail catastrophically due to super-additive 2-bit distortion compounding, proposes a cardinality constraint on 2-bit assignments as a fix, and introduces a shape-based taxonomy (Spread/Spike/Flat) with a two-metric decision rule to predict when non-uniform allocation is beneficial. The cardinality constraint yields 27.3% PPL improvement on Qwen2.5-7B while rendering solver choice irrelevant; on the four non-Spread models, uniform 4-bit remains competitive or superior.

### Strengths (Methods & Experiments)

- **Well-identified failure mode.** The paper clearly diagnoses why unconstrained solvers fail on hardware-aligned bit-widths: the additive distortion assumption breaks down when many heads are simultaneously at 2-bit. The compounding analysis (Section 2.3) with top-k vs. random-k controls and super-additivity ratios is convincing and novel.

- **Minimal, principled intervention.** The cardinality constraint is elegant -- a single linear inequality compatible with any solver, with clear theoretical motivation (restoring the additive regime). The U-shaped PPL curve as a function of k provides intuitive justification.

- **Honest negative results.** The paper is admirably transparent that non-uniform allocation helps only 1 of 5 models. The Yi-1.5-9B counterexample (highest concentration yet zero benefit) is a genuinely useful insight.

- **Solver equivalence demonstration.** Showing constrained greedy = MCKP across all architectures, with per-layer brute-force oracle validation (gap < 0.04 PPL), is a practical contribution that simplifies deployment.

- **Reasonable ablation coverage.** Cross-dataset stability (>96% agreement WikiText-2 vs C4), multi-seed stability (3 seeds, std/mean < 0.6%), numerical precision ablation (bf16 vs fp32), budget sweep (2x/4x/8x), profiling resolution comparison, KV separation, heuristic baselines, and aggressive compression analysis.

- **Good baseline selection.** Uniform, unconstrained greedy/MCKP, L0-random heuristic (5 seeds with mean/std/median), and naive positional heuristic cover the reasonable design space.

### Weaknesses (Methods & Experiments)

**W1. N=1 for the Spread category is a critical limitation.** The paper's central claim -- that Spread-shaped heterogeneity enables non-uniform benefit -- rests entirely on Qwen2.5-7B. With only a single Spread model, the decision rule's predictive power is unvalidated. The experiment plan references Qwen2.5-14B experiments that do not appear in the paper; if these exist and confirm Spread, including them would substantially strengthen the contribution.

**W2. Decision rule thresholds lack principled justification.** The concentration >= 0.50 and t1/t5 <= 0.70 thresholds are chosen post-hoc to perfectly separate 5 models. With 5 data points and 2 free parameters, perfect classification is trivially achievable. No held-out validation, threshold sensitivity analysis, or theoretical argument for these values is provided.

**W3. No statistical significance testing on downstream results.** Downstream accuracy differences range from -3.2 to +4.0 points with no error bars, confidence intervals, or significance tests. 0-shot evaluation on ARC-Challenge and WinoGrande has known high variance. The Qwen +2.6 avg improvement could partially be noise.

**W4. Profiling cost is high and incompletely discussed.** Each model requires H x |B| forward passes (448 for Qwen, 1344 for Gemma-2) on the full calibration set. Wall-clock profiling time is never reported. For hires profiling (64 seq x 2048 tokens per pass), this could be many GPU-hours.

**W5. The compounding analysis conflates correlation and mechanism.** The paper claims compounding occurs "through the residual stream" but provides no mechanistic evidence (activation norm analysis, attention pattern degradation, layer-by-layer error propagation). Super-additivity ratios demonstrate the phenomenon but the causal explanation is speculative.

**W6. Limited model scale.** All models are 7-9B parameters. KV cache quantization is most practically relevant at 70B+ where memory pressure is greatest. No evidence that findings transfer to larger scales.

**W7. Runtime benchmark is a simulation, not a real measurement.** The 8.5% overhead of mixed-precision over uniform is from PyTorch-level quantize/dequantize calls, explicitly stated as an upper bound. Without real-kernel benchmarks, practical inference speedup is unsubstantiated.

**W8. Evaluation is PPL-centric with limited downstream coverage.** Primary metric is WikiText-2 PPL; downstream uses only 4 classification/commonsense benchmarks at 0-shot. Long-context tasks (summarization, multi-document QA, retrieval) where KV cache pressure is highest are not evaluated.

**W9. The t1/t5 metric is fragile by construction.** Using the ratio of top-1 to top-5 distortion means a single noisy head measurement can flip the Spike/Spread classification. t1/t5 variance across seeds is not reported for any model.

**W10. Missing comparison to concurrent mixed-precision KV methods.** KVmix, KVTuner, PM-KVQ, Kitty, Don't Waste Bits, and AQuA-KV are cited but none appear as experimental baselines. Even one layer-level comparison would contextualize the per-head granularity tradeoff.

### Questions for Authors

**Q1.** The experiment plan references Qwen2.5-14B experiments absent from the paper. Were these conducted? If so, what were the results and why were they excluded?

**Q2.** How sensitive is the decision rule to threshold values? What happens at concentration = 0.45 or t1/t5 = 0.75?

**Q3.** What is the wall-clock profiling time for each model at both standard and high resolution?

**Q4.** The KV separation ablation shows joint > separated because cardinality counts K and V independently. Did you try separated allocation with halved k (k=4 per side)?

**Q5.** Have you analyzed which specific head combinations produce the worst super-additivity? Same-layer vs. cross-layer?

**Q6.** The multi-seed stability test uses only 3 seeds. Why not 5 or 10?

**Q7.** Mistral's constrained MCKP (7.16) is worse than uniform (7.13). Is there a constraint setting that guarantees no-worse-than-uniform?

### Missing Experiments or Analyses

1. A second Spread model (e.g., Qwen2.5-14B) to validate the decision rule beyond N=1
2. Threshold sensitivity analysis for the decision rule (perturb +/- 0.1)
3. Long-context evaluation (RULER, LongBench, needle-in-a-haystack)
4. Downstream evaluation with error bars (at least 3 seeds)
5. Profiling wall-clock time for each model at each resolution
6. Head-pair/layer-pair compounding interaction analysis
7. Direct comparison with at least one layer-level mixed-precision baseline (KVTuner or KVmix)
8. At least one model outside the 7-9B range (30B-70B)

### Preliminary Score: 4/6 (Weak Accept)
### Confidence: 4/5

**Rationale:** The paper makes a clear, well-supported core contribution (identifying 2-bit compounding failure and the cardinality constraint fix) with honest reporting of negative results and clean writing. However, the N=1 Spread limitation is serious for a paper whose title asks "when does non-uniform help?" -- the decision rule is the most ambitious claim but the weakest empirical foundation. The lack of larger-scale models, long-context evaluation, and downstream error bars are meaningful gaps. Strong diagnosis and engineering contribution, but the predictive/taxonomic claims need more evidence to clear the bar at a top venue.