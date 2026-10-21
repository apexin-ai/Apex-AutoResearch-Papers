---
dream_id: dream_20260519T034058
tier: worst
overall_score: weak reject
timestamp: 2026-05-19T04:54:50.763382+00:00
---

# Dream Review Report: "When Do Self-Extracted Symbolic Constraints Help LLM Reasoning? A Diagnostic Study"

## Roundtable Summary

Two reviewers conducted independent reviews (R1: methods + experiments; R2: novelty + related work), followed by cross-sharing and convergence discussion. Both reviewers independently scored the paper 3/6 (Weak Reject) and maintained their scores after cross-review. There is strong consensus on the key strengths and weaknesses.

---

## Consolidated Review

### Paper Summary

The paper studies SICA (Symbolic Invariant Consensus Aggregation), a pipeline that extracts first-order logic (FOL) constraints from LLM reasoning traces and aggregates them via weighted MAX-SAT to select answers. Framed as a diagnostic study across 7 models and 6 reasoning domains, the core finding is negative: self-extracted constraints yield zero or negative gains in 9 of 12 conditions. The single significant positive result (Mistral-7B on FOLIO, +4.9pp, p=0.013) does not generalize across seeds (1/3 null). An oracle control shows +14.2pp with gold FOL, localizing the bottleneck to extraction quality. Nine remediation strategies all fail to close the gap.

### Strengths

- **S1: Oracle control is well-designed and informative.** Substituting gold FOL annotations while holding the aggregation pipeline fixed cleanly isolates extraction quality from aggregation effectiveness. The +14.22pp result (p < 10^-6) is the paper's strongest contribution, establishing that constraint-based aggregation has theoretical headroom. (R1, R2 agree)

- **S2: Honest, systematic negative-result reporting.** Testing 7 models across 6 domains and transparently reporting predominantly null/negative results is commendable. The three-seed replication on the main positive finding, with one seed null, is more transparent than typical practice. (R1, R2 agree)

- **S3: MAX-SAT approximately equals count-only (803/804 agreement).** This is a genuinely informative ablation showing the symbolic optimization machinery adds negligible value over simple constraint counting, because constraint satisfaction scores are nearly uniform across candidates (mean ratio ~0.96). (R1, R2 agree)

- **S4: Extraction error taxonomy provides mechanistic explanation.** The finding that 43% of constraints are trivially satisfied and 78% mirror the model's majority-vote answer explains *why* SICA degenerates to SC, going beyond simply reporting null results. (R1)

- **S5: Regime characterization (Type A/B/C) is useful.** The three failure modes are distinct and well-defined. The Type C result (significant harm at low SC) is a practical warning. (R2)

### Weaknesses (Consensus, Ranked by Severity)

- **W1 [Critical]: Data integrity failure.** The Abstract, Introduction, Discussion, and Conclusion all report the Type C (ProofWriter) result as Delta = -4.67pp, while Table 1 reports Delta = -2.83pp. This discrepancy appears to stem from an interim analysis (n=303) that was not updated when the final analysis (n=600) was completed. A core claimed result reported with two different values in the same paper is a serious error that undermines trust in all reported numbers. (R1 identified, R2 confirmed)

- **W2 [Major]: No result survives multiple-comparison correction.** With 13 non-oracle self-extraction conditions tested, Bonferroni correction (alpha_adj = 0.0038) renders both nominally significant results (seed 42 p=0.013, seed 123 p=0.039) non-significant. The paper does not discuss multiple comparisons at all. The central positive claim therefore rests on an uncorrected p-value. (R1 identified, R2 strongly agreed)

- **W3 [Major]: The Goldilocks zone is a single fragile point, not a zone.** The positive finding requires simultaneously: the right model (Mistral-7B only), the right dataset (FOLIO only; LogiQA at similar SC shows null), the right temperature (T=0.7 is best but T=0.3 also positive, complicating the narrative), the right K (K=12 highest but no pairwise differences significant), and the right seed (2/3 successful). Five degrees of freedom that were not controlled for. The mean effect across seeds (+2.61pp) was not tested for significance. (R1, R2 strong consensus)

- **W4 [Major]: Limited impact of diagnosing a never-proposed method.** SICA is the authors' own construction, not an established method from the literature. Diagnostic studies gain force from challenging widely-adopted approaches. Showing that a method nobody advocated fails carries limited weight. The finding that "same-model FOL self-extraction is low quality" is predictable from prior work: LINC documented ~40% translation errors on FOLIO, Huang et al. (2024) established LLMs cannot self-correct reasoning. (R2 identified, R1 agreed)

- **W5 [Major]: Missing baselines leave a critical gap.** No comparison against: (a) self-verification prompting ("is this answer correct?"), (b) best-of-K with LLM-as-judge scoring, (c) weighted SC using trace confidence. These are zero-training-data baselines in the same compute regime. Without them, it is unclear whether SICA's failure is specific to symbolic constraints or reflects a general limitation of same-model verification. (R1 identified, R2 agreed)

