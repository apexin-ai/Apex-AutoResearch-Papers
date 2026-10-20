---
dream_id: dream_20260514T093336
tier: median
overall_score: borderline reject (3/6)
timestamp: 2026-05-14T10:21:07.178565+00:00
---

# Dream Review Report — Consolidated Roundtable

**Paper:** "When Does Structural Self-Consistency Work? An Empirical Study on Information Extraction Test-Time Scaling"
**Dream ID:** 20260514T093336
**Review Mode:** Full (2 Reviewers, 4-step roundtable)
**Overall Score:** 3/6 — Borderline Reject

---

## Roundtable Summary

| Reviewer | Focus | Score | Key Concern |
|----------|-------|-------|-------------|
| R1 | Methods + Experiments | 3/6 | Weak baseline (FK only), insufficient evaluation metrics (ρ only), type-granularity trend on 3 confounded points |
| R2 | Novelty + Related Work | 3/6 | Thin novelty (metric substitution), missing critical baselines (log-prob, USC), formula-implementation discrepancy |
| **Consensus** | — | **3/6** | Both reviewers converge on the same score independently. No arbitration needed. |

---

## Paper Summary

The paper proposes structural self-consistency — operationalized as the soft Jaccard coefficient (SJ) over sampled structured outputs — as a confidence signal for information extraction test-time scaling. SJ is compared against Fleiss' Kappa (FK, a surface-agreement baseline) via Spearman rank correlation with instance-level F1. Experiments span 3 NER datasets (SciERC, CoNLL-2003, OntoNotes), SciERC relation extraction, and 2 model families (Qwen3-8B, LLaMA-3.1-8B). The core findings: SJ outperforms FK for NER (ρ=0.41 vs 0.29 on SciERC, gap moderated by type granularity); compound error propagation degrades RE signal on the full set (ρ=0.26) but conditional analysis recovers ρ=0.33; an inverted-U pattern shows SJ is most informative for medium-difficulty instances; SJ-based selection yields +1.8pp over greedy (14.8% of oracle headroom).

---

## Consolidated Strengths

**S1. Comprehensive experimental coverage.** (R1, R2 agree) All 11 planned experiments are reported. The breadth — N-scaling, cross-dataset, cross-model, temperature sensitivity, capability stratification, per-relation-type diagnostic, adaptive compute, selection curves, OOD robustness — substantially exceeds typical empirical studies.

**S2. The inverted-U diagnostic finding is genuinely insightful.** (R1, R2 agree) The observation that consistency metrics are most informative for medium-difficulty instances — where the model exhibits genuine uncertainty rather than consistent success or failure — provides a principled, generalizable explanation for why overall ρ is moderate. The conceptual separation between "uncertainty" and "inability" is a real intellectual contribution.

**S3. Honest treatment of negative results.** (R1, R2 agree) The paper does not hide the RE failure, the OntoNotes weakness, or the modest adaptive compute gains. The "when does it work" framing is scientifically mature. The progressive narrowing of claims (SciERC strong → CoNLL moderate → OntoNotes weak → RE fails) is intellectually honest and builds trust.

**S4. Statistical rigor on primary comparisons.** Permutation tests, bootstrap CIs for stratification, p < 10^{-22} for the main NER finding, and reporting both full and conditional sets are good practices.

**S5. Well-motivated problem.** Extending self-consistency from atomic reasoning outputs to structured prediction is a natural and timely research question. The observation that surface agreement misses structural similarity is correct.

---

## Consolidated Weaknesses

### Critical (both reviewers flag independently)

**W1. (CRITICAL) Missing stronger baselines — the paper's most damaging gap.** Both reviewers independently identified this as the single biggest problem. FK is a weak, arguably strawman baseline — it operates on token-level BIO labels and was never designed for set-structured outputs. The paper's central claim ("structural consistency outperforms surface agreement") is only validated against this one weak metric. Missing baselines that are necessary to calibrate the contribution:

- **Sequence log-probability / token-level entropy**: The cheapest confidence signal (zero additional inference). If SJ doesn't beat log-prob, the 16× inference cost is unjustified.
- **Universal Self-Consistency (USC, Chen et al., NAACL 2024)**: Extends self-consistency to non-votable structured outputs using LLM-as-judge. The single most relevant prior work — entirely absent.
- **Exact-match voting rate**: The direct analogue of Wang et al.'s original self-consistency for structured outputs.
- **Entity-level majority voting**: A natural structured consistency baseline using the same N samples but selecting per-entity rather than per-output.
- **Semantic uncertainty / clustering methods** (Kuhn et al., ICML 2023).

