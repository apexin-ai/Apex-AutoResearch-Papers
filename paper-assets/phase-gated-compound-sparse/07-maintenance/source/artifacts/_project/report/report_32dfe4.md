# M2: Figure 1 更新为 n=496 数据

## 数据来源
- `table2_n500_full.csv`（本地 artifacts/n500_analysis/）
- 模型：DeepSeek-R1-Distill-Qwen-7B，n=496 paired problems

## 与旧图差异

| 指标 | 旧图 (n=50) | 新图 (n=496) |
|------|-------------|--------------|
| 数据来源 | bootstrap_results_full.json (profiling subset) | table2_n500_full.csv (full evaluation) |
| Importance G@s=0.15 | 14.27 [12.12, 17.42] | 7.45 [4.10, 11.36] |
| Importance G@s=0.20 | 30.85 [25.29, 41.28] | 17.90 [12.74, 26.31] |
| Importance G@s=0.25 | 55.44 [44.71, 71.36] | 49.06 [40.09, 57.83] |
| Importance G@s=0.30 | 75.50 [50.80, 95.24] | 79.79 [63.33, 96.51] |
| Random 点数 | 2 (s=0.15, 0.25) | 4 (全部 sparsity) |
| Random G@s=0.15 | 1.22 [0.96, 1.52] | 0.52 [0.40, 0.61] |
| Random G@s=0.25 | 1.00 [0.91, 1.10] | 1.09 [0.96, 1.19] |

## 主要观察
1. n=496 下 importance G 值在低 sparsity 端（s=0.15, 0.20）比 n=50 低约 50%，说明 profiling subset 高估了低 sparsity 的效应
2. 高 sparsity 端（s=0.25, 0.30）两者接近，趋势一致
3. Random 现在有 4 个点（之前只有 2 个），仍然 flat near 1×
4. 整体 narrative 不变：importance-based eviction 产生递增的 severity gradient，random 保持 ~1×

## 样式保持
- figsize: 3.5 × 2.6 inches
- 字体：DejaVu Serif
- 颜色：Importance #1f77b4, Random #d62728
- CI shading alpha=0.15
- 与旧图布局完全一致

## 输出文件
- 本地: `artifacts/m2_figure1_n500/figure1_n500.pdf`
- 服务器: `/root/autodl-tmp/pacs/figures/fig1_dose_response.pdf`（已覆盖旧图）
- 服务器: `/root/autodl-tmp/pacs/paper/figures/fig1_dose_response.pdf`（已覆盖）
- 服务器: `/root/autodl-tmp/pacs/analysis_output/figure1_n500.pdf`

## 注意：论文 caption 需同步更新
当前 caption 写的是 "from $69\times$ to $274\times$"，需更新为 "from $7.5\times$ to $79.8\times$"。
