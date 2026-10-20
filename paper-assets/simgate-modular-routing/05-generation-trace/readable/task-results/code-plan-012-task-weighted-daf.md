# code plan 012 task weighted daf

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-012-task-weighted-daf_20260514T005050_result.json`
- **Structured JSON:** [`cc177e07454b31d17c2f.json`](../../sessions/cc/cc177e07454b31d17c2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。结果对比：

| 指标 | Episode-weighted | Task-weighted |
|------|-----------------|---------------|
| DAF | 99.1% | 93.9% |
| DAF 95% CI | [0.9393, 1.0445] | [0.8462, 0.9975] |
| Δ_full | +37.39 | +41.48 |
| Δ_nd | +0.35 | +0.91 |

task-weighted DAF 93.9%，低于 episode-weighted 的 99.1%，因为 `find-non-living-thing`（DAF≈0%，25 eps）和 `measure-melting-point-unknown-substance`（DAF=59%）等任务在 task-weighted 中获得与大样本 task 相等的权重。CI 上界 0.9975 < 1，比 episode-weighted 版本更保守——正好应对 reviewer 对样本量不均衡的攻击。

三个输出文件都已包含新字段：
- `report.json`: `task_weighted_daf`, `task_weighted_daf_ci`, `task_weighted_delta_full`, `task_weighted_delta_nd`
- `paper_table.json`: `task_weighted` 对象
- `summary.csv`: `TASK_WEIGHTED` 行

---
