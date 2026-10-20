# analysis plan 004 v5 status

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-004-v5-status_20260514T082022_result.json`
- **Structured JSON:** [`d6f2fd470cacd6f2038c.json`](../../sessions/d6/d6f2fd470cacd6f2038c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan-004-v5 结果汇总

**状态**：DONE / success

| 指标 | v5 | ablation-b | 变化 |
|------|-----|-----------|------|
| accuracy | 74.5% | 65.4% | +9.1pp |
| balanced_accuracy | 79.1% | 59.3% | +19.8pp |
| internal_recall | **84.9%** | 51.5% | +33.4pp |
| internal_precision | 27.7% | 15.9% | +11.8pp |
| eval_loss | 0.238 | 0.36 | -0.122 |

**结论**：实验成功，internal_recall 84.9% 远超 30% 阈值和 ablation-b 的 51.5%。模型学会了区分 internal vs deterministic，无退化。trade-off 是 internal_precision 较低（27.7%），73/273 个 deterministic 样本被误判为 internal——模型在 upsample 后倾向过度预测少数类。

两张 GPU 目前都空闲。Registry 已更新为 DONE/success。

---
