---
dream_id: dream_20260513T155040
tier: best
overall_score: 5/10 — Borderline Reject
timestamp: 2026-05-13T16:29:14.054943+00:00
---

# DREAM Review Report: ContamCal

**Paper:** ContamCal: Calibrating Benchmark Scores for Training Data Contamination via Contamination-Augmented Item Response Theory
**Venue:** AAAI 2027 (acceptance rate ~17.6%, scale 1–10)
**Review mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-13

---

## Venue Calibration

AAAI 2026 acceptance rate was 17.6% (4,167/23,680). Scoring scale 1–10. Evaluation criteria: significance and novelty of contributions, theoretical/empirical soundness, relevance to the AAAI community, clarity. Preference for papers that explore new territory over narrow incremental advances.

---

## Reviewer 1 (R1): Methods + Experiments

### A. Methodological Soundness

**A1. 4PL+γ formulation (Adequate with concerns).**
The covariate-in-the-exponent approach (Eq. 2) is standard in item compromise IRT. However, using a **single global γ** is a strong assumption: it asserts contamination produces the same logit-scale boost regardless of model scale, item type, or benchmark. The paper's own data shows scale-dependent inflation (0.5B: 10.8pp vs. 3B: 8.2pp at 50% dosage), which directly contradicts a uniform γ. A hierarchical γ_j ~ N(μ_γ, σ_γ) or per-benchmark γ would be more defensible. The paper is ambiguous about whether IRT is fitted jointly across benchmarks or separately — this must be clarified.

**A2. RRF aggregation (Reasonable but under-justified).**
RRF with c=60 is a sensible default. However, the argument against learned weights is hand-wavy — learned weights could be trained on the authors' own synthetic contamination data, avoiding circularity. The ablation shows calibration-weighted RRF (0.86) slightly underperforms vanilla RRF (0.87), but this is tested only in the best-case SFT regime. RRF's real advantage is simplicity and robustness to outlier signal scores, which should be stated directly.

**A3. Identifiability (Ad hoc threshold).**
The claim that θ-γ posterior correlation = 0.31 < 0.4 confirms identifiability relies on an **ad hoc threshold** with no cited theoretical or empirical basis. The argument would be stronger with a simulation study showing that identifiability degrades as this correlation increases (the imagined exp-004 identifiability sweep), but the paper appears to present only a single MVP seed.

**A4. Measurement error extension (Under-specified).**
The formulation e_obs = e_true + ε is classical measurement error. However, the paper does not specify how e_true is handled in the Stan model. If e_true is a latent variable for each (j,i) pair, the parameter space explodes. If σ_e merely inflates γ's posterior variance post-hoc, the uncertainty propagation is approximate. Implementation details are missing.

**A5. Counterfactual θ* identification (Conditionally valid).**
Valid under the assumption that contamination acts purely additively in logit space and does not alter genuine reasoning ability. Plausible for SFT memorization but questionable for RL, where training on benchmark-adjacent data may genuinely improve capability.

### B. Experimental Rigor

**B1. SFT injection protocol (Sound for internal validity).**
Paraphrase-based injection at 3 scales × 5 dosages × 4 benchmarks = 15 model pairs is a solid controlled setup. However, SFT injection produces a specific memorization signature that may be easier to detect than pre-training contamination — ecological validity is limited.

**B2. Incomplete tables (CRITICAL).**
Table 4 (main result) reports per-benchmark MAE for ContamCal only; all 5 baselines show "—" for per-benchmark MAE, CI coverage, CI width, and Kendall τ. This means:
- Cannot assess whether ContamCal's advantage is uniform or concentrated on a subset of benchmarks
- Baseline uncertainty quantification is completely unreported
- Ranking preservation for baselines is unknown

Tables 5, 6, 7, 10, 11, 12 have similar pervasive "—" entries. Approximately 60% of cells that should contain values are missing. **This is the single most damaging issue** — it makes the paper appear either incomplete or as if unfavorable results are being hidden.

**B3. Zero figures (CRITICAL).**
The paper contains **no figures at all**. For a two-stage Bayesian pipeline with 12 experiments, this is disqualifying. Essential missing figures:
- Framework overview diagram (pipeline visualization)
- Calibrated vs. true accuracy scatter plot with CI error bars (the "money figure")
- Signal × regime AUC heatmap
- Dose-response curves
- Coverage calibration plot

**B4. RL regret calculation (Potentially circular).**
The 42% regret reduction claim requires knowing the "true" uncontaminated ranking for RL models, but no ground truth exists. If calibrated scores serve as the ground truth proxy, the calculation is tautological. The paper does not specify the ground truth source for RL regret computation.

