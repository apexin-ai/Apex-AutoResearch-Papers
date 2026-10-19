# Response to Reviewers

**Paper**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Round**: R23 (Overall: 3.0 Findings)
**Target**: 3.5 Borderline Conference / Findings acceptance

---

## Summary of Changes

| # | Change | Addresses | Commit |
|---|--------|-----------|--------|
| 1 | Abstract rewritten with "doubly conditional" framing, compressed 280→192 words | R22-N2, R22-N4, R23-W4 | 0d2604c |
| 2 | Intro: "retrospective classification—not online detection" explicit scope | R22-W4 | 23e8e5e |
| 3 | "cross-architecture" → "two architecture families" throughout | R23-N2 | 5087a69 |
| 4 | Limitations section changed to `\section*` (unnumbered, EMNLP format) | R23-W6 | 5087a69 |
| 5 | 3 missing references added (arXiv 2605.18549, 2603.01326, 2504.05419) with positioning | R23-REF | 54c44ad |
| 6 | Discussion §1: novelty distinction — directional systematicity vs general sensitivity | R23-N3 | 54c44ad |
| 7 | Discussion §3: audit protocol with concrete decision criteria (>20% depth divergence, >1.5x volatility) | R23-N4 | 54c44ad |
| 8 | Conclusion expanded from 2→3 sentences (directional mechanism + doubly conditional + future work) | R23-W6 note | 54c44ad |
| 9 | Intro p-value consistency fix (QwQ-32B: p<0.001 → p<0.005, matching Table 2) | consistency | abd1425 |
| 10 | R1-8B random-label control planned (GPU pending) | R23-N2, R22-N3 | — |

Code, annotations, and hidden-state extraction scripts will be released upon acceptance to facilitate reproducibility.

---

## Response to Critical Issues

### C1: 32B sample size underpowered (R23-N1)

**Reviewer concern**: With n=19-20, 32B results are underpowered; bootstrap CIs are wide (MDE 8.6-9.5pp), yet Contribution 1's core argument ("had we reported only CR-composite results...") relies on 32B reversal evidence.

**Our response**:

Contribution 1 (layer selection bias) does not depend on 32B statistical power. The *direction* of the CR→shallow bias is observed in all 4 models with 100% consistency (Table 2: L0, L0, L2, L10 for CR-composite vs L14, L16, L63, L63 for threshold-based). This directional finding is a geometric property of transformer representations—confirmed by random-label controls where 100% of permutations retain shallow selection for crossing rate (Appendix B.1, Table 7)—and does not require large samples to establish.

The 32B models do have adequate statistical protection for the final HS-vs-text tests. Exact sign-flip permutation tests (exhaustive 2^19/2^20 enumerations) yield: QwQ-32B precision p=0.003, BA p<0.001; R1-32B precision p<0.001, BA p=0.008—all rejecting at α=0.05 (Appendix D, Table 10). Power analysis confirms observed effects (+15.4–19.2pp) exceed MDE at 80% power (Appendix Z, Table 39). All 32B results are marked exploratory (†) in the Abstract, Tables, and throughout the text.

We acknowledge that the *dramatic demonstration* of conclusion reversal (p=0.83 vs p<0.005 for QwQ-32B) is concentrated in the 32B models. However, the underlying mechanism (cosine compression → crossing-rate inflation at shallow layers) is architecture-general and sample-size-independent. The 32B models provide the most striking illustration because their deeper architectures (64 layers) create a wider gap between CR-composite and threshold-based selections.

**Evidence**: Table 2 (layer selection); Appendix D (Holm-Bonferroni, Table 10); Appendix Z (power analysis, Table 39); Abstract "n ≤ 20" and "exploratory" marking.

---

### C2: Architecture diversity insufficient (R23-N2)

**Reviewer concern**: 3/4 models are Qwen architecture; "cross-architecture" claim is overclaimed.

**Our response**: We have corrected the wording to "two architecture families" throughout the paper. The CR→shallow bias is observed in both Llama (R1-8B: L0) and Qwen (OT-7B: L0, QwQ-32B: L2, R1-32B: L10), with consistent cosine volatility ratios across both architectures (Appendix C, Table 8). The random-label control on QwQ-32B confirms the mechanism is geometric; cosine volatility analysis on R1-8B confirms shallow-layer compression exists in Llama (Appendix C). We acknowledge that extending to non-Qwen/Llama architectures (e.g., Gemma, Mistral) remains important future work (Limitations §1). An R1-8B random-label control experiment is planned to provide cross-architecture mechanistic verification.

