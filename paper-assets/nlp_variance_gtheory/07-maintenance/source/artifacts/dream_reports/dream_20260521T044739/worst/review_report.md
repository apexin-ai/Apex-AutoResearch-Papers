---
dream_id: dream_20260521T044739
tier: worst
overall_score: 5/10 — Borderline Reject
timestamp: 2026-05-21T06:09:44.545942+00:00
---

# Dream Review Report — Consolidated Roundtable

**Paper:** "Reproducibility Budgets for LLM Evaluation: Why Generalizability Theory Demands 3–4× More Items Than IRT"
**Venue:** AAAI 2026 (Main Technical Track, 1-10 scale)
**Review Mode:** Full (2 Reviewers, 4-step roundtable)
**Date:** 2026-05-21

---

## 1. Paper Summary

The paper applies Generalizability Theory (G-theory) to decompose evaluation variance in LLM benchmarks using a fully crossed design on MMLU: 4 models × 3 numerical precisions × 6 prompt templates × 6 random seeds × 3 temperatures × 4 item orderings × 200 items (825,600 total evaluation records). Four contributions are claimed: (1) metric-conditional reproducibility budgets showing an 87× G-coefficient gap between binary scoring (G=0.611) and text-exact-match (G=0.007); (2) the first direct IRT vs. G-theory comparison showing G-theory requires 3.3× more items (468 vs. 142) because it accounts for prompt, seed, and ordering facets that IRT ignores; (3) model×item interaction as design-sensitive — dropping from 26.2% (2 models) to 7.3% (4 models, CI: [3.1, 12.8]); (4) an open-source G-theory toolkit with D-study budget calculators. Preliminary cross-benchmark evidence from partial GSM8K and ARC-Challenge data is also reported.

---

## 2. Reviewer Panel

| Reviewer | Focus Area | Overall Score |
|----------|-----------|---------------|
| R1 | Methods & Experiments | 5/10 (adjusted to 4-5 after cross-sharing) |
| R2 | Novelty & Related Work | 5/10 |

---

## 3. Consolidated Strengths

### S1: IRT vs. G-theory comparison is the paper's strongest and most robust contribution
Both reviewers independently identified this as genuinely novel and actionable. The 3.3× item requirement gap is well-decomposed mechanistically (prompt×item 32%, seed×item 28%, ordering/residual 40% of the gap), does not depend on the incomplete cross-benchmark or multi-hardware experiments, and directly informs practitioners choosing between IRT-based subsampling (e.g., tinyBenchmarks) and multi-facet reliability frameworks. This is the first such comparison in the literature. **Confidence: high — finding is self-contained and based on complete data.**

### S2: Dual-metric analysis reveals a non-obvious, practice-changing finding
The 87× gap between binary G=0.611 and text-exact-match G=0.007 is striking. Both reviewers agreed this is genuinely non-obvious — while one might expect string matching to be noisier, the magnitude of the gap (effectively zero reliability for text-exact-match at any temperature > 0) was not predicted by prior work. The practical implication — that reproducibility budgets cannot be specified without first conditioning on the evaluation metric — reframes the reproducibility problem. **Confidence: high.**

### S3: Comprehensive factorial design and robustness battery
The 7-facet fully crossed G-study design with 825,600 records is ambitious and well-executed for MMLU. The six methodological robustness checks (Bernoulli null simulation, bootstrap vs. jackknife agreement, fixed vs. random sensitivity, item resampling stability, infrastructure×methodology separability, power analysis) are unusually thorough for an empirical ML paper and address genuine vulnerabilities. The bootstrap-jackknife ratio (0.96–1.04) and fixed-random delta (max 0.070) provide confidence in the statistical machinery.

### S4: Honest calibration of incomplete results
The paper labels model×item interaction as "preliminary evidence" and cross-benchmark findings as "suggestive." The Limitations section explicitly acknowledges single GPU architecture, 7–9B model range, 200-item subsampling instability, inference-only scope, and Qwen3 data quality issues. This epistemic honesty is commendable and appropriate.

### S5: Item resampling stability test is a valuable methodological contribution
Testing variance structure stability across three independent 200-item stratified draws (exp-001b) is a critical validation that most psychometric studies in NLP omit. The finding that G-coefficient CV (0.139) is substantially lower than variance component CV (0.30) — meaning reliability estimates are more robust than individual percentage allocations — is useful for the field.

---

## 4. Consolidated Weaknesses

### W1 [Major]: Model×item interaction finding is statistically underpowered and unstable
**Both reviewers converged on this as a central weakness.** The 4-model bootstrap CI for model×item is [3.1, 12.8] — wide enough to include trivially small values comparable to prompt×item or seed×item. The dramatic drop from 26.2% (2-model) to 7.3% (4-model) demonstrates estimation instability rather than a robust finding. Classical G-theory guidelines (Brennan, 2001, Ch. 4) recommend ≥5-6 levels for the smallest facet; 4 models is below this threshold. The bootstrap CIs capture item-resampling uncertainty but not model-sampling uncertainty — the 4 models are fixed across all resamples. A leave-one-model-out analysis is absent. The paper appropriately labels this as "preliminary evidence," but it still occupies substantial real estate (Section 4.4, Table 5, Table 6) and features in the abstract as a numbered finding.

