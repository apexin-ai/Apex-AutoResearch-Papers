# π0.5 VLA-only Object Baseline Results (3 seeds) — ANOMALOUS

**Status: FAILED — 0% SR on all seeds, contradicts prior 72% quick verify**
**Date: 2026-05-21**
**Server: bjb1-32546**

## Per-seed Results

| Seed | Overall SR | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice |
|------|-----------|---------------|--------------|----------------|-----------|---------|--------------|--------|------|-------------------|--------------|
| 42   | 0.0%      | 0.0%          | 0.0%         | 0.0%           | 0.0%      | 0.0%    | 0.0%         | 0.0%   | 0.0% | 0.0%              | 0.0%         |
| 43   | 0.0%      | 0.0%          | 0.0%         | 0.0%           | 0.0%      | 0.0%    | 0.0%         | 0.0%   | 0.0% | 0.0%              | 0.0%         |
| 44   | 0.0%      | 0.0%          | 0.0%         | 0.0%           | 0.0%      | 0.0%    | 0.0%         | 0.0%   | 0.0% | 0.0%              | 0.0%         |

## Aggregate
- Mean SR: **0.0% ± 0.0%**
- Total rollouts: 600 (20 per task × 10 tasks × 3 seeds)
- No crashes or errors (EXIT_CODE=0 for all)

## Prior Quick Verify (bjb2-40593, same code/model)
- **72% SR** (50 rollouts: 5 per task × 10 tasks)
- Per-task: alphabet_soup 60%, cream_cheese 100%, salad_dressing 60%, bbq_sauce 40%, ketchup 80%, tomato_sauce 40%, butter 100%, milk 40%, chocolate_pudding 100%, orange_juice 100%

## Spatial Benchmark (also on bjb1-32546)
- seed42/43/44 spatial logs also show 0% SR — same anomaly pattern.

## Root Cause Analysis

Exhaustive comparison between bjb1-32546 (0%) and bjb2-40593 (72%):

| Component | bjb1-32546 | bjb2-40593 | Match? |
|-----------|-----------|-----------|--------|
| pi05_wrapper.py | 413 lines | 413 lines | ✓ |
| evaluate.py | 802 lines | 802 lines | ✓ |
| model.safetensors | 7,473,096,344 B | 7,473,096,344 B | ✓ |
| normalizer files | 7,668 B each | 7,668 B each | ✓ |
| config.json | identical | identical | ✓ |
| PyTorch | 2.10.0+cu128 | 2.10.0+cu128 | ✓ |
| lerobot | 0.5.2 | 0.5.2 | ✓ |
| transformers | 5.8.0 | 5.8.0 | ✓ |
| Image flip fix | ✓ (line 158) | ✓ (line 158) | ✓ |
| Action queue | ✓ | ✓ | ✓ |
| SmolVLA evals | 12% (normal) | — | env OK |

**All checked components are identical. Root cause unknown.**

## Hypotheses
1. GPU architecture difference — bfloat16 flow matching numerical divergence
2. Hidden env variable or system library difference
3. GPU driver version affecting bfloat16 matmul

## Recommended Next Steps (URGENT — CoRL DDL 2026-05-29)
1. **Re-run π0.5 eval on bjb2-40593** — priority path
2. Check GPU types with nvidia-smi on both servers
3. Add action value logging to compare outputs
4. If bjb2-40593 works, use it for all π0.5 experiments
