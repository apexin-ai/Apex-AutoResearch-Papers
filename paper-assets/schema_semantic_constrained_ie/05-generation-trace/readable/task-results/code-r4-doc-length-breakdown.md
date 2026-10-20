# code r4 doc length breakdown

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r4_doc_length_breakdown_20260517T122214_result.json`
- **Structured JSON:** [`20db83a40308d1ac0d47.json`](../../sessions/20/20db83a40308d1ac0d47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。两个 artifact 已注册：

**核心发现：**

| | SciERC | DocRED |
|---|---|---|
| Short 减少 | 84.1% | 74.1% |
| Medium 减少 | 81.5% | 75.2% |
| Long 减少 | 79.7% | 73.8% |

1. **约束效果跨文档长度一致**：SciERC 80–84%，DocRED 74–75%，长文档无退化
2. **ET/RV 全部消除**：grammar-constrained decoding 在所有长度桶中 100% 消除这两类违规
3. **长文档违规更多但约束等比有效**：DocRED long-bin 无约束 3550 violations vs short-bin 2445，但减少率几乎相同
4. **F1 不受损或略有提升**：DocRED constrained E-F1 提升 +0.9–1.5pp
5. **CF 违规 trade-off**：SciERC constrained 中 CF 增加（grammar 强制有效类型，但同一 entity 跨 relation 可能被分配不同有效类型）

产出：
- `r4_doc_length_breakdown_results.md` — 完整数据表格和分析
- `r4_doc_length_latex_table.tex` — 论文 appendix LaTeX 表格（3 个 table）
- `outputs/doc_length_breakdown.json` — 原始 JSON 数据

---
