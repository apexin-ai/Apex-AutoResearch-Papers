# paper unify figure colors

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_unify-figure-colors_20260524T222818_result.json`
- **Structured JSON:** [`0ee933b11bff2a170642.json`](../../sessions/0e/0ee933b11bff2a170642.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。LaTeX 编译成功（19 pages, 无 error）。

### 颜色变更汇总

| 脚本 | 变量 | 旧颜色 | 新颜色 | 语义 |
|---|---|---|---|---|
| **plot_scaling.py** | `COL_EVI` | `#0072B2` | `#5B9BD5` | SFT w/ evidence 蓝 |
| | `COL_NO` | `#999999` | `#B0B0B0` | no-evidence 灰 |
| | `COL_RSFT` | `#E69F00` | `#E8A838` | RSFT 橙 |
| | `COL_EVI_E` | `#005A8C` | `#497CAA` | edge 蓝 |
| | `COL_NO_E` | `#777777` | `#8C8C8C` | edge 灰 |
| | `COL_RSFT_E` | `#B87D00` | `#BA862D` | edge 橙 |
| **plot_spectrum.py** | `COLORS['baseline']` | `#0072B2` | `#5B9BD5` | baseline 蓝 |
| | `COLORS['treatment']` | `#E69F00` | `#009E73` | GRPO bf16 绿 |
| | `COLORS['safe']` | `#009E73` | `#E8A838` | RSFT 橙 |
| | `COLORS['neutral']` | `#999999` | `#B0B0B0` | SFT 灰 |
| **plot_variance_compression.py** | SFT inline | `#0072B2` | `#5B9BD5` | SFT 蓝 |
| | RSFT inline | `#009E73` | `#E8A838` | RSFT 橙 |
| **plot_fig_grpo_dynamics.py** | `C_ORANGE` | `#E69F00` | `#D55E00` | collapse 红 |
| | `C_BLUE` | `#0072B2` | `#009E73` | safe 绿 |
| **plot_evidence_tax.py** | `COL_BENEFIT` | `#0072B2` | `#E8A838` | 统一橙 |
| | `COL_COST` | `#E69F00` | `#E8A838` | 统一橙 |
| | edge colors | `#005A8C`/`#B87D00` | `#BA862D` | 统一 edge 橙 |
| | error bars | `#005A8C`/`#B87D00` | `black` | 黑色 |

---
