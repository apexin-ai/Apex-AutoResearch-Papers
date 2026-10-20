# research compile paper evidence table

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_compile_paper_evidence_table_20260516T032102_result.json`
- **Structured JSON:** [`944043cd7c4d3209278d.json`](../../sessions/94/944043cd7c4d3209278d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Evidence table 已编译完成，写入 `artifacts/paper_evidence_table.md` 并注册为 artifact `art_20260516_a1a71e`。

核心发现：

**Paper-ready 数据**：4 个 claim 都有实验支撑——evidence tax -7pp, CED reranker 97% recovery, decoupling spectrum 完整, EDCR per-relation 独立性 ρ=-0.064。

**4 个 blocking gaps**：
1. D076 统一协议 reeval（4/8 eval 不一致，阻塞 C3 paired t-test）
2. CED reranker 缺 Ign-F1（主表需要）
3. Test set evaluation（plan_002 未开始）
4. DREEAM-protocol Evi-F1 对齐（跨范式对比）

---
