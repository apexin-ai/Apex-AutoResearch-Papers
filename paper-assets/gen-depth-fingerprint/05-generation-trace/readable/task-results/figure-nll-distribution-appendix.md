# figure nll distribution appendix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_nll_distribution_appendix_20260520T184712_result.json`
- **Structured JSON:** [`28c736d6b33f357fc464.json`](../../sessions/28/28c736d6b33f357fc464.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出清单：

| # | 文件 | 位置 |
|---|------|------|
| 1 | `extract_token_nll.py` | 服务器 `/root/gen-depth-fingerprint/scripts/` |
| 2 | `plot_nll_distribution.py` | 服务器 `/root/gen-depth-fingerprint/scripts/` |
| 3 | `token_nll_by_depth.json` (3.8MB, 1000 records, 236k tokens) | 服务器 `/root/gen-depth-fingerprint/results/` |
| 4 | `fig_appendix_nll_distribution.pdf` (16KB) + `.png` (104KB) | 服务器 `/root/gen-depth-fingerprint/results/` |
| 5 | `appendix_nll_distribution.tex` | 本地 `artifacts/_project/paper/` |

关键数据：

| Depth | Median NLL | Mean NLL |
|-------|-----------|----------|
| 0 | 1.688 | 2.610 |
| 1 | 0.671 | 1.506 |
| 2 | 0.115 | 1.021 |
| 3 | 0.028 | 0.814 |
| 4 | 0.012 | 0.626 |

NLL 从 depth 0 的 1.69 nats 单调下降到 depth 4 的 0.01 nats，确认递归生成文本对参考模型越来越可预测。图和 PDF 已就绪，`main.tex` 中的 `\input` 引用需要你自己添加。

---
