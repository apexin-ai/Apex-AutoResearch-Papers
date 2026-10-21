# ops seed eval results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed_eval_results_20260520T094728_result.json`
- **Structured JSON:** [`837adcdd5fb3d8edb723.json`](../../sessions/83/837adcdd5fb3d8edb723.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Seed | GSM8K Accuracy | N |
|------|---------------|---|
| 42 (baseline) | **59.44%** | 1319 |
| 123 | **64.00%** | 200 |
| 456 | **66.50%** | 200 |

seed123 在 ±5pp 范围内（Δ=+4.56pp），seed456 略超上界（Δ=+7.06pp）。但 z-test 显示两者与 seed42 的差异均不显著（p=0.21 和 p=0.05），高点估计主要来自 N=200 的小样本方差。

结论：三个 seed 均落在 59–67% 区间，Standard GRPO 的 ~60% 恢复上限是剪枝方法的固有特性，非训练随机性所致。报告已注册为 artifact `seed_eval_report.md`，注册表已更新为 DONE+success。

---
