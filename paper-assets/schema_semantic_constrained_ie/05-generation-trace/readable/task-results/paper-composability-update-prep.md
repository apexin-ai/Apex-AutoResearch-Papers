# paper composability update prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_composability_update_prep_20260516T030411_result.json`
- **Structured JSON:** [`64f252f6348db8a5c533.json`](../../sessions/64/64f252f6348db8a5c533.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模板已产出并注册。总结：

**产出文件:** `artifacts/composability_update_template.md`

**关键发现:**
- `section5_composability.tex` 不存在，composability 内容实际在 `section5_scierc_draft.tex` (L125-199)
- Llama FT-U CF% 未录入 registry（缺字段），建议默认用 0
- 两个 constrained eval 仍在 RUNNING

**模板覆盖 6 个更新位置（按优先级）:**

| 优先级 | 更新 | 文件 | 行号 |
|--------|------|------|------|
| P0 | Table 5 加 DocRED LoRA 行 | section5_scierc_draft.tex | 159-199 |
| P0 | 删 "DocRED not reported" | main.tex | 70 |
| P1 | Composability 段加 DocRED 数字 | section5_scierc_draft.tex | 127-157 |
| P1 | 表 caption "one dataset" → "two datasets" | section5_scierc_draft.tex | 197 |
| P1 | Limitations ZS-only claim 修正 | main.tex | 69 |
| P2 | Appendix CF-DR trade-off 补 DocRED evidence | appendix_discussion.tex | 74 |

模板包含两种 Table 5 方案（加 Dataset 列 vs 最小改动追加行）、所有占位符的计算公式、以及结果到手后的条件判断指南（高 DR / 低 DR / 高 CF / R-F1 下降各场景如何调整 claim）。

---
