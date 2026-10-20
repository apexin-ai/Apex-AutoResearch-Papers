# research composability paper audit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_composability_paper_audit_20260516T021140_result.json`
- **Structured JSON:** [`ae7d6f7463106cb0b149.json`](../../sessions/ae/ae7d6f7463106cb0b149.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清单已保存到 `artifacts/composability_update_checklist.md`。

**总结**：论文中涉及 composability（FT + OntoCoDec）且需要 DocRED constrained eval 数字后更新的位置共 **10 处**，分布在 4 个文件中：

| 优先级 | 位置 | 要点 |
|--------|------|------|
| **P0** | `section5_composability.tex:18-51` Table 5 | 整个 DocRED 块缺失，需加 4-8 行数据 |
| **P0** | `main.tex:69` Limitations | 删除 "DocRED fine-tuning is not reported" |
| P1 | `section5_composability.tex:14-16` | 实验描述从 "SciERC" 改为 "SciERC and DocRED" |
| P1 | `section5_composability.tex:53-68` | "FT does not eliminate violations" 段加 DocRED DR 数字 |
| P1 | `section5_composability.tex:70-86` | "no F1 cost" 段加 DocRED delta 数字 |
| P1 | `main.tex:65` | Limitations CF≤1.18% 可能需扩为范围 |
| P2 | `section5_composability.tex:88-98` | Implication 定性 claim，看结果定 |
| P2 | `paper_tables_draft.tex:119` | TBD 占位符（未编译，低优先级） |

另外 `abstract.tex` 和 `section1_introduction_draft.tex` 中的 "composable" 用法是描述层间组合，不涉及 FT composability 数字，**无需更新**。

---
