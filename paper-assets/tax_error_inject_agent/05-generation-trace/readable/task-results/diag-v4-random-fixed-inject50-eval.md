# diag v4 random fixed inject50 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_v4-random-fixed-inject50-eval_20260515T015920_result.json`
- **Structured JSON:** [`af05ac9c9bf1c3460e5a.json`](../../sessions/af/af05ac9c9bf1c3460e5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**实验结果：v4-random-fixed-inject50-eval**

| 指标 | 值 |
|------|-----|
| 总成功率 | **57.4%** (27/47) |
| look_at_obj_in_light | 83.3% (5/6) |
| pick_two_obj_and_place | 85.7% (6/7) |
| pick_heat_then_place_in_recep | 75.0% (6/8) |
| pick_cool_then_place_in_recep | 42.9% (3/7) |
| pick_and_place_simple | 37.5% (3/8) |
| pick_clean_then_place_in_recep | 36.4% (4/11) |

Random 50% injection clean eval 57.4%，高于 TaxEI 50% 的 51.1%，说明在 50% 注入比例下 Random 基线反而优于 TaxEI。

---
