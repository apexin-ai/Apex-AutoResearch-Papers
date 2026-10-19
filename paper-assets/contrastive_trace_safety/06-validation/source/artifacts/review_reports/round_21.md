---
round: 21
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T17:11:02.397539+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 21 (Fresh Review)
## Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (ARR May 2026 cycle) | **Deadline**: 2026-05-25 | **Reviewers**: 2 | **Rounds**: 1 (converged)

---

## Summary

This paper investigates how the choice of layer selection metric systematically biases which transformer layer is chosen for hidden-state (HS) safety probes in reasoning models, and how this bias can reverse HS vs. text probe conclusions. Across four reasoning LLMs (3 Qwen-based, 1 Llama) on the HarmThoughts benchmark, the authors show that crossing-rate composite metrics select shallow layers (inflating threshold crossings due to representation compression), while threshold-based metrics select deep layers where HS advantages of +19.2 to +21.9pp emerge against a 384d MiniLM text encoder. The HS advantage is encoder-conditional (1/4 models survives HB correction at 1024d) and partially position-mediated (2/4 models). A three-layer ensemble provides metric-agnostic selection. The paper includes extensive negative results and an unusually honest limitations section.

---

## Strengths

**S1. Important methodological finding.** The identification of metric-induced layer selection bias as a researcher degree of freedom that can reverse HS vs. text conclusions (Table 2) has lasting value for the probing literature. The five-metric ablation with random-label control (Appendix B.1) demonstrates this is a property of representation geometry, not label-specific. [R1, R2 consensus]

**S2. Statistical rigor far exceeding peer work.** Holm-Bonferroni correction, nested 5-fold CV, BCa bootstrap CI (10,000 resamples with trace-level clustering), permutation tests, MDE calculation (Appendix AA), and explicit evidence gradient classification. Trace-level bootstrap correctly handles temporal dependence between steps. [R1, R2 consensus]

**S3. Systematic negative results.** Section 4.6 and Table 20 report failures of 7 alternative methods (BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, cross-model transfer) and distill four signal characteristic requirements. This defines method boundaries for future work. [R1, R2 consensus]

**S4. Scientific integrity.** M002 bug disclosure (Appendix N), explicit exploratory (†) markers for underpowered 32B results, seed-sensitivity reporting for R1-8B FPR, and one of the most comprehensive limitations sections in recent NLP papers. [R1, R2 consensus]

**S5. Format compliance.** 8-page main text, correct ACL template with `[review]` option, proper anonymization ("Anonymous ARR Submission"). [R1, R2 consensus]

---

## Weaknesses

### Must-Fix (3 issues — reviewer consensus)

**N1 [critical] Single dataset severely limits external validity of the core methodological claim.**
- All experiments use only HarmThoughts. The paper positions Contribution 1 as "follows from representation geometry and likely generalizes beyond HarmThoughts" (Section 5) but provides no second-dataset validation. The cosine distance geometric argument (Appendix C) is computed on HarmThoughts traces only. HarmThoughts' right-skewed CP distribution and specific category composition may drive the observed patterns. Claim scope substantially exceeds evidence scope.
- **Both reviewers independently marked critical. This is the highest-priority issue.**
- Action: Validate Table 2 core pattern on at least one additional safety benchmark, or significantly narrow generalizability claims.

**N2 [critical] Missing inter-annotator agreement (IAA) undermines CP annotation quality foundation.**
- Section 7 states: "Inter-annotator agreement (IAA) was not computed for these annotations." The entire experimental framework depends on CP annotation quality. QwQ-32B's HS lead time of -1.2 to +1.9 steps falls within plausible annotation error. Appendix J's perturbation analysis tests random noise but cannot capture systematic annotation bias (consistently early/late CP placement).
- R1: Must-Fix. R2: Should-Fix (Appendix J provides indirect evidence). Director resolution: **Must-Fix** — CP is the paper's foundational concept; marginal 32B results are vulnerable to annotation uncertainty within noise range.
- Action: Report IAA if obtainable; conduct small-scale re-annotation study; or discuss expected noise magnitude based on annotation methodology.

