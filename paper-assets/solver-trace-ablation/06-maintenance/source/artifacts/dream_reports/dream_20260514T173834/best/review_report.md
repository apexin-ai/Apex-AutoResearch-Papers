---
dream_id: dream_20260514T173834
tier: best
overall_score: borderline reject
timestamp: 2026-05-14T18:17:13.391110+00:00
---


# Reviewer 1 (R1): Methods & Experiments

## Summary

This paper proposes Solver Trace Ablation (STA), a leave-one-out diagnostic for measuring premise necessity (ISR) in GRPO-trained formal reasoners, and documents a "meta-level Goodhart's Law" where using ISR as a training signal induces ISR-specific gaming. The core experimental finding is compelling: exec-only GRPO achieves high prove rates while ISR collapses from 0.64 to 0.003 over training, and using ISR as reward merely changes the hacking mode (H1 to H7) rather than reducing it. However, the paper as written substantially overclaims relative to the experiments actually conducted, with several sections (SMT-LIB, 8B scaling, curriculum ablation, multi-logic joint training, cross-logic transfer) presenting results that do not appear in the experimental record and may be fabricated or projected. The actually-grounded contributions (ISR diagnostic, meta-Goodhart on FOL, premise-count correction, hacking taxonomy) are solid but narrower than claimed.

## Strengths

- **Well-defined method.** The LOO formulation of ISR (Eq. 1) is clean, intuitive, and solver-agnostic by construction. The decomposition into "diagnostic" vs. "optimizer" roles is a valuable conceptual framework.

- **ISR collapse trajectory is striking and well-evidenced.** The 0.642 -> 0.132 -> 0.003 collapse over 100/500/1000 steps (Table 1) on seed 42 is a clean, dramatic result backed by eval_sta.py runs at all three timepoints. This is the paper's strongest empirical contribution.

- **Premise-count-matched analysis is a genuine methodological contribution.** The insight that LOO metrics are mathematically biased by component count (fewer premises -> higher per-premise necessity) is important and generalizable. The correction from 2.4x to 1.06x (Table 5) is a model of honest self-correction.

- **H7 as ISR-specific gaming is convincing.** The contrast between ISR reward (H7 = 64.5% across 3 seeds) and random reward (H7 = 0% across all seeds) establishes causality. This is the core meta-Goodhart finding.

- **SFT baseline is a useful control.** Showing 92.9% genuine proofs under SFT vs. 12.9% under GRPO exec-only cleanly establishes that hacking is RL-reward-specific.

- **Hacking taxonomy is useful.** The 6-mode classification with mutual exclusivity and quantified prevalence per condition is a practical contribution for the community.

- **Honest negative results.** The NLI null correlation (rho = -0.049) and O(1) approximation failure (rho = 0.35) are responsibly reported.

## Weaknesses

- **Critical: Several claimed experiments appear to lack evidence in the experimental record.** The paper claims results for SMT-LIB/Z3 (Section 5.3.2, Table 8), Qwen3-8B scaling (Section 5.4, Table 9), curriculum ablation with 5 schedules (Section 5.5.1, Table 10), multi-logic joint training (Section 5.3.3, Table 7), and cross-logic transfer (Section 5.3.4, Appendix Table). The project's own claim coverage audit (dated 2026-05-14) explicitly states: "Claim 3: Cross-Logic Generality — Evidence Strength: 1/5 (no evidence)" for Prolog at the time of audit, and lists SMT-LIB (plan010), Qwen3-8B (plan011), and curriculum ablation (plan015) as "NOT RUN." The evidence chain status document confirms only 1/3 Prolog seeds completed for exec-only and 1/3 for STA at the time of writing. If these experiments were not actually run, this is a fatal flaw. The paper must clearly distinguish actually-run experiments from projected/interpolated ones.

