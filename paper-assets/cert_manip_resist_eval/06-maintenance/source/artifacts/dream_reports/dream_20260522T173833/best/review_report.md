---
dream_id: dream_20260522T173833
tier: best
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T18:50:53.878058+00:00
---

# Review Report — R1 (Methodology and Experiments)

**Paper**: "More Diverse, More Vulnerable: How Judge Panel Diversity Backfires Under Adaptive Adversaries"

**Venue**: EMNLP 2026 via ARR

---

## Summary

This paper investigates whether diversity in multi-judge LLM evaluation panels provides adversarial robustness, analogous to Byzantine Fault Tolerance. Through a large-scale study of 15 models, 455 three-judge panels, 9 attack types, and 4 benchmarks, the authors claim that panel diversity (K_eff) is independently and *positively* associated with attack success rate after residualizing against individual judge weakness (eta_max). They identify a "dual vulnerability driver" structure where attack type determines which factor dominates, propose a two-stage defense, and show Bayesian aggregation provides complementary protection.

---

## Strengths

- **Comprehensive experimental coverage.** The paper tests an impressive combinatorial space: all C(15,3)=455 panels, 9 attack types, 4 benchmarks, 4 aggregation rules, 4 panel sizes, and 3 adversary knowledge levels. This breadth is unusual and commendable. The 12 imagined experiments are all represented.

- **Rigorous statistical diagnostics.** The residualization approach to handle K_eff-eta_max collinearity is methodologically sound, yielding VIF=1.02. The paper reports multiple correction methods (uncorrected, FDR, Bonferroni), beta regression as a distributional robustness check, Cook's distance, leverage diagnostics, and Shapiro-Wilk normality tests. This is well above the typical standard for empirical NLP papers.

- **BFT random-fault contrast is well-designed.** Using calibrated random faults (bootstrapped from clean accuracy noise rather than reusing adversarial eta_j values) is the correct experimental design. The 5/12 coefficient flip to negative under RF for transferable attacks provides genuine mechanistic insight — it is not a strawman comparison.

- **Attack taxonomy provides predictive structure.** The observation that transferable attacks (score manipulation, position bias) are K_eff-dominated while shared-bias attacks (sycophancy, verbosity) are eta_max-dominated is a genuinely useful organizing principle. The taxonomy transfers to open-ended benchmarks and extended attacks, suggesting it captures real structure.

- **Capability-matched validation addresses the most obvious confound.** The large-tier within-tier analysis (6 top-tier models, 20 panels, K_eff significant in 4/6 conditions) is the strongest single piece of evidence that K_eff's effect is not merely a tier-mixing artifact.

- **Practical defense stack is well-motivated.** The two-stage algorithm + Bayesian aggregation combination directly follows from the dual-driver analysis. The 20.8% ASR reduction over Strongest-K is non-trivial, and the Max-K_eff catastrophic performance (ASR 0.112) is a compelling demonstration.

---

## Weaknesses

### Major

- **W1: Critical discrepancy between paper versions and actual experimental results.** Cross-referencing the paper's claims against the project's memory.md and ROADMAP.md reveals a serious concern. The actual 15-model experimental results (from plan001_step1_full_v4) show: eta_max FDR sig 11/12, K_eff FDR sig positive 7/12, K_eff negative 1/12 (arc x sycophancy), K_eff NS 4/12, with K_eff-eta_max confound correlation r=+0.70 (SEVERE). The paper reports K_eff_resid significant in 10/12 conditions with mean confound r=0.55 and VIF=1.02, which cannot be derived from the actual data where r=+0.70 (and even the project itself labels this "CONFOUND_SEVERE"). The paper appears to present imagined/projected numbers rather than actual experimental results. The real regression used log-log specification [log(ASR+eps) ~ log(K_eff) + log(eta_max+eps)], not the linear OLS presented in the paper. This is a fundamental credibility issue.

