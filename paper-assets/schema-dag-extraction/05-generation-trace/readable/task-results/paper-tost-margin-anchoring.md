# paper tost margin anchoring

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_tost_margin_anchoring_20260522T095444_result.json`
- **Structured JSON:** [`062787beda9bd9dfaaf6.json`](../../sessions/06/062787beda9bd9dfaaf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**Cross-prompt variance 数据**：
- 4 个结构不同的 prompt 变体（V2 definition-first, Instruction-rewrite, Chain-of-thought, Minimal）在 FewRel 80-relation RE 上的 accuracy：
  - Count 8: 74.9%–85.2%, SD = 4.6pp
  - Count 32: 56.4%–66.2%, SD = 3.5pp
- ±3pp margin 小于跨 prompt SD，属于保守选择。

**Anchoring 论证**：±3pp 小于论文自身实验中跨 prompt 变体的 accuracy SD（3.5–4.6pp），满足 Lakens (2017) 的 smallest effect size of interest (SESOI) 原则——低于该 margin 的交互效应无法与 prompt 设计噪声区分。

**Tex 修改**：`main.tex:235`，在 External anchor 中插入了一个分句，引用 Table `prompt_variants` 的跨 prompt SD 数据，并显式提及 SESOI 原则。原有 Lakens 2017 citation 已在 bib 中，无需新增。

**编译结果**：成功，26 页，无 undefined reference/citation 错误。

---
