# Handover — 2026-05-21

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **mvp_002** (negative): 语义级（sentence embedding 聚类）Hill number alpha-beta 分解能在 Doshi & Hauser 数据集上检测到 LLM 辅助写作的 alpha↑/beta↓ 模式，且效应量大于词汇级（mvp_001），因为语义向量维度固定不受文本长度线性影响，能排除长度混淆 ← 基于 mvp_001
  [semantic_mvp_results](/api/workspace-files/projects/eco_alpha_beta_diversity/artifacts/mvp_002/data/semantic_mvp_results.json) | [semantic_hill_numbers_plot](/api/workspace-files/projects/eco_alpha_beta_diversity/artifacts/mvp_002/chart/semantic_hill_numbers.png) | [semantic_baselga_plot](/api/workspace-files/projects/eco_alpha_beta_diversity/artifacts/mvp_002/chart/semantic_baselga.png) | [semantic_cosine_heatmap](/api/workspace-files/projects/eco_alpha_beta_diversity/artifacts/mvp_002/chart/semantic_cosine_heatmap.png) | [semantic_k_sensitivity_plot](/api/workspace-files/projects/eco_alpha_beta_diversity/artifacts/mvp_002/chart/semantic_k_sensitivity.png) | [semantic_mvp_002_report](/api/workspace-files/projects/eco_alpha_beta_diversity/artifacts/mvp_002/report/semantic_mvp_002_report.md)
- **mvp_001** (negative): 词汇级（word unigram）Hill number alpha-beta 分解能在 Doshi & Hauser 数据集上检测到 LLM 辅助写作的 alpha↑/beta↓ 模式，且 Baselga 分解提供 flat metrics（cosine similarity）无法等价替代的诊断信息

## 趋势
成功 0 / 负向 2 / 失败 0 / 共 2

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-25068: 无 GPU 信息

## 告警
（无）