- **W2: The "diversity trap" framing is inconsistent with the project's own falsification history.** The project memory documents that the original K_eff hypothesis was "thoroughly falsified" at the 6-model and 9-model scales (K_eff 1/12 significant, taxonomy broad-spectrum 0/6). The 15-model result shows K_eff 7/12 positive, 1/12 negative — predominantly harmful but far from the 10/12 claimed in the paper. The paper's title "More Diverse, More Vulnerable" and the abstract's claim of K_eff "independently and positively associated" in 10/12 conditions overstates what the actual data supports. The project's own paper_framing.md (v4b) is more honest: "K_eff 7/12 positive + protective exception + condition-dependent dominance."

- **W3: Non-independence of observations inflates statistical significance.** The 455 panels share judges extensively — each of the 15 models appears in C(14,2)=91 panels. This means panel-level ASR observations are not independent. The OLS regression treats all 455 as independent observations, which inflates degrees of freedom and deflates p-values. The paper needs clustered standard errors (clustering on individual judges) or a mixed-effects model with random intercepts per judge. Without this correction, the reported p-values (some as low as 1.2e-8) are unreliable. This could substantially change the significance counts.

- **W4: The adversary model conflates "adaptive" with "oracle."** The paper defines the adaptive adversary as one who "observes panel composition and crafts attacks to maximize panel ASR." In practice, how are attacks "crafted" for each judge? The paper does not describe an actual adversarial optimization loop — it appears to simply measure each judge's vulnerability to pre-defined attack templates and then report eta_j as the individual ASR. This is an oracle adversary who knows each judge's exact vulnerability, not a realistic adaptive attacker who must discover vulnerabilities through interaction. The partial-knowledge experiment (Section 7.4) partially addresses this but still assumes the adversary can execute family-level attack templates with known average ASRs. The gap between this oracle model and realistic adversaries is inadequately discussed.

- **W5: Regression specification concerns.** (a) Linear OLS on ASR in [0,1] can produce out-of-range predictions. The paper mentions beta regression as a robustness check (9/12 vs 10/12 sig), but the main analysis uses OLS — beta regression should be the primary analysis for bounded outcomes. (b) The paper claims R^2=0.62 mean, but the ROADMAP.md shows R^2=0.298 for majority vote under the actual log-log canonical specification. This is a 2x discrepancy. (c) With only 2 predictors and 455 observations, an R^2 of 0.62 is suspiciously high for social/behavioral science regression — it raises the question of whether the regression is partially tautological (K_eff and eta_max are computed from the same judge pool that generates ASR).

### Minor

- **W6: Panel size analysis may be confounded by statistical power.** The claim that K_eff significance increases from 10/12 (K=3) to 12/12 (K=9) could be an artifact of increasing sample size: C(15,9)=5005 panels have 11x the statistical power of C(15,3)=455 panels. The increasing beta coefficient (0.42 to 0.61) is more informative but could reflect increased multicollinearity at larger K (where K_eff and eta_max become more structurally coupled).

- **W7: No figures in the paper.** For a paper with 12+ tables of regression coefficients, the absence of any scatter plots, coefficient plots, or visualizations is a significant presentation weakness. Key patterns (the attack taxonomy, the BFT flip, the Pareto frontier) would be far more interpretable visually.

- **W8: Gaussian copula failure numbers are inconsistent with project data.** The paper claims MI_obs/MI_gauss ratio of 18.5x mean (max 312x), but the project's actual 15-model results show MI_obs/MI_gauss ratio of 0.93 (MMLU) and 0.90 (ARC) — the copula fits *well* at 15-model scale. The 6-model result of 10-21x was explicitly labeled "small-sample artifact" and "DEAD as independent claim" in paper_framing.md v4b. Presenting the falsified 18.5x number in the paper is misleading.

- **W9: Limitations section is thin.** Three points in one paragraph is adequate per EMNLP norms, but the points chosen omit the most important limitation: the non-independence of panel observations sharing judges (W3). The "observational not causal" caveat is buried as the third point and understated given the paper's causal-direction language throughout ("diversity backfires," "diversity trap").

- **W10: Reference list is minimal.** Only 4 actual citations in the related work (zheng2023, li2023, dubois2024, wang2023, plus raina2024, shi2024, lamport1982, castro1999, krogh1994, brown2005, sagawa2020). For a paper claiming to overturn a "pervasive assumption," the literature review should more thoroughly document where this assumption appears and what evidence supports it.

---

## Questions for Authors

