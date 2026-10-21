---
dream_id: dream_20260522T221131
tier: worst
overall_score: 2.5 — Borderline Findings
timestamp: 2026-05-22T23:09:46.739542+00:00
---

# Dream Review Report — Consolidated Roundtable

**Paper**: "The Mirage of Significance: How Non-Independence Inflates Predictor Effects in Combinatorial LLM Evaluation Panels"
**Venue**: EMNLP 2026 (ARR)
**Reviewers**: R1 (Methods + Experiments), R2 (Novelty + Related Work)
**Review mode**: Full (independent → cross-share → convergence → synthesis)

---

## Meta-Review Summary

The paper investigates vulnerability of multi-judge LLM evaluation panels to adversarial attack, decomposing panel ASR into individual judge weakness (η\_max) and structural diversity (K\_eff) across 15 models, 455 panels, 9 attack types, and 3 benchmarks. The central finding is methodological: OLS regression overstates predictor significance due to structural non-independence (each model in 91/455 panels), with wild cluster bootstrap correction collapsing η\_max significance from 11/12→3/12 and K\_eff from 8/12→1/12 (SE inflation 3.2×). Two findings survive correction: an aggregation rule R² gradient (threshold 0.89 vs. Bayesian 0.10) and min-η\_max panel selection winning 9/12 conditions.

Both reviewers appreciate the experimental scale (15 models × 455 panels × 9 attacks × 3 benchmarks × 4 correction methods × 4 aggregation rules × 4 panel sizes) and the transparency in reporting how significance collapses under correction. However, both identify fundamental problems with novelty, framing, presentation, and several critical formatting issues that collectively place the paper below the Findings acceptance threshold.

---

## Formatting and Auto-Reject Concerns

**F1. Zero in-text citations.** The paper contains no citation markup anywhere across 9 pages. The Related Work section refers to "prior work," "this analogy has been informally invoked," and "extensive study" without ever naming a single reference. No bibliography/references section is included. This is a severe formatting issue that would likely trigger desk-reject scrutiny. For a paper whose primary contribution is methodological, the absence of citations to the foundational statistical methods being applied (Cameron, Gelbach & Miller 2008 for wild cluster bootstrap; Moulton 1986 for SE inflation from shared groups) is particularly damaging.

**F2. Possible page limit violation.** EMNLP 2026 enforces a strict 8-page limit for main text. The main text (Sections 1–6 Conclusion) extends into page 9. The Limitations section (exempt from the limit) occupies the remaining ~2/3 of page 9. The main text appears to be approximately 8.3 pages, exceeding the limit.

**F3. No figures.** The paper contains 13 tables across 9 pages but zero figures. For a heavily empirical paper documenting dramatic visual contrasts (OLS vs. bootstrap significance collapse, panel co-occurrence heatmaps, diversity-capability scatter), the complete absence of figures is a significant presentation deficit.

---

## R1 Review: Methods and Experiments

### Strengths

1. **Non-independence identification is genuine and important.** The structural observation that C(15,3) = 455 panels with each model in 91 panels creates severe cross-observation correlation is well-demonstrated. The side-by-side comparison of 4 correction methods (OLS, clustered SE, mixed effects, wild cluster bootstrap) is rigorous and transparent.

