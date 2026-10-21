# C3 Chapter Outline: Graduated Filtering for Depth-Aware Data Curation

> Two structural versions for Section 3 (experiments_c3.tex), contingent on exp-006 results.
> Version B is the primary fallback plan. Each paragraph specifies heading, topic sentence(s), and required tables/figures.

---

## Version A — Graduated Filtering Outperforms Binary

> Brief skeleton; this is the existing experiments_c3.tex trajectory.

### A.1 Introduction paragraph (existing)

**Heading**: (Section intro, no separate heading)

**Topic**: The K\*=2 boundary implies a three-tier taxonomy (human / gen-1 / gen-2+); binary filtering discards depth-1 text that retains most original signal; we test whether soft depth-aware weighting improves downstream quality.

### A.2 Filtering strategies (existing)

Six strategies as currently written. No change needed.

### A.3 Results — Main comparison

**Heading**: Results

**Topic**: Graduated filtering at optimal alpha\* achieves statistically significant gains over both binary baselines on MMLU and HellaSwag, validating the practical utility of the K\*=2 trichotomy for data curation.

- **Table 1** (tab:filtering_main): 6 strategies x {MMLU, HellaSwag}, mean +/- std over 5 seeds. Graduated row bolded.
- **Figure** (optional): bar chart with 95% CI error bars, 6 strategies side by side.

### A.4 Alpha sensitivity

**Heading**: Alpha sensitivity

**Topic**: The optimal alpha\* lies in the moderate range (neither alpha->0 nor alpha->infinity), reflecting the value of retaining depth-1 content with gentle down-weighting rather than hard exclusion.

- **Table 2** (tab:alpha_sweep): alpha x {MMLU, HellaSwag}, 5 alpha values.
- **Figure** (optional): line plot alpha vs. accuracy, showing inverted-U shape.

### A.5 Analysis

**Heading**: Analysis

**Topic**: The gain is attributable to depth-1 retention; graduated filtering also exhibits lower cross-seed variance, suggesting ordinal weighting provides a more stable curation signal than binary classification boundaries.

---

## Version B — Graduated Filtering Does Not Outperform Binary (Informative Negative)

> This is the primary outline. Detailed enough to write prose directly once exp-006 numbers arrive.

### Core narrative shift

**Old claim (C3)**: Graduated filtering exploits K\*=2 trichotomy to outperform binary filtering.

**New claim (C3)**: The K\*=2 discrimination boundary is not merely a characterization result but an operationally sharp threshold --- binary filtering at the K\* boundary already captures the actionable depth signal, and more granular graduated weighting yields no additional downstream benefit. This strengthens K\*'s status as a *sufficient* operational summary of generational depth structure.

### B.1 Section introduction

**Heading**: Graduated Filtering for Depth-Aware Data Curation

**Topic sentences**: Binary filtering treats all synthetic text as equally undesirable, discarding depth-1 content that is near-human in quality. A natural hypothesis is that the K\*=2 trichotomy enables a more nuanced strategy: soft depth-aware weighting that retains depth-1 text with reduced weight while aggressively down-weighting depth-2+ text. We test this hypothesis with six curation strategies spanning binary, graduated, and distribution-matching approaches.

**Required**: None (framing paragraph).

### B.2 Experimental setup

**Heading**: Filtering strategies / Training setup / Evaluation

**Topic sentences**: We compare six data curation strategies applied to a 30,000-document corpus (5,000 per depth, depths 0--5). [Strategy descriptions as in current tex.] Each strategy is evaluated via LoRA continued pretraining of Qwen2.5-1.5B-Instruct (rank 8, 3 epochs) on the filtered corpus, with downstream evaluation on MMLU and HellaSwag (0-shot) across 5 random seeds.

**Required**: Identical to current experiments_c3.tex B.2--B.4. No structural change.

### B.3 Results --- Main comparison

**Heading**: Results

**Topic sentences**: Table N presents downstream accuracy for each filtering strategy. All filtering strategies substantially outperform the no-filter baseline, confirming that recursive synthetic contamination degrades downstream quality. However, graduated filtering at its best alpha does not significantly outperform binary-ours (p > 0.05 by paired t-test across seeds), and the confidence intervals overlap across all alpha values tested.

