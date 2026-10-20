---
loop: 4
reason: max_messages
updated: '2026-05-25T14:16:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验，所有工作在本地完成（论文写作 + 图表生成 + 匿名仓库管理）
- 匿名仓库 git remote 使用 PAT 认证：用户名 caoxiaoyu001，已配置在 remote URL 中
- 匿名仓库链接必须用 `https://anonymous.4open.science/r/nlp_variance_gtheory-11E1/`，不能用 GitHub 链接
- Figure 8 (fig4_difficulty_scatter) 生成时禁用 `bbox_inches='tight'`，必须用 `fig.subplots_adjust()` 手动控制边距（反复踩坑 5 轮才解决）
- `\enlargethispage` 已被删除，不要重新加回（用户明确反馈"左边文字贴底了"）

### 2. 🖥️ 基础设施快照
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/`
- 匿名仓库 git root：`artifacts/anon_repo/nlp_variance_gtheory/`（注意 `.git` 在 `nlp_variance_gtheory/` 下，不是 `anon_repo/`）
- 论文源码：`artifacts/anon_repo/nlp_variance_gtheory/paper/`
- 图表生成脚本：`figures/paper/gen_fig*.py`（用 `python3` 运行，无 `python`）
- 编译：`cd paper && latexmk -pdf -interaction=nonstopmode main.tex`
- 无远程服务器、无 GPU、无 wandb、无活跃进程

### 3. 📊 当前状态
刚完成 Abstract 和 Introduction 的叙事重写（用户周俊伟反馈"堆砌数字太多，像实验报告"）。改动已 push 到匿名仓库（commit 64b83d6）。

本轮 session 完成的工作：
1. Figure 8 宽度修复：canvas 5.0in, left=0.065, right=0.995，MMLU 标签移到左侧
2. Figure 9 高度增加：figsize 从 (8.5,5.0) 改为 (8.5,6.5)
3. 审计报告 4 个 critical 修复：删除 dangling contamination 引用、Conclusion 改为 Discussion and Conclusion、"confirming"→"suggesting"、552→178 明确为 MMLU-specific
4. 正文缩减适配 8 页：删除冗余句、精简 D-study 段落、去掉 `\enlargethispage`
5. Abstract/Introduction 叙事重写：problem-first framing、76pp hook、4 段+contributions 结构

Registry: 无 RUNNING/PREPARING 实验。项目处于论文写作收尾阶段。
等待中: 无 Worker 回调、无 Cron。审稿阶段已激活（review_chat_id 已配置）。

### 4. 📋 待办
- 用户对 Abstract/Introduction 重写有反馈 → 按反馈调整（注意不要回退到数字堆砌风格）
- 用户要求重新审稿 → 调用 `submit_paper_to_review` 提交
- 审计报告剩余 warnings 需处理：Figure 7 红绿色盲不友好（改 viridis/cividis）、$p$ 符号三重含义（考虑改 item difficulty 为 $d_i$）、page 7 display items 过密（4 个）
- 如果 Introduction 重写后用户满意 → 检查 Related Work 和 Method 是否需要同步调整叙事一致性（当前 Related Work 引用了 Intro 中的 gap 编号）

### 5. 🎯 战略上下文
- 投稿目标：EMNLP 2026 via ARR，DDL 2026-05-25（今天）
- 论文 2 个 core contributions：(C1) Design-dependent reproducibility budgets, (C2) Format-associated variance patterns (exploratory)
- 已完成 Dream 模拟（best 7, median 6, worst 5）
- 关键叙事决策：model×item interaction 不要用"hidden"（IRT 文献已知）；format-associated pattern 必须标注 exploratory（n=5, p=0.10）；infrastructure crossing 是 confirmatory secondary
- 易错点：Figure 8 的 `bbox_inches='tight'` 会导致 canvas 膨胀超过 figsize，永远用 `subplots_adjust` 代替
- 易错点：匿名仓库 git 操作必须 `cd` 到 `artifacts/anon_repo/nlp_variance_gtheory/`（不是 `anon_repo/`）
