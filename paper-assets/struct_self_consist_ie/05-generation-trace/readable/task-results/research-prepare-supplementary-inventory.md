# research prepare supplementary inventory

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_prepare-supplementary-inventory_20260520T071658_result.json`
- **Structured JSON:** [`04155da2309ea0c5ae05.json`](../../sessions/04/04155da2309ea0c5ae05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清单已写入 `artifacts/supplementary_materials_inventory.md` 并注册。

核心发现：
- **46 项已有**：全部核心 pipeline 代码（sampling/compute_signals/consistency/evaluation）、构建与选择脚本（8个）、分析聚合脚本（6个）、图表生成（3个）、19 个聚合结果 JSON
- **4 项 pending**：14B/32B 训练及其配置（训练中，分别 77.7% 和 56.9%）
- **~20 项需从服务器取回**：最大缺口是 **12 个 LLamaFactory 训练 YAML 配置**（全在 autodl-5090 上）和各实验的原始 `samples.jsonl` / `full_signal_report.json`

关键阻塞项：训练 config 全部在服务器端，本地零份，需要 SSH 取回后打包。

---
