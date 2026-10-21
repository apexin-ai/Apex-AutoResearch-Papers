# exp028c_selfguide_recipe Full Metrics Report

**Generated**: 2026-05-16 11:30 UTC
**W&B Run ID**: 4yu6qz1m
**PID**: 824675 (running, uptime ~6h)

## Status

- **Training is RUNNING** (step 7 rollout in progress)
- **Last completed step**: 6 (train only)
- **Last completed val**: step 5
- **Total elapsed**: 18506s (~5h 8m) at end of step 6
- **Average step time**: ~3014s (~50.2 min)
- **Estimated step 7 completion**: ~11:36 UTC (May 16)
- **Estimated total completion**: ~May 19 15:00 UTC (93 steps remaining × 50 min)
- **No checkpoints saved yet**

## Train Step Metrics

| Step | success | pass@8 | action_is_valid | action_is_effective | entropy | kl_loss | grad_norm | time_s |
|------|---------|--------|-----------------|---------------------|---------|---------|-----------|--------|
| 1 | 13.28% | 37.5% | 76.43% | 96.37% | 0.2634 | 0.0128 | 16.88 | 3252 |
| 2 | 6.25% | 25.0% | 83.20% | 97.87% | 0.2470 | 0.1706 | 17.30 | 3123 |
| 3 | 15.63% | 68.75% | 85.95% | 98.18% | 0.2488 | 0.1118 | 12.57 | 2733 |
| 4 | 18.75% | 62.5% | 87.94% | 98.62% | 0.2340 | 0.0312 | 14.53 | 2767 |
| 5 | 9.38% | 37.5% | 89.60% | 98.50% | 0.2364 | **0.8240** | 13.08 | ~3614 |
| 6 | 10.94% | 31.25% | 90.43% | 98.98% | 0.2337 | 0.0983 | 12.54 | 3010 |

## Val Step Metrics

| Step | success | pass@1 | action_is_valid | action_is_effective | reward_mean |
|------|---------|--------|-----------------|---------------------|-------------|
| 0 | 6.25% | 6.25% | 74.49% | 95.0% | 0.119 |
| 5 | 6.25% | 6.25% | 96.50% | 100.0% | 0.518 |

## Trend Analysis

### Positive
- **action_is_valid**: steady climb 76.4% → 90.4% (train), 74.5% → 96.5% (val)
- **action_is_effective**: 96.4% → 99.0% (train), 95% → 100% (val)
- **manager_invalid_action**: decreasing (3.6% → 1.0%)
- **entropy**: stable around 0.23-0.26, no collapse

### Concerning
- **kl_loss spike at step 5**: 0.824 (8x normal), recovered to 0.098 at step 6
- **train success volatile**: 13.3% → 6.3% → 15.6% → 18.8% → 9.4% → 10.9%
- **val success flat at 6.25%** across 5 training steps (step 0 vs step 5)
- **pass@8 peaked at step 3** (68.75%) then declined to 31.25% at step 6

### No Anomalies
- No OOM errors
- No crashes
- No NaN values
- grad_norm stable (12-17 range)

## MVP Assessment (preliminary, 6/100 steps)

Current train success range: 6.25% - 18.75% (mean ~12.4%)
Current val success: 6.25% (unchanged from baseline)

At this pace, **not on track for MVP pass** (20%+ success needed). The model is learning valid actions (action_is_valid climbing steadily) but not translating that into task completion. The pass@8 decline after step 3 suggests the diversity of successful strategies is narrowing.

## Raw Timing

| Step | train_step_s | eval_step_s | train_total_s | eval_total_s | total_s |
|------|-------------|-------------|---------------|--------------|---------|
| 1 | 3252 | 0 | 3252 | 0 | 3252 |
| 2 | 3123 | 0 | 6375 | 0 | 6378 |
| 3 | 2733 | 0 | 9108 | 0 | 9113 |
| 4 | 2767 | 0 | 11875 | 0 | 11883 |
| 5 | ~3147 | ~447 | ~15022 | 447 | ~15497 |
| 6 | 3010 | 0 | 18032 | 447 | 18506 |

## Additional Metrics (Step 6 snapshot)

- critic/score/mean: 0.622
- critic/advantages/mean: -0.012
- critic/advantages/max: 7.34
- response_length/mean: 669 tokens
- perf/throughput: 683 tokens/s
- perf/total_num_tokens: 4.1M per step
