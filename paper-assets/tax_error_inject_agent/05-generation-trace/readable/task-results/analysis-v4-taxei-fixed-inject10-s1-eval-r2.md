# analysis v4 taxei fixed inject10 s1 eval r2

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-fixed-inject10-s1-eval-r2_20260515T210526_result.json`
- **Structured JSON:** [`2d01a507438370ac5841.json`](../../sessions/2d/2d01a507438370ac5841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总如下：

## v4-taxei-fixed-inject10-s1-eval-r2 结果

**Overall: 24/47 = 51.1%**

| Task Type | Success | Rate |
|-----------|---------|------|
| pick_heat_then_place | 6/8 | 75.0% |
| look_at_obj_in_light | 4/6 | 66.7% |
| pick_and_place_simple | 4/8 | 50.0% |
| pick_clean_then_place | 5/11 | 45.5% |
| pick_two_obj_and_place | 3/7 | 42.9% |
| pick_cool_then_place | 2/7 | 28.6% |

## 与已知 10% inject 结果对比

| 方法 | s42 | s0 | s1 (本次) | s123 |
|------|-----|-----|-----------|------|
| **TaxEI 10%** | 61.7% | 70.2% | **51.1%** | 55.3% |
| **Random 10%** | 68.1% | 66.0% | — | 55.3% |

s1 = 51.1% 是 TaxEI 10% 四个 seed 中最低的，比 s42 低 10.6pp，比 s0 低 19.1pp。seed 间方差较大（51.1%–70.2%），说明 TaxEI 10% 在低数据量下对 seed 敏感。当前 s1 结果也低于 Random 10% 的两个已知 seed（68.1%, 66.0%）。

---
