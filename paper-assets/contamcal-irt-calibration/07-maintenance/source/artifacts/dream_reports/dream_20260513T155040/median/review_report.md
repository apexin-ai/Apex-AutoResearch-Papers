---
dream_id: dream_20260513T155040
tier: median
overall_score: borderline reject (5/10)
timestamp: 2026-05-13T16:38:35.632893+00:00
---

# Dream Review Report: ContamCal

**Paper**: ContamCal: Principled Calibration of Contaminated Benchmark Scores via Contamination-Augmented Item Response Theory
**Venue Target**: AAAI 2027
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-13

---

## Venue Calibration

**AAAI 2026 reference**: 23,680 submissions, 17.6% acceptance rate (4,167 accepted). Rating scale 1–10 (10=seminal, 6=marginally above threshold, 5=marginally below). Evaluation dimensions: significance/novelty of contributions, theoretical/empirical soundness, relevance to AAAI community, clarity of exposition.

---

## R1: Methods & Experiments

### Strengths

1. **Well-motivated problem formulation.** Grounding in educational measurement's item compromise tradition (Eckerly 2017, Sinharay 2017) is principled. The key question — "what would a model's score be without contamination?" — is precisely the right question the field needs answered, and no prior work provides it with uncertainty quantification.

2. **Comprehensive controlled experiment design.** 3 model scales × 5 dosage levels × 4 benchmarks = 60 model-benchmark pairs with known ground truth. This is one of the most thorough contamination injection studies to date. Clean SFT (0% dosage) showing <1pp degradation confirms baseline reliability.

3. **Training-free RRF avoids meta-circularity.** A learned aggregator could itself be contaminated — using RRF sidesteps this elegantly. The paper correctly identifies this as a design choice rather than claiming RRF is optimal.

4. **Honest RL characterization.** Rather than hiding the ~17pp CIs, the paper transparently presents them as the correct answer given signal quality. The 17% expected regret reduction, while modest, is honestly framed. This intellectual honesty is commendable.

5. **Signal survival analysis (Section 4.8).** The heatmap showing cliff-like degradation of embedding/logit-based signals under RL post-training is an informative empirical contribution with practical implications for the detection community.

6. **Growing Pains pre-estimation.** Extending the practical floor from N=50 to N=20 models is a useful contribution for small-scale evaluation settings.

### Weaknesses

1. **Single global γ_j per model is misspecified.** The paper's own results show benchmark-dependent effects: MMLU MAE=3.4pp but HumanEval MAE=5.6pp; γ at 100% dose varies across benchmarks (implicit in the per-benchmark MAE variation). A single γ_j forces the model to average across heterogeneous contamination effects. Per-benchmark or per-domain γ would be more appropriate and is a straightforward extension the paper does not explore or even discuss.

2. **Two-stage pipeline discards Stage 1 uncertainty.** Exposure scores e_ij from RRF are treated as fixed point estimates in the IRT model. Their estimation uncertainty is never propagated. This is likely a primary contributor to the 89% vs 95% nominal coverage gap — the model is overconfident because it ignores input noise. The noise propagation analysis (Section 4.5) partially addresses this post-hoc but does not fix the core issue. A joint model or a measurement error model should be the default, not an afterthought.

3. **No statistical significance testing.** The key claim — 14% relative MAE improvement over linear regression+CI (4.2 vs 4.9pp) — has no error bars, confidence intervals, or significance tests. With only 15 model variants in the controlled setting, this 0.7pp difference could easily be within sampling variability. The paper reports metrics from what appears to be a single experimental run per configuration. Without bootstrap CIs or cross-validation, the margin is not established as statistically meaningful.

4. **θ-γ identifiability is asserted, not proven.** The paper observes θ-γ posterior correlation of 0.38 and treats this as evidence of identifiability. No formal identifiability analysis (e.g., Fisher information matrix rank conditions, simulation recovery studies with known parameters) is presented. The posterior correlation could be low simply because the prior dominates. The 5% dosage result (γ CI includes 0) already shows identifiability failure in the most practically relevant regime.

5. **IRT local independence assumption violated.** Standard IRT assumes examinees respond independently. Here, a single model produces all responses — items within a benchmark share common model architecture, training data, and inference procedure. This violation is never discussed. It likely inflates the effective sample size, leading to narrower-than-warranted CIs (compounding the coverage gap).

