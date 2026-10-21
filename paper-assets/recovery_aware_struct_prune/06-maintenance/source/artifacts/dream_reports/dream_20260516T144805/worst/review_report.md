---
dream_id: dream_20260516T144805
tier: worst
overall_score: 3/6 Reject
timestamp: 2026-05-16T15:46:36.876347+00:00
---

# Dream Review Report: "Structured Pruning Breaks RLVR Alignment"

**Dream ID:** 20260516T144805
**Review Mode:** Full (2 Reviewers + Roundtable)
**Venue Standard:** Top ML venue, ~25% acceptance rate, 6-point scale

---

## Roundtable Summary

Two independent reviewers (R1: Methods+Experiments, R2: Novelty+Related Work) converged on **3/6 (Reject)** with **4/5 confidence**. The paper documents a real and interesting failure mode — GRPO training collapse on structurally pruned reasoning models — but falls below top-venue bar due to insufficient statistical rigor, predictable core finding, and an empirically null method contribution (RASP).

---

## R1 Review: Methods and Experiments

### Summary
The experimental campaign is extensive (4 pruning methods, 2 models, 3 sparsity levels, multiple ablations) and the paper honestly reports null results throughout. However, the statistical foundations are narrow: most method comparisons are non-significant, collapse timing lacks variance estimates, and the correlation r≈0.95 between collapse speed and post-SFT quality is computed on only 4 data points.

### Strengths
- **Reward-accuracy decoupling is well-demonstrated**: Unpruned model reward 0→0.661 with identical 1072/1319 correct at step 0 and step 100 is striking and cleanly shown.
- **Structured vs. unstructured dichotomy (Table 3)**: Unstructured-20% sustains stable GRPO for 100 steps while all structured methods collapse. This is the cleanest experimental result.
- **Four pruning methods + unstructured control**: Breadth across RASP, Standard, Bonsai, GRASPrune provides convincing evidence of universality of collapse.
- **Honest null result reporting**: SFT gap p=0.25, multi-seed p=0.15, CKA R²=0.014 are transparently reported without overclaiming.
- **Alpha ablation (Table 7)**: Post-prune and post-SFT accuracy anti-correlate (r=-0.45), directly falsifying CKA as a useful pruning proxy. This is a valuable negative result.
- **Multiple sparsity levels**: 20%/25%/30% show the collapse gradient vanishing at higher sparsity, which is informative even though it weakens the mechanism claim.

### Weaknesses
- **No variance estimation on collapse timing**: Tables 2/8/9 report single-number collapse steps (e.g., "step ~10", "step ~60"). Without multiple GRPO training seeds, these are point estimates with unknown stochastic variation. The 6x ratio (step 10 vs step 60) could easily shift to 2-3x or 10x+ under different random seeds.
- **Reward-accuracy decoupling may be a greedy-vs-sampling artifact**: GRPO optimizes the sampling policy (temp=0.7) but evaluation uses greedy decoding. The reward improvement may legitimately improve pass@k or majority voting accuracy while leaving the greedy mode unchanged. This alternative explanation is never addressed.
- **r=0.95 correlation is statistically vacuous**: Computed on 4 data points (4 pruning methods). Any monotonic-ish relationship across 4 points yields r>0.8. This cannot support the causal claim "collapse speed is determined by model quality."
- **RASP contribution is empirically null at every measurement point**: Post-prune gap 4pp (p=0.38), post-SFT gap 2.2pp (p=0.25), multi-seed Cohen's d=0.42 (p=0.15), CKA R²=0.014 (p=0.31), scoring ablation +2pp (p=0.41). The paper proposes a method that its own experiments cannot distinguish from baselines.
- **Single GRPO configuration**: One learning rate, one temperature, beta=0 (no KL penalty). Beta=0 is aggressive and may independently cause training instability. Without GRPO hyperparameter ablation, the "fundamental failure" claim is premature.
- **Cross-model results undermine claims**: Qwen2.5-Math-7B at 25% shows collapse ratio 1.14x (vs 6.0x on DeepSeek-R1 at 20%). The severity gradient is not reproducible across models or sparsity levels.
- **Inference speedup undermines practical motivation**: 1.14-1.16x speedup for ~20pp accuracy loss (Table 13). No practitioner would make this trade.
- **Multi-seed analysis (Table 4) is underpowered**: N=5 paired t-test has extremely low power; p=0.15 with Cohen's d=0.42 cannot distinguish a real 2.7pp effect from noise.

