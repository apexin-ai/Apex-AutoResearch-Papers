---
dream_id: dream_roundtable_corl
tier: best
overall_score: marginally below acceptance
timestamp: 2026-05-25T23:24:32.983571+00:00
---

# Roundtable Review Report

## Cross-Sharing Summary

**Agreements:**
- Both reviewers assign Overall = 5 (marginally below acceptance) with Confidence = 4
- Both agree the metric critique is well-motivated and clearly presented (Clarity = 3)
- Both acknowledge displacement-filtered CAR is practical and low-barrier
- Both flag insufficient statistical evidence for the LoRA-only vs. SDF comparison
- Both note the narrow experimental scope (single benchmark, limited scenes)
- Both view the paper as honest in framing negative results

**Disagreements:**
- R1 rates Significance = 3 (good); R2 rates Significance = 2 (fair). R1 values the diagnostic taxonomy and large experimental effort more highly; R2 considers the core observation obvious to safe RL practitioners.
- R1 treats the "three failure modes" taxonomy as a strength (actionable diagnostic categories); R2 dismisses it as descriptive labeling without principled basis.
- R1 finds Phase 2 irreversibility "scientifically interesting"; R2 considers it an unsurprising overlap with catastrophic forgetting literature.
- R2 raises substantial novelty concerns (inaction inflating safety metrics is well-known in safe RL); R1 does not explicitly address novelty but implicitly accepts it as adequate.

**Complementary Insights:**
- R1 provides granular statistical critiques (seed counts, CIs, threshold sensitivity) that R2 lacks
- R2 provides literature contextualization (specification gaming, reward hacking, activity-conditioned metrics) that R1 lacks
- Together they reveal the paper's core tension: real problem, limited novelty, incomplete evidence

## Consensus Assessment

### Paper Summary
The paper demonstrates that Collision Avoidance Rate (CAR) on SafeLIBERO is systematically contaminated — 98%+ of apparent safety arises from action collapse, geometric path safety, or random incompetence rather than genuine avoidance. It proposes displacement-filtered CAR (conditioning on minimum end-effector movement) as a corrective metric and uses SDF auxiliary training as a diagnostic probe, finding that SDF is neither necessary (LoRA-only matches) nor sufficient (causes irreversible task damage). The contribution is primarily diagnostic/methodological rather than algorithmic.

### Strengths (Consensus)

1. **Well-identified metric validity problem with clear quantitative demonstration.** The 99.6% fake safety finding is striking and the mechanistic decomposition into three failure modes gives practitioners actionable diagnostics. (R1-S1, R2-S1)

2. **Displacement-filtered CAR is simple, implementable, and has low adoption barrier.** Requires only EE position logging already available in standard evaluation infrastructure. (R1-S2, R2-S3)

3. **Large experimental effort with honest negative results framing.** 70+ experiments, 6000+ episodes, iterative refinement, no overselling of SDF. (R1-S3, R1-S5)

