# ssh regen split figs unified style

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_regen-split-figs-unified-style_20260525T125443_result.json`
- **Structured JSON:** [`76c08a871edd518d45ec.json`](../../sessions/76/76c08a871edd518d45ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张图全部生成成功。汇报：

| 图 | 数据来源 | figsize | 文件大小 |
|---|---|---|---|
| `fig2_ovb_bias.pdf` | 模拟数据（20 seeds, N=50, I=100, J=8） | (3.5, 2.8) | 38 KB |
| `forest_dj.pdf` | `exp003/output_003b/joint_gmfrm_idata.nc` | (3.5, 2.8) | 21 KB |
| `fig_cn_contamination.pdf` | `exp003/output_003b/joint_gmfrm_idata.nc` | (3.5, 2.8) | 20 KB |
| `fig_cn_bias_absorption.pdf` | `joint_gmfrm_idata.nc` + `mfrm_only_idata.nc` | (3.5, 2.8) | 23 KB |

- 所有 4 张图均使用统一 `PAPER_STYLE`（Times New Roman/serif, fontsize 10/12, no top/right spines, grid alpha 0.3, pdf.fonttype 42）
- 无 (a)/(b) 面板前缀
- fig2 的 Pearson r=0.79, bias absorption 的 r=0.9958

---
