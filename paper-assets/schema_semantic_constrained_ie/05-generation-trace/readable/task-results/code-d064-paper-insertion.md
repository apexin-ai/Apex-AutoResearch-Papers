# code d064 paper insertion

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d064_paper_insertion_20260519T234935_result.json`
- **Structured JSON:** [`570e242d41093787dc93.json`](../../sessions/57/570e242d41093787dc93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改完成。变更摘要：

**已修改：**
- `main.tex` — 添加 `\TBD` 命令定义（L82 DocRED 引用已在先前更新）
- `appendix_beam_search.tex` — 6 个表格数据行更新（Qwen/Llama beam 填入 998-doc 数据，greedy + Mistral 全部 \TBD 占位）；Discussion 段落更新（Qwen/Llama DR=0%+CF 描述，Mistral DocRED 行 TBD）；Clopper-Pearson CI 替换为全量验证声明
- `appendix_tcr.tex` — "50-doc subset" → "998 docs"
- `section5_runtime.tex` — 已在先前更新

**待填数据（\TBD）：** Qwen greedy (~2.5h)、Llama greedy (~1h)、Mistral 998-doc（不在 d064 范围）

变更日志已写入 `d064_paper_changes.md`。

---