6. **Missing baselines.**
   - DCR (Balachandran et al. [6]) is cited but not included as an experimental baseline despite being the most directly comparable prior work on contamination calibration for ranking.
   - No comparison to a simple "flag-and-remove" threshold approach on the RRF scores.

7. **HumanEval item count (N=164).** This is low for 4PL IRT estimation with 4 item parameters each. The paper uses Growing Pains pre-estimation for few-examinee settings but does not discuss few-item settings. HumanEval consistently shows the worst results (MAE=5.6pp, AUC=0.63–0.76), and item scarcity is a likely contributor.

8. **MCMC diagnostics marginal for RL case study.** R̂=1.015 (above the 1.01 threshold recommended by Vehtari et al. 2021), 1.2% divergent transitions (above the 0.1% heuristic), ESS_bulk=210 (below the 400 recommended minimum). These are reported but not remediated. Increasing warmup, using NUTS adaptation, or reparameterization could help.

### Questions for Authors

1. Have you evaluated per-benchmark γ_{jk} (model j, benchmark k)? What is the MAE improvement and does it close the coverage gap?
2. What are bootstrap confidence intervals on the MAE differences between ContamCal and linear regression+CI? Is the 0.7pp gap significant at p<0.05?
3. Can you provide a simulation recovery study: generate data from the true 4PL+γ model with known parameters, fit the model, and report parameter recovery rates?
4. Why is Balachandran et al. [6] not included as an experimental baseline?
5. What happens to coverage and MAE if you use a measurement error model for e_ij by default rather than treating them as fixed?

### R1 Scores
- **Soundness**: 5/10
- **Experimental Quality**: 5/10
- **R1 Overall**: 5/10
- **Confidence**: 4/5

---

## R2: Novelty & Related Work

### Strengths

1. **Problem framing fills a genuine gap.** Detection methods flag contamination but don't calibrate scores. IRT methods evaluate models but ignore contamination. Mitigation methods fail (Dong et al. ICML 2025). The paper correctly identifies this gap and proposes the first framework that bridges contamination detection and psychometric calibration.

2. **Bayesian uncertainty propagation is principled.** Unlike point-estimate approaches (remove-and-rescore, linear regression), ContamCal provides calibrated credible intervals that naturally widen when signal quality degrades. This is the paper's strongest conceptual contribution — the value of honest uncertainty.

3. **Signal survival heatmap is a genuinely new and useful contribution.** The finding that RL post-training causes cliff-like (not gradual) degradation of embedding and logit-based detection signals, while Self-Critique partially survives, is empirically novel and has immediate practical implications. This should be elevated to a primary contribution.

4. **Identifiability analysis defines operational boundaries.** Rather than claiming universal applicability, the paper explicitly maps where calibration is reliable (AUC ≥ 0.70, N ≥ 20 with GP, SFT regime) and where it is not. This is scientifically mature framing.

5. **Honest scope limitation strengthens credibility.** The paper does not overclaim. Acknowledging 89% coverage, 17pp RL CIs, and 14% margins is more trustworthy than inflated claims would be.

### Weaknesses

1. **Limited methodological novelty.** The core model (Eq. 2) adds a single linear covariate γ_j · e_ij to a standard 4PL IRT model. This is a minimal extension of Eckerly (2017) and Sinharay (2017), adapted to the LLM setting with three structural changes that are individually straightforward:
   - Independent examinees → single model with joint item distribution (a modeling choice, not an algorithmic contribution)
   - Binary leakage → continuous exposure scores (replacing a binary indicator with a continuous one)
   - Stable ability → regime-conditional ability (acknowledged but not fully modeled — the paper handles this by switching between 2-signal and 4-signal modes rather than modeling regime as a covariate)

   RRF is an off-the-shelf IR technique (Cormack et al. 2009) applied without modification. The ΔAUC of +0.03 over the best single signal raises the question of whether multi-signal aggregation adds meaningful value.

