# Negative Results Audit Report

**Project**: simgate-modular-routing  
**Date**: 2026-05-18  
**Total negative experiments**: 28  

## Summary

| Category | Count | Description |
|----------|-------|-------------|
| [已讨论] | 17 | Paper already discusses (main text or appendix) |
| [应讨论] | 4 | Informative negatives, should appear in paper |
| [基础设施] | 5 | Technical failures (bugs, OOM, pipeline issues) |
| [已过时] | 2 | Superseded by later experiments |

---

## [已讨论] — 17 experiments

### 1. retry-control-baseline
- **Hypothesis**: Retry (no self-correction) reduces death rate comparably to Reflexion
- **Parent**: reflexion-internal-baseline
- **Key metrics**: DR=40.9% ≈ baseline 42.9%, success_rate=14.1%
- **Why negative**: Blind retry without self-correction provides no meaningful death reduction
- **Paper location**: §4.3 Agent Improvement Baselines (Table 2, dose-response analysis)

### 2. reflexion-internal-baseline
- **Hypothesis**: Reflexion reduces internal DR to <20% (approaching det's 16.3%), invalidating death dominance
- **Parent**: plan-012-full
- **Key metrics**: DR=31.4%, rescue_rate=29.3%, trial-1 DR=41.8%
- **Why negative**: Reflexion reduces death but 15.1pp gap to deterministic remains; death dominance persists
- **Paper location**: §4.3 Agent Improvement Baselines, Discussion §"Non-triviality of death dominance"

### 3. death-risk-routing-analysis
- **Hypothesis**: Task-type death risk threshold routing outperforms always-det
- **Parent**: plan-005-routing-patterns
- **Key metrics**: optimal_score=-11.03 vs always-det=-9.47, Δ=-1.56
- **Why negative**: Threshold routing is worse; optimal routing ≈ always-det
- **Paper location**: Discussion §"Oracle degeneracy and routing value" (oracle matches always-det on 96.3% decisions)

### 4. plan-008-v4-4b-e2e
- **Hypothesis**: 4B router (59% episode-level) exceeds always-det in end-to-end deployment
- **Parent**: plan-008-v4-4b
- **Key metrics**: score=-12.03, CI=[-17.82, -6.45] vs always-det=-9.47, fallback_rate=68%
- **Why negative**: Trained router worse than always-det; overlapping CIs but point estimate lower
- **Paper location**: §4.5 Router Training as Diagnostic Probe, end-to-end deployment paragraph

### 5–7. plan-004-ablation-b-seed{123,456,789}
- **Hypothesis**: Verify ablation-b router stability across seeds
- **Parent**: plan-004-ablation-b
- **Key metrics**: balanced_acc ≈ 57-58% across all seeds (stable but near-random)
- **Why negative**: Router discrimination near chance; confirms signal deficit, not seed artifact
- **Paper location**: §4.5 mentions 8-seed cross-validation (47.1±2.2%); aggregated

### 8. backbone-scaling-death-rate-0.5b
- **Hypothesis**: Smaller backbones have higher death rates due to limited reasoning capacity
- **Parent**: capacity-scaling-episode-eval
- **Key metrics**: DR=13.3% (2/15), Δ=-44.6pp vs 7B baseline ~58%, 12/15 score=0
- **Why negative**: 0.5B has LOWER death rate than 7B (non-monotonic); too weak to reach dangerous states
- **Paper location**: Discussion §"Scaling predictions" ("very weak models exhibit low death rates")

### 9. r7n2-supplement-100-200
- **Hypothesis**: 100%/200% data scales fill gap in data-size ablation
- **Parent**: r7n2-data-size-ablation-r3
- **Key metrics**: 100%: bal_acc=0.499, int_recall=0; 200%: bal_acc=0.500, int_recall=0
- **Why negative**: Same majority-class collapse as all other scales; data scaling does not help
- **Paper location**: §4.5 end-to-end deployment paragraph ("augmentation provides no improvement")

### 10. plan-003-e2e-ablation-b-correct
- **Hypothesis**: Trained router (correct checkpoint, internal_recall=51.52%) exceeds always-det end-to-end
- **Parent**: plan-003-implicit-eval-full
- **Key metrics**: score=-10.70 vs always-det=-9.47, Δ=-1.23, DR=17.6%, fallback_rate=70.6%
- **Why negative**: Trained router worse than always-det by 1.23 points (CI overlaps but point estimate lower)
- **Paper location**: §4.5 Baselines table (Table 3: Trained Router -10.70)

### 11. plan-003-implicit-eval-full
- **Hypothesis**: Step-level implicit routing eval achieves meaningful discrimination
- **Parent**: plan-004-ablation-b
- **Key metrics**: score=-12.84, det_recall=0.86, internal_recall=0.444
- **Why negative**: High fallback to deterministic (86% det recall); internal recall poor
- **Paper location**: §4.5 (step-level balanced accuracy flat across scales)

### 12. plan-003-eval-implicit
- **Hypothesis**: Implicit router matches or exceeds always-det end-to-end
- **Parent**: plan-003-baseline-245eps
- **Key metrics**: trained router -12.84 vs always-det -9.47, Δ=-3.37
- **Why negative**: Same finding as plan-003-implicit-eval-full; router underperforms always-det
- **Paper location**: §4.5 (overlaps with above; earlier run of same evaluation)

### 13. cross-model-guided-router-eval
- **Hypothesis**: Qwen-derived death risk labels transfer to Llama episodes (balanced_acc > 50%)
- **Key metrics**: bal_acc=1.0 (degenerate: 0 internal-preferred episodes in Llama)
- **Why negative**: Not a valid transfer test; Llama has 0 internal-preferred episodes, always-det is trivially optimal
- **Paper location**: §4.2 Multi-Model Validation (24 det-preferred, 0 internal-preferred, 46 no-pref)

### 14. r7n2-data-size-ablation-r3
- **Hypothesis**: Router balanced_acc increases with 25%–800% data scaling
- **Key metrics**: step_bal_acc 0.493–0.511, episode_bal_acc 0.495–0.515, int_recall ≈ 0 at all scales
- **Why negative**: 32× data scaling (433→13880) produces zero improvement; majority-class collapse at all scales
- **Paper location**: §4.5 ("augmentation inflates majority class without generating novel internal-preferred patterns")

### 15. majority-vote-baseline
- **Hypothesis**: Task-type majority-vote baseline ≈ router balanced_acc (47.1%)
- **Key metrics**: majority-vote bal_acc=0.50 (all 11 types majority=det), router=0.471
- **Why negative**: Router is BELOW trivial majority-vote baseline; signal entirely at task-type level
- **Paper location**: §4.5, paper_framing C2 (core claim: "below trivial majority-vote baseline 50.0%")

### 16. cross-split-robustness-8seed
- **Hypothesis**: 8-seed balanced_acc on independent splits matches corrected_eval (55.7±5.0%)
- **Key metrics**: Episode-level 47.1±2.2% vs step-level 54.1±5.4%, Δ=-7.0pp
- **Why negative**: Cross-split NOT robust; episode-level eval reveals router failure hidden by step-level metric
- **Paper location**: §4.1 sensitivity analysis ("8-seed cross-validation...47.1±2.2%...all seeds below chance")

---

## [应讨论] — 4 experiments

### 17. plan-010-cross-task-v2
- **Hypothesis**: Routing signal transfers across task-type clusters (life↔physical)
- **Parent**: plan-010-cross-task-transfer
- **Key metrics**: life→physical cross_domain_bal_acc=0.4924 (CI [0.424, 0.559]), in-domain=0.577, transfer_gap=0.085
- **Why negative**: Routing signal does NOT generalize across task-type clusters; cross-domain performance ≈ chance
- **What it reveals**: Directly validates the paper's core claim that routing signal is task-type-level, not transferable. The in-domain→cross-domain drop (0.577→0.492) quantifies the non-transferability.
- **Suggested location**: Discussion §"Why the router fails" or Appendix ablations
- **Suggested framing**: "A cross-task-type transfer experiment confirms that routing signal does not generalize across task clusters: training on life-science tasks and evaluating on physical-science tasks yields chance-level balanced accuracy (0.49), consistent with routing signal being a task-type-level property rather than a transferable step-level feature."

### 18. loto-guided-router-eval
- **Hypothesis**: LOTO protocol tests if task-type death risk generalizes as a routing feature
- **Key metrics**: blind_loto_bal_acc=0.50 (= always-det), keyword_leaked_bal_acc=0.6292
- **Why negative**: Blind LOTO routing = always-det (degenerate); keyword variant only works by leaking task identity
- **What it reveals**: Task-type death risk cannot distinguish routing decisions within unseen task types (blind = always-det). The keyword variant's 0.63 accuracy comes from implicitly recovering task identity, not from genuine step-level features.
- **Suggested location**: Appendix (near keyword routing structural failure analysis)
- **Suggested framing**: "A leave-one-task-type-out guided routing evaluation confirms that task-type-level death risk statistics cannot be applied to unseen task types (balanced accuracy = 0.50, identical to always-deterministic). A keyword-based variant achieves 0.63 by implicitly recovering task identity, further confirming that the only discriminative information operates at the task-type level."

### 19. leave-one-tasktype-out
- **Hypothesis**: Router on held-out task types ≈ 50% (random), confirming no cross-task-type transfer
- **Key metrics**: grand_mean_bal_acc=0.5976±0.0184, but 7/11 task types are SINGLE CLASS (all deterministic)
- **Why negative**: 7 of 11 task types have zero internal-preferred labels (single class), making balanced accuracy undefined or trivial. Only 4 types (grow-fruit, find-non-living-thing, lifespan-longest, melt-to-change) have two-class signal.
- **What it reveals**: The 7/11 single-class finding is a striking statistic that crystallizes why step-level routing fails: for most task types, there is literally only one class to predict. This directly supports the Discussion's "task-type-level binary property" claim with specific numbers.
- **Suggested location**: Discussion §"Why the router fails" (as a supporting statistic) or Appendix
- **Suggested framing**: "Per-task-type analysis reveals that 7 of 11 task types contain exclusively deterministic-preferred labels, leaving only 4 types with two-class signal. This extreme class imbalance at the task-type level explains the router's majority-class collapse: for most task types, there is no internal-preferred signal to learn."

### 20. plan-002-generative-v1
- **Hypothesis**: Generative router (text-generation-based) matches implicit router performance
- **Key metrics**: balanced_acc=46.67%, internal_recall=16.67% (5/30), det_recall=76.67%
- **Why negative**: Generative router performs similarly to implicit router (~47% vs ~47%); both fail
- **What it reveals**: Routing failure is signal-limited, not architecture-limited. Whether using a classification head (implicit) or text generation (generative), the router reaches the same floor. This rules out the hypothesis that a different router architecture could extract more signal from the same data.
- **Suggested location**: Appendix ablations (§Router Architecture Ablation)
- **Suggested framing**: "A generative router variant (text-generation-based, Qwen3-1.7B) achieves comparable balanced accuracy (46.7%) to the implicit classification-head router (47.1%), confirming that the routing failure is signal-limited rather than architecture-limited."

---

## [基础设施] — 5 experiments (no paper discussion needed)

### 21. plan-002-formal-v4
- **Issue**: class_weights [4.5, 0.5625] caused loss explosion in internal-containing mini-batches
- **Result**: Degenerate (all predict deterministic), accuracy=91.9% but internal_recall=0%
- **Nature**: Training bug; root cause identified and fixed in subsequent versions

### 22. plan-002-formal-v6
- **Issue**: OOM on GPU0, auto-restarted; even after removing class_weights, model degenerate on 89.7%/10.3% imbalanced data
- **Result**: f1_internal=0.0, recall_internal=0.0 after epoch 1
- **Nature**: Hardware resource contention + training instability; superseded by plan-004 series

### 23. plan-004-v4
- **Issue**: Data pipeline issues (results/plan_c_test_labels/implicit_sft.jsonl had label mapping bug)
- **Result**: Training completed but on corrupted data
- **Nature**: Data preprocessing bug; corrected in plan-004-v5 and ablation-b

### 24. plan-004-v3
- **Issue**: Two bugs fixed (class_weights removal + data regeneration) but EXIT_CODE=129
- **Result**: Intermediate step in iterative training refinement
- **Nature**: Pipeline evolution; superseded by ablation-b (correct data + correct config)

### 25. plan-002-formal-v5
- **Issue**: pad_token_id fix attempted for Qwen3-1.7B (ModelScope download missing pad_token_id)
- **Result**: Degenerate (bal_acc=0.4936, internal_recall=0%), grad_norm 604
- **Nature**: Training bug investigation; class_weights confirmed as root cause in D021

---

## [已过时] — 2 experiments

### 26. reflexion-internal-baseline-b
- **Original purpose**: Part 2 data collection (tasks 7-11) for reflexion baseline, parallel with Part 1
- **Why outdated**: Data merged into reflexion-internal-baseline (main experiment); no independent finding
- **Superseded by**: reflexion-internal-baseline (combined 220 episodes, 11 tasks)

### 27. plan-006-deep-internal
- **Original purpose**: Collect deep-internal (CoT/thinking mode) trajectories for 2-way vs 3-way routing ablation
- **Why outdated**: 3-way routing direction abandoned; paper focuses on 2-way (internal vs deterministic)
- **Superseded by**: Paper's final framing uses only 2-way comparison; 3-way was never evaluated
- **Note**: Process died 5× with no sentinel; data quality uncertain

---

## Actionable Recommendations

### Priority 1: Add to Discussion (2 experiments)

**plan-010-cross-task-v2** and **leave-one-tasktype-out** both provide quantitative evidence for the paper's core Discussion claim ("death avoidance is a task-type-level binary property"). Currently this claim is stated qualitatively. Adding one sentence each would strengthen it:

> Cross-task-type transfer yields chance-level balanced accuracy (0.49; life→physical), and 7 of 11 task types contain exclusively deterministic-preferred labels, confirming that routing signal is a task-type-level binary property with no transferable step-level structure.

### Priority 2: Add to Appendix Ablations (2 experiments)

**plan-002-generative-v1** (generative router also fails) and **loto-guided-router-eval** (LOTO blind routing = always-det) are clean ablation results that address potential reviewer questions:
- "Did you try a different router architecture?" → generative also fails (signal-limited, not architecture-limited)
- "Can task-type death statistics be used as a routing feature?" → LOTO blind = always-det (no within-type discrimination)

### Coverage Assessment

The paper covers the vast majority of informative negative results well. The 4 [应讨论] experiments would add marginal but meaningful value, primarily by providing quantitative grounding for qualitative claims already in the paper. None represent a gap that a reviewer would likely flag as missing.
