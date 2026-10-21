# analysis token length ablation viz

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_token_length_ablation_viz_20260516T010251_result.json`
- **Structured JSON:** [`5fa099292ad4c6ad7115.json`](../../sessions/5f/5fa099292ad4c6ad7115.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**生成的文件（westd-11235 上）：**

| 文件 | 路径 |
|------|------|
| 分析脚本 | `/root/trace-verdict-study/analysis/token_length_ablation.py` |
| 图表 PDF | `/root/trace-verdict-study/analysis/figures/token_length_ablation.pdf` |
| 图表 PNG | `/root/trace-verdict-study/analysis/figures/token_length_ablation.png` |
| 汇总 CSV | `/root/trace-verdict-study/analysis/figures/token_length_ablation_summary.csv` |

**当前数据（3/5 完成）：**

| Tokens | Accuracy | 95% CI | Δ vs No-trace |
|--------|----------|--------|---------------|
| 256 | 78.82% | [76.4, 81.0] | +3.70 |
| 512 | 80.42% | [78.1, 82.6] | +5.29 |
| 1024 | — | pending | — |
| 2048 | — | pending | — |
| full | 81.76% | [79.7, 83.9] | +6.64 |

图中包含 exception_only (99.83%) 和 no_trace (75.1%) 两条参考线，pending 的 1024/2048 以虚线标注。1024tok 和 2048tok 完成后重新跑脚本即可自动补上。

---
