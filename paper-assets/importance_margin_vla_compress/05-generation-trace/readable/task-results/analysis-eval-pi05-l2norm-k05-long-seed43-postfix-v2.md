# analysis eval pi05 l2norm k05 long seed43 postfix v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_l2norm_k05_long_seed43_postfix_v2_20260525T201704_result.json`
- **Structured JSON:** [`2993cbc789b14faf2944.json`](../../sessions/29/2993cbc789b14faf2944.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果总结

**Overall SR: 53.0%** (265/500)

| Task | SR |
|------|-----|
| T0 alphabet soup + tomato | 64% |
| T1 cream cheese + butter | 64% |
| T2 stove + moka pot | 72% |
| T3 black bowl → drawer | 46% |
| T4 white mug + plate | 40% |
| T5 book → back | 50% |
| T6 white mug + plate (variant) | 38% |
| T7 alphabet soup + cream | 58% |
| T8 both moka pots → stove | 10% |
| T9 yellow mug → microwave | 88% |

**Cross-seed 对比：seed43 (53.0%) vs seed42 (50.2-51.4%) → delta +1.6~2.8pp，在 ±5pp 内，一致性验证通过。**

L2norm k=0.5 在 50% token pruning 下稳定保持 ~51-53% SR，跨 seed 可复现。

---
