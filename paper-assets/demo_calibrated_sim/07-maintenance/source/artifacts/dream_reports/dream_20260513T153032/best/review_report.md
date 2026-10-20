---
dream_id: dream_20260513T153032
tier: best
overall_score: borderline accept
timestamp: 2026-05-13T16:19:58.774936+00:00
---

# Dream Review Report — Consolidated Roundtable

**Paper**: "Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation"
**Venue**: EMNLP 2026 Findings
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-13

---

## Paper Summary

The paper investigates why calibration of LLM-based user simulators fails when attempting to correct dialect-dependent behavioral biases (AAVE, Indian English vs Standard American English). Two calibration strategies — Behavioral Calibration Prompting (BCP, inference-time) and Direct Preference Optimization (DPO, training-time) — are tested on Qwen2.5-7B/14B-Instruct in the τ-bench retail domain. Both fail. The authors propose a four-mechanism taxonomy of failure modes (FM1–FM4), demonstrate that all four are more severe at 7B than 14B via bootstrap CIs, and articulate a "safety–efficacy gap": scaling eliminates destructive side effects without improving calibration effectiveness.

---

## Reviewer Scores

| Dimension | R1 (Methods+Exp) | R2 (Novelty+RW) | Consensus |
|-----------|:-:|:-:|:-:|
| Soundness | 3.0 | 3.0 | 3.0 |
| Excitement | 2.5 | 3.0 | 2.5 |
| Reproducibility | 3 | 3 | 3 |
| Overall | 3.0 | 3.0 | **3.0** |
| Confidence | 4 | 4 | 4 |

**Consensus Overall: 3.0 — Borderline Findings Accept**

---

## Consolidated Strengths

1. **FM4 (DPO–BCP interaction reversal) is genuinely novel.** The finding that DPO training reverses BCP calibration direction — with 10/12 directional consistency (p=0.006) at 7B and statistically significant attenuation at 14B (14.7pp, CI [8.1, 21.6]) — is the paper's most compelling contribution. No prior work has documented this interaction effect in calibration contexts.

2. **Well-defined evaluation framework.** The H1/H2/H3 hypothesis structure with pre-specified thresholds (≥5% sensitivity, ≥30% gap reduction, ≥80% completion retention) provides a clear, falsifiable framework. This is a good methodological model for negative-results papers.

3. **Appropriate and rigorous statistical methodology.** Non-parametric bootstrap with BCa correction (B=10,000) is well-suited for the small-n, non-normal distributions in this study. All core claims are backed by CIs that exclude zero. The sign test for FM4 directional consistency is correctly applied.

4. **Honest reporting of limitations.** The question_rate arm is transparently reported as descriptive with absolute values due to low base rate (0.044). The paper acknowledges the Qwen-only limitation upfront and explains why Llama/Mistral controls failed (5%/0% completion).

5. **Multi-run replication for key claims.** FM3 and FM4 are validated across 4 independent runs, and the 14B DPO experiment (plan_006) uses 4 runs × 6 variants × 20 tasks = 480 episodes. The cross-scale comparison has a reasonable statistical backbone.

6. **Scale-dependent analysis adds value.** Showing that all four failure mechanisms have capacity-dependent severity, with different patterns (FM1/FM3 disappear; FM2/FM4 attenuate), is informative for calibration research even if the "taxonomy" framing is too strong.

---

## Consolidated Weaknesses

### Major

1. **FM1 and FM2 lack run-to-run replication (single-run, n=19–20).** Both FM1 (global suppression) and FM2 (cross-dimension interference) rest on single-run data with small samples. Bootstrap CIs quantify within-run uncertainty but cannot capture run-to-run variance. FM3 and FM4 benefit from 4-run replication; the same standard should apply to FM1 and FM2 before they are presented as robust "mechanisms." *[R1]*

