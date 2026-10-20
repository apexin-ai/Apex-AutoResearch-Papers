---
loop: 1
reason: max_messages
updated: '2026-05-13T08:53:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 仅限 autodl-pgpf 的 cuda:0, cuda:1（2×RTX PRO 6000 96GB），不可用其他服务器的卡
- 项目名 solver-trace-ablation 与实际研究方向不匹配——IDEA_BRIEF 是 PGPF（Property-Guided Per-Sample Filtering / model collapse），已按 PGPF 推进，用户被问了方向确认但**尚未回复**，不要擅自切换方向
- AutoDL 特殊约束：pip/git 前必须 `source /etc/network_turbo`；大文件必须放 `/root/autodl-tmp/`；HF_HOME=/root/autodl-tmp/.hf_cache

### 2. 🖥️ 基础设施快照
- 服务器：autodl-pgpf，SSH: `ssh -p 17606 root@connect.bjb1.seetacloud.com`
- 密码：`request_secret(key_id="autodl_pgpf_password")`
- 工作目录：`/root/autodl-tmp/pgpf`
- Python/conda：未确认（aml-train 镜像用 conda，需 Agent SSH 探测确认）
- 模型/数据集路径：未确认（Phase 0 期间应已下载到 autodl-tmp 下）
- 活跃进程：**不明**——Phase 0 v2 Worker 派出后 Agent session 断了，GPU 健康数据返回 "no data yet"
- W&B/cron：未配置

### 3. 📊 当前状态
- **刚做的**：API 额度恢复后重建 Agent session，派了紧急恢复指令让 Agent 检查 Phase 0 v2 状态 + 占满空卡。同时 reset 了 Reviewer（硬限到期）
- **Phase 0 v2 Worker**（worker_exp_phase0_ortho_v2_20260513T062027）：状态完全不明，可能已完成/崩溃/仍在跑。Agent 刚收到指令去 SSH 检查
- registry：成功 0 / 负向 0 / 失败 1 / 共 1（Phase 0 v1 失败过一次）
- 项目配置文件（config/projects/solver-trace-ablation.yaml）**不存在**，get_project_status 显示服务器/代码路径/飞书均未配置。但 autodl-pgpf 已注册为 SSH host 且之前的 session 用过它
- 知识文件全部未创建：ROADMAP.md / paper_framing.md / experiment_plan.yaml / report.md / ideas.md

### 4. 📋 待办
- Agent 回复 Phase 0 v2 结果 → PASS: 立即启动 Phase 1（3代过滤对比，5条件）; FAIL（属性高度相关）: 重新评估多属性 story 是否成立
- 用户确认方向（PGPF vs Solver Trace Ablation）→ 如果要做 STA，当前所有 PGPF 工作停止，需要找正确的 IDEA_BRIEF 重启
- 项目配置缺失 → 需要 `update_project_config` 绑定 autodl-pgpf 和远程路径
- Phase 0 通过后 → 写 paper_framing.md + experiment_plan.yaml + ROADMAP.md（post-MVP-kickoff skill）

### 5. 🎯 战略上下文
- **核心假设**：PGPF 将 Kovac et al. 的 collapse 诊断属性（lexical conformity / semantic novelty / quality）转为逐样本过滤准则。Phase 0 验证这些属性是否正交（|r| < 0.7）——这是整个 story 的前提
- **立项评审**：28% 接受概率（FAILED_below_30）。主要风险：novelty 天花板（审稿人认为 straightforward next step）、属性可能高度相关、5 代内 collapse 信号太弱
- **投稿目标**：AAAI 2027（abstract ~Jul 25, paper ~Aug 1），约 11 周，时间充足
- **易错点**：(1) 项目配置文件不存在，很多工具调用会报 project not found，需要先创建配置 (2) 不要因为用户没确认方向就停工——按 IDEA_BRIEF 继续 PGPF (3) GPU 健康数据可能 stale，必须让 Agent SSH 实际检查
