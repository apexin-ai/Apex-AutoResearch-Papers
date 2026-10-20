---
loop: 12
reason: max_messages
updated: '2026-05-24T19:17:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 1 张 GPU：cuda:0 @ gpu-6000pro-2（RTX PRO 6000）
- 匿名仓库 token `[REDACTED_GITHUB_TOKEN]` 绝不能进入代码文件，只存在 `_anonymous_repo.json`
- EMNLP 2026 ARR：主文严格 8 页限制，abstract ≤200 words
- 论文文本禁止 em dash（用逗号/括号替代）
- TUM 服务（localhost:8001）当前不可用，secrets 无法通过 request_secret 解密；需要 API key 时走 feishu 卡片申请流程
- GOOGLE_API_KEY: [REDACTED] store_secret，但因 TUM 宕机需显式传给 Agent）

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2（分类 B，保留至 rebuttal）
- 项目工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/`
- 论文源码：`docs/paper/`（main.tex + 10 个 section .tex）
- 匿名仓库本地克隆：`/tmp/anon_repo/`，remote push URL 在 `_anonymous_repo.json`
- PaperBanana venv：`.pb_venv/bin/paperbanana`（v0.1.2）；另有 `/tmp/pb_venv/` 副本
- Figure 备份：`docs/paper/_figure_backups/20260524_161209/` 和 `20260524_164804/`
- 无活跃进程 / 无 tmux / 无 cron

### 3. 📊 当前状态
- 全部 152 个实验已完成（95 success），论文已定稿进入 submission 准备阶段
- 刚完成：缩写/专有名词定义自检，修复 16 处（Agent 已编译通过，28 页无 Overfull）
- 之前完成：3 个 critical paper quality fix（页面溢出、accumulation paragraph、Discussion 重写）+ 10 个 appendix pointer
- Figure 1 PaperBanana 重画：Agent 跑了 6 轮 PaperBanana 迭代 + matplotlib 精修版，当前 `docs/paper/figures/fig_problem_illustration.png` 是 17:20 版本（改进版 matplotlib），尚未推送到匿名仓库
- Registry 无 RUNNING/PREPARING 实验
- 无等待中的 Worker 回调 / Cron

### 4. 📋 待办
- 匿名仓库需要 push 最新改动（缩写修复 + Figure 1 更新）→ `cd /tmp/anon_repo && cp docs/paper/* . && git add && commit && push`
- 冯元宁可能追问 Figure 1 效果 → 上传当前 PNG 到飞书（`feishu_upload_file`）让她确认
- 如果用户要求重新审稿 → `submit_paper_to_review` 提交最新稿件
- ARR submission form（OpenReview）由运维团队手动填写，不需要 Director 操作

### 5. 🎯 战略上下文
- 项目核心：用 19 个统计特征 + Random Forest 做递归生成文本的深度估计（ordinal classification），区别于 binary real/fake detection
- 论文 story 稳固，实验矩阵已满，当前是 submission finalization 阶段
- 易错点 1：Figure 1 的 PaperBanana 重画用户（冯元宁）之前不满意纯 cosmetic 改动（"你这不是完全没改吗"），需要确认当前版本是否达到她的预期后再推
- 易错点 2：TUM 宕机导致所有 stored secrets 不可解密，任何需要 API key 的操作都要走 feishu 卡片流程或显式传 key
- 易错点 3：匿名仓库 push 必须用 `_anonymous_repo.json` 里的 push_url（含 token），author 设为 Anonymous
