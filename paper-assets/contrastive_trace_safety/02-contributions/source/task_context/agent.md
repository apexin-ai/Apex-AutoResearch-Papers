---
loop: 5
reason: max_wall_time
updated: '2026-05-25T20:00:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验，纯论文编辑。不要 SSH 任何服务器，不要 submit_training_job
- 匿名仓库 push URL 在 `_anonymous_repo.json`，push 前必须确认 `/tmp/anon_repo/` clone 存在且 remote 正确
- EMNLP 2026 ARR 正文 ≤ 8 页（不含 Limitations + References），abstract ≤ 200 words
- 论文 narrative 主线已调整为 "metric choice reverses conclusions"，HS advantage 是 conditional secondary finding——任何改动不能偏离此定位
- Abstract/Intro 禁止 HS 缩写（用 hidden-state 全称）、禁止 CR-composite（用 crossing-rate composite）、正文禁止 HB（用 "after correction" / "survives correction"）、MDE 仅 appendix

### 2. 🖥️ 基础设施快照
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/`
- 论文目录：`docs/paper/`，主文件 `main.tex`，编译用 `pdflatex -interaction=nonstopmode main.tex`（在 paper 目录下）
- PaperBanana venv：`/tmp/pb_venv/`（`source /tmp/pb_venv/bin/activate`），Google API key 已在本 session 审批通过但 key 是临时的
- 无活跃进程 / cron / GPU 任务
- 匿名仓库上次 push commit: c331805（Figure 1 PaperBanana），本地已有后续 commits 未 push

### 3. 📊 当前状态
**刚完成**：
1. 论文叙事主线重构（commit 7ebe013）：Abstract/Intro/RelWork/Experiments/Discussion/Limitations 全部重写或调整，主线从 "HS beats text" → "metric choice reverses conclusions"
2. Figure 1 PaperBanana 重画（commit 50953b4）：3-panel 单行概念图（task + reversal + mechanism）

**Director 对 abstract/intro/discussion 做了进一步润色**（通过 linter/手动修改）：
- Abstract: 改为单段叙事风格，~195 words，更流畅
- Intro: 改为 3 段 + contributions（加了第 3 段讲 conditional advantage + negative results + control tasks）
- Discussion: 精简 boundary conditions 段，去掉 tab:consolidated 表格（改为 \cref 引用）

**这些 Director 修改尚未 commit**——下一个"你"接手时 git status 会显示 abstract/intro/discussion 有 unstaged changes。

Registry: 全部实验 DONE，无 RUNNING/PREPARING。无等待中的 Worker/Cron 回调。

### 4. 📋 待办
- Director 要求 push 到匿名仓库 → clone `/tmp/anon_repo/`，git pull，copy 论文文件，commit + push
- Director 要求最终编译检查 → pdflatex 两遍，确认 0 errors，≤ 8 页正文，abstract ≤ 200 words
- tab:consolidated 是否从 discussion.tex 移除（Director 的 linter 修改里已去掉表格 body，改为 \cref 引用）——需确认 tab:consolidated 定义是否移到了别处（appendix？）还是完全删除。如果 \cref{tab:consolidated} 仍在但 label 已删，会产生 undefined reference
- 如果 Director 说"提交"/"submit"→ 走 `backup_project_to_s3` + push 匿名仓库 + 最终 PDF 检查

### 5. 🎯 战略上下文
- 项目核心结论：metric-induced layer selection bias 是 robust finding（14-61 layer divergence, cosine compression mechanism, generalizes to AdvBench + Gemma-2）；HS advantage 是 conditional（cross-validated at 7-8B, diminishes with stronger encoders, suggestive at 32B）
- 32B 结果用 "suggestive" 不用 "exploratory$\dagger$"
- 最易判断错的事：Director 的 linter 修改已改变了 abstract/intro/discussion 的内容——不要用之前 session 的记忆覆盖这些修改。始终以文件当前状态为准
- Figure 1 caption 里的 p-values 已去掉，但图片本身（PaperBanana 生成的 PNG）内嵌有 p=0.83 和 p<0.005 文字——这是图片内容无法改 LaTeX 去除，Director 已接受
- 匿名仓库有多个未 push 的 commits（叙事重构 + Figure 1 重画），push 时注意一次性推送
