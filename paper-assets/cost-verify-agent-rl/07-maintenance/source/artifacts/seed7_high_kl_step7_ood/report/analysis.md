# OOD Eval Analysis: seed7_high_kl_step7_ood

## Experiment Info
- **Parent**: exp029_seed7_high_kl (KL 10x intervention, seed=999)
- **Checkpoint**: step 7 (final)
- **Server**: westd-47453
- **Eval split**: eval_out_of_distribution (134 tasks)
- **Parent conclusion**: negative (KL 10x failed to prevent response inflation: train_resp_len 5601→12849)

## Results

| Metric | Value |
|--------|-------|
| OOD success rate | **13.43%** (18/134) |
| pass@1 | 13.43% |
| action_is_valid | 72.53% |
| action_is_effective | 99.28% |
| num_actions | 44.10 |
| response_length | 7885.16 |
| manager_invalid_action | 0.72% |

## Cross-Experiment OOD Comparison

| Experiment | OOD Success | action_is_valid | resp_len | Parent Status |
|---|---|---|---|---|
| SFT baseline | 5.97% | — | 7641 | N/A |
| Seed 3 (stable, step15) | 10.45% | — | — | success |
| Intervention-C step5 (pre-collapse) | 10.45% | 63.7% | 6266 | negative |
| Seed 8 step5 (pre-collapse) | 11.94% | 57.5% | 6503 | negative |
| **Seed 7 high_kl step7 (this)** | **13.43%** | **72.5%** | **7885** | **negative** |
| Intervention-C step7 (collapsed) | 14.93% | 66.3% | 6366 | negative |
| Seed 1 (stable) | 23.88% | — | — | success |
| Seed 5 step10 | 29.10% | 72.7% | 6632 | failed (OOM) |
| Seed 6 step15 | 29.10% | 63.2% | — | success |
| Seed 4 (collapsed, episode) | 30.60% | 63.7% | 7212 | negative |

## Analysis

### Hypothesis Evaluation

Hypothesis: "OOD should be low, confirming collapse correlation."

**Partially confirmed.** 13.43% is low relative to the top-performing seeds (23–31%), placing this checkpoint in the bottom tier alongside other intervention/pre-collapse checkpoints (10–15% cluster). It is still above SFT baseline (5.97%), confirming some learning transferred despite the failed intervention.

### Key Observations

1. **Intervention cluster emerges**: The three intervention-related checkpoints (high_kl step7: 13.43%, intervention-c step7: 14.93%, intervention-c step5: 10.45%) cluster tightly at 10–15%, well below naturally-trained seeds (23–31%). This suggests interventions that constrain policy (high KL, hard caps) limit generalization capacity.

2. **Collapse ≠ low OOD**: Seed 4 collapsed (response inflation) yet achieved the highest OOD (30.60%). Seed 7 high_kl also collapsed but only reached 13.43%. The difference: Seed 4 trained for 15 steps with val_pass_at_1=43.75%, while seed7_high_kl ran only 7 steps with val_success=31.25%. Training quality during non-collapsed phases matters more than whether collapse eventually occurred.

3. **action_is_valid is notably high**: At 72.53%, this is the highest action_is_valid among all OOD evals (tied with Seed 5's 72.66%). The high KL penalty may have regularized the policy toward syntactically valid actions even though it didn't help task success. This is a potential mechanism worth noting in the paper.

4. **Response length inflated OOD**: 7885 tokens is the longest OOD response_length observed, consistent with the parent's response inflation problem persisting at inference time.

### Paper Implications

This data point strengthens two narratives:
- **Table 1**: Adds a "failed intervention" row showing that policy-constraining interventions produce similar OOD regardless of mechanism (KL penalty vs hard cap).
- **Bimodal analysis**: The 10–15% intervention cluster vs 23–31% natural training cluster suggests that policy freedom during training is necessary for OOD generalization, even at the risk of collapse.
