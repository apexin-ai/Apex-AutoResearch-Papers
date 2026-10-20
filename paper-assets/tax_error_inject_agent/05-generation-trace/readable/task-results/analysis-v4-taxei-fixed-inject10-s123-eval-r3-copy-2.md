# analysis v4 taxei fixed inject10 s123 eval r3

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-fixed-inject10-s123-eval-r3_20260515T205322_result.json`
- **Structured JSON:** [`52573a3c1ae44646bff9.json`](../../sessions/52/52573a3c1ae44646bff9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。W&B 查询接口报错（参数兼容问题），eval 脚本本身未记录 wandb run，跳过。

## 汇总

### 总体结果
**v4-taxei-fixed-inject10-s123-eval-r3: 55.3% (26/47)**

### 按 task_type 分布

| Task Type | Success | Total | Rate |
|-----------|---------|-------|------|
| look_at_obj_in_light | 5 | 6 | 83.3% |
| pick_heat_then_place_in_recep | 6 | 8 | 75.0% |
| pick_two_obj_and_place | 4 | 7 | 57.1% |
| pick_and_place_simple | 4 | 8 | 50.0% |
| pick_clean_then_place_in_recep | 5 | 11 | 45.5% |
| pick_cool_then_place_in_recep | 2 | 7 | **28.6%** |

### 跨 seed/condition 对比

| Condition | Success Rate | 26/47 equiv |
|-----------|-------------|-------------|
| TaxEI 10% seed=0 | **70.2%** (33/47) | — |
| Vanilla baseline (5-seed mean) | 67.3±4.7% | — |
| TaxEI 10% seed=42 | 61.7% (29/47) | — |
| **TaxEI 10% seed=123** | **55.3% (26/47)** | ← this run |

### 分析

seed=123 是 TaxEI 10% 三个 seed 中最差的，比 vanilla baseline 低 12 个百分点。主要弱项在 `pick_cool_then_place_in_recep`（28.6%）和 `pick_clean_then_place_in_recep`（45.5%）。三个 seed 的方差很大（55.3% / 61.7% / 70.2%），TaxEI 10% 的 3-seed 均值为 **62.4%**，低于 vanilla baseline 的 67.3%。

---
