# ssh fix analysis bugs

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-analysis-bugs_20260515T230841_result.json`
- **Structured JSON:** [`e911d6dcaa21286e883d.json`](../../sessions/e9/e911d6dcaa21286e883d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成，验证通过。

**修改摘要：**

| Bug | 文件 | 修复内容 |
|-----|------|----------|
| BUG-1 | `analyze_correlation.py` | Condition 2 改为检查 `|ρ|` 单调退化 ≥15%，删除 `mean_key`/`means` |
| BUG-2 | `plot_results.py` | `plot_rho_decay` 同时画 entropy（实线）和 spectral_rank（虚线）的 `|ρ|` |
| BUG-3 | `plot_results.py` | `set_ylim(-0.05, 1.05)` |
| BUG-4 | `plot_results.py` | 对所有 seed 生成分布图，输出 `fig_signal_distributions_seed{seed}.pdf` |

**验证结果：**
- `analyze_correlation.py` 用 Gen 0/1 数据运行成功，Condition 1/2 均为 N（符合预期：只有 2 代数据，|ρ| 下降不足 15%）
- `plot_results.py` 生成 4 个 PDF：`fig_rho_decay.pdf`、`fig_corpus_trends.pdf`、`fig_signal_distributions_seed42.pdf`、`fig_signal_distributions_seed137.pdf`

---
