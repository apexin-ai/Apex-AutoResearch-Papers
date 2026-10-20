# ops regen heatmap scatter pdf

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_regen-heatmap-scatter-pdf_20260522T083440_result.json`
- **Structured JSON:** [`84548edb0088186044bd.json`](../../sessions/84/84548edb0088186044bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四个文件全部生成，大小合理（均 > 10KB）：

| 文件 | 大小 |
|------|------|
| fig_heatmap.pdf | 47 KB |
| fig_heatmap.png | 124 KB |
| fig_theta_scatter.pdf | 33 KB |
| fig_theta_scatter.png | 88 KB |

服务器脚本也已同步更新。本地因为有 matplotlib + numpy，直接本地运行生成了 PDF 和 PNG，跳过了 scp 下载步骤。

---
