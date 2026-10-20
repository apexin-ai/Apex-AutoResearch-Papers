# monitor 008e v3 s1 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_008e_v3_s1_progress_20260514T221248_result.json`
- **Structured JSON:** [`d274237a62f36330daab.json`](../../sessions/d2/d274237a62f36330daab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_008e_v3_walker_s1

```
STATUS: RUNNING
CURRENT_STEP: ~88000
PROGRESS: 83.8% (88K / 105K)
FPS: 6.5
ETA: ~44 min

EVAL_TRAJECTORY:
  step  | eval_return | value_mean | ve_ratio
  5000  |   31.00     |    0.00    |  0.00
  15000 |  131.17     |    4.00    |  0.03
  25000 |  155.69     |    (*)     |   -
  35000 |  276.47     |    (*)     |   -
  45000 |  382.22     |    (*)     |   -
  55000 |  486.84     |    (*)     |   -
  65000 |  580.67     |    (*)     |   -
  75000 |  574.09     |  300.51    |  0.52
  85000 |  657.31     |  351.33    |  0.53

(*) value_mean truncated in output — middle checkpoints available if needed.

NOTES:
- gate_dt_mean=1.0 throughout (gate_fixed_dt=1, gate_subsample_max_dt=2 config)
- No checkpoint.ckpt file yet (written at end)
- Steady improvement: eval_return 31→657 over 85K steps
- v/e ratio stabilizing around 0.52-0.53 at recent checkpoints
```

## exp_009a_baseline_walker_s2

```
STATUS: RUNNING
CURRENT_STEP: ~335000
PROGRESS: 67% (335K / 500K)
FPS: 7.4
ETA: ~6.2 hours

LATEST_EVAL_RETURN: 930.61 (at 325K)

EVAL_TRAJECTORY (last 10 checkpoints):
  step   | eval_return
  245000 |  950.32
  255000 |  936.90
  265000 |  937.27
  275000 |  934.78
  285000 |  960.20
  295000 |  947.46
  305000 |  937.80
  315000 |  948.66
  325000 |  930.61

NOTES:
- Baseline (no gate) run, seed 2
- Performance plateaued around 930-960 since ~245K
- Peak eval_return: 960.20 at step 285K
```

---
