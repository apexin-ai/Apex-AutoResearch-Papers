# research citation verification

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-verification_20260515T025113_result.json`
- **Structured JSON:** [`a982f3286492066c73b6.json`](../../sessions/a9/a982f3286492066c73b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/citation_verification_report.md`。

结果：**1/3 完全正确，2/3 需修正，0/3 幻觉引用**。

| 引用 | 状态 | 问题 |
|------|------|------|
| Ye et al. ICLR 2025 | VERIFIED | 无 |
| Dohmatob & Feng ICLR 2025 | PARTIALLY CORRECT | 缺 2 位作者（Arjun Subramonian, Julia Kempe）|
| Seddik et al. 2024 | PARTIALLY CORRECT | 标题是内容的意译，非原始标题。实际标题: "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse" (arXiv: 2404.05090) |

`register_artifact` 不在当前可用的 MCP 工具中，文件已直接写入 artifacts 目录。如需注册到 manifest，请手动操作或提供工具。

---
