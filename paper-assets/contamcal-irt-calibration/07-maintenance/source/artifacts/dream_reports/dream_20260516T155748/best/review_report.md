---
dream_id: dream_20260516T155748
tier: best
overall_score: 4 — Borderline Reject
timestamp: 2026-05-16T16:45:26.214000+00:00
---

# Review Report: ContamCal

## Paper Summary

ContamCal introduces a two-stage framework bridging contamination detection and score calibration via contamination-augmented IRT. Stage 1 computes per-item exposure scores using embedding similarity (S1). Stage 2 fits a 4PL+γ IRT model where γ captures per-benchmark contamination effects. Through controlled SFT injection across Qwen2.5 (0.5B–7B) and Llama-3.2-3B at five dosage levels, the paper reveals: (1) within-MMLU Simpson's paradox with a STEM gradient replicated across families, (2) benchmark-dependent effects (ARC forgetting γ=−1.18, GSM8K null), (3) scale modulation from catastrophic (0.5B) to negligible (7B), (4) Min-K++ directional reversal, and (5) conditional calibration with gating. A 2-signal closed-weight ablation honestly demonstrates S1-dependence.

## Experiment Coverage

All 6 planned experiments from the design document are covered:
- QC-only d100 validation → §5.6, Table 5
- 7B scale bridging → §5.1, Table 1
- Llama cross-family validation → §5.2–5.3, Tables 2–4
- RL observational case study → §5.8, Tables 6–7
- 72B ecological validity → §5.9, Appendix A
- 2-signal closed-weight ablation → §5.10, Tables 8–9

Coverage is comprehensive. Figures mentioned in the experiment plan (paired forest plots, 4-scale dose-response curves, STEM gradient visualization) appear to be absent from the main paper or appendix — the paper may be presenting a figure-light version. Table numbering has gaps (jumps from Table 4 to Table 5 with different numbering conventions), and the "References" heading appears twice on page 9.

---

## Strengths

**S1. Novel and well-grounded formulation.** Connecting contamination detection to psychometric DIF (Differential Item Functioning) literature is intellectually compelling. The γ parameter as a contamination covariate in IRT is a clean, interpretable modeling choice with strong theoretical grounding (Holland & Wainer 1993; Eckerly 2017). No prior work has bridged detection and calibration in this way.

**S2. Rich empirical characterization.** The paper delivers several substantive empirical findings beyond the framework itself: (a) the Simpson's paradox in MMLU where aggregate γ≈0 masks STEM_Math γ=+0.97; (b) ARC forgetting as a benchmark property persisting across scales and families; (c) Min-K++ directional reversal (Cohen's d=−1.98 at 0.5B), which is an important cautionary finding for the detection community; (d) GSM8K format-driven immunity. These characterization results would be independently valuable.

**S3. Cross-family replication strengthens claims.** The STEM gradient replicating across Qwen and Llama (Math > Science ≫ CS/Eng ≈ 0, direction matching in all 5 domains including non-STEM misfit) is strong evidence that contamination susceptibility maps to item-level properties rather than model architecture. This is the paper's most convincing finding.

**S4. Commendable intellectual honesty.** The paper is transparent about its limitations in a way that builds trust: the 2-signal ablation honestly reports 0/3 benchmarks passing gating; coverage is reported below nominal; the SFT-vs-real-contamination gap is acknowledged; the identifiability mismatch is stated explicitly. The gating criterion — designed to prevent misleading calibration — is a responsible design choice that correctly rejects calibration when signal quality is insufficient.

**S5. Thorough baseline comparisons.** Seven baselines including vanilla 4PL, linear regression, DCR fuzzy, and remove-and-rescore. The bootstrap test (p=0.032) for IRT vs. linear regression on ARC provides meaningful evidence for the nonlinear modeling advantage.

**S6. Well-scoped observational extension.** The RL observational case study correctly frames results as "directional external validity" rather than quantitative confirmation. The expected regret analysis (44.1% reduction for top-5 selection) provides a concrete practical metric. The WinoGrande specificity check (γ=0.04, CI including zero) is a thoughtful control.