4. **Formalization connects to established evaluation methodology literature** (Goodhart's law, annotation artifacts). (R2-S2)

5. **Phase 2 irreversibility finding raises interesting questions** about representational damage from auxiliary losses in VLA finetuning. (R1-S4)

### Weaknesses (Consensus)

1. **[Critical] Statistical insufficiency for the central LoRA-only claim.** 2 seeds vs. 3 seeds, no confidence intervals, no hypothesis test. The +2.5pp SDF delta is well within noise for 200-episode evaluations. This undermines the paper's key "SDF is unnecessary" conclusion. (R1-W1)

2. **[Major] Limited novelty of the core observation.** That inaction/incompetence inflates safety-by-absence metrics is conceptually straightforward and has extensive precedent in safe RL (specification gaming, reward hacking, "don't move" policies). The displacement filter is the obvious fix once the problem is stated. (R2-W1, R2-W2)

3. **[Major] Narrow experimental scope.** Single benchmark (SafeLIBERO), two scenes, related model families (Pi0/Pi0.5/OpenVLA all from similar architectures). Generalization to other benchmarks, robots, or evaluation protocols is undemonstrated. (R2-W7)

4. **[Major] No sensitivity analysis for δ=5mm threshold.** The entire filtered-CAR framework depends on this parameter, yet no justification or ablation is provided. (R1-W2)

5. **[Major] Cross-model comparison (Table 1) conflates experimental conditions.** Pi0 is finetuned while others are zero-shot, making the comparison misleading for drawing conclusions about model architectures. (R1-W3)

6. **[Major] Phase 2 irreversibility based on single seed.** Insufficient to establish a general finding; could be seed-specific or hyperparameter-sensitive. (R1-W4)

7. **[Minor] Missing engagement with activity-conditioned metrics and specification gaming literature.** The paper does not position itself against closely related ideas in safe RL. (R2-W5, R2-W6)

8. **[Minor] FSR metric is redundant** — derivable from filtered CAR and raw CAR. (R1-W7)

9. **[Minor] OpenVLA 15% NaN episodes create potential selection bias.** (R1-W6)

### Required Revisions (for potential acceptance)

1. **Add third LoRA-only seed and report confidence intervals** with a formal statistical test for the "SDF unnecessary" claim.
2. **Threshold sensitivity analysis** — sweep δ from 1mm to 20mm and show filtered-CAR stability or identify the transition region.
3. **Strengthen Phase 2 finding** with at least one additional seed and hyperparameter variation (different λ schedules, different resume points).
4. **Explicitly position against safe RL specification gaming literature** — articulate what is new beyond "inaction inflates safety metrics."
5. **Separate Table 1 into zero-shot vs. finetuned** or add appropriate caveats and controls.
6. **Add spatial_bowl LoRA-only control** to properly attribute the +9pp improvement.

### Questions for Authors

1. How sensitive is filtered-CAR to the δ=5mm threshold? At what value does the metric behavior qualitatively change?
2. With only 2 LoRA-only seeds and ±5-7pp confidence intervals, how do you justify "statistically indistinguishable"? Would a third seed change the conclusion?
3. For the Phase 2 irreversibility finding — have you tried different learning rates, longer recovery training, or full-parameter unfreezing? Is the damage truly irreversible or just hard to reverse with LoRA?
4. How would you respond to the concern that displacement filtering is the obvious fix once metric contamination is identified? What is the intellectual contribution beyond stating the problem?
5. Why not evaluate on additional benchmarks (e.g., RoboCasa, CALVIN) to demonstrate generality of the metric contamination phenomenon?
6. For OpenVLA's 15% NaN episodes — what happens to CAR if these are treated as collisions vs. excluded?

### Missing Related Work

- Specification gaming and reward hacking: Krakovna et al. (2020), Amodei et al. (2016), Skalse et al. (2022), Pan et al. (2022)
- Activity-conditioned safety metrics in safe RL (conservative agent detection)
- Catastrophic forgetting literature (for Phase 2 irreversibility framing)
- LoRA/PEFT applied to robotics and VLAs
- VLA safety evaluation beyond SafeLIBERO
- Goodhart's law formalization in ML evaluation (Manheim & Garrabrant, 2019)

## Final Scores

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness/Quality | 2/4 | — | 2/4 |
| Originality | — | 2/4 | 2/4 |
| Clarity | 3/4 | 3/4 | 3/4 |
| Significance | 3/4 | 2/4 | 2/4 |
| Overall | 5/10 | 5/10 | 5/10 |
| Confidence | 4/5 | 4/5 | 4/5 |

## Meta-Review

**Recommendation: Marginally below acceptance (5/10).**

Both reviewers independently converge on the same verdict: the paper identifies a real and practically important evaluation problem, but the combination of limited novelty (the core observation is unsurprising to safe RL practitioners), insufficient statistical evidence for the central experimental claim (2 seeds, no CIs), and narrow scope (one benchmark, two scenes) places it below the acceptance threshold. The significance disagreement (R1=3, R2=2) resolves toward R2's position — while the empirical demonstration has value for the VLA community specifically, the intellectual contribution beyond "inaction inflates safety-by-absence metrics" is thin. The paper would likely reach acceptance with: (1) a third LoRA-only seed plus formal statistical tests, (2) threshold sensitivity analysis establishing filtered-CAR's robustness, (3) explicit positioning against specification gaming literature explaining what is genuinely new, and (4) at least one additional benchmark demonstrating generality.