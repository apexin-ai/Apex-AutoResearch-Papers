# code paper compile and visual check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper_compile_and_visual_check_20260517T105223_result.json`
- **Structured JSON:** [`656b00c55b495cfc3cd2.json`](../../sessions/65/656b00c55b495cfc3cd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果汇总

### 任务 1：编译结果

**Errors: 0** — 编译成功，生成 19 页 PDF。

**Warnings (7 条):**

| # | Warning | 位置 |
|---|---------|------|
| 1-4 | `'h' float specifier changed to 'ht'` (×4) | appendix.tex |
| 5 | `Underfull \vbox (badness 10000)` | p7, discussion.tex |
| 6 | `Underfull \vbox (badness 4859)` | p3, method.tex |
| 7 | `Underfull \hbox (badness 10000)` (×2) | main.bbl, 长 URL 换行 |

另有几个低 badness 的 underfull vbox（p2, p4, p14），均为页面底部留白，cosmetic 问题。

---

### 任务 2：Figure 字体检查

**所有 16 个 figure 均 ≥ 7pt，无违规。**

需关注的边界情况：
- **fig_32layer_attention.pdf** — 注释文字 ("entry", "routing", "exit", "mid-layer") 恰好 7.00pt，legend 8pt。如果栏宽缩小可能难读，建议调到 7.5-8pt。
- **fig_l1_stacked_bar.pdf** — 最小字号 7.00pt，刚好达标。
- **fig3.pdf** — legend 8.5pt，轴标签 10pt，无问题。

---

### 任务 3：corl_example.tex 检查

| 检查项 | 结果 |
|--------|------|
| main.tex 是否 include corl_example？ | **否**，未被引用 |
| corl_example.tex 含假引用？ | 是（Gauss1857, Lagrange1788），但仅存在于模板示例文件 |
| 假引用是否泄漏到正文/bib？ | **否**，其他 .tex 和 .bib 均未出现 |

该文件是 CoRL 模板自带的示例，未编译进论文，无风险。可删除以保持目录整洁。

---