2. **Severely inadequate related work.** Only 10 references is far below AAAI standards (typically 30–50). Critical missing citations include:
   - **IRT for LLMs**: Lalor et al. (AAAI 2024, "Benchmarking LLMs via IRT"), which is highly relevant and published at the target venue
   - **Contamination detection**: Only 4 methods cited; missing CDD (Oren et al. 2023), membership inference approaches, n-gram overlap variants, and the broader detection survey literature
   - **Contamination-resistant evaluation**: LiveBench, private evaluation paradigms, dynamic benchmarking approaches — these represent alternative solutions to the same problem
   - **Bayesian IRT**: The Stan/PyMC IRT literature, Bayesian psychometrics references
   - **LLM evaluation at scale**: Papers on benchmark design, scaling laws for evaluation, evaluation methodology surveys
   - **DCR/Balachandran et al. [6]**: Cited but inadequately discussed. As the most directly comparable work (contamination calibration for ranking), it deserves detailed differentiation and experimental comparison.

3. **Balachandran et al. [6] is the elephant in the room.** This paper on "Data contamination calibration for ranking LLMs" is cited once but never experimentally compared. The related work section does not explain how ContamCal differs from or improves upon DCR. This is a critical omission — a reviewer familiar with [6] would immediately ask why it's not a baseline.

4. **Contribution framing is misaligned.** The paper frames the calibration framework (Contribution 1) as primary, but the most genuinely novel findings are:
   - Signal survival analysis under RL (Contribution 4)
   - Identifiability boundaries (Contribution 3)
   
   The calibration framework itself is an engineering assembly of known components. Repositioning around signal survival and identifiability would strengthen the novelty narrative.

5. **RRF contribution is overclaimed.** Claiming RRF as a contribution when ΔAUC=0.03 and calibration-weighted RRF performs equally (0.77 vs 0.78) is a stretch. RRF is a convenience choice, not a methodological advance.

### Questions for Authors

1. How does ContamCal differ from Balachandran et al. [6] in both methodology and experimental setting? Why is [6] not included as a baseline?
2. Have you considered Lalor et al. (AAAI 2024) and how ContamCal extends or diverges from their IRT-for-LLMs framework?
3. What prevents using a simple threshold on RRF exposure scores + removal as a baseline? (i.e., remove items with e_ij > 0.5 and rescore — this is simpler than IRT)
4. Could the signal survival analysis and identifiability mapping be the standalone contribution, with calibration as a downstream application rather than the primary framing?
5. Why are contamination-resistant evaluation approaches (LiveBench, dynamic benchmarks) not discussed as alternative solutions to the same problem?

### R2 Scores
- **Novelty**: 4/10
- **Significance**: 6/10
- **Related Work & Positioning**: 3/10
- **Clarity**: 7/10
- **R2 Overall**: 5/10
- **Confidence**: 4/5

---

## Roundtable: Cross-Sharing & Convergence (Steps 2–3)

### Points of Agreement

Both reviewers independently arrived at **5/10** (marginally below acceptance threshold). Core convergence:

1. **The 14% margin over linear regression+CI is the paper's Achilles heel.** R1 notes it lacks statistical significance testing; R2 notes it doesn't justify the complexity. Combined: a 0.7pp MAE difference without error bars, over a method that is orders of magnitude simpler, is not a compelling empirical result for AAAI.

2. **Missing baselines undermine the experimental story.** R1 flags DCR absence; R2 flags Balachandran et al. [6] as the most critical missing comparison. These are the same paper — both reviewers independently identified this gap.

3. **Signal survival analysis is the strongest contribution.** Both reviewers agree this is genuinely novel and useful, yet it is framed as Contribution 4 rather than a primary result.

4. **Honest framing is credibility-positive but doesn't compensate for modest results.** Both appreciate the transparent limitation acknowledgment but note it doesn't elevate the paper above the threshold.

5. **Coverage gap (89% vs 95%) reveals model misspecification.** R1 attributes it to uncertainty propagation failure and local independence violation; R2 sees it as evidence the IRT complexity isn't justified. Both agree it's insufficiently addressed.

### Complementary Criticisms (Strengthening Each Other)

- R1's technical concerns (single γ_j, uncertainty propagation, identifiability) + R2's novelty assessment (straightforward extension) together paint a picture of a model that is **both too simple (misspecified) and not novel enough** to justify its position.
- R1's missing error bars + R2's 14% margin concern: without significance testing, the claimed improvement may be noise.
- R1's MCMC diagnostics + R2's related work gaps: the RL case study is technically questionable (marginal diagnostics) and inadequately contextualized (missing related work on RL and contamination).

### Sole Disagreement

