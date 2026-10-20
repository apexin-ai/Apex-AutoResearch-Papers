# fix polish kl plots

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_polish_kl_plots_20260523T205437_result.json`
- **Structured JSON:** [`bdb0bb850db78a59f16b.json`](../../sessions/bd/bdb0bb850db78a59f16b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图已生成，配色与论文一致（fig4 的模型颜色映射：Base=#BAB0AC, TG=#E15759, LoRA=#4E79A7, UG=#F28E2B；fig2 的 PCGrad=#EDC948；fig3 的 SS=#59A14F）。

输出文件：
- `figures/paper/fig_kl_ar_gar_curves.pdf` / `.png` — Per-turn AR GAR curves，已截断到 turns 1-5
- `figures/paper/fig_kl_ar_gar_bar.pdf` / `.png` — Mid-turn AR GAR bar chart
- `figures/paper/gen_fig_kl_ar_gar.py` — 生成脚本

---
