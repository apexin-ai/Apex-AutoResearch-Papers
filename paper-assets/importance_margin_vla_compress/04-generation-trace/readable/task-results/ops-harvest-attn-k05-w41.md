# ops harvest attn k05 w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-attn-k05-w41_20260527T145133_result.json`
- **Structured JSON:** [`cdd19a8d68528756edf6.json`](../../sessions/cd/cdd19a8d68528756edf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。实验结果：

**π0.5 Attention k=0.5 Long strict seed42 — avg SR = 52.0%**

| Task | SR |
|---|---|
| T0 put both alphabet soup and tomato | 70% |
| T1 put both cream cheese and butter | 44% |
| T2 turn on stove put moka pot | 76% |
| T3 put black bowl in bottom drawer | 66% |
| T4 put white mug on left plate | 48% |
| T5 pick up book place in back | 50% |
| T6 put white mug on plate | 12% |
| T7 put both alphabet soup and cream | 54% |
| T8 put both moka pots on stove | 20% |
| T9 put yellow white mug in microwave | 80% |

耗时 156.7 min，500 episodes，260 成功。与 L2norm k=0.5 的 50.0% 接近（Attention 52.0% 略高 2pp），说明在极端压缩（50% token）下两种方法性能差距不大。

---