R2 rates related work at 3/10 (severe); R1 did not score related work explicitly but acknowledged missing baselines. On discussion, R1 would likely assign 4/10 — the 10-reference count is objectively low for AAAI but the core positioning (detection → calibration gap) is accurate.

**Resolved**: Related work rating converges to **3–4/10** (inadequate but not misleading).

---

## Step 4: Consolidated Assessment

### Summary

ContamCal addresses a genuine and timely problem — calibrating LLM benchmark scores in the presence of training data contamination. The two-stage framework (RRF signal aggregation → contamination-augmented 4PL IRT) is competently engineered, and the controlled SFT injection experiments are thorough. The signal survival analysis under RL post-training is a genuinely novel empirical finding. The paper is commendably honest about its limitations.

However, the paper falls marginally below the AAAI acceptance threshold due to a combination of:

### Critical Issues

1. **Insufficient improvement margin without statistical evidence.** The 0.7pp MAE improvement over linear regression+CI (4.2 vs 4.9) lacks error bars or significance tests. For a paper proposing a substantially more complex method (Bayesian IRT with HMC), a statistically unvalidated 14% relative improvement is not compelling.

2. **Model misspecification indicators.** Single global γ per model despite benchmark-heterogeneous effects; 89% coverage vs 95% nominal; Stage 1 uncertainty discarded. These suggest the model is simultaneously too simple (one γ) and too complex (4PL) relative to what the data supports.

3. **Inadequate related work and missing key baseline.** 10 references for AAAI is insufficient. Balachandran et al. [6] — the most directly comparable work — is cited but not compared experimentally. Lalor et al. (AAAI 2024), contamination-resistant benchmarks, and the broader IRT-for-LLMs literature are absent.

4. **Limited methodological novelty.** The 4PL+γ model is a minimal extension of educational measurement formulations. RRF is off-the-shelf with negligible AUC gain (+0.03). The primary novelty lies in the application context and the empirical findings (signal survival, identifiability boundaries), not the method itself.

### What Would Bring This to Accept

- Per-benchmark γ_{jk} + measurement error model for e_ij → likely closes coverage gap and increases MAE margin
- Bootstrap CIs on all metric comparisons → establishes statistical significance
- Balachandran et al. as baseline + 30+ references → addresses positioning gaps
- Reframe signal survival and identifiability mapping as primary contributions
- Formal identifiability analysis (simulation recovery study)

### Consolidated Scores (AAAI 1–10 Scale)

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 5 | Competent but misspecified model; no significance tests; uncertainty propagation gap |
| Novelty | 4 | Straightforward IRT extension + off-the-shelf RRF; signal survival is novel but secondary |
| Significance | 6 | Important problem; modest but real practical value; honest uncertainty has worth |
| Experimental Quality | 5 | Thorough design but missing key baseline, no error bars, marginal MCMC for RL |
| Related Work | 3 | 10 references; critical missing citations; inadequate differentiation from [6] |
| Clarity | 7 | Well-written; good structure; "when it works/doesn't" framing effective; 17 tables is dense but organized |
| **Overall** | **5** | **Marginally below acceptance threshold** |
| Confidence | 4/5 | Both reviewers have strong familiarity with IRT, contamination detection, and Bayesian methods |

### Decision Recommendation

**Borderline Reject (5/10).** The paper makes a solid engineering contribution to an important problem and is unusually honest about its limitations. However, the combination of limited methodological novelty, statistically unvalidated improvement margins, model misspecification indicators, and severely inadequate related work places it below the 17.6% acceptance bar for AAAI. A revised version addressing the five items above could reach 6–7/10.

### Experiment Coverage Assessment

Comparing the paper against the full experiment design (review_context.yaml):
- **12/12 imagined experiments appear in the paper** (exp-001, 002, 003, 005, 006, 007, 008, 009, 010, 011, 012, 013). Coverage is complete.
- **exp-004** (identifiability simulation) is referenced indirectly via Section 4.5 noise propagation but not presented as a standalone identifiability study with formal parameter recovery — a gap given it would strengthen the identifiability claims.
- The narrative guidance to downgrade claims is well-reflected in the paper's framing ("under sufficient signal quality," explicit identifiability boundaries).
- The paper honestly reports all median-tier results including limitations (89% coverage, 17pp RL CIs, 14% margin).
