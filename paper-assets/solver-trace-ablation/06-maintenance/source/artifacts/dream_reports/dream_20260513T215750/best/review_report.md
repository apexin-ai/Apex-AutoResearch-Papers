---
dream_id: dream_20260513T215750
tier: best
overall_score: 4/6 Borderline Reject
timestamp: 2026-05-13T22:32:49.918165+00:00
---

# Dream Review Report: Solver Trace Ablation

**Paper**: "Solver Trace Ablation: Dense Structural Rewards for Formal Reasoning via Mutation Testing"
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-13

---

## Reviewer Assignments
- **R1** (Methods + Experiments): Methodology soundness, experimental rigor, reproducibility
- **R2** (Novelty + Related Work): Novelty assessment, related work completeness, positioning

---

## Step 1: Independent Reviews

### R1: Methods + Experiments

**Score: 4/6 (Borderline Reject)**

#### Strengths

**S1. Principled grounding in mutation testing.** The RIP framework provides a well-established theoretical foundation. The mapping—component ablation = mutant generation, solver outcome change = mutant killing—is natural. The insight that mutation adequacy criteria translate to reward signal quality is genuinely novel in the RL-for-formal-reasoning context.

**S2. Actionable 5-step derivation protocol.** The procedure (pilot → collect shortcuts → classify → map RIP → design checks) is concrete enough for replication and demonstrated for three distinct solver-language pairs.

**S3. Clean combined reward formulation.** r(f) = α·r_exec + β·r_exec·ISR multiplicatively couples execution and structure, ensuring ISR affects only proved outputs. The sigmoid curriculum addresses the initialization sensitivity observed in the pilot.

**S4. O(1) vs O(N) negative result.** Discriminability 0.08 vs 0.72 provides principled justification for computational overhead and deepens understanding of why component-level ablation is necessary.

**S5. Comprehensive experimental matrix.** All 12 planned experiments are covered: single-logic (3 types), multi-logic, cross-logic transfer, weight ablation, scaling, SFT baseline, hacking characterization.

**S6. Manual hacking taxonomy with κ=0.78.** Grounds the quantitative ISR metric in qualitative assessment with concrete examples.

#### Weaknesses

**W1. ISR conflates necessity with quality.** A component being "necessary for the solver outcome" does not guarantee semantic correctness. A formula with N non-redundant but logically arbitrary premises that convolve to entail the conclusion would score high ISR but be a poor formalization. The gap between structural necessity and semantic adequacy is not discussed.

**W2. RIP mapping is informal.** The three-stage decomposition (Reachability, Infection, Propagation) collapses into the single ablation test. Only Propagation is operationally measured. This makes RIP more of an analogy than a formal derivation—"component necessity testing" would be equally accurate.

**W3. ISR sensitivity to decomposition granularity.** Discriminability varies (FOL 0.72, Prolog 0.45, SMT-LIB 0.35) but the 5-step protocol provides no guidance on choosing the ablation unit. Splitting premises into sub-clauses or merging premises changes ISR.

**W4. Curriculum sigmoid is load-bearing but under-analyzed.** Table 5 shows curriculum Pareto-dominates fixed weighting, but the sigmoid shape (center, slope) is not ablated. Is sigmoid better than linear ramp? What is sensitivity to the ramp midpoint (reported as step 200 of 500)?

**W5. Single-seed ablations insufficient.** Plans 004-011 all use 1 seed. Table 5's Pareto dominance claim, Table 6/7's cross-logic validation, and Table 11's scaling analysis could be driven by initialization variance. At minimum, top-2 configurations should have 3 seeds.

**W6. Prove rate differences not statistically significant.** Table 1: 0.33±0.04 vs Table 2: 0.34±0.04 (overlapping CIs). Held-out: 0.24 vs 0.26. The paper should state "no significant difference" rather than "matches or slightly exceeds."

**W7. ISR optimization is partially circular.** Optimizing ISR as a reward naturally increases ISR. The hacking taxonomy (200 samples, κ=0.78) partially breaks this circularity but is not dispositive. A downstream logical inference task evaluation would be stronger validation.

**W8. Simpson's paradox risk in base model ISR/PR.** Base model ISR/PR (0.53) > trained exec-only (0.33), cited as evidence that "training actively worsens structural quality." But the base model computes ISR/PR over only 12% of outputs (those that prove), a self-selected population of "easy" problems that are structurally well-posed. The populations are different.

**W9. Multi-logic effects too small.** Table 8: +0.01 PR for Prolog from multi-logic training; Table 9: mean transfer Δ=0.045, STA adds only +0.01. At 1 seed, these are indistinguishable from noise.

