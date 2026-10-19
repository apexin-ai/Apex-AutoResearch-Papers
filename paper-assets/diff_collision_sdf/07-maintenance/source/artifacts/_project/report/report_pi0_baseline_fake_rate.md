# Pi0 Baseline Fake Safety Rate Analysis

**Date**: 2026-05-25
**Threshold**: FROZEN_THRESHOLD = 0.0001 (0.1mm max EE displacement)
**Definition**: fake_safe = not collided AND max_displacement < 0.0001

## Summary Table

| Model | Suite | Episodes | Collision% | Fake Safe% | Real Safe% | Non-collided Frozen% |
|-------|-------|----------|-----------|-----------|-----------|---------------------|
| **Pi0 Full-FT** | object | 200 | 17.0% | **82.5%** | 0.5% | 99.4% |
| **Pi0 Full-FT** | spatial | 800 | 100.0% | 0.0% | 0.0% | N/A (all collided) |
| **Pi0 LoRA** | object | 200 | 10.0% | **89.0%** | 1.0% | 98.9% |
| **Pi0 LoRA** | spatial | 200 | 100.0% | 0.0% | 0.0% | N/A (all collided) |
| A1 LoRA (rerun) | object | 800 | 8.5% | **91.1%** | 0.4% | 99.6% |
| A1 LoRA | spatial | 800 | 99.2% | 0.8% | 0.0% | 100.0% |
| A3 | object | 800 | 22.9% | **76.4%** | 0.8% | 99.0% |
| A3 (v11 200ep) | object | 200 | 25.5% | **73.0%** | 1.5% | 98.0% |

## Key Findings

### 1. Fake safety is inherent to Pi0, not introduced by A1/A3

Pi0 baseline models exhibit extreme fake_safe rates on the object suite:
- **Pi0 Full-FT**: 82.5% fake safe (165/200 episodes frozen with < 0.1mm displacement)
- **Pi0 LoRA**: 89.0% fake safe (178/200 episodes frozen)

Among non-collided episodes, **99.4% (Full-FT) and 98.9% (LoRA) are frozen** — the robot simply does not move.

### 2. A1 does not make fake safety worse

A1 LoRA fake_safe_rate (91.1%) is comparable to Pi0 LoRA baseline (89.0%). The slight increase is within noise. The frozen behavior is a property of the base Pi0 model encountering safety-constrained scenarios, not a consequence of the SDF-based collision loss.

### 3. Spatial suite: 100% collision, no fake safety to analyze

Both Pi0 baselines collide on every episode in the spatial suite. There are no non-collided episodes to classify as fake/real safe. The spatial tasks are fundamentally harder — obstacles are always in the path.

### 4. Displacement distribution

For non-collided episodes across all models:
- Median displacement: ~5e-09 (5 nanometers — essentially zero motion)
- Max displacement among "frozen" episodes: < 0.0001
- The gap between frozen (~1e-09) and moving (~0.0005) is 6 orders of magnitude — the threshold is robust

## Conclusion

**Fake safety is a fundamental property of Pi0 in safety-constrained environments.** When Pi0 encounters obstacles it cannot navigate around, it freezes (outputs near-zero actions). This produces high CAR (collision avoidance rate) but zero TSR (task success rate). A1 and A3 inherit this behavior from the base model — they do not introduce it.

## Source Files

- `baseline_v11_eval_safelibero_object_all_levelII_best_seed0.json` — Pi0 Full-FT, object
- `baseline_fullft_v11_eval_safelibero_spatial_all_levelII_best_seed0.json` — Pi0 Full-FT, spatial
- `eval_safelibero_object_all_levelII_best_lora_baseline_seed0.json` — Pi0 LoRA, object
- `eval_safelibero_spatial_all_levelII_best_lora_baseline_seed0.json` — Pi0 LoRA, spatial
- `a1_rerun_v11_eval_safelibero_object_all_levelII_best_lora_baseline_seed0.json` — A1 LoRA, object (800 ep)

### Note: Incomplete data

`lora_baseline_v11_eval_safelibero_object_all_levelII_best_seed0.json` was reconstructed from logs and lacks per-episode data (only task-level averages). Its task-level avg_max_displacement values (0.0, 0.007, 0.0072, 0.0257) suggest a mix of frozen and moving episodes, but cannot be decomposed into fake/real without per-episode data.