### W2 [Major]: REML on binary data is a fundamental concern not fully resolved
G-theory was developed for continuous scores, and REML assumes normally distributed residuals. Binary (0/1) item responses violate this assumption. The Bernoulli null simulation (observed/null ratio = 671×) demonstrates that item variance is not merely mechanical, but does not validate that REML correctly partitions variance among interaction terms. The paper does not compare with logistic-link generalized G-theory approaches (Jiang & Skorupski, 2017) or engage with the extensive psychometrics literature on binary-data G-theory (Brennan, 2001, Ch. 12; Shavelson et al., 1989; Mushquash & O'Connor, 2006). This is both a methodological gap and a related-work gap.

### W3 [Major]: Scope narrowing creates a gap between claims and evidence
The title promises "3–4× More Items Than IRT" generically, but evidence is primarily MMLU on a single GPU architecture with 7–9B models. Cross-benchmark data covers only 1.5 benchmarks (GSM8K complete for 1 model, ARC partial). Multi-hardware experiment (exp-003) was not completed. 14B model extension (exp-005) was not completed. The paper's D-study recommendations are MMLU-specific but framed with broader language. R2 suggested a more precise title: "Reproducibility Budgets for MMLU: A G-Theory Analysis of Variance Sources in LLM Evaluation."

### W4 [Moderate]: Positioning against Mesting (2026) lacks critical nuance
Mesting (2026, ACL) found judge choice to be the single largest variance source (43.8%). This paper excludes judge as a facet, which mechanically inflates item_id dominance. Without explicit discussion of this design trade-off, readers may incorrectly compare item_id percentages across the two studies. The paper claims four extensions over Mesting — but extension (a) (infrastructure crossing) yields a near-null result (<0.5% infrastructure×methodology for binary), meaning the most-emphasized distinction contributes least. The work is better characterized as an empirical extension within Mesting's framework than as a new framework.

### W5 [Moderate]: Single GPU architecture undermines "infrastructure" claims
The "infrastructure" facet is limited to numerical precision (BF16/FP16/FP32) on a single GPU type (RTX PRO 6000). Hardware-specific effects documented by Yuan et al. (2025) — CUDA kernel implementation differences, memory bandwidth effects — remain unquantified. The abstract and introduction should qualify "infrastructure" as "numerical precision" throughout. The conditional separability finding (<0.3% infrastructure×methodology for binary) holds for the narrowest possible definition of infrastructure.

### W6 [Moderate]: Several relevant citations are missing
- Sclar et al. (2024, ICLR): up to 76% accuracy swing from prompt formatting — directly relevant to prompt×item variance component
- Kunievsky & Evans (2025): alternative variance decomposition framework (intent/articulation/model uncertainty) that competes with G-theory
- Classical psychometrics on binary G-theory: Brennan Ch. 12, Shavelson et al. 1989, Mushquash & O'Connor 2006, Jiang & Skorupski 2017
- Bui et al. (2025): extreme seed sensitivity in fine-tuning

### W7 [Minor]: Item dominance finding is partially expected
In any assessment with a wide difficulty range, item variance dominates — this is well-established in educational measurement (Lord & Novick, 1968). The paper's contribution is in quantifying the magnitude within a multi-facet LLM design and showing its metric-conditionality, not in the item dominance finding per se. The framing in the abstract and introduction treats this as more surprising than it is.

### W8 [Minor]: Cross-benchmark evidence belongs in appendix, not main results
With only GSM8K (1 model) and ARC-Challenge (~70% of 1 model), Tables 7 and 8 in the main results section overweight incomplete data. These should be moved to an appendix with appropriate caveats if retained.

---

## 5. Key Questions for Authors

**Q1 (D-study stability):** How sensitive are the D-study item count recommendations to item-sampling uncertainty? Specifically, what are the D-study recommendations for G≥0.80 when computed separately on each of the three resampling draws from exp-001b? If the 468-item recommendation ranges from, say, 350–600, this materially affects the paper's headline number.

**Q2 (Pairwise model×item):** Can you provide model×item variance estimates for all six pairwise 2-model combinations among the 4 models? This would clarify whether the 2-model estimate (26.2%, Llama+Gemma) was anomalously inflated by architectural maximization, and whether the 4-model estimate has stabilized.

**Q3 (IRT fairness):** The IRT comparison uses a basic 2PL model. Modern IRT-based subsampling (e.g., computerized adaptive testing, multidimensional IRT) can be more efficient. Does the 3.3× gap hold against a stronger IRT baseline? Is the SE<0.3 threshold for IRT comparable to the G≥0.80 threshold for G-theory?

**Q4 (Judge facet):** Given that Mesting (2026) found judge choice accounts for 43.8% of variance, are your D-study budgets valid for evaluation setups that use LLM-as-judge? Or would judge variance overwhelm the item/prompt/seed budget recommendations?

**Q5 (Generalized G-theory):** Have you considered or attempted a logistic-link generalized G-theory analysis (e.g., Jiang & Skorupski, 2017) as a robustness check against the REML-on-binary concern? If the variance component rankings and D-study recommendations are similar under both approaches, this would substantially strengthen the methodological credibility.

**Q6 (Qwen3 confound):** The ~3.2% re-executed Qwen3 conditions were run at a different time. How was it verified that software/environment drift did not introduce a systematic confound aliased with the model facet?

---

## 6. Roundtable Convergence Summary

### Areas of Strong Agreement (both reviewers)
1. **IRT vs. G-theory comparison is the strongest contribution** — novel, self-contained, robust to incomplete experiments
2. **Dual-metric 87× gap is non-obvious and practice-relevant** — strongest empirical finding
3. **Model×item interaction is underpowered** — 4 models insufficient, CI too wide, estimation instability from 2→4 models
4. **Cross-benchmark evidence is insufficient** for main results — should be appendix material
5. **REML on binary data needs stronger methodological defense** — missing engagement with generalized G-theory literature
6. **Single GPU type limits infrastructure claims** — "precision" ≠ "infrastructure"
7. **Paper is an empirical extension of Mesting (2026)** — the "first" language overstates methodological novelty

### Areas of Disagreement
1. **Degree of novelty in model-as-crossed-facet:** R1 sees it as a genuine conceptual contribution (despite execution issues); R2 sees it as an obvious design choice within the existing framework. **Resolution:** Conceptually meaningful but statistically underpowered — the idea outpaces the evidence.
2. **How expected is item dominance:** R2 argues it's well-known from classical psychometrics; R1 argues the 87× metric-conditional gap goes beyond what measurement theory predicts. **Resolution:** The item dominance rank is expected; the metric-conditionality and magnitude are not.
3. **IRT comparison as straw-man:** R2 raised concern that basic 2PL may underrepresent modern IRT capabilities; R1 accepted the comparison as fair. **Resolution:** The paper should at minimum acknowledge that more sophisticated IRT methods exist and discuss whether the gap would narrow.

---

## 7. Scores

### Dimension Scores (AAAI 1-10 scale)

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 4-5 | 5 | 5 |
| Novelty | — | 5 | 5 |
| Significance | — | 5 | 5 |
| Empirical Quality | 5 | — | 5 |
| Related Work | — | 4 | 4 |
| Clarity/Presentation | — | — | 6 |

### Overall Score: **5 / 10 — Borderline Reject**

### Confidence: 4/5 (high — both reviewers have relevant expertise and converged independently)

---

## 8. Meta-Assessment

### What would move this to 6-7 (borderline accept / accept):
1. **Complete the cross-benchmark experiments** with at least 2 fully completed benchmarks beyond MMLU (multi-model), enabling a credible task-type comparison
2. **Add generalized G-theory (logistic link) as a robustness check** to address the binary-data concern head-on
3. **Reframe the narrative**: lead with IRT comparison and metric-conditionality as headline contributions; explicitly position as an empirical extension of Mesting (2026); downweight or remove model×item from numbered contributions
4. **Add missing related work**: Sclar et al. (2024), classical psychometrics on binary G-theory, Jiang & Skorupski (2017)
5. **Narrow the title** to match evidence scope (primarily MMLU)
6. **Explicitly discuss the judge-facet exclusion** relative to Mesting's findings and its implications for comparing results across the two studies

### What would move this to 3-4 (clear reject):
- If the REML-on-binary concern were shown to distort variance component rankings (e.g., generalized G-theory yields qualitatively different decomposition)
- If the D-study recommendations are shown to be unstable across item draws (e.g., range 300–700 instead of ~468)
- If the IRT comparison is shown to be misleading against modern IRT methods

### Assessment Summary
The paper tackles a genuinely important problem (LLM evaluation reproducibility) with a principled psychometric framework (G-theory). The experimental design is ambitious and the robustness battery is thorough. The two strongest findings — the 87× metric-conditional G-coefficient gap and the 3.3× IRT-G-theory item requirement gap — are self-contained, well-supported, and practically valuable. However, the paper's scope has narrowed significantly from its ambitious framing: primarily MMLU, single GPU architecture, 7–9B models only, and a model×item finding that is statistically underpowered. The positioning overstates novelty relative to Mesting (2026), and important related work in classical psychometrics is missing. The REML-on-binary concern, while partially mitigated, remains a methodological vulnerability that the paper does not fully confront. With the revisions outlined above — particularly completing cross-benchmark experiments, adding generalized G-theory validation, and reframing the narrative around the two strongest findings — this could become an accept-level paper at a top venue.