---

## Weaknesses

**W1. Self-undermining identifiability analysis (Major).** The Fisher Information simulation (§3.4) establishes that reliable γ recovery requires N≥50 models at signal AUC≥0.55. The paper's empirical results use N=24 (Qwen-only), N=30 (cross-family), and N≈38 (with observational). The paper acknowledges this as a "structural domain-method mismatch" but proceeds to draw conclusions from these underpowered estimates. This creates a fundamental tension: the paper's own theoretical analysis says its empirical results should not be fully trusted. The headline ARC result (γ=−1.18, CI excludes zero at N=30) sits squarely in the regime the paper's simulations flag as unreliable. This needs stronger reconciliation — either the identifiability bound is too conservative (show why), or the results should be presented more cautiously.

**W2. Cross-family pooling of heterogeneous effects (Major).** Qwen-only ARC γ=+0.52 (positive, CI includes zero) while Llama-only ARC γ=−1.65 (negative, CI includes zero). Neither alone achieves significance, but pooling produces γ=−1.18 with CI excluding zero. This is methodologically concerning: the two families exhibit qualitatively different ARC dynamics (Qwen barely forgets at ≥1.5B; Llama forgets −4.7pp at 3B). Pooling effects of opposite sign and testing for significance risks ecological fallacy. A hierarchical/mixed-effects model with a family-level random effect on γ would be more appropriate and would reveal whether the "significant" pooled result survives when between-family heterogeneity is properly modeled. The current pooling implicitly assumes a common γ across families, which contradicts the observed data.

**W3. S1 dependence severely limits practical applicability (Major).** The framework's calibration quality entirely depends on S1 embedding similarity (AUC>0.95), requiring (a) model embedding access and (b) a reference corpus of known/suspected training paraphrases. The 2-signal closed-weight ablation shows 0/3 benchmarks passing gating. For the primary use case practitioners care about — evaluating closed-weight API models (GPT-4, Claude, Gemini) — ContamCal cannot help. The paper frames this honestly, but it means the framework's practical applicability is limited to the relatively narrow setting where you have full model access AND know what contamination might look like. In that setting, you arguably already have tools to investigate directly.

**W4. Coverage consistently below nominal (Moderate).** 95% CI coverage ranges from 0.40 (2-signal) to 0.70 (cross-family GSM8K), never approaching the 95% nominal level. The paper reframes CIs as "directional indicators," but this retreat undermines the uncertainty quantification motivation. If Bayesian credible intervals don't have approximately correct frequentist coverage, the calibrated scores' uncertainty bounds are unreliable for downstream decision-making. Contributing factors (local independence violation, small N, model misspecification) are listed but not systematically addressed.

**W5. Single-seed experiments at larger scales (Moderate).** 7B and Llama experiments use 1 seed per condition. At these scales, accuracy deltas are small (±1pp), well within run-to-run variance. The ARC −0.9pp at 7B is presented as evidence that "forgetting direction persists," but without multiple seeds, it could be noise. Similarly, Llama's −4.7pp ARC forgetting — the datum that drives the cross-family pooled result negative — rests on a single run. Multiple seeds would substantially strengthen or weaken the key claims.

**W6. SFT injection ≠ real-world contamination (Moderate).** Real contamination occurs during pre-training (not SFT), involves exact matches (not quality-controlled paraphrases), interacts with billions of other training examples, and may be diluted across epochs. The controlled injection provides clean causal identification but may not transfer quantitatively. The observational extension shows directional consistency but all individual γ estimates lose significance, and coverage drops to 0.53. The gap between controlled and real-world settings remains a fundamental external validity question.

---

## Minor Issues

