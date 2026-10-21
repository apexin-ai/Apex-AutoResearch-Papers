---
dream_id: dream_20260514T203201
tier: worst
overall_score: weak reject
timestamp: 2026-05-14T21:36:15.969887+00:00
---

# Dream Review Report: "Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation–Selection Gap"

**dream_id:** 20260514T203201  
**Review mode:** full (2 Reviewers + Roundtable)  
**Venue standard:** Top ML venue, ~25% acceptance rate, 6-point scale

---

## Reviewer Assignments

- **R1** — Methods + Experiments (Score: 4→3 after discussion)
- **R2** — Novelty + Related Work (Score: 3, held)

---

## Step 1: Independent Reviews

### Reviewer R1 (Methods + Experiments)

**Initial Score: 4 (Weak Accept), Confidence: 4**

#### Strengths

- **S1. Clean conceptual contribution.** The quality estimation vs. sample selection disentanglement is crisp and practically important. The "correlation–selection gap" is a useful concept that clarifies why high correlation does not imply selection utility.
- **S2. Comprehensive experimental coverage.** 2×2 model–dataset matrix, 3-seed robustness, N=8/16 scaling, temperature ablation, per-relation diagnostics, capability stratification, LOO circularity check, ensemble analysis, OOD robustness — 17 experiments fully executed. Few papers achieve this level of completeness.
- **S3. Honest negative results.** WNUT-17 failure mode reported transparently. RE weakness acknowledged head-on. Best-of-N failure on NER is the central finding rather than buried.
- **S4. Practical utility.** Actionable guidance for practitioners: log-probability provides comparable quality estimation at zero extra cost; multi-sample generation not justified for fine-tuned models unless log-probs are unavailable.

#### Weaknesses

- **W1 (Major). Best-of-N protocol structurally biased against instance-level signals; gap explanation is near-tautological.** Instance-level signals (SJ, voting, FK, EM) assign the same score to all N samples from one input — they *cannot* rank among candidates by construction. The paper presents this as an empirical discovery when it is closer to a definitional property. The real question — whether per-sample variants of structural signals (e.g., LOO-SJ per sample as a ranking signal) could enable selection — is never tested. LOO-SJ is computed only for circularity checking, not as a selection signal. This is a significant missed opportunity.
- **W2 (Major). Single RE dataset with severe floor effects.** 44% of SciERC RE instances receive F1=0. All RE-specific claims rest on this single dataset. A second RE dataset (TACRED, DocRED) would substantially strengthen conclusions.
- **W3 (Moderate). Task-difficulty gradient conflates multiple variables.** The difficulty gradient (CoNLL easy → SciERC hard → WNUT infeasible) simultaneously varies domain, schema complexity, text style, and model capability. Unclear which variable drives observed effects.
- **W4 (Moderate). Uneven statistical rigor.** No bootstrap CIs reported for main Table 1 comparisons. Only 3 seeds. No paired bootstrap or Williams' test for comparing dependent correlations. Fisher z-test on overlapping NER/RE instances violates independence assumption.
- **W5 (Minor–Moderate). Potential method section discrepancies.** FK described as token-level but may be implemented as entity-level. SJ formula in paper may be oversimplified relative to implementation. These cannot be verified from the paper alone.
- **W6 (Moderate). N=8 may underestimate structural signals.** RE SJ improves from 0.21→0.28 at N=16. Larger N (32, 64) not explored. Negative selection results may be N-dependent.
- **W7 (Moderate). Ensemble analysis superficial.** No hybrid strategy tested (structural filtering + logprob ranking). No learned combination with cross-validation.

#### Questions for Authors
1. Have you tested per-sample variants of structural signals (LOO-SJ_i, per-sample voting score) for best-of-N selection?
2. How would practitioners perform conditional filtering (excluding zero-F1 instances) at deployment without gold labels?
3. For instance-level signals, does best-of-N selection reduce to random among tied candidates, or do you use closest-to-consensus? The protocol is unclear.
4. How sensitive are results to fine-tuning quality? Would stronger base models change signal rankings?

---

### Reviewer R2 (Novelty + Related Work)

**Score: 3 (Weak Reject), Confidence: 4**

#### Strengths

- **S1. Quality estimation vs. selection disentanglement is well-executed.** Clean separation of two objectives conflated in prior work.
- **S2. Comprehensive related work.** Well-organized into self-consistency, structured IE, and uncertainty/calibration threads. Positioning against Nédellec & Xia (2026) is explicit and fair.
- **S3. Honest negative results.** WNUT-17 analysis reported transparently as a capability boundary.
- **S4. Task-difficulty-dependent signal ranking.** EM > SJ on CoNLL but SJ > EM on SciERC provides actionable, nuanced guidance.

