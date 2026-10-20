---
dream_id: dream_20260521T122444
tier: best
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T13:11:14.585065+00:00
---

# Review Report: Detecting Benchmark Contamination from Binary Response Patterns via IRT Person-Fit Statistics

## Meta Information
- **Venue**: EMNLP 2026 (via ARR)
- **Format**: Long paper (7 pages content + 1 page references = 8 pages total, within limit)
- **Review Mode**: Simple (single reviewer, full coverage)

---

## Summary

The paper repurposes IRT person-fit statistics (ℓz*) for LLM benchmark contamination detection, requiring only binary (correct/incorrect) response patterns and externally calibrated 4PL item parameters from PSN-IRT. Controlled contamination experiments (QLoRA SFT at 0–50% on MMLU) across four model families (Qwen, Llama, Mistral, Gemma) show |d| > 2.9 at 15% contamination. The headline result is that ℓz* retains 77% of its signal after GRPO post-training, while the simpler HT statistic collapses to 20% retention and all MIA/log-probability methods fall to chance. Additional contributions include a 4PL vs. 3PL ablation, a power function across 7 benchmarks (R²=0.97), domain-level contamination typology, multiscale aggregation (ℓz_m), and the empirical finding that 57/60 model-benchmark cells show universal 4PL misfit.

---

## Scores

| Dimension | Score |
|-----------|-------|
| **Soundness** | 3.5 / 5 |
| **Excitement** | 3.5 / 5 |
| **Reproducibility** | 3.5 / 5 |
| **Overall Assessment** | 3.5 — Borderline Conference |

---

## Strengths

**S1. Novel and well-motivated minimal-information framing.** No existing contamination detection method operates at the binary-response-only level. The paper clearly positions IRT-FIT on the information axis (binary < rephrased retest < token probs < full logits < training data) and shows it is competitive with methods requiring strictly more information. This is a genuine conceptual contribution.

**S2. Post-RL robustness is timely and compelling.** The finding that ℓz* retains 77% signal (d: −3.42 → −2.65) after GRPO while HT collapses (d: 3.21 → 0.65) and MIA methods fall to chance (AUROC ≈ 0.50) directly addresses Wang et al. (2025). The mechanistic explanation — binary response patterns are invariant to the token-distribution shifts GRPO induces — is clean and persuasive. This is the paper's strongest differentiation.

**S3. Experimental breadth is impressive.** 10 tables across 7 pages covering: 4 model families × 6 contamination levels, post-RL evaluation, 7-benchmark power analysis, 4PL/3PL/2PL ablation, 6 baselines, domain-level analysis, multiscale aggregation, base-to-chat natural experiment, and IRT refit negative result. For a single paper, this is unusually thorough.

**S4. θ-fixed analysis is a methodological contribution.** Demonstrating that fixing θ to the clean baseline recovers monotonic dose-response (Qwen free-θ: non-monotonic; θ-fixed: ratio 3.12) addresses a real confound. This also rescues detection for small benchmarks (ARC-C: d from 0.65 → 2.05).

**S5. 4PL ablation is decisive.** The 357-unit divergence for DeepSeek-V3 between 4PL and 3PL ℓz* is striking. 46% of MMLU items having d < 0.95 means the feasibility parameter is structurally necessary, not a refinement. The FAR inflation (3PL: 4.7–16.5% vs. 4PL: 5.0%) and power loss (−27pp MMLU) make the case quantitatively.

**S6. Honest reporting of negative results.** The IRT refit failure (r_a = 0.127, Section 6.4), universal misfit finding (Section 6.1), and item-level near-random AUROC (0.53–0.63) are reported transparently. This increases trust in the positive results.

---

## Weaknesses

**W1. Post-RL claim rests on a single model at a single contamination level (Major).** The headline post-RL result (Tables 3–4, Section 5.2) is based exclusively on Qwen2.5-7B at 15% contamination. For the paper's central differentiating claim ("the only binary-only method surviving post-RL"), this is thin. Different model families may show different retention patterns — e.g., Llama's lower baseline misfit might yield different ℓz*/HT retention dynamics under GRPO. At minimum, replicating on Llama (for which an SFT-contaminated model presumably already exists from the controlled experiments) would substantially strengthen this claim.

**W2. Total dependence on PSN-IRT parameters with no sensitivity analysis (Major).** The framework is a single-point-of-failure pipeline: if PSN-IRT's 4PL parameters are systematically biased (e.g., discrimination estimates skewed for certain item types), all downstream ℓz* values are affected. The paper acknowledges this dependency but does not test sensitivity. A perturbation analysis — adding ±10–20% noise to a/b/c/d parameters and measuring detection degradation — would be straightforward and would quantify how robust the method is to parameter imprecision.

**W3. Small n (=3) for Cohen's d with no confidence intervals (Moderate).** All d values are computed with n=3 clean seeds (ddof=1). At this sample size, d estimates have wide uncertainty: for d=−3.42, a rough 95% CI spans approximately [−6.5, −1.0]. The paper reports d to 2 decimal places without CIs or formal significance tests (p-values), creating a false impression of precision. Bootstrap CIs or at minimum noting the uncertainty range would be appropriate.

**W4. Clean baseline requirement severely limits real-world applicability (Moderate).** The Δℓz* framework requires ≥3 clean seeds from the same model family. For the models practitioners most want to audit (GPT-4, Claude, Gemini — all closed-source production models), clean versions are unavailable. The Practical Deployment discussion (Section 7) acknowledges this but offers no mitigation. This means IRT-FIT is currently limited to auditing open-weight models where users can train clean baselines — a narrower use case than the Introduction implies.

