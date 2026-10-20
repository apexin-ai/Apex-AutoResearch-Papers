---
loop: 22
reason: max_messages
updated: '2026-05-25T18:56:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无远程 GPU 实验（纯分析+论文项目），所有实验数据在本地 `artifacts/` 目录
- 论文正文严格 8 页限制（EMNLP 2026），Limitations 只写 2-3 个短点
- Abstract ≤ 200 words
- γ 符号已拆分：cascade margin 用 γ，power-law exponent 用 η——不要混回去
- `\raggedbottom` 已删除（与官方 ACL 模板对齐），不要加回来

### 2. 🖥️ 基础设施快照
- 本地工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/`
- 论文目录：`docs/paper/`，入口 `main.tex`，编译 `pdflatex + bibtex`
- 实验数据：`artifacts/` 下各 CSV/JSON（cross_arch_table7.csv 等）
- 图表生成脚本：`docs/paper/figures/gen_fig_*.py`
- 无远程服务器、无 GPU 进程、无 wandb、无活跃 cron

### 3. 📊 当前状态
本轮完成的工作全部是论文排版修改（由用户团队 曹晓玉/周俊伟 驱动）：
- Figure 3、Figure 6 从竖版 2×1 改为横版 1×2 subfigure 布局
- Figure 5 图例移到图顶部（解决遮挡问题）
- 所有主文 figure/table 从 `[H]` 改为 `[t]` float placement
- γ→η 符号拆分（跨所有 .tex 文件）
- em-dash (`---`) 全文替换为逗号/括号/分号（去 AI 写作痕迹）
- ACL 官方模板对齐：删除 `\linenumbersep` 覆盖、删除 `\raggedbottom`
- Limitations 从 15 行压缩到 6 行（3 短点）
- 当前编译：37 页，正文 8 页，无 critical warnings
- 无 RUNNING/PREPARING 实验，无等待中的回调

### 4. 📋 待办
- 用户团队提出新排版修改请求 → 按要求修改 + 编译 + 上传 PDF 到飞书
- 用户说"进入审稿阶段"或"重新审稿" → 调 `submit_paper_to_review`
- 收到审稿报告 → Read `review-report-action.skill.md` 后按协议处理

### 5. 🎯 战略上下文
- 项目已进入审稿阶段（review_chat_id 已配置），Review Director + 2 Reviewers 并行审稿
- 论文核心 story：model collapse 的可检测性 landscape——不是提出新检测方法，而是系统性分析 5 种方法在不同 contamination regime 下的检测能力差异
- 当前论文状态稳定，主要工作是响应用户团队的排版微调请求
- 易错点：`figure*[t]` 在双栏 LaTeX 中出现在声明位置的**下一页**顶部，调整 figure 位置时需要把声明放在目标页的前一页内容中
- 每次论文修改编译后必须上传 PDF 到飞书（feedback memory 记录的硬要求）
