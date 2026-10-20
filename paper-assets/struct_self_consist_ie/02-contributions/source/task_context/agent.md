---
loop: 20
reason: max_wall_time
updated: '2026-05-25T19:18:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- 匿名仓库 git config 必须为 `Anonymous <anonymous@example.com>`，push 前必须验证 author 不含真实信息（刚因 AWS IP 泄漏被 Reviewer 抓过）
- 匿名仓库只推实验代码，**不推论文 tex 文件**（`docs/paper/` 排除）
- PAT push 完成后**立即**清除 remote URL 中的 token
- 论文 tex 中 MBR utility 参数已从 α 改为 β（theory.tex + appendix.tex），signal alignment 的 α 保持不变，不要混淆
- EMNLP 2026 严格 8 页正文限制，当前刚好压到 8 页，任何 tex 修改后必须验证页数

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，实验代码路径 `/root/autodl-tmp/struct_self_consist_ie`（不是 git 仓库）
- 本地论文路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/`
- 本地匿名仓库：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/anon_repo`（remote: `https://github.com/anonymous-nlp-2026/struct_self_consist_ie`，username: `caoxiaoyu002`）
- 匿名仓库当前 HEAD：`48849f5`，8 个 commit，全部 author 为 Anonymous
- 活跃进程：无（之前两个孤儿进程 PID 282369/282468 已 kill）
- Cron：无活跃

### 3. 📊 当前状态
EMNLP 2026 DDL sprint 收尾阶段。本 session 完成的工作：
- 匿名仓库 force-push 最新实验代码（456 files, 4.7MB）
- 紧急修复 commit author 泄漏（AWS IP → Anonymous，旧 hash 404 已验证）

Registry 无 RUNNING/PREPARING 实验。所有实验已完成。无等待中的 Worker/Cron 回调。

### 4. 📋 待办
- Director 发新指令 → 按指令执行（DDL 当天可能有最后一轮 tex 修改或仓库操作）
- 如需再次 push 匿名仓库 → `request_secret("github_anon_pat")` 获取 PAT，push 前验证 author
- 如需修改 tex → 修改后编译验证页数 ≤ 8 页 + 0 errors

### 5. 🎯 战略上下文
- 论文核心结论：NER 上 test-time scaling（self-consistency）存在 correlation-selection gap——QE 信号能预测质量（AUROC 0.82）但选不出更好的候选。原因：degeneracy + signal alignment collapse（α→0）
- Few-NERD 是唯一正向案例（LP +1.39pp, p<0.001），其余数据集 SC 无增益甚至负向
- 3-seed FewNERD 统一统计已计算：MV -3.82±0.60 pp, LP +0.12±0.10 pp, Oracle +11.13 pp headroom（entity-type-averaged macro-F1）
- 易错点：匿名仓库 push 操作必须每次都验证 author 和清除 PAT，不要假设上次设置还在