**Key data points to report**:
1. No-filter vs. base model: quantify contamination cost
2. Binary-ours and binary-Drayson vs. no-filter: confirm filtering helps
3. Graduated (best alpha) vs. binary-ours: non-significant difference (report p-value, effect size, CI overlap)
4. Surprisal and DSIR as reference points for non-depth-aware baselines
5. If surprisal or DSIR outperform graduated, note this explicitly

**Required**:
- **Table 1** (tab:filtering_main): 6 strategies x {MMLU, HellaSwag}, mean +/- std, 5 seeds. No bold on graduated; bold on whichever strategy wins (likely binary-ours or DSIR). Add column for effective corpus size (fraction retained) to show graduated retains more data for no benefit.
- **Figure 1** (fig:strategy_comparison): grouped bar chart, strategies on x-axis, accuracy on y-axis, MMLU and HellaSwag side by side, 95% CI error bars. Visual emphasis: graduated bars same height as binary bars despite different mechanism.

### B.4 Alpha sensitivity --- monotonic degradation

**Heading**: Sensitivity to the decay parameter alpha

**Topic sentences**: Table N shows that graduated filtering performance is monotonically non-increasing in alpha: the lowest penalty (alpha=0.1) achieves the best or near-best accuracy, while higher alpha values progressively degrade toward hard filtering performance. This pattern is inconsistent with the hypothesis that an intermediate alpha\* captures a sweet spot between data retention and quality control; instead, it suggests that the ordinal depth signal beyond the binary boundary carries insufficient information to guide curation.

**Key data points to report**:
1. alpha=0.1 vs. alpha=0.9: quantify the degradation
2. alpha=0.9 vs. binary-ours: should be nearly identical (degeneration to hard filtering)
3. alpha=0.1 vs. binary-ours: the closest graduated gets, and still non-significant
4. Cross-seed variance at each alpha

**Required**:
- **Table 2** (tab:alpha_sweep): alpha x {MMLU, HellaSwag}, 5 alpha values, mean +/- std.
- **Figure 2** (fig:alpha_curve): line plot, alpha on x-axis, accuracy on y-axis, with horizontal dashed lines for binary-ours and no-filter. Shows graduated never exceeds binary-ours, and converges to it at high alpha. Shaded band = seed variance.

### B.5 Analysis I --- Why graduated fails to improve on binary

**Heading**: The sharpness of the K\* boundary

**Topic sentences**: The negative result for graduated superiority is informative: it indicates that the K\*=2 discrimination boundary is not merely a characterization convenience but an operationally sharp threshold. Depth-1 text, while detectably synthetic (0v1 AUC > 0.99), does not occupy a useful intermediate quality tier for curation purposes --- its downstream contribution is either comparable to human text (making down-weighting unnecessary) or comparable to deeper synthetic text (making graduated weighting no better than binary exclusion).

**Argument structure**:
1. **Bimodal quality hypothesis**: depth-1 text is a mixture of near-human and clearly-degraded documents; the depth label provides no additional signal beyond the binary classifier's confidence score, which already captures this variance.
2. **Feature evidence**: connect to Section C1' feature degradation --- surprisal variance drops sharply from depth 0 to 1, then plateaus. The graduated scheme's exp(-alpha * d_hat) assumes a smooth quality gradient that doesn't exist; the actual gradient is step-like at the human–synthetic boundary (depth 0→1).
3. **Effective corpus size**: graduated retains more documents but assigns low weights to depth-1 text, making the effective contribution marginal. Binary filtering achieves the same downstream quality with a cleaner signal.

**Required**:
- **Figure 3** (fig:feature_stepfunction): line plot of a key feature (e.g., surp_d1_std) across depths 0--5, showing step-function-like behavior at the human–synthetic boundary (depth 0→1) rather than smooth decay. Overlay with the exp(-alpha * d) weighting curves for alpha = {0.1, 0.5, 0.9} to visualize the mismatch between assumed smooth decay and actual step structure.
- Cross-reference Table 1 from C1' (AUC decay curve).

### B.6 Analysis II --- Binary at K\* boundary is the optimal practice

**Heading**: Binary filtering as optimal practice

**Topic sentences**: The convergence of evidence --- K\*=2 universality across model configurations, monotonic alpha degradation, and non-significant graduated-vs-binary differences --- supports a parsimonious practical recommendation: binary filtering at the K\* discrimination boundary is the optimal curation strategy for recursive synthetic contamination. This finding transforms C3 from a graduated-filtering contribution to a *validation* of K\*'s operational sufficiency.

