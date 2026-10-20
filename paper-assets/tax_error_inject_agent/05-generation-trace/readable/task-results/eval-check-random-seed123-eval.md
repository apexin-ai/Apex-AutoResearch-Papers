# eval check random seed123 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-random-seed123-eval_20260515T002619_result.json`
- **Structured JSON:** [`570254c88ebcaa844265.json`](../../sessions/57/570254c88ebcaa844265.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。结果汇总：

**v4-random-seed123-eval: DONE (negative)**

| 指标 | 值 |
|------|-----|
| **Overall success_rate** | **68.1% (32/47)** |

**Per-task breakdown:**

| Task Type | Success/Total | Rate |
|-----------|:---:|:---:|
| look_at_obj_in_light | 5/6 | 83.3% |
| pick_heat_then_place | 6/8 | 75.0% |
| pick_two_obj_and_place | 5/7 | 71.4% |
| pick_clean_then_place | 7/11 | 63.6% |
| pick_and_place_simple | 5/8 | 62.5% |
| pick_cool_then_place | 4/7 | 57.1% |

**Multi-seed Random SFT 汇总:**

| Seed | Success Rate |
|------|:-----------:|
| 42 | 66.0% |
| 0 | 55.3% |
| 123 | **68.1%** |
| **Mean** | **63.1%** |

Multi-seed 平均 63.1% < vanilla 65.3%，Random SFT 无显著提升，conclusion=negative。

---
