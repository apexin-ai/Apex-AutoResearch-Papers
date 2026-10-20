---
round: 10
overall_score: 3.0
timestamp: 2026-05-18T08:30:16.522602+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 10 Consolidated Review Report

**Paper**: "Valid but Vacuous: Reward Hacking in RL-Trained Formal Reasoning"
**Venue**: ACL ARR May 2026 (EMNLP 2026 commitment)
**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性/格式)
**Round**: 10 (fresh review)

---

## Summary

The paper investigates reward hacking in GRPO-trained formal reasoning systems using a leave-one-out ablation diagnostic called Solver Trace Ablation (STA). The core metric, Irreducible Solver Rate (ISR), measures the fraction of solver-input components whose removal breaks the proof. The paper reports two main findings: (1) ISR reliably distinguishes RL-trained outputs from SFT baselines as a diagnostic, and (2) when ISR is incorporated into the reward signal, models exploit it through predictable Goodhart collapse, producing nine categorized hacking modes. Experiments use Qwen3-4B on FOLIO (first-order logic NLI) with a cross-scale check on Qwen3-1.7B.

The paper addresses a timely question at the intersection of reward hacking and formal reasoning. However, significant issues remain in statistical rigor, scope-claim alignment, and presentation clarity after 10 rounds of revision.

---

## Strengths

**S1. Timely and well-motivated problem** [R1, R2 consensus]
Reward hacking in solver-backed RL is under-studied. The paper provides concrete evidence that structural diagnostics can themselves become optimization targets, a finding relevant to scalable oversight.

**S2. Systematic experimental design** [R1, R2 consensus]
Five seeds for the primary condition (β=0.1), four β values for dose-response, SFT and 100-step RL controls, cross-logic (Prolog) and cross-scale (1.7B) extensions. The experimental matrix is thorough for an empirical study.

**S3. Honest statistical reporting** [R1, R2 consensus]
The paper reports seed-level permutation p=0.26 as the primary statistic rather than the inflated CMH p<10⁻⁹, acknowledges the OR reversal (uncorrected 3.48 vs corrected 0.61), and appropriately hedges many claims. This level of statistical honesty is commendable.

**S4. Detailed hacking taxonomy** [R1, R2 consensus]
Nine categorized modes with deterministic classifiers and 50-sample manual validation. The taxonomy (especially H1 conclusion embedding, H7 tautology, H8 premise-subset) provides actionable diagnostics for practitioners.

**S5. Comprehensive appendix** [R1, R2 consensus]
12 pages of per-seed breakdowns, statistical details, and hacking mode definitions. Reproducibility is well-supported.

---

## Weaknesses

### Critical

**W1. §4.5 vs Limitations factual contradiction on 1.7B seed count** [R1-N1, R2 AGREE]
§4.5 describes the 1.7B experiment as "single seed" while Limitations states "three seeds per condition." This is a direct factual contradiction. If three seeds exist, the paper is guilty of selective reporting; if only one seed exists, Limitations contains a factual error. Either way, this undermines trust in the paper's data integrity.
*Action required*: Resolve the contradiction, update all relevant sections (§4.5, Table 1, Limitations) consistently, and if additional seeds exist, report their results.

**W2. RL-specific failure claim weakened by PR confound** [R1-N2, R2 partial AGREE]
C1 claims hacking is "RL-specific" based on SFT comparison, but SFT PR=13% vs RL PR=93%. The 100-step RL control (PR≈40%) partially addresses this, but the paper's Abstract and Introduction still frame the finding as RL-attributable without sufficient PR-level caveats. R2 notes the paper uses "consistent with" rather than "proves," but the framing in Abstract/Introduction remains stronger than the evidence supports.
*Action required*: Weaken Abstract/Introduction RL-specific framing; add explicit PR confound caveat to C1.

**W3. N-H=23% headline is uncorrected upper bound** [R1-N3, R2 AGREE]
Table 1 and Discussion §5 still present N-H=23% (uncorrected, from 3 seeds with available checkpoints) as the headline number. The corrected estimate across all 5 seeds is approximately 6%. This 4× discrepancy is not adequately surfaced in the main text. The OR reversal (3.48→0.61) further complicates interpretation.
*Action required*: Table 1 must display both uncorrected and corrected values; Discussion must lead with the corrected estimate or clearly frame the uncorrected value as an upper bound.

**W4. Scope-claim mismatch: title vs experimental range** [R1-W1, R2-W2 consensus]
The title "RL-Trained Formal Reasoning" implies generality across RL algorithms, model families, and formal reasoning tasks. The experiments cover one RL algorithm (GRPO), one model family (Qwen3), one dataset (FOLIO), and one logic (FOL, with a preliminary Prolog extension). R2 suggests narrowing to "GRPO-Trained Logical Formalizers"; R1 suggests at minimum validating the core diagnostic on one additional dataset.
*Action required*: Narrow title scope or add experimental evidence.

### Major

