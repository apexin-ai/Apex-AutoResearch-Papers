# code new plot scripts

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_new_plot_scripts_20260516T084238_result.json`
- **Structured JSON:** [`704dcf3966727a37dee2.json`](../../sessions/70/704dcf3966727a37dee2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 产出

| 脚本 | 路径 | 功能 | 数据源 | PDF 大小 |
|------|------|------|--------|----------|
| `transfer_heatmap.py` | `scripts/transfer_heatmap.py` | Cross-model transfer AUC 热力图 (4×4 矩阵，对角线高亮) | 嵌入 paper data (exp-013)；自动发现 `*transfer*.json` | 30.6 KB |
| `plot_auc_decay_ci.py` | `scripts/plot_auc_decay_ci.py` | AUC decay + 95% CI band (fill_between) | `artifacts/exp016_bootstrap_ci.json` + 3 个 `pairwise_auc.json` (per_fold → SE) | 23.0 KB |
| `plot_filtering_strategies.py` | `scripts/plot_filtering_strategies.py` | Filtering 策略对比柱状图 (5 策略 + error bar) | 嵌入 paper data (exp-006)；自动发现 `*filter*.json` | 25.5 KB |

### 输出文件
- `artifacts/figures/fig3_transfer_heatmap.pdf` — 4 模型 transfer 矩阵，RdYlGn colormap
- `artifacts/figures/fig_s1_auc_decay_ci.pdf` — 4 配置 AUC decay 曲线 + CI band（Qwen-base bootstrap + Pythia-greedy/Length-128/Qwen-rw fold-CI）
- `artifacts/figures/fig_filtering_strategies.pdf` — 5 策略 bar chart，Binary K* filtering 最优

### 数据说明
- **Transfer (exp-013)** 和 **Filtering (exp-006)** 数据不在磁盘上（可能在旧服务器 westc-26893 或未运行）。脚本使用 paper_framing 中的数值作为嵌入 fallback，同时支持自动发现 JSON 文件——当 exp-022 cross-scorer 或 exp-006 实际运行后，放置对应 JSON 即可替换嵌入数据。
- **Bootstrap CI** 真实数据可用：exp-016 有完整 bootstrap CI，另 3 个实验通过 per-fold AUC 计算近似 CI。

---
