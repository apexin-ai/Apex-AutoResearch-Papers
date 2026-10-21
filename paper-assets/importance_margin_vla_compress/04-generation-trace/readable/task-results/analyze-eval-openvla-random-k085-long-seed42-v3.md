# analyze eval openvla random k085 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_random_k085_long_seed42_v3_20260527T004517_result.json`
- **Structured JSON:** [`d42ff4589197ef4fa642.json`](../../sessions/d4/d42ff4589197ef4fa642.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，status=DONE, conclusion=success。

**结果汇总：**

| k ratio | Overall SR | Δ vs baseline |
|---------|-----------|---------------|
| 1.0 (baseline) | 52.8% | — |
| 0.9 | 46.8% | -6.0pp |
| **0.85** | **45.0%** | **-7.8pp** |
| 0.7 | 38.8% | -14.0pp |

Random pruning 的 cliff curve 在 LIBERO-Long 上呈渐进下降，没有单一 cliff edge。k=0.9→0.85 仅降 1.8pp，但 k=0.85→0.7 降 6.2pp，说明加速退化区间在 k<0.85。v3 结果 (45.0%) 与 v2 (45.2%) 高度一致，确认可复现。

---
