# analysis v4 random fixed inject10 s0 eval r3

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-random-fixed-inject10-s0-eval-r3_20260515T205147_result.json`
- **Structured JSON:** [`899ed2d64e11f9067a27.json`](../../sessions/89/899ed2d64e11f9067a27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 汇总

**Random 10% seed=0 eval: 31/47 = 66.0%**

### 按 task_type

| task_type | success/total | rate |
|-----------|:---:|:---:|
| look_at_obj_in_light | 5/6 | 83.3% |
| pick_heat_then_place_in_recep | 7/8 | 87.5% |
| pick_clean_then_place_in_recep | 7/11 | 63.6% |
| pick_cool_then_place_in_recep | 4/7 | 57.1% |
| pick_two_obj_and_place | 4/7 | 57.1% |
| pick_and_place_simple | 4/8 | 50.0% |

### 跨 seed/condition 对比

| Condition | Seed | Success Rate |
|-----------|------|:---:|
| **TaxEI 10%** | s0 | **70.2%** (33/47) |
| Random 10% | s42 | 68.1% (32/47) |
| **Random 10%** | **s0** | **66.0% (31/47)** ← 本次 |
| Vanilla baseline | s42 | 61.7% |
| Random 10% | s123 | 55.3% (26/47) |

**Random 10% 三 seed 均值: 63.1% (89/141)**，方差较大（55.3%–68.1%）。TaxEI 10% s0 (70.2%) 仍然是最高分，高于 Random 所有 seed。

---
