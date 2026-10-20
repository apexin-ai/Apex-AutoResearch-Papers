---
dream_id: dream_20260514T093336
tier: best
overall_score: weak reject
timestamp: 2026-05-14T10:18:45.742085+00:00
---


# Review Report — Reviewer R2 (Novelty, Significance, Positioning)

**Paper:** Structural Self-Consistency Enables Test-Time Scaling for Entity-Level Information Extraction
**Tier:** Best
**Dream ID:** dream_20260514T093336
**Review Focus:** Novelty, significance, positioning against related work, clarity of contribution

---

## Summary

The paper proposes using soft Jaccard similarity over structured IE outputs as a "structural self-consistency" signal for test-time scaling. It compares this against Fleiss' Kappa across three NER datasets (SciERC, CoNLL-2003, OntoNotes), two model families (Qwen3-8B, LLaMA-3.1-8B), and relation extraction on SciERC. The main findings are: (1) SJ consistently outperforms FK for NER (rho=0.40-0.45 vs 0.29-0.32), yielding +3.9 F1 via best-of-N selection; (2) compound error propagation in RE degrades the signal on the full set (rho=0.27) but conditional analysis recovers rho=0.40, establishing a task-complexity boundary.

---

## Strengths

**S1. Comprehensive experimental matrix.** The paper covers 3 NER datasets spanning domains and type granularities (4-18 types), 2 model families, N-scaling from 2 to 16, temperature sensitivity, capability stratification, per-relation-type decomposition, OOD robustness, and selection curves. For a primarily empirical contribution, this breadth is commendable and substantially exceeds what most empirical studies deliver at top venues.

**S2. The diagnostic analysis of RE failure is genuinely insightful.** The per-relation-type breakdown (Table 7: correlation of rho with type frequency r=0.72, with span distance r=-0.65), the capability stratification revealing an inverted-U pattern (Table 8: RE achieves rho=0.42 in the 0.6-0.9 F1 bucket, matching NER-level performance), and the temperature-as-capability-filter analysis together construct a mechanistic understanding that goes beyond simply reporting negative results. The conceptual distinction between "uncertainty" (where consistency is informative) and "inability" (where it is not) is a genuine contribution that generalizes beyond this specific metric.

**S3. Practical validation through selection curves.** The paper does not stop at correlation analysis but demonstrates that correlation translates to concrete gains: +3.9 F1 via SJ-based best-of-N at N=16 (Table 9), with selection curves (Table 10) showing monotonic SJ advantage at every N. The 26.9% headroom capture rate, while modest, is meaningful given zero additional training cost.

**S4. Honest treatment of negative results and boundary conditions.** The RE analysis does not hide failure but uses it constructively. The paper explicitly identifies where structural consistency fails and provides principled explanations. This intellectual honesty strengthens the paper's credibility.

**S5. Statistical rigor for the main NER claim.** All SJ vs FK comparisons for NER report p < 10^{-27}, with large test sets providing high statistical power. The cross-dataset and cross-model replication makes the core NER finding robust.

---

## Weaknesses

### Major

**W1. (major) Critically missing baselines that undermine the contribution's strength.** The paper compares SJ exclusively against Fleiss' Kappa, which is a weak and arguably strawman baseline for this task. FK operates on token-level BIO labels and was never designed for set-structured outputs. Several natural and stronger baselines are absent:

- **Sequence log-probability / token-level entropy**: The most computationally cheap selection signal, requiring zero additional inference. If SJ does not beat log-prob, the 16x inference cost is unjustified.
- **Exact-match voting rate**: What fraction of N samples produce identical output? This is the direct analogue of Wang et al.'s original self-consistency for structured outputs.
- **Universal Self-Consistency (USC, Chen et al., NAACL 2024)**: Directly extends self-consistency to non-votable structured outputs using LLM-as-judge. This is the single most relevant prior work and is entirely absent from the paper.
- **Semantic uncertainty / clustering-based methods** (Kuhn et al., ICML 2023): Uses semantic equivalence classes for uncertainty estimation on free-form outputs.

Without these baselines, we cannot determine whether SJ's advantage reflects the merit of structural similarity or simply the inadequacy of FK. The core claim "structural consistency outperforms surface agreement" would be far more compelling if SJ also outperformed log-probability-based selection and exact-match voting.

