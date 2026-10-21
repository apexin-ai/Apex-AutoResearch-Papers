# check plan 004 v4 status

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan-004-v4-status_20260514T071834_result.json`
- **Structured JSON:** [`3ac1c76a58ac5573d3be.json`](../../sessions/3a/3ac1c76a58ac5573d3be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

### plan-004-v4 状态

**训练已完成** — 147/147 steps, 3 epochs, EXIT_CODE=0, 耗时 150s

**关键发现：数据是根因**
- v4 step 10 loss = **48.1538**，与 v2/v3 的 48.15 完全一致
- 三者用同一数据文件 `results/plan_c_test_labels/implicit_sft.jsonl`（1814行）
- ablation-b 用 `data/plan-004-implicit/`，loss 正常（0.36-0.71）
- **确认：异常高 loss 由数据文件导致，非 class_weights**

**Loss 走势**：48.15 → 42.0 → 26.1 → 13.7 → 8.5 → ... → 4.4（收敛但终态仍偏高）

**Eval loss**：epoch 1=0.95, epoch 2=0.55, epoch 3=0.49（持续下降）

**异常**：train loss 终态 ~4.4 vs eval loss 0.49，差距 ~9x，提示训练目标和评估目标可能不一致（如 class_weights 只影响训练 loss，eval 用原始 CE）。

---
