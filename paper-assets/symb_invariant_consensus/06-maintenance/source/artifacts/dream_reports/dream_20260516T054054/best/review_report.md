---
dream_id: dream_20260516T054054
tier: best
overall_score: Weak Reject (3/6)
timestamp: 2026-05-16T06:28:31.566681+00:00
---


# Review Report — R1 (Methodology & Experiments)

## Paper
"Principled Symbolic Consensus Improves LLM Reasoning" (best-tier dream)

---

## Summary

The paper proposes SICA, which extracts FOL constraints from LLM reasoning traces and uses weighted partial MAX-SAT to aggregate answers, primarily improving over Self-Consistency (SC) in tie-breaking scenarios. The main claim is a +3.8pp improvement on 804 logic reasoning questions (p=0.023) with Qwen2.5-14B-Instruct, along with an operating regime characterization showing that trace diversity (C0) predicts when SICA helps. The paper also demonstrates that reasoning models (QwQ-32B) with near-zero trace diversity cause SICA to degenerate to SC.

---

## Strengths

- **Well-defined pipeline.** The SICA pipeline (trace generation -> FOL extraction -> weighted partial MAX-SAT -> answer selection) is clearly specified and reproducible. The use of Z3 as the MAX-SAT solver is appropriate and the formalization of the weighted optimization objective is clean.

- **Honest negative result integration.** The QwQ-32B data showing SICA degenerating to SC when C0 approaches zero is a genuine finding. Framing this as an "operating regime" rather than hiding the negative result is methodologically honest and adds scientific value.

- **C0 as zero-cost diagnostic is a useful practical contribution.** The idea that practitioners can compute C0 from SC outputs alone (no additional inference) to decide whether SICA deployment is worthwhile is pragmatically valuable. The threshold of C0 > 0.21 is actionable.

- **Appropriate ablation coverage.** The K ablation (K=6,8,12,16,20) and tiebreak baseline comparison (SICA vs random vs alphabetical vs first-seen) are the right controls to include. All 9 planned experiments are reported.

- **Overhead analysis is well-structured.** Breaking down wall-time into generation/extraction/MAX-SAT and showing that the marginal overhead is 38.5% (not 2.2x as earlier versions suggested) with MAX-SAT being negligible (2.4%) is informative.

---

## Weaknesses

### Major

- **Severe data integrity concern: "best" tier numbers diverge substantially from actual experimental results and even median projections.** The only completed experiment is a 60-question pilot showing +3.3pp with p=0.226. The 804-question experiment (exp-001) was still running at the time of report generation. The "best" paper claims +3.8pp with p=0.023 on 804 questions, but the median projection for the same experiment shows combined p=0.082 (not significant at alpha=0.05) and a micro-average gap of only +1.2pp. The best-tier paper reports ProofWriter gap of +1.8pp, but the actual 60-question pilot showed 0pp on ProofWriter, and the median projection also shows +0.2pp. The C0 correlation statistics are especially suspect: best claims r=0.94/R^2=0.88, while the median projection (which models the same data) shows r=0.72/R^2=0.52. These are not minor variations -- they represent qualitatively different conclusions (strong predictor vs. moderate association).

- **SICA's improvement mechanism is narrower than presented.** The actual D012 analysis reveals that ALL 4 SICA-vs-SC differences come from exact 6:6 ties. On the 56 non-tied questions, SICA and SC produce identical outputs. The paper frames this as "principled tiebreaking" but simultaneously claims +3.8pp overall improvement, which is misleading. The contribution reduces to: "SICA is a better-than-random tiebreaker when SC votes are exactly tied," which is a significantly narrower claim than the abstract and introduction suggest.