**B5. No error bars.**
No standard deviations or confidence intervals are reported for any experimental result, despite the experiment plan specifying 3 seeds.

**B6. Scale bridging.**
7B controlled (MAE=2.2pp) adds incremental confidence. 72B observational is necessarily weaker — γ=0.18 on MMLU could reflect true contamination or systematic bias in signals at this scale. The γ CI including zero on GSM8K could mean either "reasoning benchmarks are less susceptible" or "insufficient power at 72B."

**B7. Few-examinee regime.**
N≥50 with pre-estimation from 400+ model pool is practical but assumes item parameter stability across model pools, which is not validated.

### R1 Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| Overall | **4/10** | Strong idea, but manuscript is incomplete — missing figures, pervasive "—" in tables, no error bars. Cannot evaluate empirical strength. |
| Soundness | **3/5** | Core formulation is correct. Single global γ, ad hoc identifiability threshold, potentially circular RL regret, and missing measurement error details are concerns. |
| Significance | **4/5** | High practical value. Calibration with UQ under contamination is a genuine unsolved problem. |
| Novelty | **3/5** | Non-trivial cross-disciplinary transfer. Individual components are not new. |
| Clarity | **2/5** | Good writing quality, but zero figures and sparse tables make evaluation impossible. |
| Confidence | **4/5** | Familiar with IRT, Bayesian methods, and LLM contamination literature. |

**R1 Recommendation:** Reject in current form.

---

## Reviewer 2 (R2): Novelty + Related Work

### A. Novelty Assessment

**A1. Core idea (Incremental, not transformative).**
Treating contamination as a covariate in IRT rather than removing it is the central contribution. However, this is a direct application of Eckerly (2017) and Sinharay (2017)'s item compromise IRT to a new domain. The analogy to causal inference shifting from elimination to adjustment is apt but overstated — the paper does not develop new causal identification theory.

**A2. Three structural modifications (Mixed novelty).**
- (a) Independent examinees → single model with joint item distributions: This is the most interesting adaptation but is **under-explored** — the local independence assumption is fundamentally altered when a single model responds to all items (item responses are correlated through shared model parameters). The paper does not discuss or test this violation.
- (b) Binary leakage → continuous exposure: Straightforward extension; continuous covariates in IRT are standard.
- (c) Regime-conditional ability: An engineering decision (signal selection based on training regime), not a modeling contribution.

**A3. RRF fusion (Not novel).**
RRF is an off-the-shelf rank aggregation technique. Applying it to contamination signal fusion is a reasonable engineering choice, not a methodological contribution.

**A4. Regime-conditional modeling (Engineering, not contribution).**
Detecting that RL degrades certain signals and automatically falling back to surviving signals is useful but is an implementation decision, not a theoretical advance.

**A5. Incremental novelty over remove-and-rescore (Clear but narrow).**
The improvement over remove-and-rescore (1.97pp vs. 4.2pp MAE) demonstrates the value of continuous exposure modeling over binary flagging. The provision of credible intervals is a genuine addition. However, this improvement comes entirely from (a) using continuous rather than binary exposure and (b) using IRT rather than simple rescoring — both are standard techniques.

**Overall novelty verdict:** ContamCal is a **well-executed synthesis paper** — it combines existing components (RRF, 4PL IRT, contamination signals, Bayesian MCMC) in a sensible way for a new application. The novelty is in the cross-disciplinary transfer and the specific combination, not in any individual component. For AAAI, this level of novelty is borderline.

### B. Related Work Completeness

**10 citations is critically insufficient** for a paper spanning contamination detection, IRT, Bayesian inference, and evaluation methodology. Major gaps:

1. **Missing baselines/citations:**
   - DCR (Detecting Contamination via Response patterns) — the most directly comparable prior work using IRT-adjacent ideas for contamination, absent as both citation and baseline
   - HiBayES — Bayesian evaluation scoring with hierarchical models
   - DIF (Differential Item Functioning) literature — the direct precursor to item compromise IRT, extensive body of work unacknowledged

2. **Missing related areas:**
   - Membership inference attacks (broader contamination detection literature)
   - Extraction attacks for training data
   - Post-hoc calibration in ML (Platt scaling, temperature scaling — conceptually related as post-hoc score adjustment)
   - Dynamic/live benchmarks (LiveBench, LMSYS) — the alternative approach to contamination
   - Data attribution and influence functions
   - Conformal prediction as alternative to Bayesian CIs
   - Benchmark design literature