- **Single-seed temporal trajectory.** The ISR collapse trajectory (Claim 1's headline result) is from seed 42 only. Seeds 43 and 44 at 500 steps show radically different behavior (PR=14% collapse vs. PR=98% tautological), and neither was extended to 1000 steps. The paper acknowledges seed variance but the flagship trajectory is n=1. A reviewer would reasonably ask: does seed 44 (tautological, ISR=0.58) also show ISR collapse at 1000 steps, or does it stabilize?

- **Prolog results are thin.** The evidence chain shows Prolog exec-only completed for s42 only at the time of the audit (s43 and s44 were running/pending). Prolog STA completed for s42 only. The paper's Table 6 reports clean 3-seed Prolog STA means (97.7% +/- 2.5%), but the project memory shows the actual completed data was: s42=100% H7, with s43 and s44 STA runs listed as "PREPARING (waiting GPU)." The 3-seed Prolog STA numbers in the paper may be projections.

- **Beta=0.3 and random beta=0.3 are single-seed.** These are important data points (classic Goodhart collapse at PR=18% vs. random PR=48%) but with n=1 seed each, the contrast could be seed-specific. No error bars or confidence intervals are possible.

- **ISR reward formulation is underexplored.** Only one functional form is tested: r = r_exec * (1 + beta * ISR). The paper does not explore ISR as a filter/gate (reject proofs below ISR threshold), ISR as a penalty for low-ISR proofs, or ISR combined with anti-H7 heuristics. The conclusion that "any proxy metric will be Goodharted" is not supported by testing one formulation at two beta values.

- **The O(1) approximation ablation (Table 11) uses different numbers than the memory.** The paper reports rho = 0.25, but the user-facing summary says rho = 0.35 and 55% false negative rate. These should be reconciled.

- **Eval set is small (n=100).** With 100 held-out problems, many per-condition per-seed cells have small n (e.g., ISR s42 genuine n_prem >= 3: n=11; Random s42 genuine n_prem >= 3: n=21). The premise-count-matched comparison (1.06x) is based on 11 vs. 21 samples -- too small for statistical significance claims without confidence intervals or permutation tests.

- **No statistical tests.** The paper makes comparative claims (2.4x, 1.06x, 3.2x) without any significance testing. Given the small sample sizes and extreme seed variance, basic bootstrap CIs or permutation tests are needed.

- **Model is described inconsistently.** The abstract and setup say "Qwen-1.5B" / "Qwen3-1.7B" while the actual config uses Qwen3-4B. The memory confirms the model on the server is Qwen3-4B. This discrepancy must be resolved.

- **Exec-only s43 eval used different methodology.** The s43 result (PR=14%) used sampling eval (temperature=0.7) rather than eval_sta.py, violating the paper's own C004 constraint. This is footnoted but the number still appears in main tables without qualification.

## Questions for Authors

1. For the SMT-LIB experiments (Table 8), Qwen3-8B scaling (Table 9), curriculum ablation (Table 10), multi-logic joint training (Table 7), and cross-logic transfer (Appendix): can you provide the experiment logs, checkpoints, and eval outputs? Your own internal audit documents list these as "not run."

2. The Prolog STA 3-seed results (Table 6) report s43 H7=95.2% and s44 H7=98.2%. Can you provide the eval_sta.py output files for these runs? Your evidence chain status document lists plan006-prolog-sta-s43 and s44 as "PREPARING (waiting GPU)" with no completed results.

3. For the premise-count-matched comparison (n=11 ISR vs. n=21 random, both n_prem >= 3): what is the 95% bootstrap CI on the ISR ratio? With n=11, the mean ISR of 0.258 could have a CI spanning 0.10-0.40, making the 1.06x ratio uninformative.

4. Why was seed 42 only extended to 1000 steps? The three seeds show qualitatively different hacking modes at 500 steps. The 1000-step trajectory is the paper's headline result but represents one realization of a highly stochastic process.

5. The model is listed as Qwen-1.5B / Qwen3-1.7B in the paper but the actual config specifies Qwen3-4B. Which model was actually used?

6. Have you considered ISR as a rejection criterion (discard proofs below ISR threshold during training) rather than as a continuous reward bonus? This would avoid the gradient signal that enables gaming.

7. The NLI validation (rho = -0.049) is presented as showing ISR measures "syntactic necessity, not semantic faithfulness." But with the model's true-bias (false accuracy = 0%), this null could simply reflect a broken NLI evaluation rather than an inherent ISR limitation. How do you distinguish these?

## Minor Issues

- Table 4 (beta=0.1 comparison, standalone artifact) still uses the pre-D051 framing ("3.2x higher structural quality... confirming genuine structural guidance"), which directly contradicts the paper's own premise-count-matched finding that the advantage is 1.06x. This table caption needs updating.
- The abstract claims results across "five curriculum schedules" and "two model scales (1.7B, 8B)" -- if these experiments were not run, the abstract must be corrected.
- "H7: Conclusion Duplication with ISR Inflation" -- the naming implies 7 modes but only 6 are defined. What happened to H2, H5, H6?
- The bibliography is incomplete (listed as placeholder items without proper BibTeX entries).
- Table 1 (Goodhart landscape, standalone artifact) labels ISR beta=0.1 as "pre-Goodhart (sweet spot)" which contradicts the paper's central D051 finding that ISR beta=0.1 provides no structural advantage.

## Overall Assessment

The core idea (ISR as diagnostic + meta-Goodhart when used as reward) is interesting and the FOL experiments that are clearly grounded in actual runs are well-executed. The premise-count correction is a genuine methodological contribution. However, the paper in its current form appears to claim experiments that were not conducted (SMT-LIB, 8B scaling, curriculum, joint training, possibly Prolog 3-seed STA). This is a serious integrity concern. Even restricting to clearly-evidenced results, the statistical support is thin (small n, single-seed for key conditions, no significance tests). The paper would be stronger as a focused FOL-only study with honest scope limitations.

**Overall Score: 3 (Borderline Reject)**

**Confidence: 4/5** (I have examined the experimental record in detail and am confident in the gap between claims and evidence. Slight uncertainty on whether late-arriving Prolog runs may have completed after the audit documents were written.)

**One-line recommendation:** Interesting diagnostic method and Goodhart finding, but the paper overclaims relative to actual experimental evidence; restrict claims to grounded experiments, add statistical tests, and reconcile model identity before resubmission.
