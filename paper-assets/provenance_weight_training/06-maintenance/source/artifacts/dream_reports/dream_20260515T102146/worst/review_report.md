---
dream_id: dream_20260515T102146
tier: worst
overall_score: weak reject
timestamp: 2026-05-15T11:19:20.649443+00:00
---

# Dream Review Report

**Paper**: "When Less Cleaning Hurts: An Empirical Study of Adaptive Importance Weighting for Contaminated Pretraining"
**Review Mode**: Full (2 Reviewers + Roundtable)
**Venue Standard**: Top ML venue, ~25% acceptance rate, 6-point scale

---

## Reviewer Assignments

- **R1**: Methods & Experiments
- **R2**: Novelty, Related Work & Significance

---

## R1 Assessment: Methods & Experiments

**Summary.** The paper proposes dual-constrained and ESS-only adaptive b* selection for detect-and-reweight pretraining, then presents extensive ablations showing ESS-only (max-intervention) uniformly outperforms the dual-constrained variant (min-intervention). The experimental coverage is broad but the most critical comparison (ESS-only vs dual) lacks multi-seed validation, and effect sizes are at the noise floor throughout.

**Strengths**

- S1: **Comprehensive ablation suite.** The paper covers τ sweep, n_min sensitivity, batch size, contamination ratio (ρ=0.4/0.6), detector quality, cross-generator transfer, domain-skewed injection, model scale, and multiple baselines (detect-and-remove, random reweight, Golden Ratio oracle). This is thorough for an empirical study.
- S2: **Honest framing as negative finding.** The paper does not hide that the dual-constrained formulation — its original contribution — fails. Pivoting to "ESS-only is the practical recommendation, α_eff is a cautionary finding" is intellectually honest.
- S3: **Seed variance calibration.** Establishing the 0.005 PPL seed variance from 3-seed uniform baseline and using it as a yardstick throughout is good practice.
- S4: **The τ sweep (Table 6) is well-executed.** Monotonic PPL increase from τ=0.5 to τ=0.95 with α_eff binding percentage rising from 5% to 89% cleanly demonstrates that α_eff is uniformly harmful at AUC=0.939.

**Weaknesses**

- W1 (Critical): **ESS-only vs dual is single-seed.** The paper's central claim — ESS-only outperforms dual by 0.015 PPL — rests entirely on seed 42. Table 2 provides multi-seed for uniform/grid-best/dual but not ESS-only. With seed variance of 0.005–0.007, the 0.015 gap is 2–3× seed std, which is suggestive but not conclusive without multi-seed confirmation. This is the most important comparison in the paper and it lacks the statistical rigor applied to secondary comparisons.
- W2 (Major): **Effect sizes at noise floor.** The best non-oracle improvement over uniform is 0.055 PPL (0.31% relative) at 0.6B scale. At 3B scale, it shrinks to 0.020 PPL (<0.2% relative). Downstream metrics (MMLU, HellaSwag) show no distinguishable improvement. The paper acknowledges this in Limitations but the entire experimental edifice rests on differences that may not matter in practice.
- W3 (Major): **Missing ESS-only at ρ=0.6.** Table 9 compares only uniform, dual adaptive, and grid b=0.5 at ρ=0.6. ESS-only — the paper's recommended method — is absent from the higher-contamination evaluation. The review context confirms ESS-only at ρ=0.6 was planned but not executed. This is a significant gap given that dual underperforms grid-best at ρ=0.6.
- W4 (Major): **α_eff definition ambiguity.** Equation (2) defines α_eff using a hard indicator 1[q_i < 0.5]. However, the continuous formulation α_eff(b) = Σw_i·(1-q_i)/Σw_i (no hard threshold) is equally natural and avoids an arbitrary cutoff at 0.5 for an imperfect detector. The paper does not discuss this choice or compare alternatives, yet it is load-bearing: the hard threshold determines which samples are "borderline" and thus drives the entire negative finding about α_eff preserving noisy samples.
- W5 (Moderate): **n_min operating range is knife-edge at batch_size=4.** Table 7 shows only n_min ∈ {1, 2} produce meaningful results; n_min ≥ 3 degenerates to uniform. This means the "only hyperparameter" has exactly one working value at the default batch size. The paper's rule of thumb (n_min/|B| ≤ 0.5) is post-hoc and untested at larger batch sizes.
- W6 (Moderate): **Grid-b low multi-seed missing.** The extended grid (b=0.1–0.3) is seed-42 only. The fixed-b curve shape (and thus the claim that ESS-only's mean b*=4.15 outperforms globally-optimal fixed b=0.5) could look different under other seeds.
- W7 (Minor): **No learning curves or training dynamics.** All results are final PPL. How does the adaptive b* behave over training? Does it stabilize? Drift? The per-batch adaptation is the method's core mechanism, yet its temporal behavior is never shown.

**Questions for Authors**

- Q1: Can you provide 3-seed results for ESS-only? This is the minimum needed to support the central claim.
- Q2: What is the ESS-only PPL at ρ=0.6? If ESS-only also underperforms grid-best at ρ=0.6, the practical recommendation collapses.
- Q3: What happens with n_min=2 at batch_size=32 or 64? Is the method robust at realistic training configurations?
- Q4: Have you considered a continuous α_eff formulation without the hard 0.5 threshold? If α_eff were defined continuously, would the negative finding still hold?

**R1 Preliminary Score**: 3/6 (Weak Reject)
**Confidence**: 4/5

---

## R2 Assessment: Novelty, Related Work & Significance

**Summary.** The paper replaces Drayson et al.'s validation-based grid search over b with per-batch adaptive b* using two textbook quantities (Kish's ESS and a weighted real-fraction metric). The core conceptual contribution — contrasting minimum vs maximum intervention — is genuine, and the negative finding (α_eff hurts under noisy detection) is useful. However, the novelty is narrow (automating a single scalar in an existing formula), important related work in importance sampling is missing, and the small effect sizes limit practical impact.

