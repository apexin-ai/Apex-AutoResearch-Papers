---
round: 8
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-25T21:33:32.235454+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 8 (Fresh Review)

**Paper**: "What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?"
**Venue**: EMNLP 2026 (via ARR)
**Reviewers**: R1, R2 (2-reviewer panel, method rigor + novelty/completeness focus)
**Cross-response**: Complete (both reviewers responded to each other's full reports)
**Date**: 2026-05-25

---

## Summary

This paper presents the first controlled empirical study of IRT person-fit statistics (ℓ*_z) for detecting SFT-stage benchmark contamination in LLMs. Using a matched-difference design across three 7-8B model families (Qwen, Llama, Mistral) with n=10 clean seeds on MMLU and ARC-Challenge, the authors identify three behavioral boundaries: (1) θ-shift absorption dynamics requiring θ-anchoring, (2) a detection-diagnosis tradeoff, and (3) non-monotonic dose-response as a θ-estimation artifact. The work is technically competent with a well-designed experimental framework, but suffers from critical gaps in baseline comparison, framing inconsistency between detection and diagnosis, and overstatement of experimental coverage.

---

## Strengths

1. **Well-designed experimental framework**: The matched-difference design (Δℓ*_z) with n=10 clean seeds per family and multi-seed reporting provides a rigorous foundation. The controlled contamination setup (QLoRA SFT at 5-50%) allows clear causal attribution.

2. **Novel application domain**: Applying IRT person-fit statistics to LLM contamination detection is genuinely novel. The psychometric framing (test-taker with preknowledge ↔ contaminated LLM) is theoretically motivated and well-articulated.

3. **θ-anchoring insight**: The discovery that θ-shift absorption attenuates person-fit signals, and that anchoring resolves this (2.4× amplification, CV 60%→19%), is the paper's strongest mechanistic contribution with practical implications.

4. **Honest reporting of limitations**: Multi-seed variability (CV=60% at 50% contamination), the exploratory tag on Finding 3, and acknowledgment of ARC-C's limited scope demonstrate scientific integrity.

5. **Comprehensive appendix**: 16 supplementary tables providing detailed per-seed results, power analysis, and robustness checks strengthen reproducibility.

---

## Weaknesses

### CRITICAL (Must-Fix)

**[N1] No empirical comparison with existing detection methods** (Both reviewers, consensus CRITICAL)

The paper positions ℓ*_z within a "detection frontier" (Figure 2a) alongside logit-based methods (Min-K%, membership inference) but provides zero empirical comparison. In a controlled experiment where the authors have full model access (QLoRA fine-tuned models), running Min-K% or MIA baselines has minimal marginal cost. Without this comparison, the reader cannot assess:
- When is ℓ*_z preferable to logit-based methods?
- What is the detection accuracy (precision/recall) relative to established baselines?
- Does the "complementary" claim in Discussion have empirical support?

The post-RL pilot includes Min-K% AUC (0.611→0.493 after GRPO), showing the authors can compute this metric—yet they never compute it on the main SFT experiments. This is a conspicuous omission that undermines the paper's positioning claims.

**Action required**: At minimum, run Min-K% on the most complete condition (Qwen-MMLU-15%, all seeds) and report comparative detection performance.

---

**[N2] Post-RL pilot (N=1) receives disproportionate structural weight** (Both reviewers, consensus CRITICAL)

A single-model, single-condition GRPO pilot (Qwen, 15% MMLU) appears in:
- Section 3.3 (Methods, 1 sentence)
- Section 5 Discussion (with dedicated Figure 6, ~8 lines)
- Conclusion (1 sentence, hedged)

Despite hedging ("preliminary pilot"), the structural placement—a dedicated figure in Discussion and a sentence in Conclusion—gives this N=1 observation outsized prominence. The claim "person-fit anomalies persist after RL" requires at minimum:
- Multiple contamination levels
- Multiple model families
- Multiple RL seeds

A single observation cannot distinguish signal from noise. The Min-K% comparison (AUC 0.493) is from the same single run—also insufficient for a "MIA fails post-RL" generalization.

**Action required**: Either (a) reduce to a single sentence in Discussion without a dedicated figure, or (b) provide multi-condition post-RL evidence.

---

**[N3] PSN-IRT calibration sample contamination creates non-uniform bias** (R1 primary, R2 AGREE)

The PSN-IRT item parameters are calibrated on N_J=178 Open LLM Leaderboard models (Appendix I). The Leaderboard analysis (Figure 5) reveals 5,760 model×benchmark cells with |ℓ*_z| > 1.96, suggesting widespread contamination in the calibration sample. This creates a specific threat:

- Contaminated models in the calibration sample bias item difficulty/discrimination parameters
- This bias is **non-uniform**: it disproportionately affects items that are commonly leaked (popular benchmark subsets)
- The matched-difference design (Δℓ*_z) partially cancels uniform bias but NOT item-specific bias
- Result: ℓ*_z may systematically over- or under-detect contamination on specific items

The existing Discussion paragraph ("calibration sample...may include contaminated ones, though individual contamination effects are diluted") addresses this at a surface level but does not quantify the potential impact or analyze item-specific bias patterns.

**Action required**: Sensitivity analysis where PSN-IRT parameters are perturbed with systematic (not random) bias on known contamination-prone items, showing the impact on Δℓ*_z effect sizes.

---

**[N4] Detection vs. characterization framing inconsistency** (Both reviewers, consensus CRITICAL)

The paper oscillates between two incompatible positions:
- **Detection tool**: Figure 2(a) "detection frontier," Abstract "detecting SFT contamination," Introduction "carries sufficient information for contamination detection"
- **Diagnostic/characterization tool**: Figure 2(d) two-stage workflow (screen with accuracy → diagnose with ℓ*_z), the title's interrogative framing, Section 5's "characterization" language

The θ-anchoring circular dependency makes this inconsistency substantive, not merely editorial: ℓ*_z with θ-anchoring requires a clean baseline to set θ_fixed, but determining "clean" is the detection task itself. Therefore, θ-anchored ℓ*_z cannot function as an independent detector—only as a diagnostic tool applied AFTER detection by other means.

The paper acknowledges this ("diagnostic θ-anchoring requires a clean baseline") but the framing doesn't consistently follow through. Figure 2(a) should either be removed or reframed as showing ℓ*_z's position in a post-detection diagnostic pipeline, not a detection frontier.

**Action required**: Commit to one consistent position throughout. Recommended: characterization/diagnosis framework where ℓ*_z adds mechanistic insight after initial detection by simpler means.

---

**[N5] Experimental matrix incomplete; Abstract/Introduction misleading** (Both reviewers, consensus CRITICAL)

Abstract states: "across three 7–8B model families...on MMLU (14,042 items) and ARC-Challenge (295 items)"
Introduction: "three 7–8B model families...on MMLU and ARC-Challenge"

Actual coverage:
| | MMLU 5% | MMLU 15% | MMLU 25% | MMLU 50% | ARC-C |
|---|---|---|---|---|---|
| Qwen | ✓ | ✓ | ✓ | ✓ | ✓ |
| Llama | ✓ | ✓ | ✓ | ✓ | ✗ |
| Mistral | ✓ | ✓ | ✗ | ✓ | ✗ |

ARC-Challenge is Qwen-only. Mistral lacks 25%. A reader naturally interprets "three families on MMLU and ARC-Challenge" as a 3×2 complete matrix. Section 3.3 does disclose this ("ARC-Challenge experiments were conducted on Qwen only"), but the high-level framing in Abstract/Introduction creates a misleading first impression.

**Action required**: Abstract and Introduction must explicitly qualify: "...on MMLU (all three families) and ARC-Challenge (Qwen only, as cross-benchmark probe)."

---

### SHOULD-FIX

**[W1] Diagnostic value proposition unanswered** (R1 primary, R2 AGREE)

The paper claims a "detection-diagnosis tradeoff" (Finding 2) where ℓ*_z sacrifices detection power for diagnostic capabilities. But the claimed diagnostic capabilities are not convincingly demonstrated:
1. Seen/unseen decomposition doesn't require ℓ*_z—any statistic can be decomposed given known contamination items
2. Mechanistic θ-shift analysis requires clean baseline (circular)
3. No demonstration of ℓ*_z diagnostics leading to a different practical decision than simpler methods

**Key unanswered question**: After detecting contamination via accuracy z-scores, what specifically does ℓ*_z's diagnostic output enable that accuracy-based analysis cannot?

---

**[W2] Confirmatory findings need stronger novelty justification** (R2 primary as CRITICAL, R1 partial REBUT → consensus SHOULD-FIX)

Findings 1 (θ-shift absorption) and 2 (detection-diagnosis tradeoff) are largely predictable from IRT theory. R1 argues first empirical validation in a new domain has independent value; R2 argues theoretical predictability limits novelty. Consensus: the paper should more explicitly state which quantitative aspects (exact magnitudes, boundary conditions, the 2.4× amplification factor, CV reduction) were NOT predictable from theory alone.

---

**[W3] Local dependence simulation uses simplified additive model** (R1 primary, R2 AGREE low severity)

Appendix G's simulation uses an additive memory factor (r_mem) that cannot capture LLM-specific dependencies (positional bias, attention patterns). While Table 9 shows robustness at r_v=0.5, the simulation cannot claim to model realistic LLM response dependencies. Should be acknowledged in Limitations.

---

**[W4] Cohen's d usage requires clarification** (R1 primary, R2 AGREE low severity)

The reported "d" is a one-sample standardized departure (contaminated observation vs. clean distribution), not a two-group Cohen's d. The 0.2/0.5/0.8 benchmarks do not apply. Practical impact is minimal (most |d| > 2), but a footnote or inline clarification is needed for methodological precision.

---

## Questions for Authors

1. If you ran Min-K% on your Qwen-MMLU-15% contaminated models (all 3 seeds), what ROC-AUC would you expect? Why was this not included?
2. Can you quantify what proportion of your 178 calibration models are likely contaminated on MMLU, and estimate the resulting item-parameter bias?
3. In the two-stage workflow (Figure 2d), what specific decision does ℓ*_z-based diagnosis enable that accuracy z-score screening alone cannot?
4. Why does Mistral lack 25% contamination data? Is this a compute constraint or a failed training run?

---

## Missing References

- Oren et al. (2024), "Proving Test Set Contamination in Black Box Language Models" — directly relevant black-box contamination detection without model internals
- Dekoninck et al. (2024), "Evading Data Contamination Detection for Language Models is (too) Easy" — adversarial perspective on contamination detection robustness
- Deng et al. (2024), "Investigating Data Contamination in Modern Benchmarks for Large Language Models" — systematic survey of contamination detection methods (broader context for Related Work)

---

## External Review

**Status**: Not requested (外部审稿未启用)

---

## Visual Layout Check (非评分项)

**Status**: Done (4 warnings, 17 info)

Key findings:
- **Warning**: Figure 1(c)(d) axis tick labels ≤6pt, may be illegible in print → recommend ≥8pt
- **Warning**: Pages 4-5 (~1.5 pages) continuous text without display items (Experimental Setup)
- **Warning**: Figure 5 (leaderboard heatmap) y-axis model names and cell values very small in two-column format
- **Warning**: Page 16 ~90% whitespace (AI Assistants statement alone on page)
- **Info**: 8 display items across 8 pages (density ~1.0/page), reasonable for empirical paper
- **Info**: No margin overflow, no orphaned section headings, proper ACL anonymous format
- **Info**: All figures/tables appear near first citation, no significant float drift

---

## Overall Assessment

**Score: 3.0 — Findings**

The paper makes a genuinely novel connection between IRT person-fit statistics and LLM contamination detection, backed by a well-designed controlled experimental framework. The θ-anchoring insight is the strongest contribution. However, five critical issues prevent main conference acceptance:

1. **No baseline comparison** (persistent since Round 4): A detection-oriented paper that never empirically compares against existing detection methods cannot substantiate its positioning claims. This is especially problematic given the low marginal cost of running Min-K% in the controlled setting.

2. **Framing incoherence**: The paper simultaneously claims to be a detection method and acknowledges it cannot detect independently (requires clean baseline). This circular dependency undermines the "detection frontier" positioning.

3. **Overclaims relative to evidence**: Abstract/Introduction imply broader experimental coverage than exists (3×2 matrix vs. incomplete); post-RL N=1 receives figure-level prominence.

4. **PSN-IRT contamination**: The calibration sample's likely contamination creates non-uniform bias that matched-difference cannot fully cancel, and no sensitivity analysis quantifies this threat.

5. **Diagnostic value undemonstrated**: The claimed tradeoff (detection power ↔ diagnostic capability) lacks concrete evidence of what diagnostic decisions ℓ*_z enables.

The work would be appropriate for Findings if issues N2 (post-RL prominence) and N5 (misleading framing) are addressed editorially, but N1 (baseline comparison) and N3 (sensitivity analysis) likely require additional experiments. N4 (framing consistency) requires structural revision.

---

## Detailed Comments (by section)

**Abstract** (p.1): "across three 7–8B model families...on MMLU and ARC-Challenge" → misleading; ARC-C is Qwen-only. Add explicit qualification.

**Introduction** (p.2): Contribution list frames work as detection method ("detecting SFT contamination") but θ-anchoring requires clean baseline → inconsistent with detection framing. Consider: "characterizing" or "diagnosing."

**Figure 2(a)** (p.2): "Detection frontier" concept is unsupported by data. Either remove or reframe as aspirational/conceptual with explicit caveat that no empirical comparison exists.

**Section 3.3** (p.5): ARC-C Qwen-only disclosure is buried mid-paragraph. Should be more prominent given Abstract/Intro implications.

**Section 4.2** (p.6): "detection-diagnosis tradeoff" — needs concrete example of what the diagnostic side enables in practice.

**Discussion** (p.8): GRPO figure placement gives N=1 result outsized visual weight. Consider moving to Appendix with a single-sentence Discussion reference.

**Conclusion** (p.8): "A preliminary post-RL pilot suggests..." — appropriate hedging, but given the figure in Discussion, the overall structural weight exceeds what N=1 supports.

**Limitations** (p.9): Should mention (a) simulation simplification (additive LD model), (b) PSN-IRT calibration sample contamination risk explicitly.

---

*Report synthesized from 2 independent reviewers with full cross-sharing and convergence verification. Core consensus achieved on all critical issues.*