**Evidence**: Table 2; Appendix C (Cosine Volatility, both architectures); Limitations §1.

---

### C3: Novelty unclear vs Belinkov (2022) (R23-N3)

**Reviewer concern**: Probe sensitivity to layer/metric choice is already documented in the probing literature; the paper needs clearer differentiation from known problems.

**Our response**: We have added an explicit distinction in Discussion §1: "While general probe sensitivity is well-documented (Belinkov, 2022), our finding is directional: cosine compression at shallow layers systematically biases crossing-rate metrics toward early layers, producing predictable conclusion reversals." Belinkov (2022) documents that probing results vary with hyperparameters—our contribution shows this variation is *systematic and predictable*: crossing-rate metrics always select shallow layers because of representation geometry (cosine compression), while threshold-based metrics always select deep layers. This is not unpredictable sensitivity but a deterministic geometric mechanism confirmed by random-label controls (100% shallow selection under permuted labels). The distinction is: general sensitivity → unpredictable variation; our finding → predictable, directional conclusion reversal driven by a specific geometric property.

**Evidence**: Discussion §1 (revised); Table 2 (systematic direction); Appendix B.1 (Random-Label Decomposition, Table 7); Appendix C (Cosine Volatility mechanism).

---

### C4: No actionable solution (R23-N4)

**Reviewer concern**: The multi-metric ensemble Ens-Best is not significant (p>0.27); the audit protocol lacks concrete decision criteria.

**Our response**: We have added concrete decision criteria to Discussion §3: (1) if selected layers diverge by >20% of total depth across metrics, treat conclusions as metric-dependent; (2) if inter-step cosine volatility ratio exceeds 1.5x between candidate layers, prefer the lower-volatility layer for threshold-based conclusions. These thresholds are empirically grounded: the 20% divergence threshold captures all four models' CR-vs-threshold gaps (Table 2: 44–98% divergence), and the 1.5x volatility threshold is conservative relative to observed ratios (1.4–2.7x; Appendix C, Table 8). The three-layer ensemble eliminates metric pre-selection entirely with all four models significant (p ≤ 0.002; Appendix Z.1, Table 40). While Ens-Best vs single-best is not significant, the ensemble's value is *robustness to metric choice*, not superiority to the best single metric.

**Evidence**: Discussion §3 (revised); Appendix C (volatility ratios, Table 8); Appendix Z.1 (Ensemble, Table 40).

---

### C5: Single dataset limits all claims (R23-N5)

**Reviewer concern**: All experiments use only HarmThoughts; AdvBench (388 traces) is available but unused for layer selection reversal verification.

**Our response**: HarmThoughts is currently the only publicly available dataset with step-level Safety Commitment Point annotations, which are required for temporal probe training and evaluation. AdvBench lacks step-level CP annotations, making temporal probe analysis infeasible without additional annotation effort. However, we provide cross-dataset geometric evidence: AdvBench cosine volatility ratios confirm the same shallow-layer compression pattern (1.67x ratio; Appendix C, Table 9), validating that the geometric precondition for crossing-rate bias generalizes beyond HarmThoughts. We acknowledge this limitation prominently in Limitations §1 and note that extending to additional annotated datasets is critical future work.

**Evidence**: Appendix C (AdvBench cosine volatility 1.67x, Table 9); Appendix B.1 (Random-Label Decomposition, label-independent); Limitations §1.

---

## Response to Warning Issues

### W1: QwQ-32B HS advantage absorbed by quadratic position (R23-W1)

**Reviewer concern**: Table 29 shows QwQ-32B HS advantage becomes -1.0pp under quadratic position residualization, suggesting the HS probe may primarily be a position detector.

**Our response**: This is reported transparently: the Abstract states "partially overlaps with temporal position"; Discussion §2 explicitly notes QwQ-32B's quadratic absorption (Table 29). Crucially, this finding is QwQ-32B-specific: R1-8B and OT-7B are unaffected by quadratic control. The residualized HS probe performs above chance (p<0.001), but its margin over the text baseline is not significant (precision +4.5pp, p=0.133 at n=19). This is precisely why we frame QwQ-32B's advantage as exploratory and doubly conditional—conditional on both encoder quality *and* position control. Under linear residualization, 3/4 models retain significance; under quadratic, 2/4—we report both levels completely (Table 29).

**Evidence**: Abstract ("doubly conditional"); §4.3 (position mediation); Appendix V (Position Residualization, Table 29); Discussion §2.

