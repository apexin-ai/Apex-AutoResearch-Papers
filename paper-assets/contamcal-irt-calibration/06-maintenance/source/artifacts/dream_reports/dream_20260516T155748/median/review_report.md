---
dream_id: dream_20260516T155748
tier: median
overall_score: 3/6 — Weak Reject
timestamp: 2026-05-16T16:48:16.321248+00:00
---


# Dream Review Report: ContamCal

## Paper Summary

ContamCal introduces a framework bridging benchmark contamination detection and characterization via contamination-augmented IRT. It adds per-benchmark effect parameters γ_k to a 4-parameter logistic IRT model, with item-level exposure scores computed through Reciprocal Rank Fusion of four detection signals (embedding similarity, Min-K++, ConStat, Self-Critique). Through controlled SFT injection on Qwen2.5 (0.5B–7B, N=24) and observational analysis up to 72B, the paper reports three main findings: (1) contamination effects are benchmark-dependent (ARC forgetting γ=−1.46 vs GSM8K near-immunity), (2) effects are scale-modulated (catastrophic at 0.5B, negligible at 7B+), and (3) Min-K++ exhibits directional reversal at small scales (Cohen's d=−1.98). Cross-family validation on Llama-3.2-3B shows directional consistency but lacks statistical significance (N=3). Calibration produces MAE=0.035 on ARC, competitive with but not superior to simple linear regression (MAE=0.040).

## Experiment Coverage

All six imagined experiments from the design document are present in the paper:
1. **QC Robustness (exp-015)** → Section 4.1: covered with matching tables ✓
2. **Scale Bridging 7B (exp-007)** → Section 4.2: covered with full dosage sweep ✓
3. **Cross-Family Llama (exp-014)** → Section 4.3: covered with 3 dosage levels ✓
4. **Observational RL Case Study (exp-009)** → Section 4.4: covered with 6 models ✓
5. **Frontier 72B Observation (exp-012)** → Section 4.5: covered ✓
6. **Closed-Weight 2-Signal Mode (exp-013)** → Section 4.6: covered ✓

Coverage is complete. No imagined experiment is missing.

---

## Detailed Review

### Strengths

**S1. Novel and well-motivated framework design.**
The idea of augmenting IRT with a continuous contamination exposure covariate (γ_k · τ_j) is a clean formalization that connects two previously disjoint literatures — contamination detection and psychometric evaluation. The adaptation from educational measurement's item compromise IRT to the LLM setting (single model → joint item distribution, binary leakage → continuous exposure, stable ability → regime-conditional ability) is thoughtful and well-grounded in prior work (Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004).

**S2. Structured heterogeneity finding is the paper's strongest contribution.**
The discovery that contamination effects are not uniform inflation but exhibit benchmark-dependence (ARC forgetting vs GSM8K immunity), scale modulation, and domain-level Simpson's paradox in MMLU is genuinely informative. This challenges the dominant "contamination = scores go up" narrative and has practical implications for how the community interprets contamination audits.

**S3. Min-K++ directional reversal is practically important.**
Demonstrating that Min-K++ doesn't merely fail but actively reverses direction at small scales (Cohen's d=−1.98 at 0.5B) is a valuable cautionary finding. The connection to MIA literature where membership signals degrade with model capacity (Shokri et al. 2017, Carlini et al. 2022) contextualizes this well. This has immediate practical implications: contamination audits relying solely on Min-K++ at small scales may reach opposite conclusions.

**S4. Fisher Information identifiability analysis provides useful guidance.**
The analytic derivation of I(γ_k) (Eq. 4) and the simulation sweep establishing N≥50 at AUC≥0.55 as minimum requirements give concrete, actionable thresholds. Framing this as a "structural domain-method mismatch" rather than merely "need more data" is the right characterization.

**S5. Commendable honesty about limitations.**
The paper transparently reports: calibration MAE is not superior to linear regression; 95% CIs achieve only ~50% empirical coverage (attributed to local independence violation via SBC); the framework is effectively S1-dependent; the gating criterion blocks calibration in most scenarios. This self-awareness is unusual and appreciated.

**S6. Good experimental breadth.**
Six experiments covering QC robustness, scale bridging, cross-family validation, observational case study, frontier scale, and closed-weight degradation provide a thorough characterization of the framework's capabilities and limitations.