### Questions for Authors
1. Have you evaluated GRPO accuracy using sampling-based decoding (pass@k, majority voting)? The reward-accuracy "decoupling" may be a greedy-decode artifact.
2. What is the variance of collapse onset across GRPO training seeds? Can you provide confidence intervals from 3-5 independent runs?
3. How sensitive is collapse timing to GRPO hyperparameters (learning rate, KL penalty β>0, temperature)?
4. For the unpruned model, you report exactly identical predictions (1072/1319) before and after 100 GRPO steps. Did you verify this is not a checkpoint loading artifact?
5. Why was beta=0 (no KL penalty) chosen? This is unusually aggressive and may independently cause training instability.

### Missing Experiments
- **Multiple GRPO seeds** (3-5 per condition) — the single most critical gap
- **Sampling-based evaluation** (pass@k, majority@k) — would disambiguate the decoupling finding
- **GRPO hyperparameter ablation** (especially β>0) — would establish robustness of collapse
- **Larger model scale** (13B/14B) — generalization beyond 7B
- **Per-layer collapse analysis** — which layers collapse first? Mechanistic insight
- **Controlled Self-Healing replication** — direct comparison to the work being challenged

### R1 Score: 3/6 | Confidence: 4/5

---

## R2 Review: Novelty and Related Work

### Summary
The paper documents GRPO training collapse on structurally pruned reasoning models and proposes RASP (CKA-aware pruning) as a diagnostic tool. The core empirical finding is moderately novel but predictable from policy gradient theory — removing entire computational pathways reduces rollout diversity, which is fatal for advantage estimation in GRPO. The RASP method contribution is thin given it provides no significant advantage at any measurement point.

### Strengths
- **Genuinely surprising reward-accuracy decoupling**: If confirmed (i.e., not a greedy-vs-sampling artifact), this challenges assumptions in the RLVR-for-pruning literature.
- **Clean structured vs. unstructured isolation**: Localizing the collapse to structured pruning is a useful empirical contribution.
- **Multi-method comparison**: Testing 4+ methods at same sparsity provides convincing universality evidence.
- **Honest pivot from positive to negative framing**: The paper evolved from "RASP enables better recovery" to "structural pruning breaks RLVR" based on evidence. This scientific honesty is commendable.

### Weaknesses
- **Core finding is predictable from RL theory**: Structured pruning removes entire functional units, reducing the model's ability to generate diverse completions. GRPO requires variance across group samples to estimate advantages — zero variance means zero gradients. This is a direct consequence of how policy gradient methods work, not a surprising empirical discovery.
- **Reward-accuracy decoupling novelty is questionable**: The unpruned model is already at 81% on GSM8K. With binary reward and 100 training steps, a flat accuracy trajectory is unsurprising — the model may already be near its greedy-decode ceiling on this benchmark. The paper does not disambiguate between (a) fundamental GRPO limitation, (b) GSM8K saturation, and (c) greedy-vs-sampling evaluation mismatch.
- **RASP's contribution is unclear given its empirical failure**: The paper proposes a scoring function (S(h) = I(h)×(1-F(h))^α) whose CKA component adds 2pp (p=0.41) over gradient-only scoring. The alpha ablation shows CKA optimizes the wrong proxy (r=-0.45 between post-prune and post-SFT accuracy). As a "diagnostic tool," the collapse severity gradient only appears at one sparsity on one model.
- **Self-Healing comparison is incomplete**: Self-Healing tests structured (layer-level) pruning in their Table 2, not only unstructured. The paper should directly address these results rather than claiming Self-Healing is "only unstructured."
- **Missing important related work context**:
  - GRPO/RLHF reward hacking literature (Gao et al. 2022 reward over-optimization curves)
  - Test-time compute scaling literature — does GRPO improve pass@k even if not greedy accuracy?
  - Semi-structured (2:4/N:M) pruning as a middle ground
  - Iterative prune-tune approaches that may avoid collapse
- **Circular reasoning in collapse correlation**: Collapse speed correlates with post-SFT model quality — but this may simply mean "weaker models are less stable under RL training," which is trivially expected and does not uniquely implicate redundancy as a mechanism.

### Assessment of Novelty
The paper's two claimed contributions have limited novelty. (1) Reward-accuracy decoupling on unpruned models may be a known phenomenon under a new name (reward over-optimization / reward hacking when the model is already near ceiling). (2) GRPO collapse on structurally pruned models is predictable: structured pruning removes entire attention heads and MLP neurons, reducing the model's capacity to generate diverse rollouts, which kills advantage estimation. The RASP method is empirically null and the "Redundancy-Stability Tradeoff" framing overstates what is fundamentally an observation that more damaged models are less trainable. For a top venue, the paper would need either (a) deeper mechanistic analysis connecting collapse to specific representational properties, or (b) a proposed mitigation that actually works.

