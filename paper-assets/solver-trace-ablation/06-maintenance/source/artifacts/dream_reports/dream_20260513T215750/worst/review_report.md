---
dream_id: dream_20260513T215750
tier: worst
overall_score: reject
timestamp: 2026-05-13T22:47:44.263037+00:00
---

# Dream Review Report: Solver Trace Ablation Reveals Reward Hacking in GRPO-Trained Formalizers

**dream_id:** 20260513T215750
**Review mode:** full (2-reviewer roundtable)
**Date:** 2026-05-13

---

## Roundtable Summary

Two reviewers independently assessed the paper, then cross-shared findings and converged on a unified assessment.

- **R1 (Methods & Experiments):** 3/6 (Weak Reject)
- **R2 (Novelty & Related Work):** 2/6 (Reject)
- **Consensus:** 2/6 (Reject)

---

## R1 Review: Methods & Experiments

### Summary

The paper proposes Solver Trace Ablation (STA), adapting mutation testing's RIP framework to derive structural rewards (ISR) for GRPO-trained formal logic generators. The core finding is a principled negative result: ISR effectively diagnoses structural degeneracy (~70% sensitivity) but fails as a training reward, reducing prove rate from 0.24 to 0.11 without improving structural quality. The experimental program covers 9 of 12 planned experiments.

### Strengths

- **Well-motivated problem.** Execution-only GRPO producing structurally degenerate formalizations (ISR/PR dropping 0.82→0.29) is a genuine and underappreciated failure mode, documented with clean training dynamics.
- **Honest negative result.** The paper does not overclaim. The exec+STA prove rate collapse (0.13 vs 0.28) is presented straightforwardly.
- **Informative O(1) vs O(N) ablation.** Near-zero discriminability for O(1) (0.02 vs 0.31) justifies the O(N) cost and shows hacking is multi-modal.
- **Systematic hacking taxonomy.** 200-sample annotation with 4 modes, κ=0.72, and ISR sensitivity ~70% grounds quantitative metrics in qualitative understanding.
- **Comprehensive weight ablation.** Six configurations demonstrating no stable operating point makes the negative conclusion convincing beyond poor hyperparameter choice.
- **SFT baseline provides useful calibration.** SFT dominating GRPO on all metrics (PR=0.30, ISR/PR=0.50, hack%=50%) raises important questions about paradigm choice.

### Weaknesses

- **(Major) Statistical power is insufficient.** 3 seeds for the primary comparison is borderline; 1 seed for all ablations (weight ablation, O(1) vs O(N), Prolog, cross-logic transfer) is inadequate. The weight ablation's "no stable operating point" conclusion could be a seed artifact. Top-2 configurations should be verified with ≥3 seeds.
- **(Major) Causal attribution of ISR/PR decline is unresolved.** The ISR/PR decline under exec+STA may be a punitive artifact of the 50/50 weighting rather than genuine hacking detection. The held-out evaluation partially addresses this, but the paper does not clearly separate "STA detects hacking" from "STA punishment suppresses proving."
- **(Major) ISR circularity.** ISR is used both as training reward and primary evaluation metric. The hacking taxonomy partially breaks this circularity, but no downstream task evaluation (e.g., does higher ISR correlate with better logical inference accuracy?) validates ISR as a proxy for structural quality.
- **(Major) Very limited scale.** Qwen2.5-1.5B on FOLIO with one functioning logic type (FOL). Prolog failed catastrophically. The "general, solver-agnostic" claim is unsupported empirically.
- **(Moderate) Three planned experiments not run.** Multi-logic GRPO (blocked by Prolog failure, reasonable), SMT-LIB and 8B scaling (deprioritized without strong justification). The absence of scaling analysis means the paper cannot distinguish whether the negative result is scale-specific.
- **(Moderate) Reward formulation may explain the negative result.** With r = α·r_exec + β·ISR and α=β=0.5, proved-but-low-ISR outputs get half the reward of exec-only. The model may simply learn that proving is not worth the effort. This is a reward engineering problem, not evidence that structural rewards are fundamentally incompatible with RL.

### Questions for Authors

