# ops harvest attn k07 w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-attn-k07-w41_20260527T154709_result.json`
- **Structured JSON:** [`10817957a99b45003b38.json`](../../sessions/10/10817957a99b45003b38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果汇总：

**eval_pi05_attn_k07_long_seed42_strict_w41 — 正常完成**

| 指标 | 值 |
|------|-----|
| **Avg SR** | **53.6%** |
| Total | 268/500 |
| Elapsed | 167.7 min |

**Per-task SR:**

| Task | SR |
|------|-----|
| T0 put both alphabet soup and tomato | 78% |
| T1 put both cream cheese and butter | 84% |
| T2 turn on stove put moka pot | 64% |
| T3 put black bowl in bottom drawer | 44% |
| T4 put white mug on left plate | 46% |
| T5 pick up book place in back | 20% |
| T6 put white mug on plate | 72% |
| T7 put both alphabet soup and cream | 48% |
| T8 put both moka pots on stove | 2% |
| T9 put yellow white mug in microwave | 78% |

**同系列对比（Attn Long strict）：** k=0.85→50.0%, k=0.75→49.8%, **k=0.7→53.6%**, k=0.5→52.0%。Attn 在 strict 模式下继续保持极高稳定性，k=0.7 甚至略高于 k=0.85/0.75，再次印证 Attention pruning 的 graceful degradation 特性。

---
