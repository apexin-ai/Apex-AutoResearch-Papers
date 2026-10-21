# exp entity order ablation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_entity-order-ablation_20260522T164452_result.json`
- **Structured JSON:** [`933bc208605548a2a414.json`](../../sessions/93/933bc208605548a2a414.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并配置完毕：

- **实验 ID**: `entity_order_ablation_qwen_scierc`
- **PID**: 967058，GPU 1（18999 MiB），正在推理
- **进度**: 11/551 样本（启动时）
- **Shuffle 结果**:
  - Entity types: `[Task, Method, Material, Metric, OtherScientificTerm, Generic]` → `[Metric, Method, Material, OtherScientificTerm, Task, Generic]`
  - Relation types: `[Used-for, Feature-of, ...]` → `[Conjunction, Evaluate-for, Compare, Part-of, Feature-of, Hyponym-of, Used-for]`
- **Cron 监控**: 每 8 分钟检查一次，完成后自动跑 evaluation 并对比 original order 结果
- **Parent**: `w5_lora_scierc_constrained_eval`
- **输出**: `outputs/entity_order_shuffled_qwen_scierc.jsonl`
- **日志**: `/tmp/entity_order_shuffled_qwen_scierc.log`

SciERC 551 句 Qwen FT greedy S1 推理预计 30-40 分钟完成。

---
