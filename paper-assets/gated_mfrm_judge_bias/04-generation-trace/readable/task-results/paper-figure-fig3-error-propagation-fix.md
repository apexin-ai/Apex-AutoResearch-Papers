# paper figure fig3 error propagation fix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig3_error_propagation_fix_20260522T123746_result.json`
- **Structured JSON:** [`05b070ad72d8244395b8.json`](../../sessions/05/05b070ad72d8244395b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改内容：

1. **删除了所有 "Theoretical" 曲线** — 移除了 `theta_theory`, `cn_theory`, `sigma_dense`, `*_dense` 变量及其 `ax.plot` 调用
2. **Panel (b) 添加了误差条** — 从远程 `summary.csv` 读取了真实的 `cn_rmse_std` 值：[0.1869, 0.1934, 0.1981, 0.1954]，现在两个 panel 都有 error bars
3. **保留了**绿/红 regime bands、σ_crit 竖线、百分比退化标注、panel 标签

输出文件：PDF (26KB) 和 PNG (105KB) 均已生成。

---
