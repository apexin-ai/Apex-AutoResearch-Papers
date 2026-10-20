# analysis v4 random fixed inject50 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-random-fixed-inject50-eval_20260515T015730_result.json`
- **Structured JSON:** [`698f12c4b9e9a6f6b209.json`](../../sessions/69/698f12c4b9e9a6f6b209.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果: v4-random-fixed-inject50-eval

**模型**: `checkpoint-1635` (random_fixed_inject50/v0-20260515-084528)
**评估集**: valid_unseen, 47 tasks
**注入模式**: none (纯净评估)
**退出码**: 0 (正常退出)
**W&B**: 无

### 总成绩: 27/47 = 57.4%

### 按任务类型:

| 任务类型 | 成功/总数 | 成功率 |
|----------|-----------|--------|
| look_at_obj_in_light | 5/6 | 83.3% |
| pick_two_obj_and_place | 6/7 | 85.7% |
| pick_heat_then_place_in_recep | 6/8 | 75.0% |
| pick_cool_then_place_in_recep | 3/7 | 42.9% |
| pick_and_place_simple | 3/8 | 37.5% |
| pick_clean_then_place_in_recep | 4/11 | 36.4% |

简单任务（look_at、pick_two、pick_heat）表现较好（75-86%），涉及清洁和放置的复杂任务（pick_clean、pick_and_place）成功率偏低（36-38%）。所有失败 episode 均跑满 50 步超时。

---
