---
loop: 4
reason: max_messages
updated: '2026-05-24T20:00:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文有两套 sections 目录必须保持同步：`paper/paper/sections/`（内层，编译用）和 `paper/sections/`（外层）。编辑后必须 `cp` 同步
- 图片文件有 6+ 个副本分散在不同目录，更新图片后必须复制到所有位置，否则 LaTeX 会用旧版本。关键路径：`paper/figures/paper/`（graphicspath）、`paper/paper/figures/`、`paper/paper/figures/paper/`、`figures/paper/`、`paper/paper/` 根目录
- EMNLP 2026：正文严格 8 页限制，Limitations 不计入；Abstract ≤ 200 words
- DDL：2026-05-25 AoE（明天）

### 2. 🖥️ 基础设施快照
- 本项目无远程服务器/GPU 需求（实验已全部完成，当前阶段是论文写作）
- 本地工作目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/`
- 论文编译：`cd paper/paper && latexmk -pdf -interaction=nonstopmode main.tex`
- 图片生成脚本：`paper/paper/scripts/`（heatmap、theta_scatter、grpo）和 `figures/paper/`（fig1、dose_response）
- Figure 1 原始生成脚本：`figures/paper/gen_fig1.py`（读取 `artifacts/psn_irt_params/mmlu_params.csv`）
- 活跃进程：无

### 3. 📊 当前状态
**刚完成**：缩写/专有名词定义检查（Abstract/Intro/Related Work/Method/Results 全部修完并同步），Discussion + Conclusion 压缩使正文恰好 8 页，已编译上传 PDF。

**等待用户确认的方案**：用户（周俊伟）提了 5 点图表改进需求，我发了详细分析和执行计划（见下方待办），正在等确认。

Registry: 无 RUNNING/PREPARING 实验。项目处于审稿阶段（review_chat_id 已配置）。

### 4. 📋 待办
- 用户确认图表方案 → 执行以下改动：
  1. **重画 Figure 1**（response pattern）：当前 matplotlib 基础散点图太简陋，需大幅提升专业度
  2. **重画 Figure 4**（theta scatter）：基础 scatter+errorbar，需提升美观度
  3. **GRPO 图从附录提升到正文**：支撑 Discussion 中 RL post-training 论点
  4. **Leaderboard 热力图从附录提升到正文**：支撑 57/60 cells universal misfit 论述
  5. **Figure 3 heatmap 改单栏**：信息密度不大（3×6），不需要双栏
  6. **调整图表位置**：填充 Page 2 和 Page 5（当前无图表）
  7. **压缩文字**：新增图表后确保正文仍 ≤ 8 页
- 用户如果修改方案 → 按修改后方案执行

### 5. 🎯 战略上下文
- 论文核心：IRT person-fit (ℓz*) 检测 LLM SFT 污染的 characterization study，**不是 method paper**。三个 findings：θ-shift absorption、detection-diagnosis tradeoff、non-monotonic dose-response
- Figure 1 是主图（概念类比），Figure 2 是组织性框架图（pipeline），我已向用户分析过这个判断
- 用户（曹晓玉/周俊伟）对图表质量要求很高，之前 Figure 4 图例位置改了 3 轮才满意
- 易踩坑：改完图片后必须复制到所有 6+ 个位置，之前因为只更新了一处导致 LaTeX 用旧图，用户反馈"你没挪呀"
- 审稿阶段已启动，Review Director 在 Group C 独立工作
- Abstract 当前 190 words，有 10 words 余量