**W2. (major) Thin novelty under the "structural" label.** The technical contribution reduces to applying an existing metric (soft Jaccard with Hungarian matching) as a scoring function in an existing framework (self-consistency / sample-and-select). The "structural" framing overstates what the metric actually captures: SJ operates on flat sets of (span, type) tuples and does not model inter-entity dependencies, schema constraints, co-reference structure, or any graph-level properties. A more accurate description would be "set-aware self-consistency scoring." The metric itself (Eq. 1-4) occupies less than half a page and involves no novel algorithmic ideas. The paper provides neither theoretical analysis of why SJ should correlate with accuracy, nor formal conditions under which the correlation holds. Without either theoretical grounding or differentiation from stronger baselines, the contribution sits below the novelty threshold for a top venue.

**W3. (major) Discrepancy between paper formula and actual implementation.** The paper's Equation 1 defines SJ via symmetric max-match with denominator |y_a|+|y_b|, which permits many-to-one matching. However, the actual implementation (`consistency.py`, lines 114-176) uses: (a) grouping by entity type, (b) Hungarian (optimal one-to-one) matching within each type group via `scipy.optimize.linear_sum_assignment`, and (c) `max(|g_a|, |g_b|)` as the denominator per type group. These are meaningfully different algorithms. The paper formula permits entity "a" in sample 1 to match multiple entities in sample 2 (via the max operation), while the implementation enforces one-to-one matching. The denominators differ. Anyone attempting to reproduce from the paper equations would obtain different results. This must be reconciled — the paper should present the algorithm actually used.

### Moderate

**W4. (moderate) Inconsistent N across the headline cross-dataset table (Table 1).** Table 1 uses N=16 for SciERC but N=8 for CoNLL and OntoNotes. Table 2 shows that increasing N from 8 to 16 improves rho_SJ by +0.065 on SciERC. At N=8, SciERC's rho_SJ was 0.383 — actually the lowest of the three datasets when compared at consistent N. The current presentation inflates SciERC's apparent advantage and confounds the cross-dataset comparison. This is a significant methodological issue: the main comparison table must use consistent conditions.

**W5. (moderate) Evaluation protocol has a subtle circularity.** The consistency score c(x) is computed from T=0.7 samples, but the evaluation metric is Spearman correlation with greedy (T=0) F1. Meanwhile, best-of-N selection operates on the T=0.7 samples themselves. The paper does not justify why greedy F1 is the right proxy. A more direct evaluation would correlate each sample's leave-one-out SJ score with that sample's own F1, or report Kendall's tau between the SJ ranking and the F1 ranking within each instance's sample set.

