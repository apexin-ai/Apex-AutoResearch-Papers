# analysis d166 trigger rate extraction

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d166-trigger-rate-extraction_20260526T172608_result.json`
- **Structured JSON:** [`d389b716c3e778ff216c.json`](../../sessions/d3/d389b716c3e778ff216c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已获取。pi05 Spatial Adaptive 不存在于任何服务器。

## 汇总

### SmolVLA Adaptive (tau=0.25)

| Suite | Seed | trigger_rate | crm_applied_steps | total_steps | SR | mean_uncertainty | 来源 |
|-------|------|-------------|-------------------|-------------|------|-----------------|------|
| Spatial | 42 | **19.65%** | 5,610 | 28,550 | 79.5% | 0.1857 | bjb1-32546 |
| Goal (K2) | 42 | **8.78%** | 2,508 | 28,562 | 83.5% | 0.1466 | bjb1-32546 |
| Object | 43 | **3.67%** | 1,312 | 35,796 | 77.5% | 0.1103 | bjb1-32546 |
| Long | 43 | **4.50%** | 3,276 | 72,765 | 58.0% | 0.1252 | bjb1-32546 |

### pi05 Adaptive (tau=0.25)

| Suite | Seed | trigger_rate | crm_applied_steps | total_steps | SR | mean_uncertainty | 来源 |
|-------|------|-------------|-------------------|-------------|------|-----------------|------|
| Goal | 42 | **8.12%** | 2,119 | 26,108 | 89.5% | 0.1152 | cqa1-32758 |
| Object | 42 | **3.68%** | 1,250 | 33,946 | 85.5% | 0.0842 | cqa1-32758 |
| Long | 42 | **3.94%** | 2,493 | 63,274 | 80.5% | 0.0870 | bjb1-18228 |
| **Spatial** | — | **N/A** | — | — | — | — | **不存在** |

### 关键发现

1. **JSON 中有完整 trigger rate 数据** — 所有有效的 adaptive eval JSON 都包含 `adaptive_stats` 块，含 `trigger_rate`、`total_steps`、`crm_applied_steps`、`mean_uncertainty`

2. **trigger_rate 与 suite 难度正相关** — Spatial 最高 (19.65%)，Goal 次之 (~8%), Object/Long 最低 (~3.7-4.5%)，与 mean_uncertainty 排序一致

3. **pi05 的 mean_correction_norm 恒为 0.2000** — 这是 norm_max 的硬上界，说明 pi05 CRM 每次触发都给出最大修正

4. **缺失数据**：
   - pi05 Spatial Adaptive — 三台服务器上都没有此实验
   - bjb1-18228 的 `eval_goal_adaptive_pi05_seed42.json` SR=0.0 且无 adaptive_stats（OOM 失败产物）

---
