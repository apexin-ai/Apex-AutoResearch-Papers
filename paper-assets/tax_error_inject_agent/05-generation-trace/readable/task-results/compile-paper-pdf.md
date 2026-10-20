# compile paper pdf

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compile_paper-pdf_20260515T124534_result.json`
- **Structured JSON:** [`0eee4d6ad1eb88bd7c98.json`](../../sessions/0e/0eee4d6ad1eb88bd7c98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇总：**

| 项目 | 状态 |
|------|------|
| **SYNC** | 14/14 文件同步完成 |
| **COMPILE** | latexmk 编译成功（pdflatex + bibtex 多轮） |
| **FIGURE** | 1/3 真实图存在（fig1_dose_response.pdf），2 个缺失已用 placeholder 替代（fig2_operator_gradient.pdf, fig_app_training_curves.pdf） |
| **PDF_PAGES** | 7 页 |
| **PDF_SIZE** | 229,202 bytes（~224KB） |

缺失的 2 个图需要后续生成实验数据后再替换：
- `figures/paper/fig2_operator_gradient.pdf`
- `figures/paper/fig_app_training_curves.pdf`

---
