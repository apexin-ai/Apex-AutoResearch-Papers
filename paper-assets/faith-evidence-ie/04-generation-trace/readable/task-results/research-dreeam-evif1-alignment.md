# research dreeam evif1 alignment

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dreeam_evif1_alignment_20260516T033133_result.json`
- **Structured JSON:** [`6c6289cbe95ae8595653.json`](../../sessions/6c/6c6289cbe95ae8595653.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 不在当前可用的 MCP tools 中。报告已写入 `artifacts/dreeam_evif1_alignment_report.md`。

## 调研结论

**核心发现：FREIGE 与 DREEAM 实际上是同格式（都输出 sentence indices），不存在 generative vs extractive 的 evidence 表示冲突。**

差异在于 evidence 获取机制（DREEAM: attention threshold → indices; FREIGE: LLM generation → indices），但评估时都归约为 index set comparison。

### 推荐策略

1. **方案 A（审计，立即执行）**：验证 FREIGE `evaluator.py` 与 DocRED 官方脚本完全一致，重点检查缺失 evidence annotation 的处理方式。~1-2h。

2. **方案 B（PosEvi-F1，主表补充）**：在 gold triplet pool 上评估 evidence，消除 RE-correct triplet pool 差异带来的 sample selection bias。SAIS 已有先例。~50 行代码。

3. **方案 C（NLI-based，辅助 analysis）**：不作为独立指标，在 CED analysis section 展示 evidence 语义质量，支撑 "quality > precision" 叙事。

### 待确认

- FREIGE evaluator 对 Re-DocRED 缺失 evidence 的 triplet 如何处理
- DREEAM 是否公开 per-triplet predictions（用于 PosEvi-F1 重评估）
- 论文主表在 DocRED 还是 Re-DocRED 上报 Evi-F1

---