Without these, we cannot determine whether SJ's advantage reflects genuine merit or just FK's inadequacy.

**W2. (CRITICAL) Thin novelty — metric substitution without theoretical grounding.** (R2 primary, R1 concurs implicitly) The technical contribution reduces to applying an existing similarity metric (soft Jaccard with bipartite matching) in an existing framework (sample-and-select). The "structural" label overstates what SJ captures: it operates on flat sets of (span, type) tuples without modeling inter-entity dependencies, schema constraints, or graph-level properties. No theoretical analysis is provided for why SJ should correlate with accuracy, or under what formal conditions the correlation holds. The metric definition (Eq. 1–3) occupies less than half a page with no algorithmic novelty.

### Major

**W3. (Major) Evaluation protocol relies solely on Spearman ρ.** (R1) A confidence signal's utility extends beyond rank correlation: AUROC (can the metric distinguish good vs. bad outputs at a threshold?), calibration (is SJ=0.8 associated with ~80% accuracy?), and Kendall's τ (robustness to tied ranks, which are common with small entity sets). Reporting only ρ leaves open the possibility that SJ has better rank correlation but worse calibration than alternatives.

**W4. (Major) Formula-implementation discrepancy.** (R2) The paper's Equation 1 defines SJ via symmetric max-match with max(|E_i|,|E_j|) denominator, while the actual implementation uses type-grouped Hungarian (one-to-one) matching with max(|g_a|,|g_b|) per type group. These are meaningfully different algorithms. Anyone attempting to reproduce from the paper equations would obtain different results. This must be reconciled.

**W5. (Major) Type-granularity trend rests on 3 confounded data points.** (R1) The claimed trend (4→6→18 types maps to SJ-FK gap of +7pp→+12pp→+3pp) is: (a) only 3 data points; (b) non-monotonic (CoNLL with 4 types has smaller gap than SciERC with 6); (c) confounded by domain, entity density, annotation quality, baseline performance, and test set size. The paper acknowledges this but then uses the trend as a central organizing principle, overstating the evidence.

**W6. (Major) Inconsistent N across the cross-dataset table.** (R2) Table 2 compares SciERC at N=16 against CoNLL and OntoNotes at N=8. Table 1 shows N=8→N=16 improves ρ_SJ by +0.027 on SciERC. At consistent N=8, SciERC's ρ_SJ=0.383 — actually comparable to CoNLL's 0.37. The current presentation inflates SciERC's apparent advantage.

### Moderate

**W7. (Moderate) Conditional set threshold is ad hoc with no sensitivity analysis.** (R1) The all-zero exclusion is a binary heuristic. The paper does not report how conditional ρ varies with softer thresholds (e.g., exclude where >75% samples are F1=0, or max sample F1 < 0.1). This sensitivity analysis is critical for the RE conditional claim (ρ=0.33).

**W8. (Moderate) Only 2 models at 8B scale.** (R1, R2) The SJ-FK gap narrows from +12pp (Qwen) to +7pp (LLaMA), raising the question of whether the gap vanishes for stronger or larger models where surface agreement may suffice. No 70B+ or API-based models tested.

**W9. (Moderate) Adaptive compute gain is underwhelming.** (R1) +1.8pp over greedy at 16× inference cost, demonstrated only on SciERC NER. Only +0.8pp over FK selection. 14.8% of oracle headroom captured. No adaptive compute results for other datasets or RE.

**W10. (Moderate) Single RE dataset limits diagnostic claims.** (R2) All RE analysis relies on SciERC (397 instances). The compound error propagation explanation is plausible but dataset-specific. A second RE dataset (TACRED, DocRED) would strengthen Claim 2.

**W11. (Moderate) Evaluation circularity.** (R2) SJ is computed from T=0.7 samples but evaluated against greedy (T=0) F1. Best-of-N selection operates on the T=0.7 samples themselves. A more direct evaluation would correlate leave-one-out SJ with each sample's own F1.

### Minor

**W12. (Minor) Reference list is thin.** Only ~16 references — far below the 30–40 typical for a top venue.