3. **Educational measurement connection under-developed.**
   The paper cites Eckerly (2017) and Sinharay (2017) but does not engage with the broader DIF, item preknowledge, or test security literature. Given that this is the theoretical foundation, deeper engagement is needed.

4. **Missing concurrent work.**
   The 2025-2026 period has seen active work on contamination-aware evaluation. The paper should survey recent arXiv preprints on this topic.

### C. Positioning and Framing

**"Statistical safety net" framing (Effective but overpromised).**
The framing is compelling and well-motivated. However, calling it a "safety net" implies reliability guarantees that the paper cannot deliver — particularly in the RL regime where CIs are 11.4pp wide.

**Scope of claims (Appropriate for SFT, overstated for RL).**
The SFT claims are well-supported by controlled experiments. The RL claims (42% regret reduction) rest on an observational study with 8 models and no ground truth, which is insufficient for the confidence with which they are stated.

### D. Significance and Impact

**Problem importance: High.**
Contamination is increasingly recognized as a fundamental threat to LLM evaluation validity. The community needs solutions beyond detection.

**Practical adoption barriers:**
- Requires at least 50 models for reliable estimation
- Full pipeline requires model weight access (embedding retrieval, Min-K%++)
- ConStat requires paraphrase generation infrastructure
- Stan MCMC is computationally expensive
- RL regime (where most production models live) produces very wide CIs

**Impact assessment:** If fully validated with complete experimental results, this would be a useful tool for the evaluation community. The practical barriers limit but do not eliminate impact.

### R2 Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| Overall | **5/10** | Addresses a real problem with a reasonable approach. Novelty is incremental (synthesis of existing techniques). Related work is severely incomplete. Manuscript presentation is draft-quality. |
| Soundness | **3/5** | Core framework is technically sound. Local independence violation unexamined. |
| Significance | **4/5** | Important problem, potentially impactful solution. |
| Novelty | **2/5** | Cross-disciplinary transfer, not new methodology. Every component is borrowed. |
| Clarity | **2/5** | Writing is clear but manuscript is incomplete (no figures, sparse tables). |
| Confidence | **4/5** | Familiar with IRT, contamination literature, and evaluation methodology. |

**R2 Recommendation:** Borderline reject. Could reach weak accept with complete results, 30+ citations, and proper figures.

---

## Roundtable Synthesis

### Step 2: Cross-Sharing Summary

R1's key concerns shared with R2: incomplete tables, zero figures, circular RL regret, single global γ, ad hoc identifiability threshold.

R2's key concerns shared with R1: synthesis-level novelty only, 10 citations insufficient, missing DCR baseline, local independence violation unexamined, RL practical limitation.

### Step 3: Convergence

**Points of agreement:**
1. **The problem is important and the approach is reasonable.** Both reviewers rate significance 4/5.
2. **The manuscript is incomplete.** Zero figures, ~60% missing table entries, no error bars. Both rate clarity 2/5.
3. **Single global γ is a concern.** The paper's own data shows scale-dependent contamination effects incompatible with a uniform γ.
4. **RL claims are under-supported.** Observational study with 8 models and no ground truth is insufficient. The 42% regret reduction may be circular.
5. **Soundness is adequate but with gaps.** Both rate soundness 3/5. Core IRT framework is correct; execution details (measurement error, identifiability, local independence) need work.

**Points of divergence:**
- **Novelty:** R1 gives 3/5 (acknowledging non-trivial cross-disciplinary transfer); R2 gives 2/5 (emphasizing that every component is borrowed). After discussion, consensus is **2.5/5** — the synthesis is competent but the paper needs to be more honest about its novelty positioning and develop the local independence violation as a genuine theoretical contribution.
- **Overall score:** R1 gives 4/10, R2 gives 5/10. Difference is driven by R2 weighing the problem importance more heavily despite novelty concerns.

### Step 4: Consolidated Assessment

**Consensus overall score: 4.5/10 → Round to 5/10 (Borderline Reject)**

| Criterion | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Overall | 4/10 | 5/10 | **5/10** |
| Soundness | 3/5 | 3/5 | **3/5** |
| Significance | 4/5 | 4/5 | **4/5** |
| Novelty | 3/5 | 2/5 | **2.5/5** |
| Clarity | 2/5 | 2/5 | **2/5** |

---

## Critical Issues (Must Fix)

1. **Complete all tables.** Fill in every "—" entry. All baselines need per-benchmark MAE, CI coverage, CI width, and Kendall τ. All ablation tables need full entries. (~60% of cells are missing.)