### Weaknesses

**W1. The calibration contribution — half the paper's title — is underwhelming. [Major]**
The paper's title promises "calibration" but the actual calibration results are disappointing:
- MAE=0.035 vs linear regression MAE=0.040 — not statistically distinguishable, and the paper acknowledges this.
- 95% credible intervals achieve only ~50% empirical coverage — the uncertainty quantification, claimed as IRT's advantage, is fundamentally broken at practical N.
- The gating criterion blocks calibration in 5 of 6 experiments (all except ARC at 0.5B scale with controlled SFT). This means in practice, the framework almost never calibrates.
- At 7B+, calibration is unnecessary (effects below noise floor). At small N (<50), calibration is unreliable. The practical "sweet spot" where calibration is both needed and feasible is extremely narrow.

The paper discovers that the problem it set out to solve (calibrating contaminated scores) is either unnecessary or infeasible in most realistic settings. While intellectually honest, this undermines the core value proposition.

**W2. Single-family controlled experiments with underpowered cross-family validation. [Major]**
All controlled SFT experiments use only Qwen2.5. The Llama-3.2-3B cross-family experiment has N=3 models (3 dosage levels), far too few for any γ CI to exclude zero. The paper correctly calls this "preliminary directional evidence," but the consequence is that all significant results (ARC γ CI excludes zero) rest entirely on a single model family. This limits the generalizability of the characterization claims.

**W3. SFT contamination injection has limited ecological validity. [Major]**
The controlled experiments inject contamination via SFT on paraphrased benchmark items. Real-world contamination occurs during pre-training, with different dynamics:
- SFT on 7,547–16,697 items is a much stronger signal than incidental pre-training exposure across billions of tokens.
- SFT causes capacity displacement at small scales (the ARC "forgetting" may be an artifact of catastrophic forgetting from SFT fine-tuning, not contamination per se).
- The observational case study (Experiment 4) attempts to address this but achieves no significant results with N=6 heterogeneous models.

The paper should more carefully disentangle "contamination effects" from "SFT fine-tuning artifacts." The −17.5pp ARC drop at 0.5B with d100 looks more like catastrophic forgetting from aggressive fine-tuning than a contamination-specific effect.

**W4. The framework is effectively S1-only in practice. [Moderate]**
The 4-signal RRF architecture is principled in design but empirically S1-dominated:
- S2 (Min-K++): reverses direction, actively harmful
- S3 (ConStat): AUC=0.52, near-chance
- S4 (Self-Critique): AUC=0.48, near-chance
- RRF(all 4) ≈ S1 alone (AUC=0.979 vs 0.979)

The paper reports this honestly, but the "multi-signal fusion" contribution is architectural, not empirical. The closed-weight 2-signal mode (Experiment 6) confirms the framework collapses without embedding access, meaning it cannot evaluate the models users most need to audit (closed-weight API models like GPT-4, Claude).

**W5. Coverage collapse undermines the uncertainty quantification claim. [Moderate]**
The paper identifies IRT's advantage as "principled uncertainty quantification" over linear regression's bootstrap CIs. However, 95% credible intervals achieving only ~50% empirical coverage means the uncertainty estimates are systematically overconfident. The SBC diagnostic attributing this to local independence violation is helpful for diagnosis but doesn't fix the problem. If the CIs are miscalibrated, the posterior predictive p-value check in the gating criterion is also unreliable. This circularity is not discussed.

**W6. The N≥50 threshold is impractical and the paper doesn't bridge the gap. [Moderate]**
The Fisher Information analysis establishes N≥50 as the minimum for reliable γ recovery. The paper then demonstrates that the LLM evaluation domain typically has N=8–30 models, creating a "structural mismatch." But the paper offers no path to resolving this mismatch — it simply identifies it. Future work suggestions (scale to N≥50 models) would require an unrealistic number of controlled SFT runs. This makes the framework aspirational rather than practically deployable.

### Minor Issues

**M1.** Table 4 shows ARC forgetting at 7B is −0.9pp with γ=−0.35 (CI includes zero), but this is *larger in magnitude* than 3B (−0.3pp, γ=−0.50). The non-monotonic delta at 7B (-0.9 vs -0.3 at 3B) is not discussed. Is this within noise, or does it reflect something about the 7B architecture?

