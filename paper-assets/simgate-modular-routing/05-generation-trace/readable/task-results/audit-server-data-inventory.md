# audit server data inventory

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_server-data-inventory_20260523T194816_result.json`
- **Structured JSON:** [`d8fde1c715dbf963ab77.json`](../../sessions/d8/d8fde1c715dbf963ab77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/server_data_inventory.md`。

摘要：
- **总体 11G**，其中 `checkpoints/` 占 9.4G，`results/` 占 1.3G
- 大量 LoRA adapter checkpoint（`.safetensors` + optimizer/scheduler 状态），分布在 seed-robustness、ablation 等实验目录
- `results/` 下 107 个条目，覆盖消融、跨模型、baseline、统计分析等
- **无训练进程运行**，GPU（RTX PRO 6000 Blackwell 98GB）完全空闲

---
