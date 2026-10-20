# fix figure2 degeneracy scatter

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_figure2_degeneracy_scatter_20260518T050009_result.json`
- **Structured JSON:** [`34f1864a660dc951a365.json`](../../sessions/34/34f1864a660dc951a365.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成，数据点位置正确：

- **CoNLL**: x≈59.1%, y≈-1.05pp（右下方，低于 Greedy Baseline 线）
- **SciERC**: x≈17.8%, y≈+0.61pp
- **Few-NERD**: x≈13.8%, y≈+1.36pp

Per-type 三角点和标注均未改动。

Spearman 相关性（更新后）：
- 11-point: ρ = -0.5182, p = 0.1025
- Per-type (n=8): ρ = -0.3810, p = 0.3518
- Dataset-level (n=3): ρ = -1.0000, p = 0.0000（完美负相关，三点单调递减）

### 产出

| 项目 | 路径 |
|------|------|
| 更新后脚本 | `/root/autodl-tmp/struct_self_consist_ie/output/figures/plot_degeneracy_lp.py` |
| PDF | `output/figures/fig_degeneracy_lp_scatter.pdf` + `docs/paper/figures/fig_degeneracy_lp_scatter.pdf` |
| PNG | `output/figures/fig_degeneracy_lp_scatter.png` + `docs/paper/figures/fig_degeneracy_lp_scatter.png` |

---
