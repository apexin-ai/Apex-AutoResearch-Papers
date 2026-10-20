# ops eval 15pct multiseed

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-15pct-multiseed_20260522T140836_result.json`
- **Structured JSON:** [`a80d4b6a18512b340632.json`](../../sessions/a8/a80d4b6a18512b340632.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Seed 42 的 d_fixed 和 CI 与参考值吻合，确认计算一致。

```
=== Qwen 15% Contamination Multi-seed ===

Seed 42 (original): lz*_free=3.849, d_free=-6.57 [-15.19,-4.54], d_fixed=4.77 [3.96,7.76]
Seed 123 (s2):      lz*_free=4.939, d_free=-5.09 [-11.72,-3.44], d_fixed=7.79 [6.49,12.99]

2-seed stats (free-theta):
  mean |d| = 5.83
  SD = 1.05
  range = [5.09, 6.57]

2-seed stats (fixed-theta):
  mean |d| = 6.28
  SD = 2.13
  range = [4.77, 7.79]
```

s2 的 effect size 比 seed 42 更大（fixed-θ d=7.79 vs 4.77），可能因为 s2 训练的 contamination 效果更强（lz_fixed=11.87 vs 10.12）。两个 seed 的 CI 都远离 0，contamination 信号稳定。

---
