# paper compress body to 8p

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compress-body-to-8p_20260514T213311_result.json`
- **Structured JSON:** [`a94a1825481a56a2a890.json`](../../sessions/a9/a94a1825481a56a2a890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Compilation succeeded with 0 errors, no broken refs/cites, total 13 pages. Body now ends at line 533 in left column ~middle of page 7 (was page 8 left column line 624 before). Final layout:

**结果**：
- 总页数：14 → 13
- Body：~7.5 页 → ~6.5 页（结束于 page 7 左栏中部，line 533）
- References + Appendix：6 页（从 page 7 中部到 page 13）
- 编译 0 error，无 `??` 引用，所有 figure/table 正常解析

**各章节压缩**：
- `introduction.tex`：43 → 32 行。删除了 Lines 12-18 的 neurosymbolic 综述（去 §2），合并 Lines 27-34 的 meta-Goodhart 段（保留所有数字），enumerate 4 条贡献每条压缩为 1 句
- `method.tex`：65 → 60 行。§3.4 Taxonomy 删除 7 种 mode 的逐条定义（保留 mode 名 + 指向 §4.5/Appendix），fig1 宽度 0.95 → 0.92
- `experiments.tex`：117 → 112 行。§4.4 Cross-Logic 紧凑化（保留所有数字与机制：ISR$^*{=}1.000$、$n_{\text{nec}}{=}1$ 38/38、ISR$^*{=}0.912$ 等），§4.5 Taxonomy 改为内联紧凑列表
- `main.tex`：加入 4 行排版微调（`\textfloatsep` / `\intextsep` / `\abovecaptionskip` / `\belowcaptionskip`）

**保留**：所有 claim 数字（0.642→0.132→0.003、87%→100% H1、64.5% H7、1.06×、92.9% genuine、0% Prolog genuine、PR 18%/48%、7 modes），全部 figure (Fig 1/2/3)、Table 1（goodhart-landscape），C1-C4 claim 结构，所有引用。

---
