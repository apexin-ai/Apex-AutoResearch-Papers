# analysis pilot zero f1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pilot_zero_f1_20260516T163736_result.json`
- **Structured JSON:** [`25e243277c377378df9e.json`](../../sessions/25/25e243277c377378df9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

### 数量
- 200 instances 中 24 个 greedy F1=0（gold 非空），另有 31 个 gold 本身无实体（处理正确）

### 根因：模型能力问题，非格式 bug
- **79% (19/24) EMPTY_PRED**：模型未输出任何实体。集中在只有 1 个 gold 实体的短文本（median 1 个实体，103 chars），受影响最多的类型是 other(25% 零分率) 和 product(16.7%)
- **17% (4/24) TYPE_MISMATCH**：span 完全正确但类型标错（location↔organization, art↔event），FewNERD 细粒度类型本身有歧义
- **4% (1/24) span 边界分歧**："Boeing B-52" vs "Boeing B-52 Stratofortress"

### 采样恢复
- 18/24 (75%) 至少有 1/8 sample 的 F1>0，best sample F1 median=1.0
- 仅 6 个完全不可恢复（span 边界分歧 3 个 + 语义模糊 2 个 + 极短文本 1 个）

### 对 exp-021 的预期
- EMPTY_PRED（主要问题）应通过 3 epoch + r=32 显著改善
- 类型歧义部分改善，span 边界问题属标注层面
- **推理阶段无需调整**，格式解析和 prompt 均正常

报告已保存至 `artifacts/exp_020_pilot/report/zero_f1_analysis.md`。

---
