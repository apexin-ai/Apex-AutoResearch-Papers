# analysis eval mag obsonly norm003 b2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-obsonly-norm003-b2_20260516T004734_result.json`
- **Structured JSON:** [`0fe7ecae89329bae9c7a.json`](../../sessions/0f/0fe7ecae89329bae9c7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE(success)。

## 结果汇报

**数据来源**: `/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json`

### 10-task Final SR: **34%** (34/100)

### Per-task breakdown

| Task | SR | Successes |
|---|---|---|
| between_plate_and_ramekin | 0.9 | 9/10 |
| next_to_ramekin | **1.0** | 10/10 |
| next_to_cookie_box | 0.8 | 8/10 |
| on_cookie_box | 0.3 | 3/10 |
| next_to_plate | 0.3 | 3/10 |
| in_top_drawer | 0.1 | 1/10 |
| from_table_center | 0.0 | 0/10 |
| on_ramekin | 0.0 | 0/10 |
| on_stove | 0.0 | 0/10 |
| on_wooden_cabinet | 0.0 | 0/10 |

### Obs-only Spatial Magnitude Sweep 完整对比

| norm | SR (10-task) |
|---|---|
| **0.03** | **34%** |
| 0.05 | 35% |
| 0.10 | 35% |
| 0.20 | 35% |
| 0.30 | 36% |

### 分析

Magnitude sweep 结论非常清晰：**obs_only CRM 对 correction magnitude 几乎不敏感**。从 norm=0.03 到 norm=0.30（10倍跨度），SR 仅在 34%-36% 之间波动，差异在统计噪声范围内。

norm=0.03 的 34% 比 partial 8-task 数据（38.75%）低，因为新增的两个 task（next_to_plate: 0.3, on_wooden_cabinet: 0.0）拉低了均值。

关键发现：即使 correction 被限制到极小的 0.03 norm，obs_only 模式的表现与大 norm 几乎一致。这说明 obs_only CRM 的有效性不依赖于 correction 幅度——模型本质上在做某种"方向性"修正而非"幅度性"修正，或者修正本身就很小使得 norm clipping 基本不生效。

---