### Assessment of Related Work
The related work section covers structured pruning, RLVR, and pruning-recovery interaction adequately but has notable gaps:
1. Self-Healing's structured pruning results are mischaracterized — they do test structured pruning
2. GRPO reward hacking / over-optimization literature is entirely absent
3. No discussion of semi-structured pruning as an intermediate between structured and unstructured
4. Pass@k evaluation is standard in RLVR papers and its absence weakens the comparison to prior work

### R2 Score: 3/6 | Confidence: 4/5

---

## Roundtable Step 3: Convergence

### Points of Full Agreement
1. **Score: 3/6 (Reject)**. Both reviewers independently arrived at this score.
2. **RASP is empirically null.** At every measurement point (post-prune, post-SFT, multi-seed, CKA correlation, scoring ablation), RASP vs Standard is statistically indistinguishable.
3. **Missing GRPO seed variance is the most critical gap.** Collapse timing is reported as point estimates from single runs. The 6x ratio claim is unsupported without confidence intervals.
4. **Greedy-vs-sampling evaluation may explain reward-accuracy decoupling.** Pass@k or majority voting evaluation is essential to disambiguate this finding.
5. **r=0.95 on 4 points is not statistical evidence.** The "collapse correlates with model quality" claim needs more data points.
6. **Cross-model results undermine the severity gradient claim.** Qwen2.5-Math-7B shows near-identical collapse for all methods at 25%.
7. **Honest null result reporting is the paper's strongest quality.** The scientific transparency is commendable.
8. **Beta=0 GRPO is aggressive.** KL-constrained GRPO (β>0) may prevent collapse entirely, which would invalidate the "fundamental" framing.

### Points of Disagreement (resolved)
- R2 argues the finding is "predictable from RL theory"; R1 gives more credit to empirical documentation value. **Resolution**: Even predictable findings have value when first documented empirically, but the bar for a top venue requires either deeper mechanism or proposed fix — the paper provides neither.
- R1 emphasizes confounded experimental timeline more; R2 focuses on positioning gaps. **Resolution**: Both are valid but secondary to the core statistical and novelty concerns.

---

## Roundtable Step 4: Final Consolidated Assessment

### Overall Score: 3/6 (Reject)
### Confidence: 4/5

### Decision Rationale
The paper identifies a real phenomenon — GRPO training collapse on structurally pruned reasoning models — and documents it with commendable experimental breadth and scientific honesty. However, three fundamental issues prevent acceptance:

1. **Insufficient statistical rigor for core claims.** Collapse timing is reported without variance estimates (single GRPO runs). The correlation r=0.95 is computed on 4 data points. RASP vs Standard comparisons are non-significant at every measurement point. The 6x collapse ratio (20% sparsity, DeepSeek-R1) does not replicate at 25% sparsity (1.5x) or on Qwen2.5-Math-7B (1.14x).

2. **The most interesting finding (reward-accuracy decoupling) has an unaddressed confound.** GRPO optimizes the sampling policy but is evaluated with greedy decoding. Without pass@k or majority voting evaluation, the "decoupling" may simply reflect that GRPO improves sampling diversity without changing the mode — which is expected behavior, not a pathology.

3. **Limited novelty and no actionable contribution.** The RASP method is empirically null. The collapse phenomenon is predictable from policy gradient theory (diversity collapse kills advantage estimation). The paper offers no mitigation — only "don't use GRPO on pruned models" — which limits impact. The "Redundancy-Stability Tradeoff" framing overstates what is observed: weaker models are less stable under RL training.

### What Would Raise the Score
- **To 4/6 (Borderline):** Add (a) 3-5 GRPO seeds per condition with confidence intervals on collapse timing, (b) pass@k evaluation to disambiguate the decoupling finding, (c) GRPO hyperparameter ablation (especially β>0).
- **To 5/6 (Accept):** Additionally provide (d) a proposed mitigation that demonstrably prevents or delays collapse, (e) mechanistic analysis connecting collapse to specific representational properties (not just "weaker = faster collapse"), (f) results on a truly independent model architecture (not Qwen-family).

### Experiment Coverage Assessment
The paper covers 13 of the 18 planned experiments from the design document. Key gaps:
- Inference speedup and OOD evaluation are included but support negative conclusions about practical value
- CKA reliability analysis is included and further undermines RASP (32% decision instability)
- The alpha ablation is the most damaging result for RASP: CKA optimizes the wrong proxy (r=-0.45)
- Cross-model results are included but undermine rather than support the severity gradient claim

### Summary Verdict
A well-executed empirical study with honest negative results, but the findings are either (a) predictable (collapse), (b) potentially artifactual (reward-accuracy decoupling under greedy eval), or (c) empirically null (RASP). The paper's strongest contribution — documenting that structured pruning universally breaks GRPO training — is worth publishing but needs stronger statistical foundations and ideally a proposed solution to clear the top-venue bar.