**Strengths**

- S1: **Min-intervention vs max-intervention is a genuine conceptual contribution.** The distinction between b* = inf{b : α_eff ≥ τ} and b* = max{b : ESS ≥ n_min} formalizes an important design choice. The empirical finding that max-intervention wins is non-obvious and practically useful.
- S2: **The negative finding has community value.** Demonstrating that "clean enough" constraints backfire under imperfect detection challenges conventional wisdom about conservative data curation. The detector-quality interaction (Table 5: harmful at AUC=0.939, inert at AUC=0.986) provides a clear mechanistic explanation.
- S3: **Lightweight detector sufficiency.** TF-IDF+LR (trainable in 2 minutes) providing most of the benefit is a practical finding that lowers the barrier to adoption.
- S4: **Paper is well-structured and clearly written.** The progression from main results → negative finding → sensitivity analyses → discussion is logical. Tables are informative and well-labeled.

**Weaknesses**

- W1 (Major): **Narrow novelty over Drayson et al.** The weighting formula w=(1-q)^b, the detect-and-reweight paradigm, and the overall framework are all from Drayson et al. The paper's contribution reduces to: (a) replace grid search with a 1D bisection combining Kish's ESS (1965) and a weighted fraction, and (b) use loss reweighting instead of SIR. Contribution (b) is a standard implementation choice. Contribution (a) is useful engineering but not a methodological advance. The adaptive b* algorithm is ~7 lines of pseudocode.
- W2 (Major): **τ insensitivity paradox.** The τ sweep shows PPL range of only 0.040 across τ ∈ [0.5, 0.9]. While presented as evidence that α_eff is harmful, it equally suggests that α_eff is inconsequential — the constraint barely matters regardless of τ. If removing α_eff only buys 0.010–0.015 PPL, the entire negative finding is about a negligible effect. This undermines both the dual-constrained formulation (it barely matters) and the negative finding about it (the thing that doesn't matter also doesn't hurt much).
- W3 (Major): **Significance limited by effect sizes.** The best improvement is 0.055 PPL at 0.6B scale with 40% controlled contamination — an aggressive setting. At realistic scales (3B) and natural contamination, the effect would likely vanish. No downstream task improvement is demonstrated. A practitioner reading this paper would reasonably conclude: "the effect is too small to bother implementing."
- W4 (Major): **Missing importance sampling literature.** The ESS constraint is Kish's effective sample size (1965), not cited. The connection to self-normalized importance sampling, Pareto Smoothed Importance Sampling (Vehtari et al., JMLR 2024), and ESS-constrained importance weighting in off-policy RL (Precup et al., 2000; Munos et al., 2016) is absent. AIOLI (Chen et al., ICLR 2025) — online adaptive data mixing without grid search — is the closest "no grid search" comparator and is not discussed. Self-paced learning (Kumar et al., 2010) and curriculum learning (Bengio et al., 2009) are methodological antecedents for adaptive per-sample weighting. These omissions make the contribution appear more novel than it is.
- W5 (Moderate): **"Zero tuning cost" is overstated.** The method replaces one hyperparameter (b) with two (τ, n_min) in the dual case, or one (n_min) in ESS-only. At batch_size=4, n_min=2 is the only working value. Calling this "zero-tuning" stretches the definition. A fixed b=0.5 (no adaptive machinery, no bisection overhead, no n_min sensitivity) achieves PPL 17.651 vs ESS-only's 17.635 — a 0.016 difference that may not justify the added complexity.
- W6 (Moderate): **Claims about "unknown proportion" advantage are untested.** The paper claims the method works without knowing ρ, which is true but trivial — uniform training also doesn't need ρ. The interesting question is whether the method's advantage scales with ρ, and the ρ=0.6 results (dual underperforms grid-best) suggest it does not.

