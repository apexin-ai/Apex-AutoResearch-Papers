# paper figure fig1 framework

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_framework_20260522T091503_result.json`
- **Structured JSON:** [`0adc04c4c3489e9435ad.json`](../../sessions/0a/0adc04c4c3489e9435ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 1 已完成。

**输出文件**：
- PDF: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.pdf` (52K)
- PNG: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png` (412K, 300dpi)
- 生成脚本: `figures/paper/gen_fig1.py`

**内容**：
- **(a) 左面板**：Sequential Pipeline — Path A (Bias-first) 和 Path B (Contamination-first)，红色虚线弧标注 confounding，底部 OVB 公式框 Cov(d_j, c_n·e_i) ≠ 0
- **(b) 右面板**：G-MFRM 三阶段流程 — Stage 1 Standard MFRM → Stage 2 External e_i estimation → Stage 3 Joint Gated Model with c_n·e_i gating → 4维诊断输出 (θ̂, d_j, c_n, e_i)

---
