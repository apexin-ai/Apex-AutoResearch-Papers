# prep supplementary tex

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_supplementary-tex_20260517T003241_result.json`
- **Structured JSON:** [`649bea22d43f79bc18c6.json`](../../sessions/64/649bea22d43f79bc18c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功。结果：

- **PDF 生成成功**：`supplementary.pdf`，7 页
- **无编译错误**
- **Undefined references**：存在指向 main.tex 正文中定义的 `\label`（如 `sec:model`, `sec:count_curves`, `sec:bcs_controlled` 等）的交叉引用 warning。这是预期行为，因为这些 label 定义在主文档中，supplementary 作为独立文档无法解析它们。同理有几个 citation warning（`fewnerd-2021` 等来自 `prompt_appendix.tex` 中引用但 `references.bib` 中可能缺少的条目）。
- **所有 appendix 内 `\label{}` 均保留**，内部交叉引用正常工作
- **main.tex 未修改**

---