1. Have you controlled for population composition effects in the held-out ISR/PR comparison? The base model computes ISR/PR over only its 12% proved outputs (self-selected easy population), while trained models prove different problems (Simpson's paradox risk).
2. Have you tried additive bonus formulations (r = r_exec + bonus·ISR) that provide upside without reducing the incentive to prove?
3. Who performed the hacking taxonomy annotation? Were guidelines developed independently of ISR scores?

### R1 Scores
- Soundness: 2/4
- Empirical Rigor: 2/4
- Reproducibility: 3/4
- Overall: 3/6 (Weak Reject)
- Confidence: 4/5

---

## R2 Review: Novelty & Related Work

### Summary

The paper adapts leave-one-out component ablation to RL reward design for formal logic generation, framed through mutation testing's RIP model. The negative result (STA fails as training reward) is the central finding. The paper has only 4 references and claims novelty for what is operationally LOO feature importance applied to a new domain.

### Strengths

- **Genuine problem identification.** Structural degeneracy under execution-only GRPO is real and underappreciated.
- **Principled negative result framing is honest.** Reporting failure with mechanistic explanation reflects intellectual integrity.
- **Hacking taxonomy is the most concrete contribution.** Four hacking modes with differential ISR sensitivity and κ=0.72 provide a reusable categorization.
- **SFT comparison contextualizes findings.** SFT dominating GRPO calibrates what "good" structural quality looks like.

### Weaknesses

- **(Major) ISR is leave-one-out ablation importance, not a novel metric.** ISR(f) = (1/N)·Σ 1[S(f\c_i) ≠ S(f)] is structurally identical to binary LOO feature importance, a technique with decades of history (Cook's distance 1977, SHAP 2017, permutation importance). The paper does not acknowledge this connection. Presenting ISR as novel inflates the contribution.
- **(Major) RIP framework invocation is cosmetic.** Only Propagation is operationally measured. Reachability and Infection contribute no independent signal. The three-stage decomposition collapses into a single binary test. "Component necessity testing via LOO ablation" would be equally accurate and less misleading.
- **(Major) Only 4 references is critically deficient.** A paper spanning RL, formal verification, mutation testing, reward hacking, and neurosymbolic reasoning should have 25-40 references. Critical omissions include:
  - FOLIO dataset (Han et al. 2022) — the paper's own dataset is uncited
  - Reward shaping theory (Ng et al. 1999) — directly relevant to the combined reward formulation
  - Modern formal verification + LLMs (LeanDojo, AlphaProof, Baldur, COPRA)
  - Process reward models (Math-Shepherd, Lightman et al. 2023)
  - Feature attribution literature (SHAP, Shapley values)
  - CodeRL, RLTF — structural rewards in code generation
  - Broader mutation testing literature beyond the single Jia & Harman citation
  - RLHF reward hacking mitigation approaches
- **(Major) The 5-step derivation protocol is standard engineering methodology.** "Run a pilot, observe failures, categorize, map to framework, design checks" is what any competent practitioner would do. This has reproducibility value but is not a methodological contribution.
- **(Moderate) The negative result may be predictable.** Adding a noisy, sparse reward component (ISR, defined only for ~15% of outputs) to an already sparse signal would be expected to degrade training by any RL practitioner familiar with reward shaping. The gradient variance amplification explanation is essentially "adding noisy reward to sparse reward makes training harder" — a known phenomenon.
- **(Moderate) Scope too narrow for claimed generality.** Single model, single logic type, failed extensions. One successful instantiation does not validate a "general, solver-agnostic procedure."

### Questions for Authors

1. How do you differentiate STA from LOO ablation applied as a reward signal? Have you considered interaction effects (pairs of components jointly encoding trivial reasoning)?
2. Is the ISR component potential-based (Ng et al. 1999)? If not, what guarantees adding ISR does not systematically bias the learned policy?
3. What makes the negative result non-obvious given that adding high-variance reward to sparse signal is known to degrade training?
4. Why not compare against a random structural penalty as a control? Without this, it's unclear whether ISR's specific formulation matters.

### R2 Scores
- Novelty: 2/4
- Related Work: 1/4
- Significance: 2/4
- Writing Quality: 3/4
- Overall: 2/6 (Reject)
- Confidence: 4/5

---

## Roundtable Convergence (Step 3)

### Points of Agreement

1. **Hacking taxonomy is the strongest contribution.** Both reviewers identify the 200-sample annotation with 4 hacking modes and differential ISR sensitivity as the paper's most concrete and reusable empirical finding.
2. **Single-logic, single-model scope is a major limitation.** The paper claims solver-agnostic generality but demonstrates STA successfully on exactly one solver-language pair.
3. **Honest framing is a genuine strength.** Reporting a negative result without overclaiming is appreciated by both reviewers.
4. **Statistical rigor is borderline.** R1 flags 1-seed ablations as insufficient; R2 notes this compounds the scope concern.
5. **The negative result's non-obviousness is not established.** R1 notes the reward formulation itself may explain the failure; R2 notes the result is predictable from reward shaping literature.

### Points of Complementary Concern

- R1 identifies ISR circularity (optimizing and evaluating on same metric) — R2 independently identifies ISR as LOO importance (not novel). Together: the metric is both unvalidated and unoriginal.
- R1 flags causal attribution issues in the held-out comparison — R2 flags the "dense" positioning as misleading since ISR is undefined for 75-88% of outputs. Together: the diagnostic claims rest on shaky empirical and conceptual foundations.
- R2's identification of 4 references as critically deficient is a standalone disqualifying issue that R1's experimental concerns reinforce: the paper lacks engagement with the literatures needed to contextualize its claims.

### Consensus Recommendation

Both reviewers converge on **reject** (consensus score: 2/6). The paper addresses a genuine problem and the hacking taxonomy has value, but the combination of:
1. Critically deficient related work (4 references)
2. Overstated novelty (LOO ablation presented as RIP-grounded framework)
3. Narrow experimental scope (single logic, single model, failed extensions)
4. Insufficient statistical rigor (1-seed ablations)
5. Unresolved causal attribution and metric circularity

places the paper below the acceptance threshold for a top ML venue.

---

## Synthesis & Recommendations (Step 4)

### Overall Assessment: 2/6 (Reject)

The paper tackles a real problem—reward hacking in GRPO-trained formalizers—and proposes STA, a component ablation framework for deriving structural rewards. The principled negative result (STA fails as training reward but works as diagnostic) is honestly reported. However, the paper has fundamental issues across novelty, experimental scope, and scholarly completeness that prevent acceptance.

### What Would Improve This Paper

1. **Related work expansion (critical).** Expand from 4 to 25+ references with substantive engagement. Cite FOLIO, engage with reward shaping theory (Ng et al. 1999), LOO/feature attribution literature, modern formal verification + LLMs, process reward models, and structural rewards in code generation.

2. **Honest repositioning of ISR.** Acknowledge ISR as domain-specific LOO ablation rather than claiming novelty through cosmetic RIP grounding. The contribution is applying a known technique to a new domain—frame it that way.

3. **At least one additional successful STA instantiation.** SMT-LIB/Z3 or another solver-language pair to support the "general, solver-agnostic" claim. Without this, the 5-step protocol remains aspirational.

4. **Statistical rigor.** Run top-2 weight configurations with ≥3 seeds. A single seed cannot distinguish systematic failure from bad initialization.

5. **Break ISR circularity.** Validate ISR against a downstream task (e.g., logical inference accuracy) to establish it measures structural quality rather than its own optimization surface.

6. **Alternative reward formulations.** Test additive bonus (r = r_exec + bonus·ISR) and random penalty controls to isolate whether ISR's specific formulation matters versus any regularization of proved outputs.

7. **Establish non-obviousness.** Engage with reward shaping theory to argue why the negative result is surprising, or reframe the paper around the hacking taxonomy as the primary contribution with the negative result as supporting evidence.

### Strengths Worth Preserving

- The hacking taxonomy (4 modes, κ=0.72, differential ISR sensitivity) is the paper's most publishable component. A reframed paper centered on "Characterizing Reward Hacking in GRPO-Trained Formalizers" with the taxonomy as the primary contribution and STA as the analysis tool could be stronger.
- The SFT vs GRPO comparison revealing that GRPO's on-policy exploration amplifies solver shortcuts is a genuinely interesting finding.
- The observation that the untrained base model has better structural quality (ISR/PR=0.53) than both GRPO-trained models is striking and deserves more attention.

### Key Risks for Claims

| Claim | Evidence Strength | Key Risk |
|-------|------------------|----------|
| STA as diagnostic framework | Moderate | ISR circularity; LOO is not novel; one logic type only |
| STA as training reward fails | Moderate-Weak | May be reward engineering failure, not fundamental; 1-seed ablations; predictable from theory |
| Hacking taxonomy | Moderate-Strong | 200 samples is modest; annotation may not be blind to ISR; κ=0.72 is adequate but not strong |

### Experimental Coverage Assessment

9 of 12 planned experiments appear in the paper. Plan_007 (multi-logic GRPO) was reasonably blocked by Prolog failure. Plans 010 (SMT-LIB) and 011 (8B scaling) were deprioritized—the absence of scaling analysis is the most consequential gap, as it prevents distinguishing scale-specific from fundamental limitations.