2. **FM1 and FM2 are relabeled known phenomena.** FM1 is explicitly described as "a task-oriented instantiation" of the persona–accuracy trade-off (Basil et al. 2025, Hu et al. 2026). FM2 parallels bias spillover (Gupta et al. 2026). The "first taxonomy" claim oversells the contribution — it is more accurately an organizing framework that combines two known effects with two novel observations (FM3, FM4) in a new context. *[R2]*

3. **Single model family (Qwen2.5) undermines taxonomy generality.** A "taxonomy" implicitly claims generality. With results from only Qwen2.5-7B and 14B, the four failure modes could be Qwen-specific artifacts. The paper acknowledges this but the framing doesn't match the evidence scope. The title should be hedged (e.g., "Toward a Taxonomy" or explicitly scoped to Qwen2.5). *[R1+R2]*

4. **Safety–efficacy gap is overstated from two scale points.** Drawing a general principle ("scaling changes how calibration fails, not whether it fails") from {7B, 14B} in one model family is a stretch. The relationship could be non-monotonic, could reverse at larger scales, or could differ across families. This needs much stronger caveats or should be presented as a hypothesis rather than a finding. *[R1+R2]*

5. **Significant missing related work weakens positioning.** *[R2]*
   - **Multi-objective alignment**: Rame et al. (2024, "Rewarded soups"), Yang et al. (2024, "Rewards-in-context") — FM2 is fundamentally a multi-objective problem with existing partial solutions.
   - **Controllable text generation**: FUDGE (Yang & Klein, 2021), PPLM (Dathathri et al., 2020), DExperts (Liu et al., 2021) — per-dimension control methods could address FM2.
   - **Scaling laws for alignment**: Bai et al. (2022, "Training a helpful and harmless assistant"), McKenzie et al. (2023, "Inverse scaling") — relevant to the scale-dependency claims.
   - The discussion mentions "constrained decoding [Khan et al., 2026]" but this is a 2026 preprint and the controllable generation literature has deeper prior work.

6. **FM4 baseline confound.** The FM4 reversal compares base BCP (completion ~36.8%) vs DPO+BCP (completion ~60%). These conditions have very different underlying distributions, which means the politeness gap comparison is potentially confounded — models that complete more tasks may exhibit systematically different politeness patterns simply from seeing more diverse dialogue states. The paper does not control for this. *[R1]*

### Minor

7. **H2 threshold (≥30%) is unjustified.** The paper doesn't motivate why 30% is the right threshold. The best observed gap reduction is 27.6% (CI [18.3, 35.2]) — the CI actually includes 30%. The "calibration fails" narrative is sensitive to this threshold choice. A threshold sensitivity analysis would strengthen the claims. *[R1]*

8. **DPO preference pair construction is underspecified.** The paper states 1,434 "dialect-calibrated preference pairs" but doesn't explain the construction process. Were preferred responses human-written? LLM-generated? How was "appropriate dialect-matched behavioral rate" operationalized? This limits reproducibility. *[R1]*

9. **Possible author attribution error.** R2 flagged that "Gupta et al. [2026]" for arXiv:2602.16438 may have incorrect first-author attribution — the paper at that arXiv ID may have a different first author (Paraschou). This should be verified. *[R2]*

10. **No figures.** The paper is entirely tables and text. Visualization of the scale-dependent failure patterns (e.g., a heatmap or forest plot) would substantially improve readability and impact. *[R1+R2]*

---

## Questions for Authors

1. **Can you provide multi-run replication for FM1 and FM2?** What is the run-to-run variance for the single-dimension conditions? (If available from additional runs not reported.)

2. **How were the 1,434 DPO preference pairs constructed?** Were preferred responses generated by prompting the base model with dialect-matched behavioral targets? Human-curated? What quality control was applied?

3. **Have you tested the H2 threshold sensitivity?** At what threshold does H2 start passing? The CI for best gap reduction [18.3, 35.2] suggests that at a 20% threshold, H2 might pass in some conditions.

4. **Can you control for the completion-rate confound in FM4?** For instance, by comparing politeness gaps only among completed episodes, or by matching on completion status.

