# analyze eval obs only spatial norm02 seed43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-spatial-norm02-seed43-r2_20260519T194726_result.json`
- **Structured JSON:** [`dc91f4c8c6bf229e390f.json`](../../sessions/dc/dc91f4c8c6bf229e390f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成，EXIT_CODE=0，10 个 tasks 各 10 rollouts = 100 total，无异常。

## 结果汇总

**Overall success rate: 34.0% (34/100)**

### Per-task success rates

| Task | Success Rate |
|------|-------------|
| between_plate_and_ramekin → plate | 90.0% (9/10) |
| next_to_ramekin → plate | **100.0%** (10/10) |
| from_table_center → plate | 0.0% (0/10) |
| on_cookie_box → plate | 30.0% (3/10) |
| in_top_drawer_wooden_cabinet → plate | 0.0% (0/10) |
| on_ramekin → plate | 0.0% (0/10) |
| next_to_cookie_box → plate | **100.0%** (10/10) |
| on_stove → plate | 0.0% (0/10) |
| next_to_plate → plate | 20.0% (2/10) |
| on_wooden_cabinet → plate | 0.0% (0/10) |

### 与已有 Spatial K=10 obs_only 结果对比

| Seed | Success Rate |
|------|-------------|
| seed42 | 35.0% |
| **seed43 (本次)** | **34.0%** |
| seed44 | 36.0% |
| seed45 | 34.0% |
| seed46 | 33.0% |
| seed47 | 32.0% |
| **均值 (6 seeds)** | **34.0%** |

seed43 = 34.0%，与其他 seeds 高度一致（32%-36% 范围内），均值 34.0%。分布呈现典型的两极化：3 个 task 成功率 ≥ 90%，5 个 task 成功率 = 0%，说明 obs_only CRM 对 spatial 任务的泛化存在明显的 task-specific 瓶颈。

---
