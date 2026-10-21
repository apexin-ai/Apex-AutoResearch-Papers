# figure fix framework formula

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fix-framework-formula_20260524T170311_result.json`
- **Structured JSON:** [`02a4ae1e625af1ba0402.json`](../../sessions/02/02a4ae1e625af1ba0402.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`fig1_framework_v2.png` + `fig1_framework_v2.pdf` 已生成，两个符号错误均已修正：
- 公式：`+ c_n · e_i`（正号，contamination inflates scores）
- 输出标签：`ĉ_n`（不是 `ê_n`）

PaperBanana 输出虽然公式正确但 Imagen 栅格图质量不够，最终用 gen_fig1.py 生成了矢量级 matplotlib 输出。

---
