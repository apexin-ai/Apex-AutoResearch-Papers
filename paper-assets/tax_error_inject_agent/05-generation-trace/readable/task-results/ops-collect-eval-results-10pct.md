# ops collect eval results 10pct

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-eval-results-10pct_20260515T200133_result.json`
- **Structured JSON:** [`4236dd1328d5939e564b.json`](../../sessions/42/4236dd1328d5939e564b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。汇总表格：

## 10% Dose-Response Eval 结果汇总

| Condition | seed=42 | seed=0 | seed=123 | seed=1 | seed=7 | Mean±SD |
|-----------|---------|--------|----------|--------|--------|---------|
| **TaxEI 10%** | 61.7% (29/47) | **70.2% (33/47)** | OOM | OOM | train pending | 66.0%±6.0 (n=2) |
| **Random 10%** | 68.1% (32/47) | OOM | **55.3% (26/47)** | train pending | train pending | 61.7%±9.1 (n=2) |

### 状态明细

| Eval | 状态 | 原因 |
|------|------|------|
| v4-taxei-fixed-inject10-s0-eval | **完成** | 70.2% |
| v4-random-fixed-inject10-s123-eval | **完成** | 55.3% |
| v4-taxei-fixed-inject10-s123-eval | **失败** | CUDA OOM（模型加载时 GPU 0 内存不足） |
| v4-random-fixed-inject10-s0-eval | **失败** | CUDA OOM（同上） |
| v4-taxei-fixed-inject10-s1-eval | **失败** | CUDA OOM（同上） |
| v4-taxei-fixed-inject10-s7 | 训练未完成 | registry 状态 PREPARING |
| v4-random-fixed-inject10-s1 | 训练未完成 | registry 状态 PREPARING |
| v4-random-fixed-inject10-s7 | 训练未完成 | registry 状态 PREPARING |

### 关键问题

5 个 eval 中 3 个因 CUDA OOM 失败——4 张 GPU 并行跑 eval 时 GPU 0 内存被占满。这 3 个 OOM 的 eval 和 3 个未完成训练的 seed 都需要重跑，才能得到完整的 5-seed 统计。

### by_task_type（已完成的新 eval）

**TaxEI 10% seed=0 (70.2%)**:
| Task Type | Rate |
|-----------|------|
| look_at_obj_in_light | 5/6 (83.3%) |
| pick_and_place_simple | 5/8 (62.5%) |
| pick_clean_then_place_in_recep | 8/11 (72.7%) |
| pick_cool_then_place_in_recep | 4/7 (57.1%) |
| pick_heat_then_place_in_recep | 7/8 (87.5%) |
| pick_two_obj_and_place | 4/7 (57.1%) |

**Random 10% seed=123 (55.3%)**:
| Task Type | Rate |
|-----------|------|
| look_at_obj_in_light | 5/6 (83.3%) |
| pick_and_place_simple | 5/8 (62.5%) |
| pick_clean_then_place_in_recep | 5/11 (45.5%) |
| pick_cool_then_place_in_recep | 2/7 (28.6%) |
| pick_heat_then_place_in_recep | 6/8 (75.0%) |
| pick_two_obj_and_place | 3/7 (42.9%) |

---
