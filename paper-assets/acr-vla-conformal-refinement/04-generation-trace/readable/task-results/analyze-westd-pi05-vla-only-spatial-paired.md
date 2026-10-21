# analyze westd pi05 vla only spatial paired

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_westd-pi05-vla-only-spatial-paired_20260526T124625_result.json`
- **Structured JSON:** [`32774432e91bcb87ccf1.json`](../../sessions/32/32774432e91bcb87ccf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 registry 已更新完成（之前已有 metrics/conclusion/checkpoint_path/log_path，状态已确认为 DONE）。

## π0.5 VLA-only Spatial (westd paired) 结果

| seed | success_rate | n_rollouts | total_rollouts |
|------|-------------|------------|----------------|
| 42   | 98.0%       | 20         | 200            |
| 43   | 97.5%       | 20         | 200            |
| 44   | 98.5%       | 20         | 200            |
| **mean±std** | **98.0±0.5%** | — | — |

### Per-task 成功率

| Task | s42 | s43 | s44 | mean |
|------|-----|-----|-----|------|
| between_plate_and_ramekin | 100% | 100% | 100% | 100% |
| next_to_ramekin | 100% | 100% | 100% | 100% |
| from_table_center | 100% | 100% | 100% | 100% |
| on_cookie_box | 100% | 100% | 100% | 100% |
| in_top_drawer | 100% | 95% | 100% | 98.3% |
| **on_ramekin** | **90%** | **80%** | **85%** | **85.0%** |
| next_to_cookie_box | 95% | 100% | 100% | 98.3% |
| on_stove | 100% | 100% | 100% | 100% |
| next_to_plate | 100% | 100% | 100% | 100% |
| on_wooden_cabinet | 95% | 100% | 100% | 98.3% |

**关键发现**：π0.5 Spatial VLA-only **98.0±0.5%**，远高于 SmolVLA 的 79.3±0.8%。唯一弱点是 `on_ramekin` task（85.0%），其余 9 个 task 均 ≥95%。

Registry 更新状态：三个实验均已更新为 DONE/success。

---