2. **Add figures (minimum 5).** Framework overview, calibrated-vs-true scatter with CIs, signal×regime heatmap, dose-response curves, coverage calibration plot. Currently zero figures.

3. **Clarify RL regret ground truth.** Explicitly state what serves as ground truth for expected regret on RL models. If it's a held-out clean benchmark, say so. If it's the calibrated scores, the 42% claim is circular and must be withdrawn.

4. **Expand related work to 25-30+ citations.** Add DCR, HiBayES, DIF literature, membership inference, dynamic benchmarks, post-hoc calibration methods, data attribution. Currently only 10 citations.

5. **Add error bars / standard deviations.** Report variance across seeds for all key results.

## Major Issues (Should Fix)

6. **Address single global γ limitation.** Either (a) justify why per-model heterogeneity doesn't bias θ estimates, (b) fit per-benchmark γ and report, or (c) implement hierarchical γ as an extension.

7. **Clarify IRT fitting scope.** State explicitly whether the model is fitted jointly across benchmarks or per-benchmark.

8. **Specify measurement error implementation.** How are latent true exposure scores handled in Stan? Fully marginalized? Latent variables? Post-hoc approximation?

9. **Discuss local independence violation.** When a single model is the "examinee" for all items, item responses are correlated through shared parameters. This fundamentally alters IRT assumptions and needs theoretical or empirical treatment.

10. **Discuss ecological validity of SFT injection.** SFT injection produces a specific memorization signature that may be easier to detect than pre-training contamination.

11. **Include DCR as a baseline.** This is the most directly comparable prior work and must be compared against.

## Minor Issues

12. **Embedding retrieval AUC=0.90 on base models (Table 8):** If base models have no contamination, why is AUC so high? This suggests the embedding signal may detect training data proximity rather than contamination. Discuss false positive implications.

13. **50% coverage = 0.55:** Slight overcoverage at 50% level suggests CIs may be too wide. Discuss CI calibration.

14. **Pre-estimation transfer assumption.** Validate that item parameters are stable across model pools of different capability distributions.

15. **ConStat paraphrase quality.** Discuss who generates paraphrases and potential bias.

16. **Computational cost.** Report Stan MCMC wall-clock time and signal computation costs.

---

## Experiment Coverage Assessment

Comparing the paper against the full experiment plan (review_context.yaml):

| Experiment | Planned | Present in Paper | Quality |
|-----------|---------|-----------------|---------|
| exp-001: Controlled SFT injection | ✓ | ✓ | Table 1 adequate but only MMLU fully reported |
| exp-002: Signal pipeline | ✓ | ✓ | Table 2 adequate |
| exp-003: RRF ablation | ✓ | ✓ | Table 3 adequate |
| exp-005: Noise propagation | ✓ | ✓ | Table 6 has "—" entries |
| exp-006: IRT + baselines | ✓ | ✓ | **Table 4 critically incomplete** — baselines lack per-benchmark data |
| exp-007: 7B scale bridging | ✓ | ✓ | Table 7 adequate |
| exp-008: Signal survival | ✓ | ✓ | Table 8 complete |
| exp-009: RL case study | ✓ | ✓ | Table 9 adequate but regret ground truth unclear |
| exp-010: Prior sensitivity | ✓ | ✓ | Table 11 adequate |
| exp-011: Few-examinee | ✓ | ✓ | Table 12 has "—" entries |
| exp-012: 72B observational | ✓ | ✓ | Table 7 adequate |
| exp-013: 2-signal mode | ✓ | ✓ | Table 13 adequate |

All 12 experiments are present but many have incomplete reporting. Of 21 planned figures, **zero** are included.

---

## Bottom Line

ContamCal addresses a genuine and timely problem — post-hoc calibration of contaminated benchmark scores with proper uncertainty quantification. The approach (RRF signal fusion → contamination-augmented 4PL IRT) is methodologically sound in concept and draws on a solid theoretical foundation from educational measurement. The experimental design is comprehensive.

However, the **manuscript is clearly incomplete**: zero figures, ~60% of table cells missing, no error bars, 10 citations. The novelty is incremental (synthesis of existing techniques for a new application). The RL claims may rest on circular reasoning. At AAAI's 17.6% acceptance rate, this paper in its current form would not pass the completeness bar, let alone compete on novelty and execution quality.

**With full experimental reporting, 5+ figures, expanded related work, and resolution of the RL regret circularity, this paper could reach 6-7/10 (weak accept range) at AAAI.** The research direction is promising and the community needs this kind of work.
