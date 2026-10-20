---
loop: 5
reason: idle_timeout
updated: '2026-05-25T14:15:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- EMNLP 2026 主文 ≤ 8 页（当前刚好卡线，任何主文增加都会超限；Limitations 不计入页数）
- Abstract ≤ 200 words（当前 ~143 words）
- 匿名 repo `anonymous-nlp-2026-2/nlp_variance_gtheory`，禁止出现作者姓名/机构/个人 GitHub
- Overview figure 已移至 Appendix（method.tex 用 `Figure~\ref{fig:overview} (Appendix)` 引用）——不要移回主文，会超页
- 本地 `docs/paper/` 和匿名 repo `artifacts/anon_repo/` 必须保持同步，之前多次出现只改一边的情况

### 2. 🖥️ 基础设施快照
- 服务器：westd-32570 + westd-19912，各 4× RTX PRO 6000 96GB，均空闲
- 远程代码目录：`/root/nlp_variance_gtheory`（westd-32570）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/`
- 论文源文件：`docs/paper/*.tex`（本地）+ `artifacts/anon_repo/nlp_variance_gtheory/paper/`（匿名 repo clone）
- 活跃进程：无。无 RUNNING 实验、无 cron、无 tmux session

### 3. 📊 当前状态
项目处于 **全部就绪、等待用户 OpenReview 提交** 状态（DDL 2026-05-25，即今天）。Loop #5 确认：
- Registry：0 RUNNING，22 PREPARING 均已 killed（post-submission 扩展实验：OLMo/Yi/InternLM/DeepSeek + Llama-70B）
- ROADMAP、report、decisions 均无变动，与 Loop #4 一致
- 已向 Director 发送 dormant 状态确认
- 编译：8 页主文 + 9 页 appendix，0 critical warnings
- 匿名 repo 最终版 commit 0a73ee7

### 4. 📋 待办
- 用户完成 OpenReview 提交 → Reviewer 进入 dormant，无主动任务
- 收到审稿意见 → 读 `docs/rebuttal_prep.md`（4 主攻击点 + 3 补充预案）→ 按 rebuttal skill 启动审查
- 审稿人攻击 C2 (n=5 benchmarks) → 预案：降级为 "empirical observation"，C1 独立不受影响
- 审稿人要求更多 benchmark → GPU 空闲可立即跑，需 Director 决策 scope
- 22 个 killed 扩展实验可作为 rebuttal 期间的补充弹药，Director 决策是否激活

### 5. 🎯 战略上下文
- 核心贡献：C1 = 3×3 design 178 items for G≥0.80（强，数据充分，12 实验支撑）；C2 = MC vs FF format-associated variance（exploratory，n=5，p=0.10，较弱）
- Score trajectory: R5→R10 稳定在 3.5（Borderline Conference），目标 4.0
- 最容易判断错的事：**不要把 Sclar 的 50-76% accuracy swings 与我们的 <3% prompt variance share 直接对比**——前者是 range，后者是 variance share，metrics 不同
- C2 Bootstrap 加固已完成：MC vs FF item-related variance CI 不重叠（21pp gap），但样本量仍是弱点
- Llama-3.1-70B 跨家族验证通过（item_id=74.5%, G_item=0.957），是 C1 的关键 out-of-sample 证据
- 页数极度敏感：如需在 rebuttal 后加内容到主文，必须同时删等量文本
