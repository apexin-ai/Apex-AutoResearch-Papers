# analysis fig consensus heatmap d120

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fig_consensus_heatmap_d120_20260520T065207_result.json`
- **Structured JSON:** [`4a089e09d30155b1986b.json`](../../sessions/4a/4a089e09d30155b1986b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件：

- **PDF**: `artifacts/figures/fig_consensus_heatmap_d120.pdf`
- **PNG**: `artifacts/figures/fig_consensus_heatmap_d120.png`
- **数据表**: `artifacts/figures/consensus_heatmap_d120_data.csv`

几个要点：

1. **α=0.60 异常偏低**（K≥3 平均仅 1.0/8）。原因：s42 来自 `a060_s42_fp32_v3_d080`（v3 decay=0.80 变体，非标准设置），s43 才是标准实验。如果要排除 v3_d080，α=0.60 只剩 s43 单 seed 且 K≥3=0/8。
2. **α=0.05 也来自 v3_d080 变体**（`a005_s42_fp32_v3_d080`），非标准 alpha_sweep，酌情是否纳入。
3. **α=1.00 来自 padding_robustness** 实验（非 alpha_sweep），因 alpha_sweep 无 α=1.0 实验而补入。
4. **Threshold Onset 全面塌陷**：D120 true 3σ 修复后，除 α=0.50 (s42: 4/8, s43: 6/8) 和 C4 α=0.25 (2/8) 外，其余全部 0/8。
5. **TY Granger 信号明显减弱**：D120 signonly bug 修复后，TY 在大多数 α 下降至 0-4/8，不再像之前虚高。

---
