---
loop: 3
reason: max_messages
updated: '2026-05-25T06:13:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验，纯论文写作项目（CSD = Controlled Style Decomposition，LLM judge style bias 分析论文）
- 匿名 repo 路径：`/tmp/anon_repo`，remote：`https://github.com/anonymous-nlp-2026-2/causal_style_decomp_judge.git`
- EMNLP 2026 DDL：2026-05-27 AoE，主文严格 8 页，Limitations 不计入页数但必须在第 9 页开始
- Abstract ≤ 200 words（当前 186 词）
- Appendix 已有 27 个编号 section（A-AA），不能再加编号 section（会超字母计数器上限 crash）
- 论文源码在本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/`

### 2. 🖥️ 基础设施快照
- 无远程服务器，所有工作在本地完成
- LaTeX 编译：`latexmk -pdf -interaction=nonstopmode main.tex`（在 `docs/paper/` 目录下）
- PDF 渲染检查：`pdftoppm -png -r 200 -f N -l M main.pdf _pdf_images/main`
- 匿名 repo 同步流程：cp 修改文件到 `/tmp/anon_repo/sections/` + `main.pdf` → git commit → git push → feishu_upload_file
- 无活跃进程 / tmux / cron

### 3. 📊 当前状态
本轮完成了大量论文排版和质量修复：
- Related Work 从 5 段压缩到 3 段
- Method/Experiments 扩写填满 8 页
- Conclusion 从 7 句压缩到 4 句，释放空间补到 Method 和 Analysis
- 审计报告 critical 修复：WildBench→MT-Bench、four→five providers
- ~20 处 em-dash AI 指纹替换为逗号/括号/冒号
- 13 处缩写首次出现未展开的修复（LLM/NLI/OR/RLHF/DPO/NLP/BT/ATE/NLG/MNLI/FWER/IIA/FK）
- Code and Data 移到 appendix 末尾（无编号 section）
- `\ref{app:power}` → `\ref{app:power_analysis}` 修复 ?? 引用
- 最新 commit：f9c9514，编译无 undefined reference

Registry 无 RUNNING 实验，项目处于纯写作/投稿准备阶段。

### 4. 📋 待办
- 用户要求新修改 → 编译 → 检查页面 8/9 分界（Limitations 必须在第 9 页）→ 推送匿名 repo → feishu_upload_file
- 收到审稿报告 → Read `review-report-action` skill → 逐条处理
- DDL 前最终检查：abstract 字数、undefined refs、float 位置、页数

### 5. 🎯 战略上下文
- 项目核心发现：Likert Blindspot（pairwise 检测到 style bias 而 Likert 检测不到）+ GEE per-axis confound 分解（verbosity style-dominated，formality conditional）
- 页面布局极度敏感：增/删 1 句话（~2-3 列行）就可能导致 Limitations 在第 8/9 页之间跳动。每次修改后必须编译+渲染 page 8-9 确认
- 易踩坑：appendix 不能加编号 section（27 个已到上限）；abstract 改动后必须重新计词（≤200）
- 用户对排版质量要求极高，之前因 `\enlargethispage` 导致内容溢出到页码下方被严厉批评
- 审稿阶段已启动（review_chat_id 存在），但当前重心是投稿前最终打磨
