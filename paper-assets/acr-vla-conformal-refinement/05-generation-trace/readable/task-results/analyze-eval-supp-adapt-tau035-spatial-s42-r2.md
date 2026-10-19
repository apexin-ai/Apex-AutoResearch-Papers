# analyze eval supp adapt tau035 spatial s42 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-adapt-tau035-spatial-s42-r2_20260523T061940_result.json`
- **Structured JSON:** [`d25e3a3e7af76ab28306.json`](../../sessions/d2/d25e3a3e7af76ab28306.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，实验标记为 DONE (success)。

**结果摘要：**

| Metric | Value |
|--------|-------|
| overall_sr | **80.0%** (160/200) |
| trigger_rate | 12.17% |
| mean_unc | 0.1873 |
| conformal_threshold | 0.35 |
| max_correction_norm | 0.2 |
| crm_applied_steps | 3,474 / 28,549 (12.2%) |

**Per-task SR:**

| Task | SR |
|------|-----|
| between_plate_and_ramekin | 95% |
| next_to_ramekin | 100% |
| from_table_center | 90% |
| on_cookie_box | 95% |
| in_top_drawer | 70% |
| on_ramekin | 0% |
| next_to_cookie_box | 95% |
| on_stove | 85% |
| next_to_plate | 85% |
| on_wooden_cabinet | 85% |

**对比：** tau=0.35 以仅 12.2% 的 trigger rate 达到 80.0% SR，超过 baseline (78.5%) 和 always-on CRM (79.0%)。在 tau 系列中效率最高——触发最少但提升依然有效。

---
