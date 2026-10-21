# analysis pi05 l2norm k05 spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05_l2norm_k05_spatial_20260521T210443_result.json`
- **Structured JSON:** [`67745e283582e620d90a.json`](../../sessions/67/67745e283582e620d90a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Conclusion: **success**.

## 结论

**π0.5 L2norm k=0.5 Spatial SR = 55.6%** (278/500, 108.9min)

Per-task SR: T0=74%, T1=82%, T2=78%, T3=28%, T4=38%, T5=44%, T6=32%, T7=74%, T8=62%, T9=44%

**跨 suite 对比：**

| Method | Object | Spatial |
|--------|--------|---------|
| Random k=0.5 | 69.4% | 71.6% |
| L2norm k=0.5 | 33.4% | 55.6% |
| Gap (random - L2norm) | **36.0pp** | **16.0pp** |

两个 suite 上 random 均显著优于 L2norm（Object 36pp, Spatial 16pp），method preference (random >> L2norm at k=0.5) **跨 suite 一致**。

不过 Spatial 上 L2norm 的降幅（16pp）远小于 Object（36pp），说明 L2norm 在 Spatial 任务上保留了更多有用信息——可能因为 spatial reasoning 对 vision token 的 norm distribution 依赖模式不同于 object manipulation。

---