---

### W2: R1-32B control task selectivity 3.0pp (R23-W2)

**Reviewer concern**: R1-32B's residualized selectivity is 3.0pp, below the 5pp threshold from Hewitt & Liang (2019), making results questionable.

**Our response**: The 3.0pp value is *residualized* selectivity (after removing position-correlated signal). Raw selectivity is 16.8pp, well above the 5pp threshold, confirming genuine safety structure exists. The low residualized value indicates substantial position overlap, which is why R1-32B is marked exploratory (†) with explicit caveats. Discussion §1 now clarifies this distinction. Combined with n=20 and W=1-only significance, R1-32B's evidence is the weakest in our study—we do not hide this.

**Evidence**: Discussion §1 ("residualized selectivity is 3.0pp"); Appendix H (Control Task); §4.4 (32B-specific analysis).

---

### W3: CP binary formulation crude (R23-W3)

**Reviewer concern**: Oscillating traces may be misclassified; the proportion and error rate are unquantified.

**Our response**: CP is defined as "the first reasoning step after which safety deliberation permanently ceases" (§1)—a deterministic rule applied to published HarmThoughts annotations, reducing subjective judgment. Limitations §4 explicitly acknowledges oscillating traces as a limitation: "In practice, some reasoning traces exhibit oscillating patterns where the model intermittently returns to safety-aware reasoning." Quantifying the exact proportion requires re-annotation with relaxed CP definitions, which we identify as future work. The AdvBench LLM-based annotation achieved Cohen's κ = 0.606 (Appendix J.1, Table 19), providing proxy evidence for CP-type annotation reliability.

**Evidence**: §1 (CP definition); Limitations §4; Appendix J.1 (IAA, κ=0.606, Table 19).

---

### W4: Abstract information overload (R23-W4)

**Reviewer concern**: ~190 words with excessive numbers sacrifices readability.

**Our response**: The abstract was compressed from ~280 to 192 words in revision. Given that the paper's core contribution is methodological (quantifying how metric choice reverses conclusions), the specific numbers (+15.4 to +21.9pp, 4/4→1/4 HB, p=0.83 vs p<0.005) are essential to the abstract's argument—they demonstrate the reversal effect concisely. Further trimming risks losing the quantitative evidence that distinguishes our work. We defer to the reviewer's judgment on whether additional reduction would improve accessibility.

**Evidence**: Abstract (revised, 192 words).

---

### W5: Negative results failure analysis shallow (R23-W5)

**Reviewer concern**: Seven failed methods have only 1-2 sentences of explanation each.

**Our response**: The 8-page main text limit constrains detailed failure analysis. Section 4.6 provides the key diagnostic insight: "These failures show the signal is directional, gradual, model-specific, and linearly separable." Detailed per-method analysis is available in Appendix Q (Negative Results Details): BOCPD/CUSUM fail because the transition is gradual rather than abrupt; Mahalanobis fails because the pre/post-CP distributions overlap substantially; RepE is model-dependent because safety directions are not universal across architectures; cross-model transfer fails because representations are model-specific. We can expand the appendix discussion if reviewers find it insufficient.

**Evidence**: §4.6 (Table 23); Appendix Q (Negative Results Details).

---

## Response to Questions

### Q1: Is QwQ-32B's HS probe essentially a position detector?

Partially yes—under quadratic position residualization, the HS advantage is absorbed (Table 29: -1.0pp). The residualized HS probe still exceeds chance (p<0.001), but its margin over the text baseline is not significant (precision +4.5pp, p=0.133 at n=19). The "doubly conditional" framing already front-loads this conclusion: QwQ-32B's HS advantage may not generalize when position is controlled. R1-8B and OT-7B are unaffected by quadratic control, supporting genuine non-positional safety signal in smaller models.

**Evidence**: Appendix V (Position Residualization, Table 29); §4.3; §4.4.

---

### Q2: Why no nested CV on 32B?

With n=95 total (QwQ-32B) or n=100 (R1-32B), a 60/20/20 split yields ~57 train traces. Nested 5-fold CV on the train set would create inner validation folds of ~11 traces (~5-6 per class)—insufficient for stable layer/window selection across a 64-layer × 7-window search space. We use LOO-CV and multi-seed analyses (Appendix B, Appendix X) as partial robustness checks, and report nested CV shrinkage estimates from the 7-8B models (13-25%; Appendix W.1) as reference bounds.

**Evidence**: §4.4 (nested CV infeasibility); Appendix B (LOO-CV); Appendix X (Multi-Seed); Appendix W.1 (Nested CV on 7-8B).