**N3 [critical] Tiny 32B sample size (n=19-20) bears excessive inferential load.**
- MDE at 80% power is 8.6-9.5pp (Table 35), far exceeding R1-32B's residualized +1.9pp. With W=5, probe input is 25,600-dimensional with only ~60 training samples — overfitting risk is severe even with L2 regularization. Despite correct † markers, the paper draws multiple substantive conclusions from these micro-samples: QwQ-32B "position-competitive," R1-32B "position-mediated," 32B cross-model divergence analysis, quadratic position absorption.
- **Both reviewers independently marked critical.**
- Action: Collect more 32B data; restrict 32B discussion to purely descriptive observations; or reposition as pilot study with explicit power requirements.

### Should-Fix (7 issues)

**W1 [warning] Position baseline threatens core HS advantage — 2/4 models absorbed or severely weakened.**
QwQ-32B's HS advantage fully absorbed by quadratic position term (Table 26); R1-32B residualized gap +1.9pp (p=0.914). The paper labels quadratic control as "sensitivity analysis, not primary specification" (Section 5) without sufficient justification for why linear should be preferred. HS probes may simply be better position encoders than text probes rather than capturing genuine safety-relevant features. [R1, R2 consensus]

**W2 [warning] MiniLM-384d is a weak baseline — capacity mismatch makes HS advantage partly expected.**
HS representations from 7-32B models (3584-5120d) compared against 384d/22M-parameter MiniLM. At 1024d BGE-large, only 1/4 models passes HB. E5-Mistral-7B (2/4 HB) shows monotonic gradient: stronger encoder → smaller HS advantage. PCA capacity matching preserves advantage but does not fully resolve quality differences. Abstract leads with "+19.2 to +21.9pp" without immediately qualifying this is against the weakest baseline. [R1, R2 consensus]

**W3 [warning] HB correction scope may be insufficient.**
HB covers 12 final tests (3 metrics × 4 models), but total researcher degrees of freedom include 5 metrics × 7 W values × 28-64 layers × multiple thresholds × 2 split ratios. Evidence gradient classification itself is a post-hoc decision. Nested CV addresses within-loop selection for 7-8B but not the full exploration space. [R1: Should-Fix, R2: Minor — Director keeps at Should-Fix given cumulative exploration acknowledged in Section 7]

**W4 [warning] 3/4 models share Qwen architecture — limited architectural diversity.**
Only R1-8B (Llama) provides cross-architecture evidence, and it happens to show the strongest HS advantage. R1-32B and QwQ-32B share Qwen-32B base but show qualitatively different probe characteristics — training method may matter more than architecture, but tested on only one architecture pair. [R1, R2 consensus]

**W5 [warning] CP definition creates conceptual tension with online detection motivation.**
CP requires observing the full trace ("the first reasoning step after which safety reasoning permanently ceases"), yet the introduction frames the work toward "production detectors." R1 flagged this as Should-Fix; R2 rebutted (standard probing paradigm). Director resolution: the probing setup is methodologically valid, but the introduction should more clearly distinguish retrospective classification from online detection. [R1 raised, R2 partial rebut]

**W6 [warning] FPR 11-50% inconsistent with deployment narrative.**
76.7% oracle gap (Appendix I) further highlights the performance ceiling. The paper acknowledges in Limitations that methods "characterize the phenomenon rather than constitute production detectors," but this caveat should appear earlier. [R1, R2 consensus]

**W7 [warning] "Confirmatory" terminology potentially misleading.**
R2 flagged as Must-Fix (no pre-registration); R1 rebutted as Should-Fix (paper defines it operationally in footnote 1 as "nested CV validated," not in the pre-registration sense). Director resolution: **Should-Fix** — the paper does provide a clear operational definition, making this a terminology issue rather than a methodological flaw. Renaming to "validated" or "cross-validated" would resolve the concern without affecting any substantive conclusion.

---

## Reviewer Consensus

