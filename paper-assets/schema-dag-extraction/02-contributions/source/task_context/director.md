---
loop: 11
reason: max_messages
updated: '2026-05-25T19:17:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无远程 GPU 实验，所有工作在本地完成（纯论文写作+排版项目）
- 论文正文严格 8 页限制（EMNLP 2026 via ARR），Limitations 不计入但必须在正文内
- `\enlargethispage{2\baselineskip}` 在 discussion.tex 第 1 行是第 8 页填满的关键机制，不能删
- 改任何正文文本都要重新编译+渲染第 8 页验证没溢出（之前加 ~10 个单词就从 26 页溢出到 27 页）
- float spacing 参数已压缩到极限（textfloatsep/floatsep/dbltextfloatsep/dblfloatsep 全 10pt plus 2pt minus 4pt），不要再动
- Abstract 不超过 200 words（当前 158 words）
- bib 文件曾有两个严重幽灵作者（AI 生成的假作者），已修复。后续新引用务必验证

### 2. 🖥️ 基础设施快照
- 无远程服务器，纯本地论文项目
- 论文源码：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/`
- 编译：`latexmk -pdf main.tex`，需要 `texlive-fonts-extra`（已安装，inconsolata 包）
- PDF 渲染检查：`pdftoppm -png -r 300 -f N -l N main.pdf /tmp/paper_pages/page`
- 当前 PDF：26 页（8 页正文 + 3 页 references + 15 页 appendix）
- 无活跃进程/cron/tmux

### 3. 📊 当前状态
Loop #11 刚启动即收到 RESET_BOTH 请求，无新工作产出。前一轮（Loop #10）完成了两批修复：
- 论文审计报告修复：RQ2 叙事不一致、appendix 实验编号、IntraSub 内联定义、总计算量标注
- 引用验证报告修复：两个严重幽灵作者（baan-2023、dlisc-2025）、三个标题/作者小修
- 排版修复：第 8 页空白消除、orphan/widow 修复、ACL 模板对齐

Registry: 70 个实验，无 RUNNING/PREPARING。12 个 pending 状态（prompt_sensitivity 系列等）但均为历史遗留，不打算执行。

### 4. 📋 待办
- 用户回复 checklist A1 vs Limitations 不匹配问题 → 按用户指示修改 checklist.tex 或 Limitations 正文
- 用户决定是否修 Figure 6 红绿配色 → 如果要改，派 Agent 用 draw-paper-figure skill 重新生成
- 用户/Review Director 发来新一轮审稿报告 → 按 review-report-action skill 处理（Holistic Pass + Per-Comment Action Matrix）
- 用户说"重新审稿"/"进入审稿" → 调 `submit_paper_to_review`

### 5. 🎯 战略上下文
- 项目核心结论：schema complexity = count（Dim 1）+ confusability（Dim 2），BCS 独立解释 RE 27% 方差，NER 无 BCS 信号（错误分散），schema decomposition 因 routing failure 和 merge amplification 失败
- 论文 framing 是 analysis paper（非 method paper），三个 RQ 结构清晰
- 审计报告总结：0 critical，主要 warning 已修复
- 易踩的坑：第 8 页极度拥挤，任何文本变动都可能导致溢出；R²=0.218 数据错误已修复（r/R² 混淆），pooled semipartial R²=0.273 是 C3 primary 证据
- 决策日志 72 条，论文溯源覆盖率 54/57
