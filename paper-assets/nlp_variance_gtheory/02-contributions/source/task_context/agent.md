---
loop: 2
reason: max_wall_time
updated: '2026-05-25T20:01:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验，纯论文写作项目。所有实验数据已在 `artifacts/exp001`-`exp004` 中完成
- 匿名仓库 commit 必须用 `git -c user.name="Anonymous" -c user.email="anonymous@anonymous.invalid" commit`，否则暴露服务器 hostname
- 正文严格 ≤ 8 页（EMNLP 2026 ARR）。当前通过 `\enlargethispage{8\baselineskip}` 在 Conclusion 前勉强卡住 8 页边界——任何增加正文内容的改动都可能溢出，改完必须编译验证
- Abstract ≤ 200 words，匿名链接只能放在 Abstract 首页脚注（`anonymous.4open.science`）
- `docs/paper/` 是本地编译目录，`artifacts/anon_repo/nlp_variance_gtheory/paper/` 是匿名仓库副本——两处必须同步

### 2. 🖥️ 基础设施快照
- 无远程服务器，全部在本地完成（`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/`）
- 论文源码：`docs/paper/`（main.tex + 各章节 .tex），编译命令 `pdflatex -interaction=nonstopmode main.tex`
- 图表源码：`figures/paper/gen_fig*.py`（matplotlib 脚本，本地 python3 直接运行）
- 匿名仓库：`artifacts/anon_repo/nlp_variance_gtheory/`，remote = `https://github.com/anonymous-nlp-2026-2/nlp_variance_gtheory.git`
- 实验数据：`artifacts/exp001/`-`artifacts/exp004/`（JSON/CSV，只读参考）
- 无活跃进程 / tmux / cron

### 3. 📊 当前状态
刚完成 Figure 8（`fig4_difficulty_scatter`）第三轮重绘——Director 亲自重写了生成脚本，去掉 `bbox_inches='tight'`，改用 `subplots_adjust` 手动控制边距，figsize 精确 3.4×2.6in。已编译验证正文 8 页，匿名仓库已推送。

本 session 完成的所有改动：
- Figure 4+5 合并为 `figure*[t]` 并排（method.tex）
- Figure 8 三轮重绘（字体放大 + 填满列宽 + 去 bbox_inches 缩放）
- Figure 9 重新生成（高度 3.5→5.0，figsize `(8.5, 5.0)`）
- `\enlargethispage{8\baselineskip}` 加在 main.tex Conclusion 前解决页面溢出
- 匿名仓库多次推送，最新 commit `0a81a17`

无等待中的 Worker/Cron/Director 决策。

### 4. 📋 待办
- Director 发新指令 → 按指令执行（当前处于投稿 DDL 当天 2026-05-25，可能有最后一轮修改）
- 如需修改任何正文内容 → 编译后必须验证 Conclusion 仍在 P8（`\enlargethispage{8\baselineskip}` 余量极小，约 1-2 行）
- 如需修改图表 → 同步更新 `figures/paper/` + `artifacts/anon_repo/.../figures/` + 推送
- 投稿前最终检查 → Abstract word count（≤200）、orphan bib entries、匿名仓库 commit author 全为 Anonymous

### 5. 🎯 战略上下文
- 论文核心结论：G-theory 方差分解表明 3-prompt × 3-seed 设计将 MMLU 可靠性阈值（G≥0.80）所需 items 从 552 降至 178。Item difficulty 是最大方差源（MC 68-72%），format 影响方差结构（MC vs FF）
- 页面预算极紧：`\enlargethispage{8\baselineskip}` 是 aggressive hack，任何图表放大/文本增加都可能打破平衡。下一个"你"改完任何东西后第一件事就是检查 Conclusion 是否仍在 P8
- Figure 生成脚本位置易混淆：`gen_fig1_cross_benchmark.py` 和 `gen_fig4_difficulty_scatter.py` 在 `figures/paper/`，但原始 `difficulty_heterogeneity.py` 在 `artifacts/anon_repo/.../scripts/`（需要服务器数据目录，本地无法运行）
- 匿名仓库的 `main.tex` graphicspath 是 `figures/`（相对路径），本地是 `../../figures/paper/`——两处路径不同
