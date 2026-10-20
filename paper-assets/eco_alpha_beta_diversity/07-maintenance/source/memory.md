# Project Memory — eco_alpha_beta_diversity

## 核心假设
生态学 alpha-beta-gamma 多样性分解能揭示 LLM 辅助写作中 flat metrics 无法捕捉的层次多样性结构。具体表现为：LLM 提高个体创作质量（alpha↑）的同时压缩群体多样性（beta↓）——"创造力-多样性悖论"。

## 数据集
- **Doshi & Hauser (2024)**: Dryad DOI: 10.5061/dryad.qrfj6q5k2, CC-BY
  - 文件：`writers-2023-06-28.csv`（500行×478列）
  - 条件列：`participant.condition`，值 `human`/`human_1AI`/`human_5AI`
  - 文本列：`ai_story_gen.1.player.story`
  - 有效故事：297 篇, no-AI=98, AI-editor=100, AI-ideas+editor=99
  - **文本长度差异**：no-AI=130w, AI-editor=145w, AI-ideas+editor=155w
  - **句子数极少**：平均 ~8 句/story → 语义级 species 只有 ~5 个，严重限制多样性估计

## MVP 结果汇总

### mvp_001（词汇级）— FAIL
- 方向正确但效应量不足，q=1 CI 重叠
- **根因**：文本长度混淆。rarefaction 归一化后差异消失
- **亮点**：q=2 beta 显著下降（高频词同质化）；Baselga PASS 3 通过；修正 FAIL test 2 后翻转为 PASS（R²=0.037）

### mvp_002（语义级）— FAIL → KILL
- sentence embedding + k-means 聚类做"语义 species"
- k=50/100/200 全部 FAIL，结论稳定
- **根因**：句子粒度太粗（8 句/story → 5 semantic species），方差极大
- **亮点**：Baselga PASS 3 仍通过；FAIL test 2 未触发（R²=0.001，框架有独特信息）

### 跨 MVP 一致性发现
1. **Baselga 分解始终有独特价值**：两个 MVP 中 PASS 3 都通过，FAIL 2 修正后都不触发
2. **Cosine similarity 始终无区分力**：r~0.03-0.04
3. **框架本身的数学结构成立，但在这个数据集+特征粒度上缺乏统计 power**

## 教训
- 词汇级：文本长度直接决定 unique word count，是致命混淆
- 语义级：Doshi 数据集故事太短（8 句），sentence embedding 聚类后 species 数太少
- 需要更长文本（或更细粒度的语义 unit）才能让多样性估计有足够分辨率
- Bootstrap 95% CI 不重叠标准 ≈ p<0.006，对 ~100 样本/条件 的小效应量来说太严格

## 投稿目标
主投 TACL（rolling deadline），备选 CHI 2027 / EACL 2027
**状态**：Director 待决策（kill 或 pivot）

## 决策记录
- [2026-05-21] MVP 在本机运行，纯 CPU
- [2026-05-21] MVP 词汇级 FAIL，核心瓶颈是文本长度混淆
- [2026-05-21] 延伸分析修正：FAIL test 2 翻转为 PASS，q=2 多种标准化下一致
- [2026-05-21] 语义级 MVP FAIL，句子粒度太粗。Director 预设 kill 条件触发。
