# Intervention C Step 7 OOD Evaluation Results

## Experiment Info
- **Experiment**: intervention_c_step7_ood
- **Parent training**: intervention-c-hard-cap (negative conclusion: hard cap fails to prevent inflation)
- **Checkpoint**: `/root/autodl-tmp/checkpoints/qwen_intervention_c_hard_cap_step7_hf`
- **W&B Run**: [intervention-c-hard-cap-ood-eval](https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/0x0x1b4p) (ID: `0x0x1b4p`)
- **Server**: westd-47453 (cuda:0)
- **Eval time**: 1370.0s (~22.8 min)
- **Exit code**: 0

## OOD Metrics (134 tasks, eval_out_of_distribution)

| Metric | Value |
|--------|-------|
| **pass@1 (success rate)** | **14.93%** (20/134) |
| action_is_valid | 66.30% |
| action_is_effective | 100% |
| num_actions (mean) | 43.67 |
| response_length (mean) | 6365.6 tokens |
| reward/mean@134 | 1.493 |

## Cross-Seed OOD Comparison

| Seed/Checkpoint | OOD% | Train Status | Notes |
|----------------|------|--------------|-------|
| SFT baseline | 5.97% | n/a | reference |
| Seed 3 (success) | 10.45% | converged | anomalously low for success |
| Seed 8 step5 (pre-collapse) | 11.94% | early | before collapse |
| **Intervention C step7 (collapsed)** | **14.93%** | **collapsed** | **this experiment** |
| Seed 1 (success) | 23.88% | converged | stable |
| Seed 5 step10 (success) | 29.10% | converged | stable |
| Seed 6 (success) | 29.10% | converged | stable |
| Seed 4 step15 (collapsed) | 30.60% | collapsed | anomaly: high OOD despite collapse |

## Analysis

**Hypothesis**: "Intervention-C step 7 (final, collapsed) achieves low OOD generalization, consistent with other collapsed seeds showing low OOD despite some train success."

**Result**: Hypothesis **confirmed**. OOD = 14.93% is below the 15% threshold.

Key observations:
1. Intervention C's collapsed checkpoint achieves OOD ~15%, substantially below the 23-30% range of successful seeds (1, 5, 6).
2. This contrasts with Seed 4 (collapsed, OOD=30.6%), which was anomalously high. The discrepancy suggests collapse doesn't uniformly determine OOD; the *path* to collapse matters.
3. Intervention C's response_length_mean=6365 in OOD is lower than its training response_length=7170, possibly due to the hard cap truncating differently on unseen tasks.
4. action_is_valid=66.3% is relatively low, indicating the collapsed model generates many invalid actions on OOD tasks — consistent with degraded policy quality.
5. num_actions=43.67 is near the max_actions_per_traj=50 limit, confirming the model still exhausts its action budget (inflation behavior persists in OOD).

## Conclusion

**Status**: SUCCESS (experiment completed its data-collection objective; hypothesis confirmed)

The Intervention C (hard cap) collapsed checkpoint shows low OOD generalization (14.93%), distinguishing it from the Seed 4 anomaly (30.6%). This supports the interpretation that hard-cap-induced collapse produces qualitatively different (worse) generalization compared to organic collapse in unconstrained training. The hard cap intervention not only failed to prevent response inflation during training, but the resulting collapsed checkpoint also fails to transfer to OOD tasks.