**W5. Only QLoRA SFT contamination tested (Moderate).** Real-world contamination often occurs through pretraining data inclusion or continued pretraining, which may produce more diffuse memorization patterns than QLoRA SFT. SFT is known to produce sharp, targeted parameter changes — the detection signal may be weaker for pretraining contamination where item exposure is diluted across billions of tokens. The Limitations section mentions this but does not discuss expected degradation.

**W6. Accuracy z-score comparison is not adequately addressed (Minor).** The acc z-score achieves d=160.6 on Qwen — nearly 50× larger than ℓz*'s d=3.42. The paper dismisses it as "non-specific" (any performance change triggers it), but if the practical goal is binary contamination detection and clean baselines are already available (as required by IRT-FIT), why not just compare accuracy? The paper needs a concrete example or analysis showing a scenario where ℓz* flags contamination that accuracy misses — e.g., contamination that doesn't substantially change overall accuracy but alters response patterns.

**W7. HumanEval anomaly unexplained (Minor).** Table 5 shows HumanEval simulated power (0.243) exceeding theoretical power (0.120), a gap of −0.123 in the opposite direction from all other benchmarks. This is not discussed anywhere in the text.

**W8. Tables 3 and 4 are largely redundant (Minor).** Both present post-RL baseline comparisons with overlapping columns (method, info, d_SFT, d_RL, retention). Consolidating would free space for CI reporting or additional analysis.

---

## Questions for Authors

1. **Post-RL replication**: Do you have SFT-contaminated Llama/Mistral models from the controlled experiments? If so, why not run GRPO on at least one to replicate the post-RL finding?

2. **Parameter sensitivity**: How does detection degrade if PSN-IRT parameters are perturbed? Even a simple simulation (add Gaussian noise to a_i with σ = 0.2× true value) would be informative.

3. **Accuracy vs. ℓz***: Is there a realistic scenario where contamination changes response patterns (triggering ℓz*) without meaningfully changing accuracy (not triggering acc z-score)? If so, that would be the strongest motivation for ℓz* over the trivially powerful accuracy comparison.

4. **Confidence intervals**: Can you provide bootstrap CIs for the d values in Table 1, or at least report the clean seed variance more prominently so readers can assess uncertainty?

5. **HumanEval**: What explains the reversed theory-simulation gap in Table 5?

---

## Experiment Coverage Assessment

Comparing against the full experiment plan (review_context.yaml):

| Experiment | Status in Paper |
|------------|----------------|
| Controlled Contamination Pilot | ✅ Covered (Section 4) |
| Full Controlled Contamination (4 families) | ✅ Table 1, Section 4.2 |
| Leaderboard Audit v1 | ✅ Acknowledged as abandoned; data availability noted (Section 7) |
| Base→Chat Natural Experiment | ✅ Table 10, Section 6.5 |
| v1 IRT Refit (N=178) | ✅ Table 9, Section 6.4 |
| 4PL vs 3PL Ablation | ✅ Table 2, Section 4.4 |
| Baseline Comparison (≥5) | ✅ Tables 3–4, Section 5.1 |
| Multiscale ℓz_m | ✅ Table 8, Section 6.3 |
| Post-RL Hypothesis Test | ✅ Table 4, Section 5.2 |
| Extra Benchmarks (BBH + MATH) | ✅ Table 5, Section 5.3 |
| Domain Analysis | ✅ Table 7, Section 6.2 |

All 11 planned experiments are present. Coverage is comprehensive.

---

## Formatting & Compliance Checks

- **Page limit**: 7 pages content + references on pages 7–8. ✅ Within 8-page limit.
- **Anonymity**: Author line reads "Anonymous". No self-citations or identifying information detected. ✅
- **Limitations section**: Present (Section 8), covers 5 points. ✅
- **References**: Only 12 citations — somewhat thin for EMNLP but not a violation.
- **Responsible NLP Checklist**: Not visible in the PDF. ⚠️ Must be included for ARR submission.

---

## Minor Comments

- Tables 3 and 4 could be merged to save space.
- The paper uses "ℓz*" in formulas but "lz*" sometimes in running text — standardize.
- Section 6.1's claim about "57 of 60 model-benchmark cells" would benefit from noting the BH-FDR α level used.
- The memorization fraction concept (33–40%) is used throughout but never formally defined with an equation.

---

## Overall Assessment

This paper introduces a novel angle on contamination detection — IRT person-fit at the minimal-information operating point — with an impressive experimental scope. The post-RL robustness finding is timely and the 4PL ablation is convincing. The writing is efficient and the narrative is clear.

The main concerns are: (1) the headline post-RL claim relies on a single model/condition, (2) no sensitivity analysis for the critical PSN-IRT parameter dependency, and (3) the practical applicability is narrower than implied (requires clean baselines from the same model family).

The paper is above Findings quality — the contribution is conceptually interesting and experimentally supported — but the thin post-RL replication and missing sensitivity analysis keep it from a confident Conference recommendation. With one additional model's post-RL replication and a parameter perturbation experiment, this would be a clear accept.

**Recommendation**: 3.5 — Borderline Conference. The core idea and post-RL story are strong enough for Main if the authors address the replication concern in revision.
