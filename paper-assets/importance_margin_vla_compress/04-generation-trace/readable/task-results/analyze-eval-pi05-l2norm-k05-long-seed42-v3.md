# analyze eval pi05 l2norm k05 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k05_long_seed42_v3_20260523T213109_result.json`
- **Structured JSON:** [`72d81e4ec15e51f2c538.json`](../../sessions/72/72d81e4ec15e51f2c538.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

RESULT:
- **overall_sr: 51.4%**
- **per_task:**
  - T0 put both the alphabet soup and the tomato sauce in the basket: **58%**
  - T1 put both the cream cheese box and the butter in the basket: **60%**
  - T2 turn on the stove and put the moka pot on it: **82%**
  - T3 put the black bowl in the bottom drawer of the cabinet and close it: **44%**
  - T4 put the white mug on the left plate and put the yellow and white mug on the right plate: **32%**
  - T5 pick up the book and place it in the back compartment of the caddy: **52%**
  - T6 put the white mug on the plate and put the chocolate pudding to the right of the plate: **28%**
  - T7 put both the alphabet soup and the cream cheese box in the basket: **54%**
  - T8 put both moka pots on the stove: **16%**
  - T9 put the yellow and white mug in the microwave and close it: **88%**
- **total_episodes: 500** (10 tasks × 50 eps)
- **elapsed: 154.8 min**
- **anomalies:**
  - T8 (put both moka pots on the stove) SR=16% — 明显低于其他 task，可能是该 task 本身难度高（需要精确放置两个物体）
- **comparison: v1 was 50.2%, v3 = 51.4% (Δ=+1.2pp)** — CPU RNG 修复后结果与 v1 基本一致，差异在正常波动范围内，验证了 L2norm k=0.5 在 Long 套件的稳定性

---
