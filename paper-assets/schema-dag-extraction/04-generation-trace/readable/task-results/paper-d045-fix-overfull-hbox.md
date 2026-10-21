# paper d045 fix overfull hbox

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d045_fix_overfull_hbox_20260516T110759_result.json`
- **Structured JSON:** [`282e9be2718cc70e1cb6.json`](../../sessions/28/282e9be2718cc70e1cb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The 45pt overfull is gone. The remaining overfull hboxes are:
- **1.46pt** at line 37 of main.tex (Table 1 caption — negligible, under 5pt)
- Everything else is in `prompt_appendix.tex` (code listings in monospace font)

**正文中 > 5pt 的 overfull hbox：0 个。** 

修复内容：Batch Composition 表格（原 lines 209-218）——用 `@{}` 去除两侧列间距，缩短首列文字 "Confusability-aware (graph coloring)" → "Confus.-aware (coloring)"，缩短表头 "Accuracy" → "Acc."，消除 45pt overfull。正文残留仅 1.46pt（Table 1 caption），在 5pt 阈值内。

---
