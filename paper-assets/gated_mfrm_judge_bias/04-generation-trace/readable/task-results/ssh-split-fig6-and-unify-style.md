# ssh split fig6 and unify style

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_split-fig6-and-unify-style_20260525T124129_result.json`
- **Structured JSON:** [`801bf6040308c2392853.json`](../../sessions/80/801bf6040308c2392853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All figures generated and verified. Here's the summary:

### 原始脚本
- `scripts/generate_paper_figures.py` — 原来只生成 fig2_ovb_bias 和 fig4_bias_vs_rho
- `exp008/generate_diagnostics.py` — 包含 forest_dj 的代码（诊断用，非论文风格）

### 修改的脚本
- **`/root/gated_mfrm_judge_bias/scripts/generate_paper_figures.py`** — 完全重写，统一 PAPER_STYLE，生成所有 4 个主文图

### 生成的文件

| 文件 | 大小 | figsize |
|------|------|---------|
| `fig2_ovb_bias.pdf` | 38 KB | (3.5, 2.8) |
| `forest_dj.pdf` | 21 KB | (3.5, 2.8) |
| `fig_contamination_bars.pdf` | 20 KB | (3.5, 2.8) |
| `fig_bias_absorption.pdf` | 23 KB | (3.5, 2.8) |

### 统一风格
- `font.family: serif` (Times New Roman / DejaVu Serif)
- `font.size: 10`, `axes.labelsize: 12`, `axes.titlesize: 12`
- 去掉 top/right spines，`grid.alpha: 0.3`，`grid.linestyle: --`
- `pdf.fonttype: 42`（嵌入字体），`figure.dpi: 300`
- 所有图 figsize=(3.5, 2.8)，适合单栏 `\columnwidth`

### 关键数据
- fig2: Pearson r=0.7949 (OVB bias vs c_n, 20 seeds synthetic)
- fig_bias_absorption: Pearson r=0.9958 (θ_MFRM − θ_G-MFRM vs ĉ_n，来自 exp003b MCMC posteriors)
- 数据源: `exp003/output_003b/joint_gmfrm_idata.nc` (G-MFRM) + `mfrm_only_idata.nc` (standard MFRM)

---
