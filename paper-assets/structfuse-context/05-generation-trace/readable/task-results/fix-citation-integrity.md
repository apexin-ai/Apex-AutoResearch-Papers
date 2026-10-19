# fix citation integrity

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_citation-integrity_20260514T213133_result.json`
- **Structured JSON:** [`92eed36061adedb3c551.json`](../../sessions/92/92eed36061adedb3c551.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改已验证。处理结果：

**问题 1 — RepoGraph + GraphCoder 缺失**：两篇均经 WebSearch 确认真实存在。RepoGraph（Ouyang et al., ICLR 2025）和 GraphCoder（Liu et al., ASE 2024）已录入 `literature_map.yaml` 的 `graph_guided_inference` 类别，含完整作者/venue/year/relation/summary。discussion_v2.md 引用无需修改。总计从 37 → 39 entries。

**问题 2 — ARISE 年份不一致**：arXiv ID 2605.03117 确认为 2026 年 5 月发布。`literature_map.yaml` 已从 `year: 2025` 修正为 `year: 2026`，与 `discussion_v2.md` 的 `(Seddik & Fard, 2026)` 一致。

**问题 3 — CodeGRAG + CodeRAG 排除说明**：`plan_017_literature` registry notes 已更新。排除理由：CodeGRAG 关注 NL→code generation 的 graph-augmented prompting，CodeRAG 系列关注 retrieval-augmented code generation benchmark/bigraph 代码生成，均为生成任务，与 StructFuse 的 scope（训练时结构信号用于对比学习代码检索）不符。

---
