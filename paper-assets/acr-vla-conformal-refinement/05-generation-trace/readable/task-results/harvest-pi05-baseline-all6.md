# harvest pi05 baseline all6

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_pi05-baseline-all6_20260521T121929_result.json`
- **Structured JSON:** [`d3e73a4c158d10b0c330.json`](../../sessions/d3/d3e73a4c158d10b0c330.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个实验已更新为 DONE/success。汇总：

## π0.5 VLA-only Baseline 结果

### Object (LIBERO-Object, 10 tasks × 20 rollouts)

| Experiment | Seed | Success Rate |
|---|---|---|
| eval-pi05-vla-only-object-seed42-r3 | 42 | 82.0% |
| eval-pi05-vla-only-object-seed43-r3 | 43 | 81.5% |
| eval-pi05-vla-only-object-seed44-r3 | 44 | 81.0% |
| **Mean ± Std** | | **81.5% ± 0.5%** |

### Spatial (LIBERO-Spatial, 10 tasks × 20 rollouts)

| Experiment | Seed | Success Rate |
|---|---|---|
| eval-pi05-vla-only-spatial-seed42-r3 | 42 | 84.5% |
| eval-pi05-vla-only-spatial-seed43-r3 | 43 | 83.0% |
| eval-pi05-vla-only-spatial-seed45 | 45 | 85.0% |
| **Mean ± Std** | | **84.2% ± 1.0%** |

### Per-task 细节

**Object 难点任务**（跨 seed 一致偏低）：
- tomato_sauce: 55-60%
- salad_dressing: 60-70%

**Spatial 难点任务**：
- bowl_on_the_ramekin: 20-30%（最难）
- bowl_in_top_drawer: 60-75%

D105 记录的 Object 81.5%±0.5% **完全一致**。Registry 已全部更新为 DONE。

---
