# analysis exp 008e v3 s3

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_008e_v3_s3_20260518T112231_result.json`
- **Structured JSON:** [`1171a673dab81a1d0125.json`](../../sessions/11/1171a673dab81a1d0125.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Checkpoint confirmed. Here's the full analysis:

```
CONCLUSION: negative (COLLAPSED with CIVO)
FINAL_EVAL: 92.7
PEAK_EVAL: 520.4@85K
FINAL_VE: 2.635
FINAL_NVE: 5.00× (baseline V/E from seed1 = 0.527)
GATE_DT_MEAN: 1.000
GATE_DT_1_FRAC: 1.000
COLLAPSE_ONSET: ~85K-95K. eval dropped 520.4→379.2 (27%) between 85K-95K, then crashed to 92.7 (82% from peak) at 105K. V/E accelerated 0.511→0.734→2.635. CIVO detector fired at 105K.
CHECKPOINT_PATH: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s3/latest.pt (confirmed, 220MB)

EVAL_TRAJECTORY: [
  {step: 5000, eval_return: 36.1},
  {step: 15000, eval_return: 180.0},
  {step: 25000, eval_return: 279.8},
  {step: 35000, eval_return: 272.2},
  {step: 45000, eval_return: 276.8},
  {step: 55000, eval_return: 268.6},
  {step: 65000, eval_return: 465.5},
  {step: 75000, eval_return: 421.1},
  {step: 85000, eval_return: 520.4},
  {step: 95000, eval_return: 379.2},
  {step: 105000, eval_return: 92.7}
]

VALUE_TRAJECTORY: [
  {step: 5000, value_mean: 0.00},
  {step: 15000, value_mean: 4.04},
  {step: 25000, value_mean: 32.04},
  {step: 35000, value_mean: 71.00},
  {step: 45000, value_mean: 108.00},
  {step: 55000, value_mean: 145.54},
  {step: 65000, value_mean: 182.84},
  {step: 75000, value_mean: 230.00},
  {step: 85000, value_mean: 265.72},
  {step: 95000, value_mean: 278.19},
  {step: 105000, value_mean: 244.29}
]

VE_TRAJECTORY: [
  {step: 15000, ve: 0.022, nve: 0.04},
  {step: 25000, ve: 0.114, nve: 0.22},
  {step: 35000, ve: 0.261, nve: 0.50},
  {step: 45000, ve: 0.390, nve: 0.74},
  {step: 55000, ve: 0.542, nve: 1.03},
  {step: 65000, ve: 0.393, nve: 0.75},
  {step: 75000, ve: 0.546, nve: 1.04},
  {step: 85000, ve: 0.511, nve: 0.97},
  {step: 95000, ve: 0.734, nve: 1.39},
  {step: 105000, ve: 2.635, nve: 5.00}
]

ACTOR_ENTROPY_TRAJECTORY: [
  {step: 5000, actor_entropy: 8.237},
  {step: 15000, actor_entropy: 2.235},
  {step: 25000, actor_entropy: -1.559},
  {step: 35000, actor_entropy: -2.570},
  {step: 45000, actor_entropy: -3.852},
  {step: 55000, actor_entropy: -4.186},
  {step: 65000, actor_entropy: -3.167},
  {step: 75000, actor_entropy: -3.260},
  {step: 85000, actor_entropy: -3.854},
  {step: 95000, actor_entropy: -4.213},
  {step: 105000, actor_entropy: -4.892}
]

NOTES:
- seed 3 COLLAPSED, matching seed 2's pattern. Collapse rate now 2/4 (50%).
- Collapse pattern: eval plateaued 270-280 range (25K-55K), broke through to 520@85K, then crashed. Value kept climbing monotonically (0→278) while eval collapsed, causing V/E spike.
- vs seed 2: similar onset window (seed2 peaked 715@85K crashed to 137@105K; seed3 peaked 520@85K crashed to 92.7@105K). Both collapsed around 85K-95K.
- vs healthy seeds 0,1: those reached 869.9@105K with ve~0.527. seed3 peaked at only 520 before collapsing.
- Gate locked at dt=1 throughout (all seeds same), confirming gate provides no adaptive escape.
- Actor entropy monotonically declining to -4.9, lower than typical healthy runs, suggesting policy collapse into narrow mode.
- NVE=5.0× is worse than seed 2's 3.78×, indicating more severe value overestimation relative to actual performance.
- 50% collapse rate with this configuration strongly suggests trained dt_emb + dt=1 imagination is unstable.
```

---
