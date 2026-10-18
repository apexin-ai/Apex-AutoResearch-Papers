# ops harvest l2norm k095 s43 w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-l2norm-k095-s43-w38_20260527T160337_result.json`
- **Structured JSON:** [`d39733073f489bdb4e01.json`](../../sessions/d3/d39733073f489bdb4e01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

**π0.5 L2norm k=0.95 Long seed43** — **85.8%** (seed42=86.2%, Δ=-0.4pp)

| Task | SR |
|---|---|
| T0 alphabet soup + tomato | 98% |
| T1 cream cheese + butter | 98% |
| T2 stove + moka pot | 94% |
| T3 black bowl → drawer | 96% |
| T4 white mug → left plate | 94% |
| T5 book → back | 94% |
| T6 white mug → plate + ... | 44% |
| T7 alphabet soup + cream | 94% |
| T8 both moka pots → stove | 56% |
| T9 yellow mug → microwave | 90% |

耗时 135.6 min，500 episodes / 429 success。两个 seed 均值 **86.0% ± 0.2pp**，非常稳定。T6 和 T8 仍是两个弱项 task（两 seed 一致的 pattern）。

---