#### Weaknesses

- **W1 (Major). Correlation–selection gap is near-tautological.** An instance-level signal c(x, {y_i}) → ℝ produces one number per input; it *cannot* rank N candidates by construction. The conceptual contribution reduces to: (a) instance-level signals can't rank samples (definitional), and (b) logprob helps on RE but not NER (a single empirical observation). Neither alone meets the novelty bar for a top venue.
- **W2 (Major). Insufficient differentiation from Nédellec & Xia (2026).** SJ is a straightforward extension of Jaccard similarity to entity sets. The best-of-N analysis yields a negative result that is partly predetermined (W1). Multi-domain evaluation is valuable but incremental. The paper reads as "Nédellec & Xia + better metrics + negative selection result."
- **W3 (Major). No proposed solution or path forward.** Paper identifies the gap and stops. Pure negative-result papers need either (a) a very surprising negative result, or (b) deep mechanistic understanding enabling future solutions. The explanation here is shallow — it does not explain why consensus-closest selection fails, whether per-sample structural signals could work, or what properties a successful selector would need.
- **W4 (Moderate). Ambiguous positioning.** Caught between "systematic comparison" and "novel finding." Systematic comparisons are typically Findings-level unless they reveal unexpected phenomena.
- **W5 (Major). Missing MBR decoding connection.** MBR decoding — selecting argmax_i Σ_j SJ(y_i, y_j) — is the natural per-sample adaptation of instance-level SJ. This converts an instance-level signal into a per-sample ranking. If MBR-with-SJ fails, that's a much stronger negative result. If it succeeds, it resolves the gap. Omitting this connection is a significant gap in both the experimental design and the related work (Eikema & Aziz 2020, 2022; Freitag et al. 2022, 2023).
- **W6 (Minor). "Logprob paradox" is well-known.** High AUROC + low ρ from bimodal score distributions is standard in calibration literature (Guo et al. 2017). Presenting it as novel overstates the contribution.

#### Questions for Authors
1. Did you try MBR decoding with SJ as the utility function? This is the natural per-sample adaptation of your best instance-level signal.
2. For oracle-selected samples, are they structurally different from consensus (suggesting consensus-based selection is fundamentally wrong) or close but slightly better (suggesting finer discrimination is needed)?
3. Within-stratum correlations "approach zero" — can you provide actual numbers and CIs?

---

## Step 2: Cross-Sharing

### R1 Response to R2

**Points of agreement:** Strong convergence on the tautological gap (both W1s). R2's MBR omission point (W5) is "the most impactful new concern" — "If the authors had run MBR-with-SJ, the paper would be substantially stronger regardless of outcome." Agreement on no-solution weakness.

**Points of disagreement:** R1 considers R2 too harsh on differentiation from Nédellec & Xia — the multi-domain evaluation and task-difficulty-dependent signal ranking represent nontrivial work. R1 disagrees that ambiguous positioning (R2-W4) is a serious standalone weakness.

**Score revision:** R1 revised from **4 → 3 (Weak Reject)**. The convergence on the tautological gap plus R2's MBR omission point tipped the assessment.

### R2 Response to R1

**Points of agreement:** Strong agreement on tautological gap, statistical rigor issues, single RE dataset, and missing hybrid strategies. R1's specific critique about Fisher z-test on overlapping instances is valid.

**Points of disagreement:** R2 considers R1 too generous on related work positioning and on the initial score of 4. R1's own identified weaknesses (tautological design W1, uneven statistics W4) should have prevented acceptance from the start. R1 also understates the "logprob paradox" issue.

**Score:** R2 held at **3 (Weak Reject)**. R1's review surfaced additional technical concerns (method discrepancies, Fisher z-test) that reinforce the assessment.

---

## Step 3: Convergence

Both reviewers converged to **3 (Weak Reject)** with confidence 4.

**Consensus strengths:**
1. Well-executed empirical comparison with commendable breadth (2 models × 2+ datasets × 5 signals × multiple ablations)
2. Honest treatment of negative results; WNUT-17 reported transparently
3. The quality estimation vs. selection distinction is practically useful
4. Task-difficulty-dependent signal ranking is a genuine empirical contribution