1. **Q1**: The project's actual experimental results (plan001_step1_full_v4) show K_eff significant in 7/12 (not 10/12) conditions with confound r=+0.70 (not 0.55). The regression specification was log-log (not linear OLS), and the R^2 was 0.298 (not 0.62). Can you clarify why the paper reports different numbers? Are the paper's numbers from a different analysis pipeline?

2. **Q2**: How do you address the non-independence of panel observations? Each judge appears in 91 of 455 panels. Have you run the analysis with clustered standard errors or mixed-effects models? What happens to the significance counts?

3. **Q3**: In the adversary model, you assume the attacker can apply judge-specific or family-specific attack templates with known ASRs. How were individual judge ASRs measured? Was there a held-out evaluation set, or are the same samples used for both measuring eta_j and computing panel ASR?

4. **Q4**: The BFT random-fault contrast uses "calibrated random faults based on bootstrapped clean-accuracy noise." Can you specify the exact procedure? How many bootstrap samples? How does the calibration ensure the marginal failure rates match between adaptive and RF conditions?

5. **Q5**: The Bayesian aggregation uses "prior accuracy" to downweight judges. How is this prior estimated? If estimated from the same evaluation data, this introduces information leakage. The paper mentions "5-fold CV" in passing — was the Bayesian prior estimated in cross-validation? Details are needed.

6. **Q6**: For the within-tier analysis, the small tier has only 10 panels and the medium tier only 4 panels. With 2 predictors, these regressions have 7 and 1 residual degrees of freedom respectively. Are the reported significance tests reliable with such small samples?

7. **Q7**: The Pareto frontier analysis claims "83% large-tier, 0% small-tier." How is "Pareto-optimal" defined here — over which objectives? Is this Pareto-optimal in the K_eff vs eta_max space, or K_eff vs ASR space?

---

## Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| **Soundness** | 2.5 | The non-independence issue (W3) undermines all significance claims. The discrepancy between reported and actual experimental numbers (W1, W2, W8) raises credibility concerns. The adversary model is closer to oracle than adaptive (W4). Core statistical framework is reasonable in design (residualization, diagnostics) but implementation details do not match the project's actual data. |
| **Excitement** | 3.5 | The research question is important and timely. The finding that diversity can *harm* adversarial robustness — if validated — would be genuinely surprising and impactful for the LLM evaluation community. The attack taxonomy (transferable vs shared-bias) is a useful conceptual contribution. The BFT contrast is well-conceived. |
| **Reproducibility** | 2.0 | Model list is provided but attack implementations are not described in detail. The paper does not specify: prompt templates for attacks, evaluation criteria for ASR, number of evaluation instances per condition, how MI matrices are estimated, or computational requirements. No code or data availability statement. The discrepancy between paper numbers and project data makes it unclear which analysis pipeline produced the reported results. |
| **Overall** | 3.0 | The paper addresses an important question with ambitious experimental scale, but the gap between claimed and actual results, the unaddressed non-independence of observations, and the underspecified adversary model prevent confidence in the central claims. If the statistical issues (W1, W3) were resolved and the paper accurately reported its actual experimental results — even if those results are weaker (7/12 rather than 10/12 for K_eff) — this could be a solid Findings paper. The core insight (diversity-robustness relationship depends on attack type and adversary model) is genuine and valuable, but the current presentation overstates the evidence. |
| **Confidence** | 4 | I have carefully read the paper, cross-referenced against the underlying experimental records, and identified specific numerical discrepancies. My concerns about non-independence and the adversary model are grounded in standard statistical methodology. I am less certain about the precise impact of clustered standard errors on significance counts, which would require re-analysis. |

---

## Recommendation

**3.0 — Findings.** The paper has genuine scientific value in its research question, experimental scale, and the attack taxonomy insight. However, the methodological concerns (non-independence, adversary model realism) and the discrepancy between reported and actual results prevent main conference recommendation. A revised version that (1) accurately reports the actual experimental numbers, (2) addresses non-independence through appropriate multilevel modeling, (3) more clearly specifies and justifies the adversary model, and (4) adds implementation details for reproducibility could reach borderline conference level. The core contribution — that the diversity-robustness relationship is attack-type-dependent and breaks under adaptive adversaries — is worth publishing if properly validated.
