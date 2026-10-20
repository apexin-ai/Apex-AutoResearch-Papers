# figure trace length ablation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_trace_length_ablation_20260516T040933_result.json`
- **Structured JSON:** [`de1dbcefbbf8829a65c4.json`](../../sessions/de/de1dbcefbbf8829a65c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册完毕。

**产出文件**（服务器 westd-11235）：
- `/root/trace-verdict-study/figures/fig_trace_length_ablation.pdf` (21K, 矢量)
- `/root/trace-verdict-study/figures/fig_trace_length_ablation.png` (79K, 300dpi)

**补充的 CI 数据**（从 eval_results.json 获取）：
| Condition | Accuracy | CI |
|---|---|---|
| 512tok | 80.42% | [78.15%, 82.61%] |
| no_limit (full_trace) | 81.76% | [79.66%, 83.95%] |

**图表规格**：单栏宽 3.5×2.8in，serif 字体 11pt，无标题，蓝色主线 (#0072B2) 带 error bars，灰色虚线 No Trace baseline (75.10%)，红色虚线 Exception Only (99.83%)，每个数据点标注精确数值。

---
