# analysis v4 random fixed inject10 s1 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-random-fixed-inject10-s1-eval_20260515T212711_result.json`
- **Structured JSON:** [`d9b8f21550d7dae7d674.json`](../../sessions/d9/d9b8f21550d7dae7d674.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v4-random-fixed-inject10-s1-eval 结果：**

- **Success rate: 68.1% (32/47)**
- 无错误，EXIT_CODE=0

| Task Type | Success | Total | Rate |
|---|---|---|---|
| look_at_obj_in_light | 5 | 6 | 83.3% |
| pick_and_place_simple | 5 | 8 | 62.5% |
| pick_clean_then_place_in_recep | 5 | 10 | 50.0% |
| pick_cool_then_place_in_recep | 6 | 7 | 85.7% |
| pick_heat_then_place_in_recep | 7 | 8 | 87.5% |
| pick_two_obj_and_place | 4 | 7 | 57.1% |

**Random 10% 四个 seed 汇总：**
- seed=42: 68.1%
- seed=0: 66.0%
- seed=1: **68.1%**
- seed=123: 55.3%

seed=1 与 seed=42 持平，均为最高。Registry 已更新为 DONE/success。

---
