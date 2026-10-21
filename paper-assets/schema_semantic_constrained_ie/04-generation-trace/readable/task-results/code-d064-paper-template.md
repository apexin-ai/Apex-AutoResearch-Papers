# code d064 paper template

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d064_paper_template_20260519T172509_result.json`
- **Structured JSON:** [`12ee3b88f8ae8a38e532.json`](../../sessions/12/12ee3b88f8ae8a38e532.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/report/d064_paper_template.md`。

总结：

**需更新的文件共 4 个，25+ 个具体位置：**

- **appendix_beam_search.tex** — 主战场，共 ~17 处：表格 6 行 DocRED 数据 + caption + Discussion 段落全部百分比 + parse failure 统计 + CI 辩护 + 一处 "50 DocRED documents"
- **section5_runtime.tex** L13 — "50-document subset" → "998-document dev set" + Mistral 数字
- **main.tex** L82 — "a DocRED subset" → "the full DocRED dev set (998 documents)"
- **appendix_tcr.tex** L82 — "DocRED 50-doc subset" → "DocRED (998 docs)"

**不需要动的：** abstract、intro、conclusion、§5 SciERC 段落——它们只引用 SciERC beam 结果。

**关键决策点：** 如果 998-doc 结果 Qwen/Llama DR 仍=0%，叙事结构不变只换数字；如果 DR>0%，需要将 "eliminates" 降级为 "substantially reduces"，且可能波及 abstract/intro 中的 claim。

---
