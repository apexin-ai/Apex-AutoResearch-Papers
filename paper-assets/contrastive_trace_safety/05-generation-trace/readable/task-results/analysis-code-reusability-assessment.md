# analysis code reusability assessment

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_code_reusability_assessment_20260519T183417_result.json`
- **Structured JSON:** [`e67046b316a768a903a0.json`](../../sessions/e6/e67046b316a768a903a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，产出文件：`artifacts/code_reusability_assessment.md`

核心结论：

**~80% 代码可直接复用。** 唯一需要重写的是 `data_loader.py`（HarmThoughts 字段名、trace_id 解析、安全标签全部硬编码）。统计核心（bootstrap、Holm-Bonferroni、window features、probe training）零修改可用。

关键数据：
- Hidden states 格式：`.pt` dict，`hidden_states` tensor `[T, L, D]` + metadata
- Text embeddings：`.pkl` dict，trace_id → ndarray `(T, 384)`
- 现有 traces：R1-8B=268, OT-7B=228, R1-32B=100, QwQ-32B=95

执行计划（并行冲刺）：
- **Critical path: 8–14h**（2h prep → 4–8h GPU 推理+HS提取 → 2–4h 分析）
- 如果新数据集已有推理 traces（不需要从头生成），GPU 时间可降到 2–4h
- 最大风险：新数据集是否有现成 traces；CP 定义能否迁移；pattern 本身是否可复现

---
