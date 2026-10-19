# analyze eval supp adapt tau025 spatial s44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318_result.json`
- **Structured JSON:** [`7463904d488fea55f04d.json`](../../sessions/74/7463904d488fea55f04d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。结果汇总：

**eval-supp-adapt-tau025-spatial-s44** — Adaptive CRM τ=0.25, LIBERO-Spatial, seed=44

| Metric | Value |
|--------|-------|
| **Overall SR** | **80.5%** (161/200) |
| trigger_rate | 20.0% |
| mean_unc | 0.1881 |

**Per-task SR:**

| Task | SR |
|------|-----|
| bowl_from_table_center | 100% |
| bowl_on_cookie_box | 100% |
| bowl_next_to_cookie_box | 100% |
| bowl_next_to_ramekin | 95% |
| bowl_on_wooden_cabinet | 95% |
| bowl_between_plate_and_ramekin | 90% |
| bowl_on_stove | 80% |
| bowl_next_to_plate | 80% |
| bowl_in_top_drawer | 65% |
| bowl_on_ramekin | 0% |

**3-seed 汇总 (τ=0.25, Spatial):**

| Seed | SR | Trigger Rate |
|------|----|-------------|
| 42 | 82.0% | 19.4% |
| 43 | 80.0% | 19.4% |
| 44 | 80.5% | 20.0% |
| **Mean** | **80.83%** | **19.6%** |

vs VLA-only baseline 79.8%±1.2% → Adaptive CRM 一致性地优于 baseline，conclusion=**success**。

---