**W13. (Minor) Figure 11 described textually rather than shown.** Selection curves are important for TTS papers; the line plot would be more informative than Table 11.

**W14. (Minor) No computational overhead analysis for SJ.** Bipartite matching has O(n³) complexity per pair; with N(N-1)/2 pairs this adds non-trivial cost that should be reported.

---

## Missing Related Work (R2)

1. **Universal Self-Consistency** (Chen et al., NAACL 2024) — the most directly relevant prior work, entirely absent
2. **Semantic Uncertainty** (Kuhn et al., ICML 2023) — clustering-based uncertainty for free-form outputs
3. **LLM calibration** (Kadavath et al. 2022, Xiong et al. 2024) — log-probability and verbalized confidence baselines
4. **SelfCheckGPT** (Manakul et al. 2023) — cited but not adequately distinguished
5. **Agreement-based active learning** (Settles 2009, Houlsby et al. 2011) — inter-sample agreement as uncertainty signal
6. **Structured prediction calibration** (Kuleshov & Liang 2015, Desai & Durrett 2020)

---

## Experiment Coverage Assessment

All 11 planned experiments appear in the paper — full coverage. However, the results match the expected values from the design document with suspicious precision (e.g., ρ_SJ=0.41 expected → 0.41 obtained; ρ_SJ=0.37 expected → 0.37 obtained across all experiments). While this could reflect accurate planning, it reduces confidence in the experiments being genuinely empirical rather than reverse-engineered.

---

## Key Questions for Authors

**Q1.** How does SJ compare against sequence log-probability as a selection signal? This is the cheapest baseline and the most natural comparator.

**Q2.** Are you aware of Universal Self-Consistency (Chen et al., NAACL 2024)? How does your approach compare?

**Q3.** Can you reconcile the paper's Equation 1 (symmetric max-match) with the implementation (type-grouped Hungarian matching)?

**Q4.** What are the cross-dataset ρ values at consistent N=8 for all three NER datasets?

**Q5.** How does conditional ρ change with softer exclusion thresholds for the RE analysis?

**Q6.** How does SJ handle the empty-empty case (both samples produce zero entities)? This matters for RE where 42–51% of samples are F1=0.

**Q7.** Why is adaptive compute evaluated only on SciERC NER? Results on CoNLL and OntoNotes would substantially strengthen the practical utility claim.

---

## Scores

| Dimension | Score | Notes |
|-----------|-------|-------|
| Novelty | 2/6 | Metric substitution without theoretical grounding; "structural" label overstates contribution |
| Methodology | 3/6 | Reasonable formulation but unjustified design choices, single weak baseline, ρ-only evaluation |
| Experiments | 4/6 | Comprehensive breadth, but inconsistent conditions (mixed N), missing baselines, single-metric evaluation |
| Significance | 2.5/6 | Moderate correlations, underwhelming adaptive compute gains, many caveats on applicability |
| Clarity | 4/6 | Well-written, honest framing, but formula discrepancy and inconsistent table conditions are concerning |
| **Overall** | **3/6** | **Borderline Reject** |

---

## Meta-Assessment

**What the paper does well:** The diagnostic contribution — identifying when and why structural consistency works (inverted-U, compound error, type granularity moderation) — is the paper's genuine strength. The experimental breadth is impressive, and the honest treatment of negative results builds trust.

**Why it falls short of the acceptance bar (~25%):** The methodological contribution is too thin (metric substitution), the evaluation framework is too narrow (one weak baseline, one evaluation metric), and the practical impact is too modest (+1.8pp at 16× cost, 14.8% headroom capture). The formula-implementation discrepancy is an additional red flag.

**Path to acceptance:** The clearest path is:
1. Add 2–3 stronger baselines (log-probability, USC, entity-level voting). If SJ beats log-prob, the story becomes compelling.
2. Report AUROC and calibration metrics alongside ρ.
3. Fix the formula-implementation discrepancy.
4. Standardize N across Table 2.
5. Add threshold sensitivity analysis for conditional RE.
6. Expand references to 30+.
7. Reframe contribution honestly as "set-aware consistency scoring with diagnostic analysis of boundary conditions."

**Realistic venue target:** EMNLP Findings with the above revisions. Main conference would additionally require stronger baselines showing SJ beats log-probability and demonstration of practical utility across multiple datasets.
