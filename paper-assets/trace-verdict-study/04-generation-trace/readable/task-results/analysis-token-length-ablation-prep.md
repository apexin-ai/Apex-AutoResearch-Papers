# analysis token length ablation prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_token_length_ablation_prep_20260516T002034_result.json`
- **Structured JSON:** [`2807c99e8b1c2648f0d0.json`](../../sessions/28/2807c99e8b1c2648f0d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出汇总：

**脚本**: `/root/trace-verdict-study/analysis/token_length_analysis.py`

**产出文件** (在 `analysis/figures/`):
- `token_length_ablation.pdf` (14KB)
- `token_length_ablation.png` (71KB, 300dpi)
- `token_length_ablation_table.tex`

**Dry-run 结果** (3/5 数据点，1024tok 和 2048tok 缺失被正确跳过):

| Token Limit | Accuracy | 95% CI | Δ vs No-trace |
|---|---|---|---|
| 256 | 78.82% | [76.4, 81.0] | +3.70 |
| 512 | 80.42% | [78.1, 82.6] | +5.29 |
| full | 81.76% | [79.7, 83.9] | +6.64 |

图表样式：单栏宽度 3.5in，无 grid，top/right spine 去除，两条虚线 baseline（majority 71.5% 灰色，no-trace 75.1% 黄色），蓝色实线带 95% CI error bar。1024tok 和 2048tok 完成后重跑即可自动补上。

---