**Consensus weaknesses (ordered by severity):**
1. **(Critical) Tautological core finding.** The correlation–selection gap, as presented, is partly a consequence of signal definition rather than an empirical discovery. Instance-level signals cannot rank by construction; the paper never tests per-sample structural variants that could resolve or sharpen the finding.
2. **(Critical) Missing MBR decoding.** MBR with SJ as utility is the natural bridge between instance-level signals and per-sample selection. Its absence is a major experimental design gap.
3. **(Major) No proposed solution.** Pure negative result without deep mechanistic insight or preliminary remedy. The oracle headroom (+15pp NER, +19pp RE) is tantalizingly large but receives no investigation.
4. **(Major) Insufficient differentiation from Nédellec & Xia (2026).** Structural metrics are straightforward extensions; the best-of-N negative result is partly predetermined by the tautological gap.
5. **(Moderate) Statistical rigor.** Missing CIs for main comparisons, only 3 seeds, invalid Fisher z-test on overlapping instances.
6. **(Moderate) Single RE dataset with severe floor effects.** 44% zero-F1 instances limit RE conclusions.

---

## Step 4: Meta-Review & Recommendation

### Overall Assessment

This paper presents a thorough empirical comparison of five unsupervised confidence signals for LLM-based information extraction, covering NER and RE across two models and two primary datasets. The experimental breadth (17 experiments, N-scaling, temperature ablation, cross-model validation, OOD analysis) is commendable, and the honest treatment of negative results is a credit to the authors. The practical guidance — that log-probability provides comparable quality estimation at zero extra inference cost — is useful for practitioners.

However, the paper's central novelty claim, the "correlation–selection gap," is undermined by a structural issue in the experimental design: the tested instance-level signals *cannot* perform per-sample selection by definition. Both reviewers independently identified this as near-tautological. The natural resolution — MBR decoding, which converts instance-level SJ into a per-sample ranking — is neither tested nor discussed, despite being the standard approach in the structured prediction literature. This omission means the paper's headline claim ("self-consistency fails for structured prediction") is both overstated and undertested.

The differentiation from Nédellec & Xia (2026) is incremental: structural metrics over surface matching, with a negative selection result that is partly predetermined. The paper proposes no solution to the identified gap, and the mechanistic explanation is shallow. Statistical rigor is uneven, with missing confidence intervals for key comparisons and methodological concerns about the Fisher z-test on overlapping instances.

The work has merit as a systematic comparison and would be appropriate for a **Findings** track, where the comprehensive evaluation and practitioner guidance would be valued. For the main conference, the novelty bar is not met: the core insight is partly definitional, the most relevant experimental variant (MBR) is untested, and no path toward closing the gap is offered.

### Recommendation

**Score: 3 (Weak Reject)**  
**Consensus: Reject for main track; recommend resubmission to Findings**

### Key Revisions for Resubmission

1. **Test MBR decoding with SJ as utility function.** This is the single highest-impact addition. If MBR-SJ fails, the negative result becomes genuinely strong. If it succeeds, the paper gains a positive contribution.
2. **Test per-sample structural signal variants** (LOO-SJ_i, per-sample voting score) for best-of-N selection.
3. **Add a second RE dataset** to validate RE-specific conclusions beyond SciERC's floor effects.
4. **Report bootstrap CIs** for all main comparisons (Table 1) and use appropriate tests for dependent correlations.
5. **Connect to MBR decoding literature** (Eikema & Aziz 2020/2022, Freitag et al. 2022/2023).
6. **Soften the title and framing.** "Self-consistency fails" overstates — it works for quality estimation. The gap is specifically about selection with instance-level aggregates.

### Experiment Coverage Assessment

The paper covers all 17 planned experiments from the design document:
- Baseline comparisons (exp-012 to exp-014): ✓ Table 1
- Metrics expansion (exp-015): ✓ Tables 1–2
- N=16 scaling (exp-001, exp-008): ✓ Table 4
- CoNLL-2003 (exp-002): ✓ Table 2
- WNUT-17 (exp-003): ✓ Reported despite abandonment
- RE diagnostics (exp-004): ✓ Table 7
- Temperature (exp-005): ✓ Table 5
- Best-of-N (exp-006): ✓ Table 6
- Cross-model LLaMA (exp-007): ✓ Table 3
- Capability stratification (exp-009): ✓ Table 8
- Selection curves (exp-010): ✓ Section 5.6 text
- OOD robustness (exp-011): ✓ Table 9
- Signal ensemble (exp-016): ✓ Section 5.6
- LLaMA×CoNLL (exp-017): ✓ Table 3

Coverage is comprehensive. The main gap is not in experiment coverage but in experimental *design* — the missing MBR variant and per-sample structural signals.