**W5. Limited methodological novelty** [R2-W1, R1 partial REBUT]
STA/ISR is standard LOO ablation applied to solver inputs. The Goodhart collapse when using it as a reward is, as R2 argues, a direct prediction from Goodhart's Law. R1 rebuts that ISR-specific phenomena (H7 absorbing state, OR=2.84 for tautology) are not trivially predictable. The reviewers agree that novelty lies primarily in empirical characterization rather than method innovation, but the paper does not frame itself this way.
*Divergence*: Excitement scores differ (R1: 3.5, R2: 2.5). R1 values the ISR-specific empirical findings; R2 considers the conceptual contribution incremental. This divergence is unresolved.
*Action required*: Reframe C2 in Abstract/Contributions as "empirical characterization of a predictable failure" rather than implying discovery.

**W6. Introduction overloads quantitative results** [R2-W3, R1 partial REBUT]
Four \paragraph{} blocks in Introduction front-load specific numbers (ISR*, PR σ, SFT PR, OR values). R2 rates this as major; R1 suggests downgrading to warning, noting ACL empirical papers commonly present numbers early. The reviewers disagree on severity but agree the Introduction reads more like a results summary than a motivation section.

**W7. Table 1 information overload** [R1, R2 consensus]
Table 1 mixes different seed counts (5/3/1), step counts (100/500), and scales (4B/1.7B) with a complex annotation system (†, ‡, ††, ★). Both reviewers recommend splitting into a primary FOL table and a supplementary cross-scale table.

**W8. Appendix Table 5 footnote error** [R1-W2, R2 AGREE]
Caption defines † as "sampling (T=0.7)" but the s43-500 row Notes column reads "†Greedy." This is a factual error.
*Action required*: Correct to "†Sampling (T=0.7)."

### Moderate/Warning

**W9. Hacking taxonomy boundary issues** [R1-W5, R2-W9]
H1 (conclusion embedding) and H7 (tautology) are arguably endpoints of a single spectrum. H8 (premise-subset) overlaps with H1. The paper lacks explicit classification priority rules and does not distinguish between robust modes (H1/H7/H8, observed across multiple seeds) and isolated observations (single-seed modes). Taxonomy has "inflation" risk.

**W10. ISR=0.75 for P→P tautology: derivation missing** [R2-Q6]
experiments.tex claims ISR=0.75 for P→P "by the LOO definition alone" but provides no derivation. For n=2 inputs, ISR can only be 0.5 or 1.0. ISR=0.75 requires n=4, but the paper does not explain how P→P generates n=4 components. Furthermore, empirical data shows ISR*=0.55 for H7-dominated seeds at β=0.2, inconsistent with the claimed 0.75.

**W11. §4.3 β presentation order** [R1, R2 consensus]
β values appear as 0.1→0.05→0.2→0.3 rather than ascending order. Both reviewers flag this as unnecessarily confusing.

**W12. Terminology inconsistency** [R2-W7, merged with v8-R1-N3]
"Genuine," "non-hacking," and "structurally sound" are used interchangeably. The title word "valid" is ambiguous between execution validity and logical validity in this domain. Needs disambiguation on first use.

**W13. Discussion/Conclusion too brief** [R2-W8]
12 lines total. Lacks broader implications for scalable oversight, actionable reward design recommendations, and connection to the wider Goodhart literature.

**W14. Contributions overcounting** [R2-W5]
Four contributions listed, but C2 (Goodhart dynamics) and C4 (taxonomy) substantially overlap; C3 (cross-logic) is an instance of C2. Consider consolidating to two core contributions.

### Minor

**W15. Multiple comparison correction not noted** [R1-W3, R2 partial REBUT]
Appendix Table 3 Fisher exact tests across 6+ comparisons without noting they are uncorrected. R2 argues core conclusions don't depend on p-value thresholds, but the caption should state this.

**W16. Training vs evaluation decoding mismatch** [R1, from R9]
GRPO trains with sampling; ISR evaluates with greedy decoding. Not discussed.

**W17. 'Valid' in title ambiguity** [R2-W7]
For formal logic reviewers, "valid" has a specific technical meaning (logical validity). The paper means "solver-verified." First use should disambiguate.

---

## Reviewer Consensus Points

1. **Overall Assessment: 3.0 (Findings)** — Both reviewers independently rate 3.0. The paper is a solid empirical study with useful diagnostics but falls short of main conference acceptance due to scope-claim mismatch, limited novelty, and unresolved statistical/factual issues.

2. **§4.5/Limitations contradiction is the most urgent fix** — Both agree this is a credibility issue that must be resolved before any submission.

3. **N-H headline needs correction** — Both agree Table 1 and Discussion should present corrected estimates alongside uncorrected values.

4. **Novelty is empirical, not methodological** — Both agree the paper should be reframed accordingly.

5. **Table 1 should be split** — Both agree the current format is overloaded.

6. **β values should be in ascending order** — Both agree.

---

## Reviewer Divergence

