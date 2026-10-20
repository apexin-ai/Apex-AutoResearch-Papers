# submit d022 phaseA execute

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_d022-phaseA-execute_20260515T093007_result.json`
- **Structured JSON:** [`d5414d3f2f8f3ebc78fe.json`](../../sessions/d5/d5414d3f2f8f3ebc78fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## Eval 结果

| 实验 | success_rate | successes/total |
|------|-------------|-----------------|
| **v4-taxei-fixed-inject25-s0-eval** | **0.468** | 22/47 |
| **v4-taxei-fixed-inject25-s123-eval** | **0.468** | 22/47 |

### Per-task 明细

| task_type | s0 | s123 |
|-----------|-----|------|
| look_at_obj_in_light | 4/6 (0.667) | 4/6 (0.667) |
| pick_and_place_simple | 2/8 (0.250) | 3/8 (0.375) |
| pick_clean_then_place_in_recep | 5/11 (0.455) | 5/11 (0.455) |
| pick_cool_then_place_in_recep | 2/7 (0.286) | 1/7 (0.143) |
| pick_heat_then_place_in_recep | 6/8 (0.750) | 6/8 (0.750) |
| pick_two_obj_and_place | 3/7 (0.429) | 3/7 (0.429) |

## 训练已提交

| 实验 | GPU | PID |
|------|-----|-----|
| **v4-random-fixed-inject25-s0** | cuda:0 | 134514 |
| **v4-random-fixed-inject25-s123** | cuda:1 | 134594 |

Registry 已更新，两个训练在 autodl-5090 上运行中。

---