Both reviewers independently agree on:
- [AGREE] **N1**: Single dataset is the most critical limitation (both marked critical without seeing each other's initial review)
- [AGREE] **N3**: 32B sample size inadequate for the inferential load placed on it
- [AGREE] **W1**: Position confound is serious for 2/4 models
- [AGREE] **W2**: Encoder capacity mismatch partially explains HS advantage
- [AGREE] **W4**: Architecture diversity insufficient (3/4 Qwen)
- [AGREE] **S1-S4**: All strengths confirmed by both reviewers
- [AGREE] Methodological contribution (Contribution 1) has lasting community value
- [AGREE] Paper should be reframed with Contribution 1 as primary, Contribution 2 as initial characterization

---

## Reviewer Divergence

**D1: Ensemble evaluation.**
- R1: Ensemble claim is well-supported — the claim is metric-agnostic selection (vs. text: 4/4 significant, p≤0.002), not superiority over best single metric. [REBUT]
- R2: Ens-Best is not significant (p>0.27), incremental value indistinguishable from zero. [REBUT to R1's S5]
- Director note: Both interpretations are valid. Ensemble provides practical metric-agnostic value but does not improve over oracle single-metric selection. The claim boundary should be stated more clearly.

**D2: IAA severity.**
- R1: Must-Fix (CP annotation quality is foundational; marginal 32B results vulnerable)
- R2: Should-Fix (Appendix J perturbation provides indirect evidence; CP comes from original benchmark)
- Director resolution: Must-Fix (see N2 above).

**D3: CP definition circularity.**
- R1: Should-Fix (conceptual tension with online detection)
- R2: Rebut (standard probing paradigm; paper is analysis not deployment)
- Director resolution: Should-Fix (W5 above), but acknowledges R2's point that the probing paradigm itself is standard.

---

## Questions for Authors

1. If Table 2's metric-layer interaction pattern were tested on WildJailbreak or another safety dataset, would it persist? This is the single most important open question.
2. Was the "confirmatory / significant / exploratory" evidence tier classification determined before or after seeing results? If post-hoc, how does this not constitute additional reporting degrees of freedom?
3. For QwQ-32B, why should the linear position specification be preferred over quadratic? Can you rule out that HS probes are simply better position encoders rather than capturing genuine safety content?
4. With W=5 and 5120d hidden states, probe input is 25,600-dimensional but training set is ~60 samples. How do you ensure L2 regularization is sufficient to prevent overfitting?
5. Are results stable across different harmful categories within HarmThoughts? Could the HS advantage be driven by specific attack types?
6. R1 correctly noted that R2 misattributed R1-32B's 3.0pp selectivity to R1-8B. Please confirm: R1-8B selectivity is 14.1pp/22.9pp (well above threshold), and R1-32B residualized selectivity is 3.0pp (below threshold)?

---

## Missing References

1. **Zou et al. (2024)**, "Improving Alignment and Robustness with Circuit Breakers" — representation-level safety intervention, directly relevant to causal validation discussion
2. **Templeton et al. (2024)**, "Scaling Monosemanticity" — large-scale feature extraction for understanding safety representations
3. **Gelman & Loken (2013)**, "The garden of forking paths" — already in bib (`gelman2013garden`) but never cited; Section 5's "researcher degree of freedom" discussion should cite this foundational work
4. **Turner et al. (2023)**, activation addition — relevant to activation steering for safety

---

## External Review (Stanford Agentic Reviewer)

**Status: Skipped.** External review request was sent but skipped by user (2026-05-19T17:01:27Z). No external review data available for this round.

---

## Visual Layout Check (非评分项)

**Status: Timeout** (815 seconds elapsed without completion). Visual review agent did not return results in time.

Known visual issues from reviewer comments:
- Figure 1 (p.6) heat map too small — axis labels and metric names hard to read (R1 m2)
- Figure 1 not colorblind-friendly (R2 minor)
- Abstract information density excessive for first-time readers (R1 m1, R2 minor)

---

## Overall Assessment

**Score: 3.0 (Findings)**
**Confidence: 4/5**

### Scoring Rationale

**Contribution 1 (metric-induced layer selection bias)** is the paper's core strength: a methodologically sound finding with practical community value that both reviewers recognized as important. However, it is validated on only one dataset, preventing confidence in the generalization claim.

**Contribution 2 (HS vs. text empirical comparison)** is substantially weakened by multiple compounding limitations:
- Single dataset (no external validity)
- 32B results statistically underpowered (n=19-20, effects below MDE)
- Position confound absorbs HS advantage for 2/4 models
- Encoder-conditional advantage (1/4 HB at 1024d BGE-large)
- Missing IAA for CP annotations

The paper's exceptional statistical rigor, honest limitations disclosure, and systematic negative results elevate it above typical Findings-level work in methodology. However, when half the results require † markers, footnotes, and multi-layer qualifications, the empirical signal is too fragile for Conference acceptance.

**Findings recommendation**: Reframe with Contribution 1 as primary, Contribution 2 as initial characterization on one benchmark. The methodological warning about layer selection bias has sufficient community value for Findings.

**Conference acceptance would require**: (a) second dataset validating layer selection bias generalizability, (b) larger 32B samples or withdrawal of 32B inferential claims, (c) stronger position control justification.

### Individual Reviewer Scores
| Reviewer | Overall | Confidence | Key Concern |
|----------|---------|------------|-------------|
| R1 | 3.5 (Borderline Conference) | 4/5 | Single dataset + 32B underpowered + position confound |
| R2 | 3.0 (Findings) | 4/5 | Single dataset + encoder conditionality + incremental excitement |

The 0.5 gap stems from: (1) R1 gives more weight to Contribution 1's independent methodological value; (2) R2 penalizes "confirmatory" terminology more severely; (3) R2 rates excitement lower (2.5/5 vs R1's 3.0/5). On substantive weaknesses (N1, N3, W1, W2, W4), both reviewers are in close agreement.

Director's consolidated score follows R2's assessment: **3.0 (Findings)**.

---

## Detailed Comments

### Abstract
- Information density too high — reads as compressed results summary rather than accessible abstract. Should present core finding first, then add qualifications incrementally. [R1, R2]
- Leads with "+19.2 to +21.9pp" without immediately qualifying this is against MiniLM-384d. Encoder-quality boundary should be reflected in abstract. [R1, R2]

### Section 1 (Introduction)
- Problem framing is clear: methodological question (layer selection sensitivity) before empirical question (HS vs. text)
- "Before building production detectors" creates deployment expectations inconsistent with 11-50% FPR reality. [R1]
- Contribution 2 listing reads defensively — too many qualifications in the contribution statement itself. [R1]
- "We show this choice alone can reverse a study's central conclusions" — R2 flagged as over-strong; R1 defended with Table 2 evidence. Director: the claim is supported but "a study's" is ambiguous (could imply published work was reversed).

### Section 2 (Related Work)
- Comprehensive and well-organized. Correct distinction between attack characterization / detection / mitigation. [R1]
- Chan & Yong (2025) relationship discussed appropriately. [R1]
- "Alternative Detection Approaches" paragraph could better distinguish temporal/spatial/cross-model methods. [R2]

### Section 3 (Methods)
- CP definition (Section 3.1) is concise but oscillation handling needs more discussion. [R1]
- MiniLM baseline weakness should be declared earlier. [R1]
- Five-metric design (Section 3.3) is well-conceived — the methodological core. [R1]
- Bootstrap clustering and HB implementation are correct. [R1]

### Section 4 (Experiments)
- Table 2 is the most important table and clearly demonstrates the core finding. [R1, R2]
- Section 4.3 position mediation is honest but weakens the central claim — consider giving quadratic control more narrative weight. [R1]
- Section 4.4 32B analysis over-interprets given sample sizes. [R1]
- 18/20 model-seed pass rate: the 2 failures should be clearly identified in main text. [R1]

### Section 5 (Discussion)
- Correct distinction between Contribution 1 (geometric, potentially generalizable) and Contribution 2 (dataset-dependent). [R1, R2]
- "Researcher degree of freedom" discussion should cite Gelman & Loken (2013) — already in bib but uncited. [R1, R2]
- Ensemble proof-of-concept adds practical value; claim boundaries should be stated more precisely. [R1, R2 diverge on evaluation]

### Section 6 (Conclusion)
- Concise and appropriately conditional. [R1]

### Section 7 (Limitations)
- Exceptionally comprehensive: dataset, statistical power, hyperparameters, architecture diversity, CP definition. [R1, R2]
- "One of the most honest limitations sections" (R1) — but the volume of limitations is itself a signal about empirical fragility.

### Appendix (17 pages)
- Extensive robustness checks far exceeding typical NLP papers. [R1]
- Bug disclosure (Appendix N) is excellent scientific practice. [R1, R2]
- Power analysis (Appendix AA) correctly highlights 32B sample inadequacy. [R1]
- Section labels (V, Z, AA) could be more descriptive. [R2]

### Format Notes
- ✅ Main text: 8 pages (Sections 1-6), compliant with EMNLP 2026 strict 8-page limit
- ✅ Anonymization complete: "Anonymous ARR Submission", no de-anonymization found
- ✅ ACL template correctly used (`\usepackage[review]{acl}`)
- ✅ Limitations section present, not counting toward page limit
- ⚠️ Orphan bib entry: `gelman2013garden` defined but never cited
- ⚠️ Missing references: Zou et al. 2024, Templeton et al. 2024, Turner et al. 2023