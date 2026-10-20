---
dream_id: dream_20260514T203201
tier: best
overall_score: 4/6 Weak Accept
timestamp: 2026-05-14T21:23:36.870254+00:00
---

# Dream Review Report: "Structural Self-Consistency for Quality Estimation in LLM-Based Information Extraction"

**Review Mode:** Full | **Reviewers:** R1 (Methods+Experiments), R2 (Novelty+Related Work)
**Standard:** Top ML venue, ~25% acceptance rate, 6-point scale

---

## Consolidated Assessment

**Overall Score: 4/6 (Weak Accept)**

Both reviewers independently scored 4 (Weak Accept) and converged after cross-discussion. The paper is a borderline submission with one genuinely useful finding (the correlation–selection gap) embedded in an otherwise expected empirical comparison. The methodological contribution (Soft Jaccard) is incremental. Strengths are systematic experimental coverage and honest reporting; weaknesses are limited novelty, narrow scope, and missing key comparisons.

---

## Summary of Contributions

The paper systematically compares five unsupervised confidence signals (log-probability, exact match, Fleiss' κ, Soft Jaccard, entity voting) for quality estimation and sample selection in LLM-based information extraction (NER, RE) across two models (Qwen3-8B, LLaMA-3.1-8B) and two datasets (SciERC, CoNLL-2003), with an OOD appendix on WNUT-2017.

Three main findings:
1. Structural consistency signals (voting, SJ) are the strongest unsupervised quality estimators, outperforming logprob by 17–30 AUROC points.
2. A *correlation–selection gap*: strong instance-level quality prediction does not translate to effective best-of-N selection on NER.
3. A *task-complexity boundary*: compound error propagation in RE degrades all signals; conditional filtering restores power.

---

## Strengths (Consensus)

- **The correlation–selection gap is a genuine and useful finding.** The formal separation of quality estimation (which inputs are reliable?) from sample selection (which output is best?) is the paper's strongest conceptual contribution. The finding that no consistency signal beats greedy on NER despite ρ=0.50 challenges implicit assumptions in the TTS scaling literature and has implications beyond IE. (R1, R2)

- **Systematic experimental design.** The 2×2 model-dataset matrix, 5 signals, multiple evaluation metrics (ρ, τ, AUROC, best-of-N F1), temperature/N ablations, and 3-seed robustness provide thorough coverage for an empirical study. (R1)

- **Cross-model stability is compelling.** SJ Δρ=0.005 on CoNLL between architecturally distinct 8B models (Qwen3 vs. LLaMA-3.1) is strong evidence for model-agnosticism within this scale. (R1, R2)

- **Honest reporting of negative results.** NER selection failure, WNUT-17 boundary, RE signal weakness — the paper does not oversell. (R1, R2)

- **The logprob paradox (AUROC-ρ divergence).** The observation that logprob achieves highest AUROC (0.761) but lowest ρ (0.307) on LLaMA×CoNLL is a methodologically important point about evaluation metric choice. (R1, R2)

- **Conditional filtering analysis.** The finding that SJ maintains ρ=0.308 on RE while logprob collapses is the most practically actionable result. (R2)

- **Clear, well-organized writing** with appropriate quantitative specificity and hedging. (R1, R2)

---

## Weaknesses (Consensus)

### Major

1. **Limited methodological novelty.** (R1, R2) No new algorithm. Soft Jaccard assembles known components (type-grouped Hungarian matching, span-overlap similarity, Jaccard normalization) — competent engineering, not a conceptual advance. The paper is fundamentally an empirical comparison study, which raises the bar for surprising results.

2. **Missing MBR decoding connection.** (R2) SJ-based selection is essentially Minimum Bayes Risk decoding with SJ as the utility function (cf. Kumar & Byrne 2004; Freitag et al. 2022). This framing is never discussed, which is a significant positioning oversight that makes the selection analysis appear disconnected from a well-studied literature.

3. **Missing LLM-as-judge comparison.** (R2) Universal Self-Consistency (Chen et al. 2024) is cited but never empirically compared. An LLM-judge baseline for quality estimation is the most natural alternative to structural metrics for non-identical structured outputs. Even a small-scale comparison would strengthen positioning.

4. **No confidence intervals on primary comparison tables.** (R1) Tables 1–2 lack error bars or bootstrap CIs for any signal comparison. With ~20–30 implicit pairwise comparisons and some narrow gaps (CoNLL SJ vs. FK = 0.003), this is a significant statistical omission. The memory.md mentions bootstrap CIs exist for some comparisons but they are absent from the paper.

5. **Single RE dataset.** (R1, R2) Claim 3 (compound error propagation) rests entirely on SciERC RE (n=397, 44% zero-F1). Generalization to ACE05, TACRED, or other relation benchmarks is untested. This is the single biggest empirical gap.

### Moderate

6. **Soft Jaccard under-specified.** (R1) The matching threshold for bipartite matching and the entity-matching criterion for voting confidence are not explicitly defined in the paper. Different thresholds could change SJ values materially.

7. **Selection heuristic confound.** (R1) For best-of-N with instance-level signals, the paper selects the sample closest to consensus. This heuristic is untested against alternatives (e.g., median-SJ sample, mode sample). Selection failure may be partially attributable to this heuristic rather than inherent signal limitations.

8. **Narrow scope.** (R1, R2) Only entity-level IE (NER + RE), only 8B models, only 2–3 datasets. The claim that SJ "generalizes to arbitrary set-structured outputs" is asserted but never tested beyond NER/RE. "Model-agnostic" is overstated for two same-scale models.

9. **Narrow N range (8–16).** (R1) Two points define a line, not a curve. Whether N-scaling gains plateau or continue is unknown. A single experiment at N=32 or N=64 would clarify.

10. **Temperature analysis incomplete.** (R1) Only two temperatures (0.7, 1.0). Logprob excluded from temperature comparison. Cannot characterize the temperature–signal relationship.

### Minor

11. **3-seed robustness only on NER, not RE.** RE has no multi-seed analysis despite being the more fragile setting. (R1)

12. **Set similarity metric precedents not engaged.** (R2) BioNLP shared tasks use similar relaxed matching schemes. The paper does not engage with this evaluation metric literature.

13. **"Structural self-consistency" framing somewhat misleading.** (R2) "Set-aware consistency metrics" would be more accurate. The current title implies a deeper architectural contribution than delivered.

---

## Key Questions for Authors

1. **(SJ specification)** What is the exact matching criterion in entity voting confidence — exact string match or span overlap? If exact string, how does voting differ from a surface signal? What is the matching threshold for SJ's bipartite assignment? (R1)

2. **(Selection heuristic)** Did you test alternative selection strategies for instance-level signals? How sensitive is the NER selection failure to the consensus-proximity heuristic? (R1)

3. **(Bootstrap CIs)** Can you provide confidence intervals for key signal-vs-signal deltas in Tables 1–2? The +2.3pp RE logprob selection gain — is it statistically significant? (R1)

4. **(MBR connection)** Have you considered framing SJ-based selection as MBR decoding? Does this reframing change any findings? (R2)

5. **(LLM-judge baseline)** How does SJ compare to an LLM-as-judge baseline (e.g., self-evaluation or pairwise comparison)? The absence of this comparison against cited USC needs justification. (R2)

6. **(Generalizability)** Has the correlation–selection gap been tested on tasks beyond IE (code generation, SQL, summarization) to support broader claims? (R2)

7. **(Conditional filtering in practice)** What is the mechanism for conditional filtering without gold labels at deployment time? How would a practitioner identify "capability boundary" instances? (R2)

8. **(EM competitiveness)** On CoNLL, EM (ρ=0.451) rivals SJ (0.436). What is the marginal value of SJ over trivially computable EM for high-accuracy NER? (R2)

---

## Experiment Coverage Assessment

| Planned Experiment | Status | Notes |
|---|---|---|
| exp-011 (SciERC→WNUT-17 OOD) | ✅ Covered | Table 6, Appendix A. Results match expected: greedy F1 drops to 0.143, logprob negative, structural weak but positive. |
| exp-017 (LLaMA×CoNLL + 3-seed) | ✅ Covered | Tables 2, 3, 4. Results match expected: SJ ρ=0.431, cross-model Δ=0.005, 3-seed σ=0.008. |

Both planned experiments are fully reflected in the paper. The experiment design is complete as specified.

**Missing experiments that would strengthen claims:**
- Second RE dataset (ACE05/TACRED)
- N > 16 experiment
- LLM-as-judge / USC empirical comparison
- Closed-source API evaluation (logprob-unavailable regime)
- Supervised verifier upper bound

---

## Reviewer Score Breakdown

| Criterion | R1 | R2 | Consensus |
|---|---|---|---|
| Soundness | 3.5/5 | 3/5 | 3.25/5 |
| Novelty | 3/5 | 2.5/5 | 2.75/5 |
| Significance | 3.5/5 | 3/5 | 3.25/5 |
| Clarity | 4/5 | 4/5 | 4/5 |
| **Overall** | **4/6** | **4/6** | **4/6 (Weak Accept)** |

---

## Actionable Recommendations

**To reach score 5 (Accept):**
1. Add bootstrap CIs to Tables 1–2 for all signal comparisons
2. Add an MBR decoding discussion connecting SJ-based selection to established literature
3. Include at least a small-scale LLM-judge comparison or provide a principled argument for its exclusion
4. Specify SJ implementation details (matching threshold, voting matching criterion) precisely
5. Test selection with at least one alternative heuristic to rule out the consensus-proximity confound

**To reach score 6 (Strong Accept):**
All of the above, plus:
6. Second RE dataset (ACE05 or TACRED)
7. One N=32 or N=64 experiment to characterize scaling
8. Demonstrate correlation–selection gap on at least one non-IE task
9. Complete all planned figures (the correlation-selection gap visualization is critical)

---

## Meta-Assessment

This is a well-executed empirical study with one genuinely novel finding (the correlation–selection gap). The experimental matrix is thorough by comparison-paper standards, and the honest reporting of negative results is commendable. However, the limited methodological novelty (SJ is standard engineering), the narrow scope (8B models, entity-level IE only), and the missing connections to established frameworks (MBR decoding) prevent a confident accept. The paper would be strengthened most by (a) framing the selection gap as the headline contribution, (b) connecting to MBR literature, and (c) adding statistical rigor to the comparison tables. In its current form, it is borderline for a main conference track and well-suited for a Findings track.