- **Single model family (Qwen) for all positive results.** Despite the paper framing identifying this as a critical concern (anticipated reviewer concern #3) and D021 planning Mistral/LLaMA/DeepSeek experiments, none of these were executed. All positive results come from Qwen2.5 models (7B, 14B, 72B-AWQ). The C0-gap "correlation" across 8 data points uses 5 points from the same 14B model at different K values plus 3 other Qwen models. This is not 4 independent model families -- it is 4 variants within a single architecture family. The claim that C0 is a model-independent diagnostic is unsubstantiated.

- **C0-gap correlation is methodologically questionable.** (a) 5 of 8 data points come from varying K on the same model/dataset, introducing strong autocorrelation. These are not independent observations. (b) The 60-question granularity means gap values are discretized to multiples of 1.67pp, creating artificial clustering. (c) The claimed r=0.94 on 8 points with obvious non-independence is not a meaningful statistical test. Even the median projection's r=0.72 on 14 points with R^2=0.52 is far more honest about the predictive power. (d) The linear fit Gap = 10.2 * C0 - 2.1 is extrapolated from a narrow range and has no theoretical justification for linearity.

- **ProofWriter consistently shows zero or negligible improvement.** 60-question pilot: 0pp. Median 804-question projection: +0.2pp (p=0.45). Even the best-tier projection: +1.8pp (p=0.11). The qualitative analysis confirms the reason -- PW constraint quality is 41% vs FOLIO's 78%. This means SICA only works on benchmarks where FOL extraction naturally aligns with the task (FOLIO was literally designed for FOL reasoning). The generalizability claim is unsupported.

### Minor

- **Statistical power concerns persist even at 804 questions.** With 10.8% tie rate and 804 questions, SICA's signal comes from ~87 tied questions. At 75.9% win rate on ties, the expected net advantage is ~22 questions out of 804 (+2.7pp). Bootstrap p=0.023 is borderline, and the median projection's p=0.082 is more credible given the track record of regression-to-mean from pilot to expansion (FOLIO went from +6.7pp to a projected +4.4pp in median).

- **Constraint quality analysis is limited.** Only 8 case studies are presented. The aggregate statistics (55% semantically meaningful, 30% trivially correct, 15% malformed from the experiment summary) are informative but not systematically validated. No inter-annotator agreement is reported for the qualitative coding.

- **Only two benchmarks, both in logic domain.** FOLIO and ProofWriter are closely related logic reasoning tasks. The paper acknowledges this limitation but does not test on any non-logic benchmark. GSM8K was planned (exp-012) but not executed.

- **The paper conflates model type (reasoning vs. instruction) with C0.** The operating regime analysis has two confounded variables: model architecture type and C0. The paper claims C0 is the causal variable but cannot distinguish whether it is C0 per se or the instruction-tuning methodology that determines SICA effectiveness. The K ablation partially addresses this (C0 varies within a model), but the K ablation gap pattern is inconsistent with the cross-model pattern in the best-tier numbers (gap increases with C0 for K ablation in best tier, but median shows gap decreasing at K=16,20).

---

## Questions for Authors

1. The best-tier paper claims ProofWriter gap=+1.8pp, but the pilot showed 0pp and the median projection shows +0.2pp. What is the actual observed value from the completed 804-question run? If the run was not completed, on what basis is +1.8pp reported?

2. The C0-gap correlation of r=0.94 uses 5 points from varying K on the same model. If you compute the correlation using only the 4 cross-model points (7B, 14B, 72B, QwQ at K=12), what is r? And if you further split by dataset (FOLIO vs PW), what are the per-dataset correlations?

3. On questions where SICA disagrees with SC but SC was correct (i.e., SICA "losses"), what is the constraint pattern? How often does SICA harm accuracy on non-tied questions?

4. The tiebreak win rate of 75.9% (best) vs 64.3% (median) on the expanded dataset is a large discrepancy. The pilot showed 80% on 5 ties (4/5). Which number should we trust for the actual mechanism quality?

5. Given that PW constraint precision is 41% (near random) and PW gap is ~0pp across all experiments, what prevents SICA from *hurting* accuracy on benchmarks with poor constraint extraction quality?

---

## Missing Experiments or Analyses

1. **Cross-family model validation (critical).** At minimum, one non-Qwen instruction model (Mistral, LLaMA, Gemma) should be tested to rule out Qwen-specific artifacts. The paper_framing.md lists this as anticipated concern #3 and #4, and D021 planned 3 additional models, but none were run.

2. **Non-logic domain evaluation.** GSM8K, commonsense reasoning (e.g., StrategyQA), or any task outside formal logic is needed to assess generalizability. Currently the method is validated only on tasks designed for FOL reasoning.

3. **Constraint ablation.** Is MAX-SAT necessary, or would simpler constraint-count weighting achieve the same tiebreak quality? The paper_framing lists this as anticipated concern #9 (exp-013) but it was not executed.

4. **Confidence intervals on the C0-gap regression.** With 8 data points and significant non-independence, the prediction interval for the C0 threshold of 0.21 should be reported. A bootstrap CI on the slope and intercept would reveal the uncertainty.

5. **Per-question analysis of SICA losses.** The confusion matrix shows SICA loses 1 question on the 60-question pilot (where SC was correct but SICA was wrong). At 804 questions, how many such losses occur? If SICA flips correct SC answers to incorrect ones on non-tied questions, the mechanism is less principled than claimed.

6. **Odd-K experiments.** The paper only tests even K (where exact ties are possible). Testing K=11 or K=13 would reveal whether SICA provides any value beyond tiebreaking, which would clarify whether the contribution is genuinely about constraint quality or merely about resolving an artifact of even-K sampling.

---

## Score and Confidence

**Score: 3 (Weak Reject)**

**Confidence: 4/5 (high)**

**Justification:** The paper addresses a reasonable question (when does symbolic consensus help?) and the C0 operating regime concept has merit. However, the positive results are confined to a single model family on two closely related logic benchmarks, the claimed statistics in the best-tier paper substantially exceed what the median projections support, the actual completed experiment (60 questions, p=0.226) does not reach significance, and SICA's improvement mechanism reduces to tiebreaking on exact vote splits rather than the "constraint-based aggregation" suggested by the framing. The contribution as a tiebreaker is real but narrow -- insufficient for a top venue at ~25% acceptance rate. The missing cross-family and cross-domain experiments are not optional extensions but prerequisites for the claims made. If the expanded 804-question results and cross-family validations were completed and confirmed the best-tier projections (particularly p<0.05 combined and non-zero PW gain), this could rise to a 4 (Weak Accept), but the current evidence does not support the claims.
