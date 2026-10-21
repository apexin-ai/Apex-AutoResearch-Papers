# analyze westd pi05 vla only goal s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_westd-pi05-vla-only-goal-s42_20260526T083355_result.json`
- **Structured JSON:** [`9d7ee929e19b2927abc3.json`](../../sessions/9d/9d7ee929e19b2927abc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇报

**westd-pi05-vla-only-goal-s42 — Overall SR: 97.5% (195/200)**

### 与 4090 同 seed 对比
| 硬件 | SR | 差异 |
|------|-----|------|
| 4090 (eval-pi05-vla-only-goal-s42) | 95.5% | baseline |
| westd RTX PRO 6000 (本次) | 97.5% | **+2.0pp** |

westd 比 4090 高 2pp，方向与 D158 发现的 ~3pp 系统性偏差一致（量级相近），但方向相反——VLA-only baseline 在 westd 上反而更高。这说明硬件偏差可能不是单向的，而是 task/mode 相关。

### Per-task 明细
| Task | SR |
|------|-----|
| open_the_middle_drawer_of_the_cabinet | 95% |
| put_the_bowl_on_the_stove | 100% |
| put_the_wine_bottle_on_top_of_the_cabinet | 100% |
| open_the_top_drawer_and_put_the_bowl_inside | **90%** |
| put_the_bowl_on_top_of_the_cabinet | 100% |
| push_the_plate_to_the_front_of_the_stove | 95% |
| put_the_cream_cheese_in_the_bowl | 100% |
| turn_on_the_stove | 100% |
| put_the_bowl_on_the_plate | 100% |
| put_the_wine_bottle_on_the_rack | 95% |

7/10 tasks 满分，最低的是 open_top_drawer_put_bowl_inside (90%)。无 W&B run。

---
