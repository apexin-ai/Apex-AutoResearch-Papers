---
dream_id: dream_20260517T013445
tier: worst
overall_score: reject
timestamp: 2026-05-17T02:15:13.703014+00:00
---

# Dream Review Report: Phase-Dependent Compound Severity Scales with Eviction Discriminativeness

**Dream ID**: 20260517T013445
**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)
**Venue Standard**: Top ML venue, ~25% acceptance, 6-point scale

---

## Roundtable Summary

### Step 1: Independent Reviews

**R1 (Method + Experiments)** and **R2 (Novelty + Related Work)** reviewed the paper independently. Both converge on a negative assessment, though for partially distinct reasons.

### Step 2: Cross-Sharing

R1's method concerns reinforce R2's novelty concerns: the "discriminativeness" concept that anchors the claimed scaling law is never formally defined or independently measured, making the "scaling law" framing even weaker than a mere 3-data-point empirical trend. R2's observation that the core finding is predictable from first principles aligns with R1's concern about phase segmentation circularity (phases defined by attention distribution properties that directly determine eviction behavior).

Both reviewers independently flagged: (a) Contribution #4 (discrimination collapse via Gini/CV analysis) is listed in the contributions but **no supporting analysis appears anywhere in the paper body**; (b) the recency control is confounded; (c) the GPQA random s=0.30 result is projected, not measured.

### Step 3: Convergence