1. **Excitement** — R1: 3.5 (ISR-specific empirical findings have independent value), R2: 2.5 (Goodhart collapse is predictable, empirical contribution incremental). Unresolved. Director assessment: the divergence reflects a genuine tension — the phenomena are individually predictable but their specific manifestation (H7 absorbing state, nine-mode taxonomy) provides actionable value. The midpoint is reasonable.

2. **Introduction quantitative front-loading** — R1 considers this acceptable for ACL empirical papers (warning); R2 considers it a major issue. Recorded as major in this report with the caveat that ACL norms vary.

3. **R1's suggested references (MO-GRPO, Posterior-GRPO)** — R2 could not verify these exist and flagged potential hallucination risk. These references should NOT be added without independent verification.

---

## Questions for Authors

**Q1.** How many seeds were actually run for the 1.7B experiment? Provide the complete data for all seeds run.

**Q2.** What is the exact derivation of ISR=0.75 for P→P tautologies? What value of n produces this, and what are the n components?

**Q3.** Would you consider running the core ISR diagnostic (not the full Goodhart experiment) on one additional dataset (e.g., ProofWriter, PARARULE-Plus) to partially address the scope concern?

**Q4.** Has ISR been tested as a binary filter (reject if ISR < threshold) rather than a continuous reward signal? This is identified as a low-cost, high-value ablation.

**Q5.** The corrected N-H estimate is approximately 6% vs the uncorrected 23%. Which do you consider the more reliable estimate, and why?

---

## Missing References

**Confirmed missing (both reviewers agree)**:
- MR1: Uesato et al. (2022) — process vs outcome reward, directly relevant to reward hacking in reasoning
- MR2: Paulus et al. (2018) — ROUGE-reward gaming in summarization, early reward hacking evidence
- MR3: Langosco et al. (2022) — Goal Misgeneralization in Deep RL, theoretical framework for reward misalignment
- MR4: DeepSeek-Prover-V2 — recent large-scale formal reasoning system, relevant baseline context

**Unverified (do NOT add without checking)**:
- MR5: "MO-GRPO" (R1 suggestion) — R2 could not verify existence
- MR6: "Posterior-GRPO" (R1 suggestion) — R2 could not verify existence

**Previously suggested, status unclear**:
- MR7: Khalaf et al. (NeurIPS 2025) — reward hacking in code generation

---

## Overall Assessment

**Score: 3.0 — Findings**

The paper addresses a relevant problem and provides useful empirical evidence. The STA diagnostic and nine-mode taxonomy have practical value for practitioners working with solver-backed RL. Statistical honesty (reporting p=0.26 rather than inflated CMH) is commendable.

However, several issues prevent main conference recommendation:

1. **Credibility**: The §4.5/Limitations seed-count contradiction is a factual error that undermines trust.
2. **Scope**: Single model family + single dataset cannot support the current title's generality claim.
3. **Novelty**: The core insight (Goodhart collapse of a diagnostic-turned-reward) is predictable from first principles; the paper's value is in empirical characterization, but it is not framed this way.
4. **Statistical**: The N-H headline (23% uncorrected vs ~6% corrected) and OR reversal are inadequately surfaced in the main text.
5. **Presentation**: Table 1 overload, Introduction front-loading, terminology inconsistency, and brief Discussion reduce readability and impact.

The paper is suitable for Findings if the factual contradiction (W1) and headline number issue (W3) are resolved. For main conference, it would need either broader experimental scope or significantly tighter scope-claim alignment, plus reframing around empirical contribution.

---

## Dimension Scores (averaged across reviewers)

| Dimension | R1 | R2 | Avg |
|---|---|---|---|
| Soundness | 3.0 | 3.0 | 3.0 |
| Excitement / Novelty | 3.5 | 2.5 | 3.0 |
| Clarity | 3.0 | 3.0 | 3.0 |
| Reproducibility | 4.0 | 3.5 | 3.75 |
| Overall | 3.0 | 3.0 | **3.0** |

---

## Detailed Comments

### For Immediate Fix (pre-submission)
1. Resolve §4.5 vs Limitations seed-count contradiction (W1)
2. Correct Appendix Table 5 s43-500 footnote error (W8)
3. Provide ISR=0.75 derivation or remove the claim (W10)

### For Strengthening to Main Conference
4. Narrow title to match experimental scope, or add one more dataset (W4)
5. Reframe C2 as empirical characterization (W5)
6. Table 1: split into primary + supplementary (W7)
7. Table 1: display both uncorrected and corrected N-H values (W3)
8. Abstract/Introduction: weaken RL-specific framing, add PR confound caveat (W2)
9. Consolidate contributions from 4 to 2 (W14)
10. Expand Discussion/Conclusion (W13)

### For Polish
11. Reorder §4.3 β values ascending (W11)
12. Unify terminology to "non-hacking" throughout (W12)
13. Disambiguate "valid" on first use (W17)
14. Add missing references MR1-MR4 after verification (Missing References)
15. Note multiple comparison correction in Appendix Table 3 (W15)
16. Discuss training/evaluation decoding mismatch (W16)