**W6. (moderate) Single RE dataset limits diagnostic claims.** All RE analysis relies on SciERC (397 instances, 7 relation types). The "compound error propagation" explanation is plausible and well-argued, but it remains an interpretation of one dataset. A second RE dataset (TACRED, DocRED, or even SciERC's own event structures) would substantially strengthen Claim 2. As it stands, the boundary condition findings are suggestive but dataset-specific.

**W7. (moderate) No confidence intervals for rho estimates.** Bootstrap confidence intervals are absent throughout. Some capability-stratified analyses have small sample sizes (42-85 instances per bucket in Table 8), where rho estimation is noisy. The rho values in Table 7 are reported as ranges ("0.36-0.40") rather than point estimates, which is unusual and unexplained.

### Minor

**W8. (minor) No RE best-of-N selection results.** The adaptive compute demonstration and selection curves are NER-only. Even a negative RE selection result would complete the story and prevent the impression that RE results are selectively omitted from the practical evaluation.

**W9. (minor) Reference list is thin.** Only 10 references in the bibliography — far below the 30-40 typical for a top venue paper. This exacerbates the missing related work issues described below.

**W10. (minor) Temperature analysis (Table 5) headroom values are inconsistent.** Table 5 reports NER T=0.7 headroom as 0.055 while Table 2 reports N=8 headroom as 0.108. The relationship between these numbers is not explained (presumably one is N=8 at T=0.7 and the other is N=8 at T=1.0, but this should be explicit).

---

## Questions for Authors

**Q1.** How does SJ compare against sequence log-probability as a selection signal? This is the most natural and cheapest baseline — it requires no additional inference passes.

**Q2.** Are you aware of Universal Self-Consistency (Chen et al., NAACL 2024), which extends self-consistency to free-form structured outputs using LLM-as-judge? How does your approach compare in cost and effectiveness?

**Q3.** Can you reconcile Equation 1 (symmetric max-match, |y_a|+|y_b| denominator) with the actual implementation (type-grouped Hungarian matching, max(|g_a|,|g_b|) denominator per group)? Which version produced the reported results?

**Q4.** For Table 1, what are the rho values for all three datasets at a consistent N=8? The current mixed-N presentation confounds the cross-dataset comparison.

**Q5.** What explains the rho ranges (rather than point estimates) in Table 7? Are these from multiple seeds, bootstrap intervals, or different conditions?

**Q6.** The inverted-U pattern in Table 8 is computed by stratifying on greedy F1, which is the same quantity being correlated against. Does this introduce a selection bias? Have you verified the pattern holds when stratifying on an independent difficulty proxy (e.g., sentence length, entity count)?

**Q7.** Have you considered whether the SJ advantage over FK is simply an artifact of FK's known sensitivity to prevalence? When entity density is low (few entities per sentence), FK is known to underestimate agreement even when absolute agreement is high. A prevalence-adjusted FK (PABAK) would be a more appropriate surface baseline.

---

## Missing Related Work

The following are significant omissions:

1. **Universal Self-Consistency (USC)** — Chen et al., NAACL 2024. Extends self-consistency to non-votable outputs using LLM-as-judge to assess pairwise equivalence. This is the most directly relevant prior work and must be discussed.

2. **Semantic Uncertainty** — Kuhn et al., ICML 2023. Uses bidirectional entailment to cluster semantically equivalent outputs for uncertainty estimation. Relevant to the question of how to measure agreement between complex structured outputs.

3. **Verifier/reward model TTS** — Cobbe et al. 2021 (math verification), Lightman et al. 2024 (process reward models). The dominant TTS paradigm; entirely absent from discussion.

4. **LLM calibration literature** — Kadavath et al. 2022 (P(True)), Xiong et al. 2024 (Can LLMs Express Uncertainty?). Log-probability and verbalized confidence baselines are standard comparators for any confidence estimation approach.

5. **SelfCheckGPT** — Manakul et al. 2023. Cited in the paper summary but not adequately distinguished from in the paper body. SelfCheckGPT also uses sample consistency for hallucination detection — the paper should explain how its approach differs beyond the metric choice.

6. **Agreement-based active learning** — Settles 2009, Houlsby et al. 2011. Query-by-committee methods use inter-model agreement as an uncertainty signal, which is conceptually similar to inter-sample agreement for selection.

7. **Structured prediction calibration** — Kuleshov & Liang 2015, Desai & Durrett 2020. Calibration methods for structured outputs are relevant to the confidence estimation framing.

8. **IE-specific confidence estimation** — Culotta & McCallum 2004 (confidence estimation for IE), Shelmanov et al. 2021 (active learning for NER with uncertainty). Cited in the paper summary but absent from the actual paper text.

---

## Novelty Score: 2 / 6

The core technical contribution — applying soft Jaccard as a self-consistency metric for IE outputs — is a straightforward adaptation of an existing metric to an existing framework. The "structural" framing overstates what is essentially set-level scoring. The empirical findings (inverted-U, compound error, type granularity moderation) are the paper's strongest novelty dimension, but they are empirical observations without theoretical underpinning, and several are predictable given the metric design (e.g., multiplicative RE scoring naturally amplifies noise). The diagnostic contribution is genuinely interesting but does not compensate for the thin methodological novelty, especially given the missing baselines that prevent us from assessing whether SJ itself is the right metric or merely better than one weak baseline.

---

## Preliminary Overall Score: 3 / 6 (Weak Reject)

**Justification:** The paper addresses a relevant problem and provides thorough experiments with honest analysis. The diagnostic framework for understanding when consistency-based TTS works is the paper's strongest element and represents a genuine intellectual contribution. However, for a top venue with ~25% acceptance rate, the paper falls short on three critical dimensions:

(1) **Novelty is thin.** The methodological contribution reduces to metric substitution (SJ for FK) without theoretical justification or algorithmic innovation. The "structural" label overpromises relative to what SJ actually captures.

(2) **Missing baselines leave the core claim unsupported.** Without comparison to log-probability, USC, exact-match voting, or semantic uncertainty, we cannot assess whether SJ is genuinely a good confidence signal or merely better than a weak baseline. This is the most fixable issue.

(3) **Formula-implementation discrepancy undermines reproducibility.** The paper presents one algorithm; the code implements another. This is a significant methodological concern.

The path to acceptance exists and is relatively clear: add 2-3 stronger baselines (especially log-probability and USC), fix the formula discrepancy, standardize N across Table 1, expand the reference list substantially, and reframe the contribution more honestly as "set-aware consistency scoring with diagnostic analysis of boundary conditions." If SJ outperforms log-probability, the metric design argument becomes compelling. If it does not, the paper's value shifts entirely to the diagnostic framework, which would need to be foregrounded much more aggressively. As currently written, the paper is between Findings and Reject — the experimental depth pushes toward Findings, but the novelty gap and missing baselines push toward Reject.
