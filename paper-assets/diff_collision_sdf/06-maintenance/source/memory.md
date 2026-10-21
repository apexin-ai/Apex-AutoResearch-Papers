# Memory

## Fig 5 数据更新 (2026-05-27)
- λ=0 现在有 3 seeds: s0=57%, s1=52.5%, s2=55% → CAR 54.83±2.26%
- λ=0.1 只有 2 seeds: s0=58%, s1=58.5% → CAR 58.25±0.35% (s2 training)

## CoRL 2026 提交要求 (2026-05-28)
- **平台**: OpenReview (https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference)
- **DDL**: Abstract 2026-05-25, Full Paper 2026-05-29
- **会议**: 2026-11-09 ~ 11-12, Austin, TX
- **页数**: 正文 8 页（含 Limitations），Acknowledgments/References/Appendix 不计入
- **模板**: `\usepackage{corl_2026}`（submission），`\usepackage[final]{corl_2026}`（camera-ready 9 页）
- **附录**: 放在同一 PDF 末尾，不另交文件
- **Supplementary**: 通过 OpenReview 上传单个 zip（可含代码/数据，不含视频）
- **视频**: 鼓励提交，≤250MB / ~3分钟，必须外部托管（YouTube 等），PMLR 不允许视频在 supplementary 中
- **代码/数据**: 鼓励提供链接，写在论文正文中
- **AI 声明**: 提交时必须简要说明 LLM/生成式 AI 使用情况
- **审稿**: 每位有 3+ 篇投稿的作者必须同意担任审稿人，否则可能 desk-reject
- **匿名**: 提交阶段必须匿名

### 当前 PDF 状态
- main.pdf: 18 页（正文 8 页 + References 2 页 + Appendix 8 页）
- ⚠️ Limitations 段末尾溢出 ~2 行到第 9 页，需要修剪
- 已匿名，使用 submission 模式模板
- paper_switch.py --verify 全部通过