**Points of agreement (high confidence):**
1. The statistical methodology is rigorous (Wilcoxon, bootstrap, Bonferroni, Cohen's d_z). This exceeds most empirical ML papers.
2. The core phenomenon (phase-dependent compound severity) is real but **predictable**: score-based eviction fails worse during phases with diffuse attention because the scores themselves become less discriminative. This is an expected consequence, not a surprising discovery.
3. The "scaling law" claim is overstated. Three benchmarks with different chain lengths showing a monotonic trend is an empirical observation, not a scaling law. No functional form is fitted, no extrapolation is validated.
4. No method contribution. No mitigation, no deployable system, no actionable algorithm. The paper is purely descriptive.
5. The paper has only **8 references**, far below the standard for any top ML venue. Critical areas are uncited: attention head pruning literature, CoT robustness, structured pruning, compression-quality tradeoffs.
6. **No figures at all.** The paper contains only tables. For a paper claiming a "scaling law" and dose-response patterns, the absence of any visualization is a significant presentation weakness.
7. Contribution #4 (discrimination collapse mechanism via Gini/CV) is a **phantom contribution**: claimed in the contribution list but absent from the paper body. This is a serious integrity issue.

**Points of partial disagreement:**
- R1 gives Soundness 3/6 (crediting the statistical framework), while R2 gives it implicitly lower by noting the mechanism doesn't explain the observations. **Resolved**: Soundness of the statistical tests is adequate; soundness of the explanatory framework is weak. Net: 3/6.
- R1 is slightly more generous on significance (3/6) than R2 (2/6). **Resolved**: Without a method contribution and with predictable findings, significance is low. Net: 2/6.

---

## Consolidated Review

### Summary

The paper studies compound sparsity (head pruning + KV cache eviction) in LLM inference and shows that the super-additive degradation varies across reasoning phases, with late phases more vulnerable. It further shows that random eviction on long-chain benchmarks (GPQA) produces nearly as strong phase gradients as importance-based eviction (ratio ~1.5x), while on medium-chain benchmarks (MATH-500) the ratio is ~16x. The paper frames this as a "scaling law" relating eviction discriminativeness to phase gradient magnitude.

### Strengths

1. **Rigorous statistical framework.** Wilcoxon signed-rank tests with Bonferroni correction, bootstrap CIs (B=10,000), Cohen's d_z effect sizes, and paired within-problem design. The statistical methodology is exemplary for an empirical ML paper.

2. **Honest limitation reporting.** The paper acknowledges that GPQA random s=0.30 is projected, that recency is not a clean negative control (reframed as "temporal locality confound"), and that this is a measurement study without a method contribution. This transparency is commendable.

3. **Cross-model consistency.** The Qwen/DeepSeek ratio (~40%) is stable across benchmarks (MATH-500 and GPQA), providing evidence that the phase gradient is a stable model-level property.

4. **Clear problem formulation.** The Interaction Index (II) as the super-additive perplexity component is well-defined, and the phase gradient metric G is a clean paired-difference measure.

5. **Appropriate self-positioning.** The paper correctly frames the universality of phase-dependent severity as the main finding, rather than over-claiming importance-specificity.

### Weaknesses

1. **(Major) Predictable finding, limited novelty.** The core observation reduces to: "score-based eviction degrades more during phases where attention is broadly distributed, because the scores themselves become less discriminative under head pruning." This is an expected consequence of how H2O-style scoring works. The extension to "random eviction also shows gradients on long chains" is interesting but can be trivialized as "removing more tokens from longer phases causes more damage." The novelty is quantitative documentation of a qualitatively predictable phenomenon.

2. **(Major) No method contribution.** The paper is purely descriptive. No phase-aware compression algorithm is proposed or tested. No mitigation strategy is presented. The practical implication ("be more conservative during late reasoning phases") is qualitative advice already implicit in phase-aware systems like ThinKV. For a top venue, an empirical finding paper needs either high surprise value or immediate practical utility; this paper offers neither.

3. **(Major) Phantom contribution.** Contribution #4 claims "discrimination collapse mechanism via Gini coefficient and coefficient of variation analysis of attention scores under compound sparsity." However, **no Gini coefficient analysis, no CV analysis, and no discrimination collapse characterization appears anywhere in the paper body.** A claimed contribution with no supporting content is a serious issue.

4. **(Major) Severely insufficient references.** The paper cites only 8 works. For any top ML venue, this is far below the expected standard (typically 30-50+ for a well-positioned paper). Missing entirely:
   - Attention head pruning foundations (Voita et al. 2019, Michel et al. 2019)
   - Structured pruning literature (magnitude pruning, movement pruning)
   - CoT reasoning robustness and sensitivity analysis
   - Additional KV cache methods (SnapKV, AdaKV, DuoAttention, KIVI, etc.)
   - Compression-quality tradeoff theory
   - Quantization as a compression axis

5. **(Major) No figures.** A paper claiming dose-response curves, scaling laws, and cross-benchmark trends presents zero figures. All data is in tables. The phase gradient trends, the imp/rand ratio vs. chain length relationship, and the dose-response curves should be visualized. The absence of figures makes it very difficult for reviewers to grasp the patterns quickly and undermines the "scaling law" narrative.

6. **(Moderate) "Scaling law" overstated.** The relationship between chain length and imp/rand ratio is observed across exactly 3 benchmarks (3 data points). No parametric form is fitted. No prediction is made for untested chain lengths. This is an empirical trend, not a scaling law.

7. **(Moderate) Recency control is confounded.** The paper correctly identifies that recency eviction preserves temporal locality, making it inherently mild for sequential reasoning. But it then fails to provide an adequate alternative control. The paper argues random eviction serves as the appropriate baseline, but this conflates the control's role: random was originally a "low discriminativeness" condition, not a negative control for the scoring mechanism.

8. **(Moderate) Projected results presented as findings.** The GPQA random s=0.30 result (gradient = 2.25) is explicitly noted as projected from trend extrapolation, not measured. Yet this projected value appears in Table 5 (the cross-benchmark comparison) and underpins the headline 1.47x ratio claim. A projected data point should not anchor a paper's central quantitative claim.

9. **(Moderate) Third architecture invisible.** The abstract and introduction claim experiments across "three model architectures" including DeepSeek-R1-Distill-Llama-8B. However, no LLaMA-specific results appear in any table. The third architecture exists only as a claim, not as reported data.

10. **(Minor) Phase segmentation is simplistic.** Equal-thirds partitioning by token position ignores the actual structure of reasoning (problem parsing, computation, verification). Content-aware segmentation could yield different (and potentially more informative) phase boundaries. The paper does not justify why equal thirds is appropriate beyond convenience.

### Questions for Authors

1. Where is the Gini coefficient and CV analysis claimed in Contribution #4? This analysis is absent from the paper.

2. Where are the DeepSeek-R1-Distill-Llama-8B results? The paper claims three architectures but presents data for only two (DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct).

3. Can you provide a concrete deployment scenario where knowing the exact magnitude of the phase gradient (vs. the qualitative intuition "protect late reasoning phases") would change an engineering decision?

4. The GPQA random s=0.30 ratio of 1.47x is projected. If the actual measured value were, say, 1.1x (effectively no discriminative advantage) or 2.5x (substantial advantage), how would this change the paper's conclusions?

5. Why does the paper contain no figures? The dose-response curves and cross-benchmark scaling trends are inherently visual and would benefit enormously from graphical presentation.

---

## Scores

| Criterion | R1 | R2 | Consolidated | Justification |
|-----------|----|----|-------------|---------------|
| Soundness | 3 | 3 | **3/6** | Statistical tests are rigorous, but the explanatory framework is weak. Contribution #4 is claimed without supporting analysis. One key data point is projected. Third architecture is invisible. |
| Novelty | — | 2 | **2/6** | The core finding is predictable from first principles. The "scaling law" is an empirical observation across 3 benchmarks. The measurement combination (compound x phase x strategy) is new in a narrow sense but not conceptually novel. |
| Significance | 3 | 2 | **2/6** | No method contribution, no mitigation, no deployable system. The finding does not change how practitioners would design compression systems beyond what is already implicit in phase-aware approaches. |
| Clarity | 4 | 4 | **3/6** | The writing is competent and the statistical reporting is clear, but: no figures, a phantom contribution, a missing architecture, and only 8 references significantly reduce the paper's clarity and completeness. |
| Overall | 3 | 2 | **2/6 (Reject)** | A statistically rigorous measurement study of a predictable phenomenon, with no method contribution, a phantom contribution claim, insufficient references, no figures, and limited practical impact. Does not meet the bar for a top ML venue. |
| Confidence | 4 | 4 | **4/5** | |

---

## Detailed Verdict

**Recommendation: Reject (2/6)**

The paper's statistical methodology is its clear strength, exceeding the rigor of most empirical ML papers. However, the contribution does not meet the bar for a top ML venue for the following reasons:

1. **Predictability**: The core finding (phase-dependent compound severity scaling with discriminativeness) is an expected consequence of attention-score-based eviction under head pruning, not a surprising discovery.

2. **Incompleteness**: A claimed contribution (Gini/CV discrimination collapse analysis) has no supporting content. A claimed third architecture has no reported results. A key data point is projected rather than measured.

3. **No actionable output**: The paper is purely descriptive with no method, algorithm, or demonstrated mitigation. The qualitative insight ("late reasoning phases are more vulnerable") is already captured by existing phase-aware systems.

4. **Presentation gaps**: 8 references and 0 figures are far below venue standards. Critical related work areas are entirely uncited.

**What would strengthen this paper:**
- Complete all claimed experiments and contributions (Gini/CV analysis, LLaMA results, GPQA random s=0.30 actual measurement)
- Add a working phase-aware compression method that demonstrates practical recovery
- Expand references to 30+ covering all relevant areas
- Add 3-4 figures visualizing the key trends (dose-response, scaling law, cross-benchmark comparison)
- Scale to at least one model where compound sparsity is deployed in practice (70B+)
- Fit an actual parametric scaling law with held-out validation, rather than observing a 3-point trend