**Argument structure**:
1. **Occam's razor for practitioners**: K\*=2 tells practitioners exactly what to do --- train a binary human-vs-synthetic classifier and filter. No ordinal depth estimation needed, no alpha tuning, no expected-depth computation.
2. **Connection to model collapse literature**: Drayson et al. (2025) SIR weighting is already binary; our result confirms this is not a limitation of their approach but a reflection of the underlying information structure. Even with access to ordinal depth estimates, one cannot do better than binary at K\*.
3. **Information-theoretic interpretation**: K\* marks the point where mutual information I(X_0; X_k) drops below the operational threshold. The graduated scheme attempts to exploit residual information in the 1v2 contrast, but this residual (1v2 AUC ~ 0.61--0.70) is insufficient to produce meaningful downstream differentiation.
4. **Comparison with DSIR and surprisal**: these depth-agnostic methods provide a lower bound on what non-depth-aware curation achieves. If they match or exceed graduated, the depth signal is provably not adding value beyond binary.

**Required**:
- No new table/figure; synthesizes from B.3--B.5 results.
- Cross-reference C1' 1v2 AUC values and K\* bootstrap CIs.

### B.7 Discussion paragraph (within section, before closing)

**Heading**: Limitations of the curation evaluation

**Topic sentences**: Several factors may attenuate the sensitivity of our evaluation to curation strategy differences: the LoRA fine-tuning protocol (rank 8, 3 epochs) imposes strong implicit regularization that compresses downstream differences; the corpus size (30,000 documents) is small relative to pretraining-scale data selection; and MMLU/HellaSwag measure broad capabilities that may be less sensitive to fine-grained corpus composition than domain-specific tasks.

**Argument structure**:
1. **LoRA bottleneck**: low-rank adaptation limits how much the model can exploit distributional nuances in the training corpus. Full fine-tuning or larger-rank LoRA might reveal graduated benefits.
2. **Scale**: 30K documents is a controlled but small corpus. At web scale, the volume of depth-1 content retained by graduated filtering could matter more.
3. **Evaluation granularity**: generation-intensive tasks (open-ended QA, summarization) may be more sensitive to corpus quality than multiple-choice benchmarks.
4. These caveats do not undermine the conclusion but scope it: *at the tested scale and evaluation protocol*, binary suffices.

**Required**: None (prose paragraph, no new data).

### B.8 Section summary

**Heading**: (Closing paragraph, no separate heading)

