# research related work survey

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_survey_20260516T131804_result.json`
- **Structured JSON:** [`42911731ffc9b45291a7.json`](../../sessions/42/42911731ffc9b45291a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。已更新 `artifacts/related_work_survey.md`，新增三篇审稿人指定论文的完整条目：

**新增内容：**
- **SynCode** (Ugare+ TMLR'25) — §1 Grammar-Constrained Decoding 首条，含 DFA mask store 技术细节
- **IterGen** (Ugare+ ICLR'25) — §1 第二条，含回溯机制 + KV cache 复用 + 语义检查器细节
- **BoostCD/BoostIE** (Šakota & West, EMNLP'25) — §3 Structural Constraints for IE 中，含两阶段 boosting + DPO 细节
- §6 新增 **审稿人指定论文对比表**（4 行 × 6 维度）和更新的差异化分析（5 个维度明确对标三篇论文）

**关键定位论点：**
1. vs. SynCode/IterGen: 约束来源自动化（ontology 编译 vs 手写 CFG/检查器）
2. vs. IterGen: 前向预防 vs 回溯修复
3. vs. BoostCD: training-free + model-agnostic vs 需训练 boosted model
4. vs. all: 语法+语义双层约束的唯一 IE 专用方案

---
