# paper 1000step panorama table

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_1000step-panorama-table_20260515T124454_result.json`
- **Structured JSON:** [`12ae05fa461386b71766.json`](../../sessions/12/12ae05fa461386b71766.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个产出已完成并注册：

**产出 1 — LaTeX 表格**: `artifacts/paper_tables/table_1000step_comparison.tex` (`art_20260515_35553a`)
- booktabs 风格，SFT 行用 `\rowcolor{gray!15}` + bold 突出
- 表注包含 H7/H1/H8/Genuine 定义和数据来源说明

**产出 2 — Genuine Rate Collapse 图**: `artifacts/paper_figures/genuine_rate_collapse.pdf` + `.png` (`art_20260515_ebc419`)
- 4 条 RL 实线全部从 500 步崩塌至 0-2.2%，SFT 虚线稳定在 ~93%
- 单栏 3.5×2.5 inch，serif 字体，300 dpi

---