**Topic sentences**: The graduated filtering experiment yields an informative negative result: exploiting the ordinal depth structure beyond the K\*=2 binary boundary does not improve downstream language model quality under our evaluation protocol. This finding complements rather than contradicts the K\* characterization (C1'): it demonstrates that K\*=2 is not only a discrimination boundary but also an *actionable* boundary --- binary filtering at K\* is the simplest and most effective curation strategy, requiring no ordinal depth estimation or hyperparameter tuning beyond the binary classifier itself.

**Required**: None.

---

## Version B: Table/Figure Checklist

| ID | Type | Content | Status |
|----|------|---------|--------|
| tab:filtering_main | Table | 6 strategies x {MMLU, HellaSwag, effective corpus %}, 5 seeds | Awaiting exp-006 |
| tab:alpha_sweep | Table | 5 alpha values x {MMLU, HellaSwag}, 5 seeds | Awaiting exp-006 |
| fig:strategy_comparison | Figure | Grouped bar chart, 6 strategies, 95% CI | Awaiting exp-006 |
| fig:alpha_curve | Figure | Line plot alpha vs accuracy, binary/no-filter reference lines | Awaiting exp-006 |
| fig:feature_stepfunction | Figure | Feature value vs depth + exp(-alpha*d) overlay | Can draft now from C1' data |

## Version B: Contingency Triggers

- **Activate Version B if**: graduated (best alpha) vs. binary-ours difference is non-significant (p > 0.05) across both MMLU and HellaSwag, AND no alpha value achieves > 0.5pp improvement over binary-ours.
- **Stay with Version A if**: graduated achieves significant improvement (p < 0.05) on at least one benchmark with effect size > 1pp.
- **Hybrid (A/B) if**: graduated wins on one benchmark but not the other, or wins only for a narrow alpha range. In this case, use Version A structure but adopt Version B's interpretive framing ("marginal benefit, high complexity cost").

## Version B2 — Depth-Agnostic Methods Outperform Depth-Aware Filtering

> Contingency version if DSIR or surprisal-based filtering outperforms binary-ours on at least one benchmark (p < 0.05).

### Trigger condition

Activate Version B2 if a depth-agnostic baseline (DSIR or surprisal filtering) significantly outperforms binary-ours on MMLU or HellaSwag (p < 0.05, effect size > 0.5pp), regardless of graduated filtering's performance. If graduated also fails to beat binary, combine B2 framing with Version B's information-theoretic argument for binary optimality.

### B2.1 Results reframing

**Heading**: Depth-agnostic curation matches or exceeds depth-aware filtering

**Topic sentence**: DSIR (or surprisal filtering), which operates on distributional alignment (or surface-level quality heuristics) without any depth information, achieves XX.X ± X.X on MMLU compared to XX.X ± X.X for binary-ours, demonstrating that depth-specific filtering is not the optimal curation strategy even when accurate depth estimates are available.

### B2.2 Separating characterization from curation

**Heading**: K\* as a characterization boundary, not a curation prescription

**Topic sentence**: The K\* discrimination boundary answers the question "at what depth does generational identity become indistinguishable?"—a characterization question about the information structure of recursive synthetic text. That depth-agnostic methods outperform depth-aware filtering shows that the answer to this characterization question does not directly prescribe the optimal curation strategy: distributional alignment (DSIR) or quality heuristics (surprisal) capture curation-relevant signal that is orthogonal to depth.

### B2.3 Why depth-aware filtering underperforms

**Heading**: The gap between discrimination and curation

**Topic sentence**: Depth is a sufficient statistic for detecting contamination but not for predicting training utility—a document's downstream value depends on distributional properties (topic coverage, lexical diversity, factual density) that correlate imperfectly with generational depth. DSIR directly optimizes for distributional alignment with the target domain, capturing these properties without the indirection of depth estimation.

### B2.4 K\*'s independent contribution

**Heading**: The value of K\* beyond filtering

**Topic sentence**: Even when depth-aware filtering is not the optimal curation strategy, K\* retains independent scientific value: it quantifies the saturation point of depth discrimination, establishes that recursive generation produces a measurable structural boundary, and provides the theoretical grounding for why model collapse literature observes qualitative degradation thresholds. K\*'s contribution is to the understanding of recursive synthetic text, not to the engineering of data pipelines.

### Impact on other sections (B2-specific)

If Version B2 is activated, the following sections require adjustment relative to Version B:

- **Abstract**: Replace curation claim with "we show that K\* characterizes the depth discrimination boundary but that downstream curation benefits more from distributional alignment than depth-specific filtering."
- **Conclusion (C3)**: Frame C3 as a negative result for depth-aware curation, with K\*'s contribution repositioned as characterization rather than operational guidance.
- **Discussion 6.2 (Three-Level Schema)**: Weaken from "3-class taxonomy identifies the optimal filtering boundary" to "3-class taxonomy identifies a structural boundary; optimal curation may require orthogonal signals."
- **Discussion 6.6 (Drayson comparison)**: Note that Drayson's binary SIR, while optimal among depth-aware strategies, may itself be outperformed by depth-agnostic approaches—their contribution (like ours) is characterization of contamination structure.
- **Key takeaway 7.2**: Revise practitioner guidance to "K\* tells you where depth discrimination saturates; for curation, consider distributional matching (DSIR) or quality heuristics alongside or instead of depth-based filtering."

---

## Impact on Other Sections

If Version B is activated:

- **Conclusion (C3 summary)**: Use the pre-written Version B text from c3_contingency_versions.tex. Change "K\*-aware graduated filtering yields X% improvement" to "binary filtering at the K\* boundary is the optimal practice; graduated weighting does not yield additional benefit."
- **Discussion 6.2 (Three-Level Schema)**: Reframe from "3-class enables graduated curation" to "3-class taxonomy identifies the boundary; optimal curation is binary at that boundary."
- **Discussion 6.6 (Drayson comparison)**: Strengthen the argument --- Drayson's binary SIR is not a simplification but already optimal. Our contribution is explaining *why* via K\*.
- **Abstract**: Replace graduated filtering claim with "we show that binary filtering at the K\* boundary is the simplest optimal curation strategy, and graduated depth-aware weighting provides no additional benefit."
- **Key takeaway 7.2**: Simplify practitioner guidance --- "train a binary classifier, filter at K\*=2, done."