- M1: "References" header duplicated on page 9.
- M2: HumanEval is described as "appendix only" (§4.1) but no appendix section reports HumanEval-specific IRT results; only the 72B Table 11 mentions it.
- M3: Table 10 (Qwen-only pooled IRT) is presented late (§5.11, page 8), after the cross-family results. Moving it earlier would better motivate WHY cross-family pooling is needed, making the narrative clearer.
- M4: The 0.5B position bias finding (§6) — MMLU option-A prediction shifting from 46% to 98% under contamination — is fascinating and deserves more analysis. What is the mechanism? Is it specific to Qwen2.5-0.5B's architecture or tokenizer?
- M5: The paper mentions 4 signals (S1–S4) but S3 (ConStat) and S4 (Self-Critique) are barely evaluated outside the 2-signal ablation. The 4-signal RRF achieves AUC=0.68, substantially worse than S1-only (0.98), raising the question of why these signals are retained in the framework at all.
- M6: The calibration formula (Eq. 3) sets τ_j=0 to compute decontaminated scores. This assumes contamination effect is purely additive via γτ_j. If contamination also changes item discrimination (a_j) or difficulty (b_j) — which the paper's controlled experiments would allow testing — this is an incomplete correction.

---

## Questions for Authors

1. The Fisher Information analysis says N≥50 is needed for reliable γ recovery. Your headline result uses N=30. Have you run the simulation specifically at N=30 with AUC=0.98 (your actual S1 quality) to check whether recovery is reliable in this specific operating point? The published sweep may use conditions that don't match your actual setup.

2. What happens to the cross-family ARC γ if you fit a hierarchical model with family-level random effects? Does the pooled γ still exclude zero? This is critical for assessing whether the significance is an artifact of treating heterogeneous families as exchangeable.

3. Have you considered running 3–5 seeds for the Llama-3B conditions? The −4.7pp ARC forgetting from a single seed is the linchpin of the cross-family result. Its stability under replication would substantially change confidence in the headline finding.

4. For the specificity check (WinoGrande), how was "known-clean" status established? If WinoGrande items appear in training corpora (e.g., via Common Crawl), the specificity check is invalidated.

5. Could you test whether contamination changes item parameters (a_j, b_j) in addition to operating through γ? Your controlled setup enables this by fitting IRT separately on d000 and d100 data and comparing item parameters.

---

## Scoring

| Criterion | Score | Notes |
|-----------|-------|-------|
| Novelty | 7/10 | IRT+contamination bridge is genuinely new; DIF connection is insightful |
| Significance | 6/10 | Characterization findings are important; calibration limited by S1 dependence |
| Soundness | 5/10 | Identifiability gap and heterogeneous pooling undermine quantitative claims |
| Clarity | 7/10 | Dense but well-organized; honest about limitations |
| Reproducibility | 6/10 | Controlled injection is reproducible; single seeds limit verifiability |
| Experiment Coverage | 9/10 | All planned experiments represented; some figures from plan missing |

**Overall Score: 4 — Borderline Reject**

**Confidence: 4 (Confident)**

---

## Justification

The paper introduces a novel and intellectually compelling framework grounding contamination calibration in psychometric theory. The characterization findings — STEM gradient, ARC forgetting as benchmark property, Min-K++ reversal, scale modulation — are substantive empirical contributions that advance understanding of contamination's structured effects.

However, the paper has a fundamental self-consistency problem: its own identifiability analysis (N≥50 required) contradicts the operating regime of its experiments (N=24–30). The headline ARC result depends on pooling two families with opposite-sign γ estimates, which is methodologically fragile without hierarchical modeling. The S1 dependence limits practical applicability to settings where full model access is available. Coverage consistently below nominal undermines the uncertainty quantification claims.

The characterization contributions are strong enough to be valuable, but the calibration contributions — which the title and framing emphasize — are not convincingly established given the identifiability gap. For a top venue at ~25% acceptance, the quantitative soundness concerns push this below the acceptance threshold. A revision addressing (1) hierarchical cross-family modeling, (2) multi-seed replication of key conditions, and (3) explicit reconciliation of the identifiability bound with actual N could elevate this to an accept.

**Recommended decision: Reject (weak), with encouragement to revise and resubmit.**