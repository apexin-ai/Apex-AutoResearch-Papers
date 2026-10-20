# ssh unify fig2 style

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_unify-fig2-style_20260525T114109_result.json`
- **Structured JSON:** [`6660c3c35b18de83a61f.json`](../../sessions/66/6660c3c35b18de83a61f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 中只有 rho=0.0 和 rho=0.3 的数据（exp009 Part A 还没跑完 rho=0.6 和 0.9）。这不影响当前任务——脚本会使用现有数据正确绘图，等数据补全后重新运行即可。

汇报：

**脚本路径**
- 统一生成脚本：`/root/gated_mfrm_judge_bias/scripts/generate_paper_figures.py`
- 原 fig2 脚本：`mvp/bias_scatter.py`（未修改，新脚本替代）
- 原 fig4 函数：`exp009/run_exp009.py` 中的 `plot_bias_vs_rho()`（未修改，新脚本替代）

**修改前后参数对比**

| 参数 | fig2 (修改前) | fig4 (修改前) | 统一后 |
|------|-------------|-------------|--------|
| figsize | (7, 5) | (16, 5) | (4.5, 3.2) / (13.5, 3.2) |
| DPI | 150 | 150 | 300 |
| axis label | 12pt | 默认 | 12pt |
| tick label | 默认 | 默认 | 10pt |
| legend | 默认 | 默认 | 10pt |
| grid | 无 | 无 | alpha=0.3, dashed |
| spine | 四边 | 四边 | despine (top/right removed) |
| 颜色 | steelblue | #e41a1c/#377eb8 | #e41a1c/#377eb8 统一 |
| 格式 | PNG only | PNG only | PDF + PNG |
| tight_layout | 有 | 有 | 有 |

**生成文件**

| 文件 | 大小 |
|------|------|
| `/root/figures/paper/fig2_ovb_bias.pdf` | 33 KB |
| `/root/figures/paper/fig2_ovb_bias.png` | 244 KB |
| `/root/figures/paper/fig4_bias_vs_rho.pdf` | 22 KB |
| `/root/figures/paper/fig4_bias_vs_rho.png` | 198 KB |

图片位于 `\graphicspath` 指向的 `/root/figures/paper/`，LaTeX 可直接引用。两图高度统一 (3.2 inches)，字体/grid/spine/颜色风格一致。

**注意**：fig4 当前仅有 rho ∈ {0.0, 0.3} 的数据，完整实验 (rho=0.6, 0.9) 需先补跑 exp009 Part A。

---
