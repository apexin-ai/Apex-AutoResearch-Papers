# analyze feature group ablation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_feature-group-ablation_20260518T135038_result.json`
- **Structured JSON:** [`0cb3196e09f78df0b471.json`](../../sessions/0c/0cb3196e09f78df0b471.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### 结果概览

| Feature Group | Single (C4/arXiv/Wiki) | LOO Drop (C4/arXiv/Wiki) |
|---|---|---|
| **Surprisal (base)** | .597 / **.809** / .581 | -0.007 / **-0.031** / -0.003 |
| **Surprisal (deriv.)** | .590 / .789 / .590 | +0.003 / -0.003 / +0.004 |
| Lexical diversity | .550 / .691 / .557 | -0.001 / -0.005 / -0.005 |
| Freq. distribution | .533 / .684 / .564 | -0.005 / -0.009 / -0.007 |
| **Full (15D)** | **.609 / .860 / .619** | --- |

### 核心发现

1. **Surprisal (base) 是跨域最强的单组特征**，在 arXiv 上单独达到 0.809 AUC（Full 才 0.860），LOO drop 也最大（arXiv -0.031）
2. **Surprisal (deriv.) 排第二**，但在 C4/Wiki 上 LOO drop 为正（去掉反而微升），说明与 base 有冗余
3. **Lexical diversity 和 freq distribution 单独较弱**（接近 0.5），但 LOO 表明它们仍有微小贡献（drop 0.005~0.009）
4. **arXiv 域的区分度远高于 C4/Wiki**，各组特征在 arXiv 上都更有效

### 产出文件

**本地:**
- CSV: `artifacts/feature_ablation/ablation_results.csv`
- JSON: `artifacts/feature_ablation/ablation_results.json`
- LaTeX: `artifacts/feature_ablation/latex_table.tex`
- Heatmap: `artifacts/figures/fig_feature_ablation.{pdf,png}`

**服务器 (cqa1-22115):**
- 全部结果: `/root/autodl-tmp/gen-depth-contamination/results/feature_ablation/`
- 脚本: `scripts/feature_group_ablation.py`

---