2. **BFT random-fault contrast is well-designed.** Testing whether K\_eff differentiates random faults from adaptive attacks is a clean experimental design. The GO/NO-GO gate framework (with pre-specified thresholds for Cohen's d, β ratio, contrast p-value) demonstrates good scientific practice, even though the gate fails.

3. **Aggregation gradient is the strongest surviving finding.** The R² gradient from threshold (0.89) to Bayesian (0.10) is a descriptive statistic unaffected by SE correction, providing genuinely actionable insight about how aggregation rule choice modulates vulnerability predictability.

4. **Capability-matched validation (Section 4.4).** The within-tier analysis revealing that η\_max significance depends on cross-tier spread (r = 0.82 between capability range and significance count) is a well-designed robustness check that reveals the confounded nature of the main finding.

5. **Panel size sensitivity (Section 4.6).** Demonstrating that SE inflation scales from 3.2× (K=3) to 7.2× (K=9) as model overlap increases from 91 to 2,002 panels is informative for future experimental designs.

### Weaknesses

1. **(Major) 15 clusters is insufficient for reliable clustered inference.** Cameron, Gelbach & Miller (2008) recommend ≥50 clusters for CR1 reliability. Wild cluster bootstrap with <20 clusters is known to be unreliable (Webb 2023). The max-p procedure (taking the maximum p-value across 3 cluster positions) further compounds conservatism. The paper's central finding — that K\_eff collapses to 1/12 under bootstrap — could be a power artifact rather than a genuine null. No power analysis is provided. This limitation is never discussed in the paper.

2. **(Major) K\_eff computation is never specified.** No formula is given for how the MI matrix is converted to K\_eff. How is MI estimated? What eigenvalue decomposition or thresholding is applied? The main predictor variable is irreproducible.

3. **(Major) Attack implementation is absent.** The 9 attack types are listed by name only. No prompt templates, no definition of "adaptive" in operational terms, no query budget, no details on how ASR is computed beyond one sentence. The gap between the claimed adaptive adversary threat model and the (presumably) fixed-template implementation is never addressed.

4. **(Major) Diversity-capability confound (r = 0.65) undermines predictor decomposition.** VIF > 7 for both predictors means the regression cannot reliably separate η\_max from K\_eff. The paper acknowledges this but still devotes 8 subsections to reporting results of a decomposition it has shown to be unreliable. K\_eff unique variance is only 3% — this should be prominently reported rather than buried in Section 4.5.

5. **(Moderate) Epsilon constant in log-log specification is unspecified.** log(ASR + ε) with unknown ε can substantially affect results for near-zero ASR values. Beta regression (the natural choice for [0,1]-bounded outcomes) is mentioned as giving K\_eff 3/12 but is not used as the primary specification without justification.

6. **(Moderate) No multiple testing correction across conditions.** Significance counts (e.g., "3/12") are reported without FDR or Bonferroni correction across the 12 or 18 conditions, creating an inconsistency in a paper that emphasizes proper statistical correction.

7. **(Moderate) MT-Bench results (Section 4.10) are extremely thin.** Bootstrap η\_max 1/12, K\_eff 0/12, with lower R² (0.15 vs. 0.25). Three attacks required "substantial adaptation." This effectively makes the paper a two-MCQ-benchmark study with an unconvincing third benchmark.

### R1 Scores
- **Soundness**: 3/5
- **Excitement**: 2.5/5
- **Reproducibility**: 2/5
- **Overall Assessment**: 2.5
- **Confidence**: 4/5

---

## R2 Review: Novelty and Related Work

### Strengths

1. **Experimental scale is impressive.** 15 models, 455 panels, 9 attacks, 3 benchmarks, 4 correction methods, 4 aggregation rules, 4 panel sizes — the combinatorial coverage is thorough and provides a complete landscape.

2. **Methodological transparency is commendable.** Reporting how significance changes across 4 correction methods, with honest admission that most findings collapse, sets a good example for NLP empirical work.

3. **GAM attack taxonomy.** The targeted/shared-bias split with directional K\_eff predictions is a useful organizing principle, though it develops 3 reversals when extended to 9 attacks.

4. **Aggregation gradient.** The threshold R²=0.89 vs. Bayesian R²=0.10 contrast is non-obvious and practically relevant.

### Weaknesses

1. **(Major) The central "finding" is a well-known statistical fact.** OLS overstating significance when observations are non-independent is standard econometrics (Moulton 1986, 1990). Clustered SEs, wild cluster bootstrap, and mixed effects are textbook corrections. Applying known corrections to a new domain (combinatorial LLM panels) and observing the expected result is not a methodological contribution — it is a methodological application. The abstract and introduction frame this as a discovery ("Our central finding is methodological"), which overstates the novelty.

2. **(Major) Related work is critically inadequate.** Section 2 spans ~0.5 pages with 4 brief paragraphs containing zero specific citations. Missing foundational references include:
   - Clustered inference: Cameron, Gelbach & Miller (2008); Cameron & Miller (2015); Moulton (1986, 1990)
   - Multi-annotator aggregation: Dawid & Skene (1979); Raykar et al. (2010); Welinder et al. (2010)
   - Ensemble diversity theory: Kuncheva & Whitaker (2003); Krogh & Vedelsby (1995); Brown et al. (2005); Dietterich (2000)
   - Adversarial ensemble robustness: He et al. (2017); Tramèr et al. (2018)
   - LLM-as-Judge: Zheng et al. (2024); Li et al. (2024)
   - Multi-agent debate: Du et al. (2023)

3. **(Major) Post-hoc reframing of negative results.** The paper reads as if the original hypothesis was that η\_max dominates and K\_eff matters directionally. When bootstrap correction collapsed both, the paper pivoted to "the collapse itself is the finding." While legitimate, this produces a paper that is structurally a collection of negative results wrapped in methodological commentary, lacking a clear positive contribution.

4. **(Major) Surviving findings are thin relative to paper length.** After the paper's own corrections, only two robust findings remain: (a) aggregation R² gradient, and (b) min-η\_max selection wins 9/12. Eleven subsections in Section 4 for two surviving findings and nine non-findings creates a bloated structure. The paper would benefit from substantial compression.

5. **(Moderate) Oracle adversary assumption limits practical relevance.** The adversary has complete knowledge of panel composition and per-judge vulnerability profiles. Under partial knowledge (Section 4.11), family knowledge adds only Δ=0.014 ASR over exact profile knowledge (p=0.18), but neither η\_max nor K\_eff significance improves. The practical relevance of findings under realistic adversary knowledge is unclear.

6. **(Moderate) Practical recommendation is trivial.** "Use the strongest available models" (min-η\_max ≈ strongest-K, r = 0.72) is not a novel insight. The two-stage algorithm adds only 0.003pp over simple min-η\_max selection, providing no marginal value. The entire practical contribution reduces to an obvious recommendation.

7. **(Moderate) K\_eff as sole diversity metric.** Alternative diversity metrics (Q-statistic, disagreement, κ-diversity) are not compared. Kuncheva & Whitaker (2003) showed no single diversity metric reliably predicts ensemble improvement — relying on one metric weakens generalizability.

### R2 Scores
- **Soundness**: 3/5
- **Excitement**: 2/5
- **Reproducibility**: 2.5/5
- **Overall Assessment**: 2.5
- **Confidence**: 4/5

---

## Roundtable Convergence

### Points of Agreement (R1 + R2)

1. **The non-independence observation is correct but not novel.** Both reviewers agree the structural non-independence in combinatorial panel designs is a real problem worth documenting, but applying standard econometric corrections to a new domain does not constitute a methodological contribution at the conference level.

2. **The paper reads as reframed negative results.** The original η\_max dominance and K\_eff diversity claims both collapse under correction. The paper pivots to "the collapse is the finding," but this creates a paper without a strong positive contribution.

3. **Related work is critically deficient.** Zero in-text citations anywhere in the paper. The Related Work section is ~0.5 pages of unsupported assertions. For a paper claiming methodological contribution, this is unacceptable.

4. **Surviving findings are modest.** Aggregation R² gradient and min-η\_max selection are the only robust results. Both are interesting but individually insufficient for a conference paper.

5. **Practical recommendation is trivial.** "Use strong models" is not a novel insight. The two-stage algorithm provides negligible marginal improvement (0.003pp).

6. **Reproducibility concerns.** K\_eff formula absent, attack implementations absent, epsilon unspecified. R1 rates reproducibility 2/5; R2 rates 2.5/5.

### Points of Disagreement

- **Severity of 15-cluster limitation**: R1 emphasizes this as potentially invalidating the K\_eff null (power artifact); R2 views it as less central because the finding (OLS inflation) is expected regardless. After discussion, both agree this is a major limitation that should be prominently discussed — the paper claims K\_eff is unreliable but never tests whether this is due to genuine absence of effect vs. insufficient cluster count for detection.

- **Excitement**: R1 initially rated 3/5 (for experimental breadth), R2 rated 2/5 (for limited novelty). After cross-sharing, R1 revised downward to 2.5/5, acknowledging R2's point that the methodological contribution is an application, not an innovation.

### Consolidated Assessment

The paper tackles an important and timely research question with impressive experimental scale. The transparency in reporting statistical correction is genuinely commendable and rare in NLP. However, the paper suffers from several fundamental problems:

1. **The central contribution is applying known statistical methods to a new domain**, which is valuable as a cautionary note but insufficient as a primary contribution for a venue paper.
2. **Zero citations** and critically thin related work undermine scholarly positioning.
3. **Possible page limit violation** (main text ~8.3 pages vs. 8-page limit).
4. **No figures** in a heavily empirical paper.
5. **The surviving findings are modest**: an aggregation R² gradient and a trivial panel selection recommendation.
6. **Critical reproducibility gaps**: K\_eff formula, attack implementations, epsilon constant.
7. **15-cluster limitation** is never discussed but may invalidate the K\_eff null.

---

## Consolidated Scores

| Dimension | R1 | R2 | Consolidated |
|-----------|-----|-----|-------------|
| Soundness | 3/5 | 3/5 | **3/5** |
| Excitement | 2.5/5 | 2/5 | **2/5** |
| Reproducibility | 2/5 | 2.5/5 | **2/5** |

## Overall Assessment: 2.5 (Borderline Findings)

The paper demonstrates genuine experimental rigor and commendable statistical transparency, but the central contribution (applying known econometric corrections to combinatorial LLM panel designs) is insufficient novelty for EMNLP Findings. The surviving empirical findings are modest. Critical presentation issues (zero citations, possible page limit violation, no figures) compound the problem. The paper would need substantial revision: (1) add a proper bibliography (30+ references) with in-text citations, (2) cut main text to 8 pages, (3) specify K\_eff formula and attack implementations, (4) add key figures, (5) reframe around the aggregation gradient and GAM taxonomy as primary contributions rather than the non-independence observation, (6) add power analysis for the 15-cluster limitation, and (7) honestly report K\_eff practical effect size (~0.8pp). With these revisions and a tighter narrative focused on 2-3 positive findings rather than 11 subsections of mixed results, a resubmission could target Findings (3.0) in the next cycle.

---

## Revision Roadmap (if resubmitted)

1. **Add bibliography and citations** — minimum 25-30 references covering clustered inference, ensemble diversity, LLM-as-judge, adversarial robustness, multi-annotator aggregation.
2. **Cut to 8 pages** — compress Sections 4.9 (ASR concentration), 4.10 (MT-Bench), 4.11 (partial-knowledge) into appendix. Focus main text on: (a) OLS→bootstrap collapse, (b) VIF/multicollinearity, (c) aggregation gradient, (d) panel selection.
3. **Specify K\_eff formula** — exact MI estimation method, eigenvalue decomposition procedure, and sensitivity to alternative diversity metrics.
4. **Add 3-4 key figures** — OLS vs. bootstrap significance comparison, diversity-capability scatter with Pareto frontier, aggregation R² gradient, panel co-occurrence heatmap.
5. **Add power analysis** — what K\_eff effect size can be detected with 15 clusters at 80% power? This contextualizes the null.
6. **Reframe narrative** — lead with "what we learned" (aggregation gradient, min-η\_max selection) rather than "what collapsed" (η\_max, K\_eff significance). The non-independence observation is supporting methodology, not the headline.
7. **Report practical effect sizes** — K\_eff IQR-based ΔASR of 0.8pp should be prominently featured. Even if significant, the effect is negligibly small.
8. **Discuss 15-cluster limitation** — acknowledge that bootstrap may be over-conservative and true η\_max significance likely lies between 3/12 and 11/12.

---

## 引用验证结果

**统计**: 40 篇文献 / 61 处引用 / 在线验证 40/40 篇

### 问题 (10)

- ⚠️ `almasoud2026security` — 元数据不匹配: first_author: bib=al masoud vs api=masoud
- ⚠️ `tramer2018ensemble` — 元数据不匹配: first_author: bib=tram\`er vs api=tramèr
- ⚠️ `schneier2000secrets` — 元数据不匹配: first_author: bib=schneier vs api=1963-
- ⚠️ `hendrycks2021mmlu` — 元数据不匹配: year: bib=2021 vs api=2025, first_author: bib=hendrycks vs api=son
- ❌ `condorcet1785essai` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.38 below threshold 0.82
- ⚠️ `brown2005managing` — 元数据不匹配: year: bib=2005 vs api=2023, first_author: bib=brown vs api=zelenkov
- ⚠️ `keppo2026fragility` — 在 .bib 中但正文未引用
- ⚠️ `kraskov2004estimating` — 在 .bib 中但正文未引用
- ⚠️ `schulhoff2023hackaprompt` — 在 .bib 中但正文未引用
- ⚠️ `zheng2024lmsyschat` — 在 .bib 中但正文未引用

### ✅ 通过 (34)