# analyze eval openvla random k085 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_random_k085_long_seed42_v3_20260526T143107_result.json`
- **Structured JSON:** [`523b7773354497f19e72.json`](../../sessions/52/523b7773354497f19e72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验结果：OpenVLA Random k=0.85 Long (libero_10) seed42**

**Overall SR: 45.2% (226/500)**

10 tasks 各 50 episodes 全部完成，无错误。

| Task | SR |
|---|---|
| 1. alphabet soup + tomato sauce → basket | 66.0% (33/50) |
| 2. cream cheese + butter → basket | 56.0% (28/50) |
| 3. stove + moka pot | 66.0% (33/50) |
| 4. black bowl → drawer + close | 34.0% (17/50) |
| 5. white mug left + yellow mug right | 22.0% (11/50) |
| 6. book → caddy | 78.0% (39/50) |
| 7. white mug plate + chocolate pudding | 20.0% (10/50) |
| 8. alphabet soup + cream cheese → basket | 66.0% (33/50) |
| 9. both moka pots → stove | 30.0% (15/50) |
| 10. yellow mug → microwave + close | 14.0% (7/50) |

**与已知数据点对比（Long suite）：**

| 方法 | SR |
|---|---|
| Random k=0.9 | 46.8% |
| **Random k=0.85** | **45.2%** |
| Random k=0.7 | 38.8% |
| L2norm k=0.85 | 38.8% |

Random k=0.85 比 k=0.9 仅降 1.6pp，仍显著优于 L2norm k=0.85（+6.4pp），符合预期的单调递减趋势。

---
