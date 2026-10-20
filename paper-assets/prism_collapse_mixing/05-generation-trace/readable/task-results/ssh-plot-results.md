# ssh plot results

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plot-results_20260515T191558_result.json`
- **Structured JSON:** [`202676f6dc43ea9dc4ce.json`](../../sessions/20/202676f6dc43ea9dc4ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**产出文件：**

| 文件 | 行数/大小 |
|------|-----------|
| `plot_results.py` | 271 行 |
| `results/fig_rho_decay.pdf` | 15K |
| `results/fig_corpus_trends.pdf` | 20K |
| `results/fig_signal_distributions.pdf` | 41K |

**dry-run 结果：** 成功。只有 Gen 0 的 2 个 seed 文件，脚本正确识别 2 files / gens=[0] / seeds=[42,137]，3 个 PDF 均正常生成，大小合理（含 KDE 曲线和散点图的 fig_signal_distributions 最大）。只有 1 个 generation 时每条线只画 1 个点，无报错。

---