---

### Q3: Does random-label → shallow simply reflect noise?

No. If shallow layers were merely noisier, threshold-based metrics would *also* prefer shallow layers under random labels—but they do not. Random-label threshold-based metrics scatter across layers (mean L33-36, only 10-20% deep), losing their deep-layer preference entirely. Only crossing-rate retains its shallow preference (100% under random labels). This asymmetry confirms the bias is specific to the crossing-rate mechanism (cosine compression → inflated threshold crossings), not general noise. R2's counter-argument in the reviewer discussion is correct.

**Evidence**: Appendix B.1 (Random-Label Decomposition, Table 7); Appendix C (Cosine Volatility).

---

### Q4: CP annotation IAA and systematic bias risk?

HarmThoughts annotations come from the published benchmark. Our CP definition ("first step after which safety deliberation permanently ceases") is a deterministic text-pattern rule, reducing subjective judgment. We have not computed CP-position vs chain-length correlation, but note that position mediation analysis (§4.3) controls for this: residualized HS advantage removes linear and quadratic position effects. AdvBench LLM annotation achieved κ=0.606 (Appendix J.1, Table 19) as proxy IAA evidence. Multi-annotator IAA with Cohen's kappa is identified as future work.

**Evidence**: §1 (CP definition); §4.3 (position residualization); Appendix J.1 (IAA, κ=0.606); Limitations §1.

---

### Q5: Ensemble Ens-Best practical value?

The ensemble's value is *metric-independence*, not superiority over the best single metric. Ens-Best vs best-single is not significant (p>0.27), but the ensemble eliminates the need to pre-select a layer selection metric—all four models achieve p ≤ 0.002 without any metric choice (Appendix Z.1, Table 40). This directly addresses Contribution 1: if metric choice can reverse conclusions, removing metric choice from the pipeline is inherently valuable. Learned weighting is a natural extension but risks overfitting at current sample sizes.

**Evidence**: Appendix Z.1 (Ensemble, Table 40); Discussion §3 (audit protocol).

---

### Q6: AdvBench layer selection reversal?

AdvBench lacks step-level CP annotations, so full temporal probe training is infeasible. However, the geometric precondition for crossing-rate bias (shallow-layer cosine compression) is confirmed on AdvBench: volatility ratio 1.67x (Appendix C, Table 9). This validates that the representation geometry driving Contribution 1 generalizes beyond HarmThoughts, even though we cannot run the full probe comparison without CP labels.

**Evidence**: Appendix C (AdvBench Cosine Volatility, 1.67x, Table 9).

---

### Q7: Oscillating traces false positive/negative rate?

We have not quantified this rate, as it requires re-annotation with relaxed CP definitions. Limitations §4 acknowledges oscillating traces as a limitation. The binary CP assumption may introduce both false positives (trace marked as committed when model temporarily returns to safety reasoning) and false negatives (trace marked as uncommitted when oscillations eventually cease). Quantifying this rate and developing a soft-CP formulation are identified as future work.

**Evidence**: Limitations §4 (CP permanence assumption).

---

## Pre-emptive Responses to Anticipated Attacks

### A1: Crossing-rate composite is a strawman

Even if no prior work explicitly uses BA×CR as a layer selection metric, two arguments establish its relevance: (1) Any threshold-counting metric is susceptible to cosine compression at shallow layers—in compressed representation space, noise fluctuations more easily cross decision boundaries, inflating transition counts. This is an a priori prediction from the geometry, not a post-hoc observation. (2) "When does the model first trigger a safety detection?" is the natural temporal safety question; crossing rate formalizes exactly this notion of detection frequency. Any layer sweep that implicitly favors "transition-rich" layers is equivalent to incorporating crossing-rate logic. Our characterization of this failure mode class has value regardless of whether the specific composite metric has been used in prior work. See §4.2, Appendix C (Cosine Volatility).

### A2: Retrospective vs prospective gap

Abstract, Introduction §1, and Limitations all explicitly state retrospective scope. FPR 11-50% is acknowledged as non-deployable. Retrospective tools have independent value for post-hoc audit, model selection, and red-teaming. All prior work (TrajGuard, SafeSwitch) also evaluates retrospectively.

### A3: CP annotation IAA weakness

Published benchmark annotations; deterministic rule-based definition; AdvBench proxy κ=0.606 (Appendix J.1); limitation explicitly acknowledged. Multi-annotator IAA is future work.
