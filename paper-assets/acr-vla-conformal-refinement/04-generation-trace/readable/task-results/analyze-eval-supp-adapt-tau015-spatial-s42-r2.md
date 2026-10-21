# analyze eval supp adapt tau015 spatial s42 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-adapt-tau015-spatial-s42-r2_20260523T061528_result.json`
- **Structured JSON:** [`0fe6bc4945878b58d209.json`](../../sessions/0f/0fe6bc4945878b58d209.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。结果汇总：

## eval-supp-adapt-tau015-spatial-s42-r2 结果

| 指标 | 值 |
|------|-----|
| **Overall SR** | **80.5%** (161/200) |
| **Trigger rate** | **40.7%** |
| **Mean uncertainty** | 0.1852 |
| **Conclusion** | success (> baseline 78.5%) |
| W&B | 无 |

### Per-task SR

| Task | SR |
|------|-----|
| between_plate_and_ramekin | 100% |
| from_table_center | 95% |
| on_cookie_box | 95% |
| next_to_cookie_box | 95% |
| next_to_ramekin | 90% |
| on_stove | 90% |
| on_wooden_cabinet | 85% |
| next_to_plate | 80% |
| in_top_drawer | 75% |
| **on_ramekin** | **0%** |

### Tau sweep 汇总

| tau | SR | trigger_rate |
|-----|-----|-------------|
| 0.075 (默认) | 81% | 91.8% |
| **0.15** | **80.5%** | **40.7%** |
| 0.25 | 82% | 19.4% |
| 0.35 | 进行中 |

tau=0.15 将 trigger rate 从 91.8% 大幅降至 40.7%，SR 仅下降 0.5pp，效率收益显著。`on_ramekin` task 在所有配置下都是 0%，是任务本身的硬瓶颈而非 tau 的问题。

---
