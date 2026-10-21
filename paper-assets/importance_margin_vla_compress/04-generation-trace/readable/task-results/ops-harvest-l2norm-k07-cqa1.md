# ops harvest l2norm k07 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-l2norm-k07-cqa1_20260527T161530_result.json`
- **Structured JSON:** [`65266b4627f9a705df63.json`](../../sessions/65/65266b4627f9a705df63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

**π0.5 L2norm k=0.7 Long strict seed42** — **SR = 63.2%**（316/500），耗时 251.7 min

Per-task: T0=76%, T1=90%, T2=72%, T3=46%, T4=56%, T5=80%, T6=52%, T7=58%, T8=8%, T9=94%

Cliff curve 中间点定位：strict 模式下 L2norm k=0.7 的 63.2% 与 lenient 模式完全一致，说明该 keep ratio 下没有 lenient/strict 差异。对比 cliff curve：k=0.85 strict=70.8% → **k=0.7 strict=63.2%** → k=0.5 lenient=49.2%，从 k=0.85 到 k=0.7 下降 7.6pp，曲线在此区间仍呈平缓下降。

---