**Questions for Authors**

- Q1: How does ESS-only compare to simply setting b=0.5 universally? The 0.016 PPL gap seems small relative to the added algorithmic complexity.
- Q2: Have you considered the connection to off-policy RL importance sampling, where ESS-constrained weighting is standard? How does this work position against that literature?
- Q3: The AIOLI framework (Chen et al., ICLR 2025) eliminates grid search for data mixing via online optimization. How does your approach compare conceptually and empirically?
- Q4: At what contamination rate and model scale would you expect the effect to become practically meaningful (e.g., >0.5% relative PPL improvement)?

**Missing Related Work**

- Kish, L. (1965). Survey Sampling — foundational source for ESS.
- Vehtari, A. et al. (JMLR 2024). PSIS — ESS diagnostics in importance sampling.
- Chen, M. et al. (ICLR 2025). AIOLI — online adaptive mixing without grid search.
- Off-policy RL importance weighting (Precup et al., 2000; Munos et al., 2016).
- Self-paced learning (Kumar et al., 2010) / Curriculum learning (Bengio et al., 2009).
- MATES (Yu et al., NeurIPS 2024) — online adaptive instance-level selection.

**R2 Preliminary Score**: 3/6 (Weak Reject)
**Confidence**: 4/5

---

## Roundtable Discussion

### Step 2: Cross-Sharing

R1 shared with R2: The ESS-only single-seed problem, the missing ρ=0.6 ESS-only experiment, and the n_min knife-edge at batch_size=4. R2 agreed these are critical experimental gaps that compound the novelty concern.

R2 shared with R1: The τ-insensitivity paradox (if α_eff barely matters regardless of τ, the negative finding is about a negligible effect), the missing importance sampling literature, and the narrow novelty over Drayson et al. R1 agreed that the significance concern is fundamental — even if all experimental gaps were filled, the effect sizes may be too small to matter.

### Step 3: Convergence

**Points of agreement (both reviewers):**
1. The paper is well-written and honest about limitations — this is a strength.
2. The ESS-only vs dual comparison lacks multi-seed validation — this is the most critical experimental gap.
3. Effect sizes are at or near the noise floor, especially at 3B scale and on downstream tasks.
4. The α_eff definition (hard threshold at 0.5) is questionable and underdiscussed.
5. The contribution is incremental over Drayson et al. — automating one hyperparameter using standard importance sampling diagnostics.
6. The paper would be better suited as a short/findings paper than a full paper at a top venue.

**Points of partial disagreement:**
- R1 sees the τ sweep as a clean demonstration of α_eff's harm; R2 sees the same data as showing α_eff is inconsequential (the paradox). **Resolution**: Both interpretations are valid and reflect the same underlying issue — the absolute magnitudes are too small for either interpretation to be strongly compelling.
- R2 is more critical of novelty; R1 is more critical of experimental rigor. **Resolution**: These are complementary weaknesses that both need addressing.

### Step 4: Final Consensus

