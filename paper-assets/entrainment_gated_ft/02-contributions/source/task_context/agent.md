---
loop: 3
reason: max_wall_time
updated: '2026-05-25T19:55:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 匿名仓库 push URL 含 PAT token，禁止在任何日志/汇报/paper 中泄露（仅存于 `_anonymous_repo.json`）
- 匿名仓库 git config 必须是 Anonymous / anonymous@example.com，禁止用真实身份
- 本项目无 GPU 实验在跑，核心工作是论文写作 + 图表 + 投稿准备（EMNLP 2026 ARR）
- PaperBanana 使用 `google_api_key`（通过 request_secret 获取），有配额限制，429 时需等待恢复

### 2. 🖥️ 基础设施快照
- 本项目无远程服务器，所有工作在本地完成
- 项目目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/`
- 匿名仓库：`/tmp/anon_repo/`（已 push 到 GitHub）
- 匿名 GitHub：`https://github.com/anonymous-nlp-2026-2/entrainment_gated_ft`（commit 3b4dc1c）
- 论文图表源码：`figures/paper/`（8 个 gen_*.py + palette.py）
- 论文图表输出：`figures/paper/` + `docs/paper/figures/`（双目录输出）
- PaperBanana 输出：`docs/paper/figures/fig2_banana_*.png`、`fig_method_overview_banana_v9.png`（当前最佳）
- 实验数据：`artifacts/_project/data/`（45 个 JSON/CSV 文件）
- 无活跃进程 / 无 tmux / 无 cron

### 3. 📊 当前状态
刚完成匿名仓库推送（61 files，已验证匿名性，已向 Director 汇报）。

PaperBanana v10 之前在后台运行（task byp44ztjh），session 重置后状态未知——可能已完成但结果未收集。当前最佳版本是 `fig_method_overview_banana_v9.png`（separate circles + dashed triangle，白背景，无 card borders）。

Registry 状态：本项目实验全部 DONE，无 RUNNING/PREPARING。

等待中：无 Worker 回调、无 Cron、无 Director 决策pending。

### 4. 📋 待办
- Director 要求查看 v10 结果 → 检查 `docs/paper/figures/` 是否有 v10 输出，有则与 v9 对比选最佳，无则用 v9 作为 final
- Director 要求更新匿名仓库 → `cd /tmp/anon_repo && git add -A && git commit && git push origin main`
- Director 要求最终 Figure 2 定稿 → 将最佳 PaperBanana 版本复制为 `fig_method_overview.pdf`（或保留 matplotlib 版本）
- 投稿前 → 检查 paper PDF 中 Figure 2 引用是否指向正确文件

### 5. 🎯 战略上下文
- 论文核心发现：Aggregate equivalence ≠ behavioral equivalence — hybrid linear recurrent models 在 per-example 级别表现出 architecture-specific sensitivity（Jaccard J≈0.10，极低重叠）
- 三个架构对比：GatedDeltaNet、RetNet、HGRN2（Pure vs +Attention variants）
- Figure 2 是 method overview 概念图，Director 对视觉质量要求极高（"Nature/Science 级别"），Gemini Imagen 的 Venn 图始终 overlap 过大，v9 用"三个分离圆 + 虚线连接"绕过了这个限制
- 易错点：PaperBanana prompt 中不要写"Venn diagram"（Gemini 会强制画重叠圆），要写"three separate circles with dashed connecting lines"
- 调色板已统一升级（BLUE=#4E79A7, CORAL=#C56C6C, TEAL=#59A572, AMBER=#E49444），所有 8 个图表脚本已用新配色重新生成
- DDL 是今天（2026-05-25），匿名仓库已推送完毕，论文投稿的其余步骤由 Director 协调
