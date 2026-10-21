# analysis eval openvla l2norm k07 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_openvla_l2norm_k07_goal_seed42_20260526T164209_result.json`
- **Structured JSON:** [`55bb9e3d5640c6f36142.json`](../../sessions/55/55bb9e3d5640c6f36142.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结果总结

**Overall SR: 68.4% (342/500)** — conclusion: **success**（≥67.3% 阈值）

**Goal cliff curve 完整数据：**

| k (保留比例) | Vision tokens | SR | 相对 baseline |
|---|---|---|---|
| 1.0 (baseline) | 256 | 74.8% | — |
| 0.9 | 230 | 74.8% | 0.0pp |
| 0.85 | 218 | 75.4% | +0.6pp |
| **0.7** | **179** | **68.4%** | **-6.4pp** |

**关键发现：** Cliff 在 k=0.85→0.7 之间出现。k=0.85 时性能完全无损甚至微升，但 k=0.7 时下降 6.4pp，性能衰减加速。特别是 Task 4（open drawer + put bowl inside）崩塌至 16%，说明复杂多步任务对 token 数量更敏感。

---
