# analysis v4 random fixed inject10 s7 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-random-fixed-inject10-s7-eval_20260515T221421_result.json`
- **Structured JSON:** [`0ddc06cbd08d97d3e22f.json`](../../sessions/0d/0ddc06cbd08d97d3e22f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果总结

**Random 10% s7 eval: 61.7% (29/47)**

Per-task breakdown:

| Task Type | Success | Rate |
|---|---|---|
| pick_heat_then_place | 7/8 | 87.5% |
| look_at_obj_in_light | 5/6 | 83.3% |
| pick_cool_then_place | 4/7 | 57.1% |
| pick_two_obj_and_place | 4/7 | 57.1% |
| pick_and_place_simple | 4/8 | 50.0% |
| pick_clean_then_place | 5/11 | 45.5% |

无错误或异常，wall clock ~14 min。

## Random 10% 5-seed 对比

| Seed | Rate | Successes |
|---|---|---|
| original (42) | 68.1% | 32/47 |
| s0 | 66.0% | 31/47 |
| s1 | 68.1% | 32/47 |
| **s7** | **61.7%** | **29/47** |
| s123 | 55.3% | 26/47 |

**Random 10% 5-seed mean: 63.8% ± 5.4% (SD)**

对比 TaxEI 10% 4-seed (s0/s123/s1/s7): 70.2%, 55.3%, 51.1%, 68.1%。TaxEI 的 5th seed (original) 需确认后可算完整 5-seed 统计。

---
