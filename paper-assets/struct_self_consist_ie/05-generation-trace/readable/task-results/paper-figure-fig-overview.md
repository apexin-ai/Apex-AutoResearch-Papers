# paper figure fig overview

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_overview_20260514T133527_result.json`
- **Structured JSON:** [`4c6de1981a79bd7010bc.json`](../../sessions/4c/4c6de1981a79bd7010bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成并注册。

**输出**: `/figures/paper/fig_overview.pdf` (45KB, 矢量 PDF)

**布局**:
- **左面板 (绿色)** — Quality Estimation: Input → N samples → Consistency Score，High S_J → High F1 / Low S_J → Low F1，底部 AUROC ≈ 0.70, ρ ≈ 0.39
- **右面板 (红色)** — Sample Selection: 同一 input 的 y₁/y₂/y₃ 得到相同 S_J 分数，无法区分最佳样本，best-of-N ≤ greedy
- **中间** — Correlation–Selection Gap 标签

生成脚本在 `/tmp/gen_fig_overview.py`，可随时调整细节重新运行。

---
