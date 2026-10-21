# analysis forest plot tier boundary

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_forest_plot_tier_boundary_20260520T162215_result.json`
- **Structured JSON:** [`cdd723854b94c2691b3c.json`](../../sessions/cd/cdd723854b94c2691b3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。

**输出文件：**
- PDF: `artifacts/figures/forest_plot_tier_boundary.pdf`
- PNG: `artifacts/figures/forest_plot_tier_boundary.png`
- Artifact ID: `art_20260520_f4e3a5`

**数据说明：**
- Wilson interval，n=1190（164 unique programs × multiple test instances）
- DeepSeek vota 用 seed123（0.9916）替代 seed42（0.8445 为已知 outlier）
- Tier 1（exception_only / ae_only / vota）CI 全部在 95% 线以上，与 Tier 2（loop_only 77–86%）和 baseline（no_trace 67–77%）的 CI 完全不重叠

---