5. **Why no controllable generation baselines?** FUDGE or DExperts-style approaches could provide per-dimension behavioral control that avoids FM2 by design. Even if infeasible to run, discussing why these are excluded would strengthen the paper.

---

## Missing Experiments or Ablations

- Multi-run replication for FM1 and FM2 (4 runs each, matching FM3/FM4 rigor)
- DPO-only evaluation *without* BCP (isolate DPO's standalone calibration effect)
- BCP prompt intensity ablation (does graduated vs binary targeting affect FM3?)
- H2 threshold sensitivity analysis
- Completion-matched FM4 analysis (compare gaps only among completed episodes)
- At least one non-Qwen model with sufficient tool-calling ability (even if limited to BCP-only)

---

## Experiment Coverage Assessment

Comparing against the full experiment design (review_context.yaml):

| Experiment | Status | Notes |
|-----------|--------|-------|
| Bootstrap CI (plan_005) | ✅ Fully covered | Table 2, all 5 comparisons |
| 14B DPO+BCP (plan_006) | ✅ Fully covered | Tables 3–5, 480 episodes |

Both planned experiments are well-reflected in the paper. The paper covers what was planned; the gaps identified above are beyond the original experiment design.

---

## Roundtable Discussion Summary

### Points of Agreement
- FM4 is the strongest and most novel contribution; its scale-dependency analysis is the paper's highlight
- Bootstrap methodology is appropriate and well-executed
- Single model family is the biggest external validity concern
- Safety–efficacy gap needs stronger caveats or reframing as hypothesis
- The paper reads as slightly overselling known effects (FM1, FM2) as novel taxonomy entries

### Points of Productive Disagreement
- R1 weighted the FM4 baseline confound more heavily (potentially undermining the strongest claim); R2 considered this less fatal given the sign test's robustness to baseline shifts. Consensus: it warrants acknowledgment and ideally a completion-matched analysis, but likely doesn't overturn FM4.
- R2 was more concerned about missing related work (multi-objective alignment, controllable generation) implying that FM2 has known solutions; R1 noted the τ-bench tool-calling setting is sufficiently distinct that those methods may not directly apply. Consensus: the paper should discuss these methods and explain why they don't straightforwardly transfer.

### Accept/Reject Reasoning
**For acceptance (Findings):** FM4 is genuinely novel with strong statistical support. The scale-dependent failure analysis is informative. The H1/H2/H3 framework is well-constructed. Negative results with clear characterization have value for the community. The experimental execution (especially plan_005 and plan_006) is solid for the claims actually supported.

**Against acceptance:** The "taxonomy" framing is stronger than the evidence warrants — two of four mechanisms are known phenomena, and the single-family evidence doesn't support the generality that "taxonomy" implies. Key experiments (FM1/FM2 multi-run) are missing. The safety–efficacy gap, while intriguing, is underpowered.

**Consensus recommendation:** Borderline Findings accept (3.0). The paper would benefit from (1) reframing from "taxonomy" to "empirical characterization," (2) multi-run FM1/FM2 replication, (3) expanded related work, and (4) explicit caveats on the safety–efficacy gap. If the authors can address items 1, 3, and 4 in a revision (items requiring no new experiments), the paper clears the Findings bar comfortably.

---

## Final Assessment

**Overall Score: 3.0 (Borderline Findings Accept)**

The paper presents a well-executed empirical investigation of calibration failures in dialect-aware LLM user simulation. FM4 (DPO–BCP interaction reversal) is a genuinely novel finding with rigorous statistical validation. The scale-dependent analysis across 7B and 14B is informative. However, the "taxonomy" framing oversells the novelty (FM1/FM2 are known phenomena in new context), the single model family limits generalizability, and several experimental gaps (FM1/FM2 multi-run replication, FM4 baseline confound control) prevent a confident accept. With moderate revisions — primarily reframing and expanded related work — this would be a solid Findings paper.
