# code seed robustness core

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed-robustness-core_20260515T131911_result.json`
- **Structured JSON:** [`4585b983ec9639e82c09.json`](../../sessions/45/4585b983ec9639e82c09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并在运行。总结：

**Part B (bootstrap) 已完成**：
| 指标 | Point | Mean ± Std | 95% CI |
|------|-------|------------|--------|
| Δ_full | 29.60 | 29.61 ± 3.18 | [23.76, 35.82] |
| Δ_nd | 2.84 | 2.78 ± 1.27 | [0.34, 5.57] |
| DAF | 90.41% | 90.58% ± 4.25% | [81.60%, 98.76%] |
| Pearson r | 0.9698 | 0.9752 ± 0.0108 | [0.952, 0.995] |

Jackknife：去掉任意单一 task 后 DAF 范围 89.0%–100.0%，Pearson r 范围 0.963–0.980，无单一 task 主导。

**Part A (router training)** 正在 GPU1 上运行（PID=474403）：
- 3 seeds (43,44,45)，每个 ~8.5 min 训练 + ~5 min eval
- 预计 ~40-50 min 全部完成
- 日志：`results/seed-robustness/run.log`
- 每个 seed 完成后会保存中间结果到 `results/seed-robustness/router_seed{N}.json`
- 最终汇总：`results/seed-robustness/summary.json`

---
