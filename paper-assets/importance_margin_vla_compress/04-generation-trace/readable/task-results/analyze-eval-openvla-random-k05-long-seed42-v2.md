# analyze eval openvla random k05 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_random_k05_long_seed42_v2_20260526T151649_result.json`
- **Structured JSON:** [`d59c81f365856d759822.json`](../../sessions/d5/d59c81f365856d759822.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

**Overall SR: 18.6% (93/500)** — conclusion: **negative**

对比 baseline (k=1.0) 46.8%，random k=0.5 下降 **28.2 个百分点（-60%相对降幅）**。

| Task | SR |
|------|----|
| T1 alphabet soup + tomato sauce → basket | 30.0% |
| T2 cream cheese + butter → basket | 26.0% |
| T3 stove + moka pot | 22.0% |
| T4 black bowl → drawer | 2.0% |
| T5 white mug left + yellow mug right | 6.0% |
| T6 book → caddy | 44.0% |
| T7 white mug plate + chocolate pudding | 26.0% |
| T8 alphabet soup + cream cheese → basket | 16.0% |
| T9 moka pots → stove | 8.0% |
| T10 yellow white mug → microwave | 6.0% |

OpenVLA Long cliff curve 目前：k=1.0 → 46.8%, k=0.7 → 38.8%, k=0.5 → 18.6%。k=0.5 到 k=0.7 之间存在明显的性能悬崖，随机剪枝在 50% 压缩率下性能崩塌严重。

---