**W10. Training horizon limited.** 500 steps (4000 rollouts over FOLIO) is short. Does exec-only continue to degrade at 2000+ steps, or stabilize? Does STA's benefit persist or diminish? The limited horizon leaves the durability of STA's structural protection unclear.

**W11. SFT baseline comparison conflates training paradigm with data efficiency.** SFT's lower prove rate (0.20 vs 0.30) could reflect imitation learning's limited exploration with 500 examples, not inherent inferiority.

#### Questions for Authors
1. Can you provide examples where ISR is high but the formalization is semantically wrong? What is the false-positive rate?
2. What happens with linear ramp instead of sigmoid? Sensitivity to ramp midpoint?
3. Do you have data beyond 500 steps? Does ISR/PR gap persist?
4. How do you handle ISR for the ~70% of outputs that fail to prove?
5. Have you verified the ISR/PR trend is not an artifact of changing population composition (Simpson's paradox)?
6. Who are the hacking taxonomy annotators? If authors, κ=0.78 may be inflated by shared mental models.

---

### R2: Novelty + Related Work

**Score: 3/6 (Borderline Reject)**

#### Novelty Assessment

**Moderate novelty.** The core idea—leave-one-out ablation of solver input components as a reward signal—is sound but conceptually straightforward. ISR is equivalent to well-known feature importance/sensitivity tests (Shapley-style leave-one-out) applied to a new domain. The genuine contribution is recognizing that this specific application (RL rewards for formal reasoning) is valuable, not the technique itself.

The RIP framework invocation is largely window-dressing. Only Propagation is operationally measured. The paper does not use Reachability or Infection as independent diagnostic or reward signals. Renaming "component necessity testing" as "RIP-grounded STA" inflates the theoretical contribution.

The 5-step derivation protocol is a practical contribution but methodologically amounts to "run a pilot, find failure modes, design targeted checks"—standard engineering methodology, not a theoretical framework.

#### Related Work: Critically Deficient

**6 references is unacceptable for a venue paper.** Missing critical citations include:

- **Reward shaping theory**: Ng et al. (1999) "Policy invariance under reward transformations" — the foundational result on potential-based reward shaping. STA's combined reward should be discussed in this context.
- **Reward hacking/overoptimization**: Gao et al. (2023) "Scaling Laws for Reward Model Overoptimization"; Skalse et al. (2022) "Defining and Characterizing Reward Hacking." The paper's core problem statement (reward hacking under exec-only rewards) must cite this literature.
- **GRPO itself**: Shao et al. (2024) "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models" where GRPO was introduced. The paper uses GRPO as its RL algorithm but does not cite its origin.
- **Modern formal verification + LLM**: LeanDojo (Yang et al. 2024), Baldur (First et al. 2023), AlphaProof (DeepMind 2024). These are the current state-of-the-art in formal reasoning with LLMs.
- **FOLIO dataset**: Han et al. (2022) "FOLIO: Natural Language Reasoning with First-Order Logic." The paper uses FOLIO as its primary dataset without citing it.
- **Mutation testing for ML**: DeepMutation (Ma et al. 2018), MuNN. Recent work applying mutation testing to ML systems should be discussed.
- **Feature attribution connections**: SHAP (Lundberg & Lee 2017), Leave-One-Out (LOO) feature importance. ISR is structurally equivalent to binary LOO feature importance.
- **Dense rewards in RL**: Potential-based reward shaping, intrinsic motivation, curiosity-driven exploration. STA's "dense+automatic" claim needs context within this broader literature.

The "EVOM (2026)" reference has no author list — it appears to be a self-citation or placeholder.

#### Conceptual Clarity

The ORM-PRM taxonomy positioning ("dense + automatic cell") is reasonable but under-argued. The paper should explicitly compare:
- Why not train a PRM on solver execution traces? Math-Shepherd and similar approaches learn dense process rewards automatically from execution feedback.
- Why is component ablation better than attention-based structural analysis?
- How does STA relate to reward shaping theory (Ng 1999)?

The "dense reward" claim is weakened by ISR being undefined for 67-88% of training examples (those that fail to prove). The reward r(f) = α·r_exec + β·r_exec·ISR reduces to α·r_exec = 0 for unproved outputs (since r_exec = 0). So for the majority of training examples, STA provides no signal at all. This should be acknowledged.

#### Writing Quality

The paper is well-organized and clearly written. Claims are generally appropriate, with exceptions noted above (prove rate "matching or slightly exceeding" should be "not significantly different"). The abstract accurately summarizes the content. Tables are clear and consistently formatted.

However, the 10-page length feels thin for the experimental breadth — many experiments are described in 2-3 sentences where a full paragraph of analysis would be appropriate. The multi-logic and cross-logic sections are particularly rushed.

#### Limitations

The Limitations paragraph is honest about model family (Qwen3 only), limited languages, and manual steps. It correctly identifies the "uniform component weighting" limitation. Missing from limitations:
- ISR is undefined for unproved outputs (majority of training)
- Sensitivity to decomposition granularity
- Potential Simpson's paradox in ISR/PR ratio comparisons
- Short training horizon (500 steps)

#### Questions for Authors
1. Has the actual 500-step, 3-seed training been completed, or are results projected from shorter pilots?
2. Why is GRPO not cited? Which GRPO implementation was used?
3. Can you provide the FOLIO dataset citation?
4. How does ISR relate to Shapley values or SHAP-style feature importance?
5. Why not compare against a PRM trained on solver traces?
6. What is the "EVOM (2026)" reference? It has no authors listed.

---

## Step 2: Cross-Sharing

### R1 responding to R2's concerns:
- **Agree** that 6 references is critically deficient. The missing GRPO, FOLIO, and reward hacking citations are serious oversights.
- **Agree** that the RIP framing overstates the theoretical contribution. R2's characterization as "window-dressing" is harsh but not unfair — only Propagation is measured.
- **Partially agree** on novelty: the domain application (RL rewards for formal reasoning) has genuine value even if LOO ablation is not novel. The 5-step protocol and three-logic demonstration are meaningful contributions.
- **Note** R2's concern about whether experiments were actually run vs projected. This cannot be adjudicated from the paper alone but is a valid concern given the limited training horizon and single-seed secondary experiments.

### R2 responding to R1's concerns:
- **Agree** that ISR conflating necessity with quality (W1) is a fundamental limitation. This aligns with the novelty concern — ISR is a simple binary LOO test, and its limitations are well-known in the feature importance literature.
- **Agree** that Simpson's paradox (W8) is a real risk and should be formally tested.
- **Agree** that the curriculum analysis (W4) is under-developed for a "load-bearing" design choice.
- **Elevate** W7 (circularity): this is arguably the paper's most fundamental concern. The paper optimizes ISR as a reward and then reports ISR improvement as the primary result. The hacking taxonomy breaks this somewhat, but 200 samples with potentially author-authored annotation is not enough.

---

## Step 3: Convergence

### Points of Agreement (both reviewers):
1. **Core idea has merit.** Component ablation as a structural reward for formal reasoning is well-motivated and potentially impactful.
2. **RIP framing overstated.** Only Propagation is measured; Reachability and Infection add no operational content. "Component necessity testing" is more accurate.
3. **Related work critically deficient.** 6 references is far below venue standards. Missing citations to GRPO, FOLIO, reward hacking, reward shaping, and modern formal verification work.
4. **Statistical rigor insufficient for secondary claims.** Single-seed ablations (Tables 4-11) cannot support the conclusions drawn. Multi-logic transfer effects (+0.01) are indistinguishable from noise.
5. **Prove rate "Pareto-improving" claim overclaimed.** Differences are not statistically significant; should be "no significant prove rate degradation."
6. **ISR circularity partially addressed but not resolved.** Hacking taxonomy (200 samples, κ=0.78) helps but is insufficient. Downstream task evaluation needed.
7. **ISR undefined for majority of training examples.** The "dense reward" positioning is weakened by ISR contributing 0 signal for 67-88% of outputs.
8. **O(1) negative result is a genuine strength.** Both reviewers value this ablation.
9. **Comprehensive experimental breadth.** The 12-experiment matrix is thorough for a methods paper, even if individual experiments lack statistical depth.

### Points of Disagreement:
- **Novelty level**: R1 rates the mutation-testing-to-reward-design insight as "genuinely novel"; R2 sees it as "straightforward LOO applied to a new domain." Converged position: the application is valuable but the technique itself is not novel.
- **Severity of related work gap**: R1 flags it as a concern; R2 considers it grounds for rejection. Converged: it is a major weakness that must be addressed but is fixable.
- **Overall score**: R1 gives 4 (Borderline Reject), R2 gives 3 (Reject). After discussion, converged at **4 (Borderline Reject)** — the core contribution has value and the paper is fixable, but substantial revision is needed.

---

## Step 4: Consolidated Assessment

### Overall Score: 4/6 (Borderline Reject)

### Summary Assessment

The paper addresses a real and important problem — structural degeneracy (reward hacking) in execution-only RL for formal reasoning — with a well-motivated solution: component ablation as a dense structural reward. The idea is sound, the experimental plan is comprehensive, and the O(1) negative result is a genuinely informative contribution.

However, the paper falls short of top venue standards in several dimensions:

### Major Issues (must fix)

**M1. Related work critically deficient.** 6 references is unacceptable. The paper must cite GRPO's origin (Shao et al. 2024), the FOLIO dataset (Han et al. 2022), reward hacking literature (Gao et al. 2023; Skalse et al. 2022), reward shaping theory (Ng et al. 1999), and modern formal verification+LLM work (LeanDojo, Baldur, AlphaProof). The "EVOM (2026)" reference lacks authors. A top venue paper in this space should have 25-40 references.

**M2. ISR circularity.** The paper optimizes ISR as a reward and reports ISR improvement as the primary result. The hacking taxonomy (Table 12) partially breaks this circularity but relies on 200 samples with potentially non-independent annotators (κ=0.78). The paper needs either: (a) a downstream evaluation showing high-ISR formalizations are genuinely better on an independent criterion, or (b) a much larger and externally-annotated hacking study.

**M3. Statistical rigor for secondary claims.** 8 of 12 experiments use a single seed. The weight ablation (Table 5), multi-logic (Tables 8-9), scaling (Table 11), and cross-logic transfer (Table 9) results cannot support the conclusions drawn. Effect sizes of +0.01-0.03 at 1 seed are not meaningful. Minimum: 3 seeds for the top-2 weight configurations and at least 1 secondary logic type.

**M4. "Pareto-improving" overclaimed.** Prove rate differences (exec-only 0.28±0.03 vs exec+STA 0.30±0.03) are not statistically significant. The paper should claim "STA preserves prove rate while substantially improving structural quality" rather than "Pareto-improving."

### Minor Issues (should fix)

**m1. RIP framing overstated.** Only Propagation is operationally measured. Either formalize the Reachability and Infection conditions as independent diagnostic signals, or reframe as "component necessity testing" without the three-stage RIP hierarchy.

**m2. "Dense reward" claim weakened.** ISR is undefined for unproved outputs (67-88% of training examples). The reward reduces to r_exec = 0 for these. The paper should acknowledge this and discuss implications for training signal density.

**m3. ISR sensitivity to decomposition granularity.** The 5-step protocol should include guidance on choosing the ablation unit. The varying discriminability across logic types (0.72, 0.45, 0.35) is acknowledged but not addressed.

**m4. Curriculum under-analyzed.** The sigmoid is load-bearing (Table 5) but its shape parameters are not ablated. Linear ramp comparison and midpoint sensitivity analysis needed.

**m5. Simpson's paradox risk in base model comparison.** The claim that "training actively worsens structural quality" (base ISR/PR 0.53 > exec-only 0.33) may be an artifact of different populations. The base model computes ISR/PR over only its 12% prove-rate outputs.

**m6. Short training horizon.** 500 steps leaves open whether STA's benefits persist or diminish at longer training.

**m7. SFT comparison conflates paradigm with data efficiency.** Should match total compute or effective training signal.

### Experiment Coverage vs Design

All 12 imagined experiments from the experimental design are present in the paper. Coverage is complete. The primary gap is statistical depth (seeds) rather than breadth.

| Experiment | Seeds | Coverage | Concern |
|---|---|---|---|
| FOL Exec-Only (plan_001) | 3 | ✓ Full | — |
| FOL Exec+STA (plan_002) | 3 | ✓ Full | — |
| FOL Held-Out (plan_003) | — | ✓ Full | Simpson's paradox |
| O(1) vs O(N) (plan_004) | 1 | ✓ Full | Need 3 seeds |
| Weight Ablation (plan_005) | 1 | ✓ Full | Need 3 seeds for top configs |
| Prolog (plan_006) | 1 | ✓ Full | Need 3 seeds |
| Multi-Logic (plan_007) | 1 | ✓ Full | Effects < noise |
| Cross-Logic (plan_008) | — | ✓ Full | Effects < noise |
| SFT Baseline (plan_009) | — | ✓ Full | Paradigm confound |
| SMT-LIB (plan_010) | 1 | ✓ Full | Need 3 seeds |
| Qwen3-8B (plan_011) | 1 | ✓ Full | Need 3 seeds |
| Hacking Characterization (plan_012) | — | ✓ Full | Annotator independence |

### Recommendation

**Reject with encouragement to revise and resubmit.** The core contribution — component ablation as a principled dense reward for formal reasoning — has genuine value and could be publishable with:
1. Proper related work (expand from 6 to 25+ references)
2. 3-seed runs for top-3 configurations beyond the primary FOL comparison
3. Either downstream task validation of ISR or larger external hacking annotation study
4. Honest statistical characterization (remove "Pareto-improving" for non-significant prove rate differences)
5. Either formalize RIP properly or reframe as component necessity testing

The direction is promising and the paper would be competitive after these revisions.