**M2.** The calibration formula θ̂^clean = θ̂ − γ̂_k · τ̄ (Eq. 3) uses the mean exposure score τ̄ rather than model-specific exposure. This assumes exposure is model-independent, which may not hold — different models may have been exposed to different subsets of benchmark items.

**M3.** The paper uses "calibration" in an unusual sense (decontamination, not probability calibration). While Section 6 briefly disambiguates, the potential for confusion with the dominant ML usage (Guo et al. 2017, Platt 1999) could cause misunderstandings. Consider a different term.

**M4.** The connection to Differential Item Functioning (DIF) in the Related Work is intriguing but underdeveloped. If γ_k is analogous to DIF parameters, the extensive DIF literature on detection and correction methods could provide additional baselines or theoretical grounding.

**M5.** No appendix or supplementary material with MCMC diagnostics (R-hat, ESS, trace plots). Given the coverage collapse issue, showing convergence diagnostics would strengthen confidence in the posterior estimates.

### Questions for Authors

1. How do you disentangle contamination-specific effects from generic SFT catastrophic forgetting at 0.5B? Would the same ARC forgetting occur if you SFT on random (non-benchmark) data at the same volume?

2. The coverage collapse is attributed to local independence violation. Have you tried relaxing this assumption, e.g., via testlet models or multidimensional IRT?

3. Given that calibration is unnecessary at 7B+ and unreliable at N<50, what is the intended practical use case for ContamCal calibration? Is the target audience researchers evaluating many small models?

4. The Qwen-3B γ for ARC is reported as −1.46 in Table 7 but −0.50 in Table 4. Table 7 header says "3B Scale" but the Qwen-3B γ value matches the 0.5B value from the abstract. Is this a reporting error?

## Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| Novelty | 6/10 | IRT+contamination covariate is a novel formalization; structured heterogeneity finding is new. But the IRT adaptation is relatively straightforward and the key insight (contamination effects vary) is intuitive once stated. |
| Rigor | 6/10 | Controlled experimental design is sound; Fisher Information analysis is solid. But single-family experiments, coverage collapse, and SFT-as-proxy-for-contamination limit rigor. Potential reporting error in Table 7. |
| Significance | 5/10 | The characterization findings (heterogeneity, Min-K++ reversal) are useful for the community. But calibration — the paper's primary application — is impractical in most settings and not better than linear regression where it does work. |
| Clarity | 7/10 | Well-written, well-structured, honest about limitations. Notation is clear. The 6-experiment structure provides good coverage. Minor: "calibration" terminology is confusing. |
| Reproducibility | 5/10 | N=24 controlled models on Qwen2.5 is reproducible in principle but expensive (~37.5 GPU-hours for 7B alone). No code or model checkpoints mentioned. MCMC diagnostics absent. |
| Overall | 3/6 | **Weak Reject** |

## Overall Assessment

ContamCal presents a novel framework with genuinely interesting characterization findings — the structured heterogeneity of contamination effects and the Min-K++ directional reversal are contributions the community should know about. The Fisher Information identifiability analysis adds useful theoretical grounding.

However, the paper's central applied contribution — contamination-aware calibration — is undermined by its own results. Calibration is unnecessary for large models (7B+), unreliable at practical N (<50), not superior to simple linear regression where it works, and produces miscalibrated uncertainty estimates (50% coverage at nominal 95%). The framework requires embedding access, precluding evaluation of closed-weight models. The controlled experiments rest on a single model family with SFT injection as a proxy for real contamination.

The paper would be stronger if it repositioned itself purely as a characterization framework (dropping the calibration claim from the title) and invested the calibration sections into deeper analysis of the structured heterogeneity findings — for instance, understanding *why* ARC exhibits forgetting while GSM8K is immune, or what drives the MMLU Simpson's paradox at the domain level. As it stands, the paper tries to deliver both characterization and calibration but the calibration half is weak, diluting the impact of the characterization half.

For a top ML venue with ~25% acceptance rate, the contribution is below the acceptance threshold. The characterization findings alone are interesting but incremental — they don't change how practitioners should evaluate models (the paper's own gating criterion blocks calibration in most cases). A revision addressing the calibration weakness, expanding cross-family evidence, and disentangling SFT artifacts from contamination effects could make this competitive.

**Recommendation: Weak Reject (3/6)**
