# check exp fewrel 40rel r4 progress

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_fewrel_40rel_r4_progress_20260515T213748_result.json`
- **Structured JSON:** [`7e5250631a41e0c177fa.json`](../../sessions/7e/7e5250631a41e0c177fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_fewrel_40rel_r4 结果报告

**状态**: 已完成，退出码 0  
**运行时间**: ~21:13 → 05:29 UTC（约 8h16m），其中 exp1 ~8h9m，exp2 ~6m  
**产出文件**: eval_exp1.json, eval_exp2.json, predictions_exp1/exp2.json, results_incremental.jsonl (14736 行)

---

### EXP1: Count Curve（Qwen3-32B-FP8, FewRel 40-rel）

| count | batches | avg_acc | 趋势 |
|------:|--------:|--------:|------|
| 1 | 80 | ~0.858 | baseline |
| 4 | 5 | 0.867 | ≈持平 |
| 8 | 5 | 0.802 | 下降 |
| 16 | 5 | 0.697 | 明显下降 |
| 32 | 5 | 0.658 | 继续下降 |
| 40 | 5 | 0.588 | 最低 |

**count_1→40 accuracy 从 ~0.86 降到 ~0.59，降幅 ~27pp。** 符合预期的 schema 复杂度效应。

---

### EXP2: BCS-Controlled

| 条件 | count | BCS | acc | 
|------|------:|----:|----:|
| low_bcs | 8 | 0.4715 | **0.833** |
| high_bcs | 8 | 0.9706 | **0.500** |
| low_bcs | 16 | 0.5705 | **0.818** |
| high_bcs | 16 | 0.9706 | **0.500** |

**BCS 效应极强**:
- count_8: low vs high BCS → Δacc = **0.333**（0.833 vs 0.500）
- count_16: low vs high BCS → Δacc = **0.318**（0.818 vs 0.500）
- high_bcs 条件下 acc 恰好 0.500，模型几乎在语义相近的关系间随机猜

---
