# analyze eval pi05 l2norm k085 long seed43 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k085_long_seed43_v3_20260525T133243_result.json`
- **Structured JSON:** [`cba81a92d5170a3256f6.json`](../../sessions/cb/cba81a92d5170a3256f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**π0.5 L2Norm k=0.85 Long seed43: SR = 80.0% (400/500)**

| Task | SR |
|---|---|
| T0 put both alphabet soup and tomato | 96% |
| T1 put both cream cheese and butter | 92% |
| T2 turn on stove put moka pot | 86% |
| T3 put black bowl in bottom drawer | **100%** |
| T4 put white mug on left plate | 78% |
| T5 pick up book place in back | 98% |
| T6 put white mug on plate and put | **14%** |
| T7 put both alphabet soup and cream | 90% |
| T8 put both moka pots on stove | 52% |
| T9 put yellow white mug in microwave | 94% |

### 与 seed42 (78.0%) 对比

seed43 = **80.0%** vs seed42 = **78.0%**，差距 +2%，在正常 seed 方差范围内。两个 seed 结果高度一致，确认 L2norm k=0.85 性能稳定。

### Conclusion: **success**

理由：seed43 (80.0%) 与 seed42 (78.0%) 差距仅 2%，跨 seed 表现一致。同时与 L2norm k=0.9 (~81%) 形成单调下降趋势 (81% → 79% 均值 at k=0.85)，验证了 L2norm pruning 的平滑降级特性。

---
