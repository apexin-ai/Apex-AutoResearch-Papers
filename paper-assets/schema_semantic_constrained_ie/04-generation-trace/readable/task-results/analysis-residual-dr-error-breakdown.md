# analysis residual dr error breakdown

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_residual_dr_error_breakdown_20260516T160550_result.json`
- **Structured JSON:** [`53d9c3116fcd42010126.json`](../../sessions/53/53d9c3116fcd42010126.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/residual_dr_error_analysis.md`。

核心发现：

- **36 个残余 DR violation** 分布在 3 个 setting（Llama DocRED 贡献 33 个，占 92%）
- **4 类根因**：Entity type 错误（39%）> Schema 覆盖不全（33%）> 错误关系选择（17%）> 方向反转（11%）
- Qwen DocRED 和 Llama SciERC 的残余 violation 全部是 schema long-tail coverage gap，LLM 自身的 typing 已无错误
- Llama DocRED 的主要问题是 entity type 标注错误（地名/国籍词混淆、人名标为 LOC 等），分布在 16 种不同关系上，无明显集中
- `P361 part of` (6 个) 和 `P710 participant` (4 个) 是 violation 最多的两个关系，前者集中在 Tolkien 虚构世界语境

---
