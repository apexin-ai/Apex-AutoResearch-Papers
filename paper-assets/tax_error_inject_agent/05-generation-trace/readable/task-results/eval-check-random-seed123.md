# eval check random seed123

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-random-seed123_20260515T002611_result.json`
- **Structured JSON:** [`b338a3235fa7088beb63.json`](../../sessions/b3/b338a3235fa7088beb63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。v4-random-seed123-eval 结果汇总：

**v4 Random SFT — 3-seed 完整结果**

| Seed | Success Rate |
|------|-------------|
| 42 | 66.0% |
| 0 | 55.3% |
| 123 | **68.1%** |
| **Mean** | **63.1%** |

**seed=123 per-task breakdown (32/47)**

| Task Type | Success | Rate |
|-----------|---------|------|
| look_at_obj_in_light | 5/6 | 83.3% |
| pick_heat_then_place | 6/8 | 75.0% |
| pick_two_obj_and_place | 5/7 | 71.4% |
| pick_clean_then_place | 7/11 | 63.6% |
| pick_and_place_simple | 5/8 | 62.5% |
| pick_cool_then_place | 4/7 | 57.1% |

seed=123 是三个 seed 中最高的，3-seed 均值 63.1%。

---