- **W6 [Moderate]: Condorcet/Eff-K framework is descriptive, not predictive.** Joint Eff-K+SC prediction accuracy is 50% (= random chance) across 12 conditions. Eff-K is non-monotonic with SICA delta across seeds (lowest Eff-K produces highest delta). The paper acknowledges this but continues to use "independence bottleneck" as a central explanatory concept. R1 considers the framework "ornamental"; R2 grants modest descriptive value for cross-model comparison but agrees it is not predictive. (R1, R2 converge on substance; slight disagreement on severity)

- **W7 [Moderate]: Remediation strategy count inconsistency.** The Abstract says "six," Section 5.8 describes nine across six dimensions, and the appendix table shows six rows. This suggests sections were written at different times and not reconciled. (R1, R2 both identified independently)

- **W8 [Moderate]: Selective temperature reporting.** Table 6 shows T=0.3 (+3.92pp, p=0.065), T=0.5 (+2.45pp), T=0.7 (+4.90pp), T=1.0 (+0.49pp). The pattern is positive across low-to-medium temperatures, not a "narrow window." This undermines both the fragility narrative and the "all remediations fail" claim (multi-temp at +2.45pp is a partial positive). The paper discusses this in Section 5.5 and Table 6 but the broader temperature robustness is underplayed relative to the fragility framing in the Abstract and Introduction. (R1 identified, R2 agreed)

- **W9 [Minor]: Reference quality issues.** Several entries use "and others" instead of full author lists (FoVer, Aristotle, Loo et al.). Cobbe et al. (2021) appears duplicated. Multiple 2026-dated venue references may be difficult for reviewers to verify. Below the standard for a top venue. (R2 identified)

- **W10 [Minor]: Sample size heterogeneity.** Seven of eleven non-oracle conditions have n <= 60, plotted alongside n=200-804 conditions. Power analysis shows n=200 cannot detect effects below ~4.6pp. Small-n conditions are essentially uninformative for the regime boundaries claimed. (R1 identified)

### Questions for Authors

1. Which is the correct Type C delta: -2.83pp (Table 1) or -4.67pp (Abstract/Introduction/Conclusion)? All occurrences must be reconciled.
2. How many remediation strategies were tested: six or nine? Reconcile across all sections.
3. Have you considered Bonferroni or Holm-Bonferroni correction across the 13 non-oracle conditions? Would any result survive?
4. Why should the community care that an author-constructed method (SICA) fails, given no prior work proposed it? What prior belief does this paper update beyond what LINC and Huang et al. already established?
5. If MAX-SAT adds nothing over count-only (803/804 agreement), why frame the paper around "symbolic consensus" rather than the more general question of whether self-extracted features of any kind improve multi-sample aggregation?
6. The multi-temperature intervention shows a positive trend (+2.45pp, increased Eff-K from 1.85 to 2.80). Why was this not scaled up to a larger sample to resolve statistical power? This seems like the most promising direction left unexplored.
7. Can you provide the correlation between Eff-K and Delta across all conditions with a significance test?

### Scores

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Methods + Experiments | 3/6 | 4/5 |
| R2 | Novelty + Related Work | 3/6 | 4/5 |
| **Consensus** | | **3/6 (Weak Reject)** | **4/5** |

### Meta-Review

Both reviewers independently arrived at 3/6 and maintained their scores after cross-review, indicating strong consensus. The paper's core strength is the well-designed oracle control establishing that constraint-based aggregation has theoretical headroom (+14.2pp). The honest negative-result reporting and systematic coverage are appreciated.

However, the paper faces several compounding problems. First, it diagnoses a method (SICA) that was never proposed by others, limiting the impact of showing it fails. Second, the single positive finding does not survive multiple-comparison correction, does not generalize across models, domains, or seeds, and requires five simultaneous conditions to manifest. Third, internal inconsistencies (the -2.83 vs -4.67pp discrepancy, six-vs-nine remediation count) undermine confidence in the reported results. Fourth, the Condorcet/Eff-K theoretical framework operates at chance-level prediction accuracy, making it descriptive rather than predictive. Fifth, the absence of simple baselines (self-verification, best-of-K with LLM judge) leaves open whether the failure is SICA-specific or general.

The paper occupies an awkward middle ground: the temperature results (positive across T=0.3-0.7) and multi-temp intervention (positive trend) suggest SICA is not a dead end, yet the paper frames it as one. This tension between the data and the narrative weakens both a "method paper" reading and a "clean negative result" reading.

**Recommendation:** Below the acceptance threshold for a top ML venue main conference (which would require ~4/6). The oracle control and regime characterization have value and could support a Findings-level contribution after: (1) fixing all numerical inconsistencies, (2) adding multiple-comparison discussion, (3) adding missing baselines, (4) honestly presenting the temperature results as showing broader-than-claimed robustness, and (5) reframing the contribution around what the oracle gap reveals about extraction quality rather than around the Condorcet/Eff-K framework.