**Overall Score: 3/6 (Weak Reject)**
**Confidence: 4/5**

---

## Consolidated Assessment

### Summary

The paper studies adaptive per-batch exponent selection for detect-and-reweight pretraining under synthetic contamination. It compares a dual-constrained formulation (quality floor + stability ceiling) against a simpler ESS-only formulation (stability ceiling only), finding that the quality floor constraint (α_eff) is harmful under imperfect detection and inert under strong detection. The recommended ESS-only adaptive b* eliminates grid search and outperforms fixed-b baselines. The paper is well-written and honest, but the contribution is incremental, effect sizes are marginal, and the central comparison lacks multi-seed validation.

### Key Strengths

1. **Honest negative finding with mechanistic explanation.** The α_eff → detector noise → borderline sample preservation chain is clearly articulated and empirically supported by the detector quality interaction (Table 5).
2. **Comprehensive ablation coverage.** τ, n_min, batch size, ρ, detector quality, model scale, cross-generator, domain-skewed, and multiple baselines are all examined.
3. **Clear practical recommendation.** ESS-only with n_min=2 is simple and actionable.
4. **Good experimental practice.** Seed variance calibration, oracle upper bound, random reweight sanity check.

### Key Weaknesses

1. **Central claim is single-seed (Critical).** The ESS-only vs dual gap (0.015 PPL) — the paper's primary finding — is reported only for seed 42. Multi-seed results exist for secondary comparisons (Table 2) but not for the most important one.
2. **Effect sizes are marginal (Major).** Best improvement: 0.055 PPL (0.31%) at 0.6B/ρ=0.4. At 3B: 0.020 PPL (<0.2%). No downstream metric improvement. These magnitudes are unlikely to matter in practice.
3. **Narrow novelty over Drayson et al. (Major).** The contribution is automating one hyperparameter (b) using Kish's ESS (1965) — a textbook quantity. The formula, paradigm, and weighting scheme are all from prior work. Important connections to importance sampling literature (PSIS, off-policy RL, propensity scores) are missing.
4. **ESS-only missing at ρ=0.6 (Major).** The recommended method is not evaluated at higher contamination, where dual already underperforms grid-best. This is a critical gap.
5. **n_min knife-edge (Moderate).** At batch_size=4, only n_min=2 works. The "zero-tuning" claim is undermined when the hyperparameter has one viable value.
6. **α_eff definition uses arbitrary hard threshold (Moderate).** The 1[q<0.5] indicator in Eq. (2) is unmotivated for an imperfect detector and undiscussed.

### Experiment Coverage Assessment

The paper covers most planned experiments from the design document. Key gaps:
- **ESS-only multi-seed**: Not reported (critical)
- **ESS-only at ρ=0.6**: Not reported (major)
- **Low-b grid multi-seed**: Not reported (minor)
- **Training dynamics / b* evolution over training**: Not reported (minor)

### Recommendation

**Weak Reject.** The paper addresses a relevant problem and is executed with care, but it falls below the bar for a top ML venue full paper on three grounds: (1) the novelty is incremental — one scalar automated with a textbook diagnostic; (2) the effect sizes are too small to demonstrate practical impact; and (3) the central finding lacks multi-seed statistical support. The work would be well-suited as a **short paper or findings paper** focusing on the ESS-only practical heuristic and the negative finding about minimum-intervention principles under noisy signals. To strengthen for a full paper: provide multi-seed ESS-only results, evaluate ESS-only at ρ=0.6, test at batch_size ≥ 32, connect to importance sampling literature, and demonstrate meaningful downstream task improvement at scale.

### Actionable Suggestions for Revision

1. Run ESS-only with seeds {42, 123, 456} and report in Table 2.
2. Add ESS-only to the ρ=0.6 comparison (Table 9).
3. Test n_min sensitivity at batch_size ≥ 32 to show the method works beyond the knife-edge regime.
4. Add a training dynamics figure showing b* distribution evolution over training steps.
5. Cite and connect to Kish (1965), PSIS, AIOLI, and off-policy RL importance weighting literature.
6. Discuss the α_eff hard threshold choice (Eq. 2) and compare against a continuous formulation.
7. Consider reframing as a short/findings paper with tighter claims matched to the evidence.
