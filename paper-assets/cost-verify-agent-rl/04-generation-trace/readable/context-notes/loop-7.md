# director / loop_7.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`b7404094c14849b1e81a.json`](../../sessions/b7/b7404094c14849b1e81a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T13:54:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 bjb1-17606:cuda:0 和 bjb1-17606:cuda:1（2× RTX PRO 6000 Blackwell 98GB）
- exp026 训练进程 PID=781795（Ray TaskRunner）正在双卡运行，**不要 kill**
- Registry 中 exp026 曾被 cron 误标 DONE(failed)，已修复为 RUNNING（D029/D033）。如果再次被误标，先检查进程再处理
- standalone eval 脚本 eval_checkpoint.py 有 CRITICAL 缺陷（SYSTEM_PROMPT 与训练不一致），**修复前禁止运行**（已发紧急指令给 Agent）
- 后续实验禁止 WANDB_MODE=disabled（这是 cron 误判的根因）
- 两级阈值（D034）：MVP=20% val，论文 baseline 最低=50% val。MVP 通过不等于论文可行

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606 (connect.bjb1.seetacloud.com)，用户 root
- 代码路径：/root/cost-verify-agent-rl
- SFT checkpoint：/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/
- exp026 训练日志：Ray worker logs（/root/autodl-tmp/tmp/ray/session_2026-05-15_18-38-45_487055_778562/logs/worker-*.out），不在 tee 主日志中
- checkpoint save_freq=25，首个 checkpoint 约 step 25（~17h after start）
- W&B：exp026 未启用（WANDB_MODE=disabled），指标只能从 Ray worker logs 提取
- 磁盘：/root/autodl-tmp/ 114GB 可用（55%）
- 活跃进程：exp026 PID=781795（Ray TaskRunner），cuda:0+cuda:1

### 3. 📊 当前状态
**刚做完**：
- Reviewer 交叉验证 exp026 train metrics（8/8 精确匹配，PASS）
- Reviewer story 强度评估（Self-Guide baseline 72.7%，我们 32.81% 是极早期）
- Reviewer 审查 standalone eval 脚本（CRITICAL：prompt 不一致）
- D034 两级阈值决策记录
- 用户预期校准（从"突破性"调整为"方向正确，极早期"）
- B-IAVR 核心代码 68/68 测试通过，4 模块完整
- 文献调研 25+ 篇，novelty claim 成立

**Registry**：exp026_step_independent_grpo RUNNING（实际 step 2 已完成，step 3+ 进行中）

**等待中**：
- Step 5 val eval（~14:30 UTC，首个真实 val 信号）
- Agent 处理 eval 脚本修复紧急指令
- Agent 处理 step progress check worker 结果

### 4. 📋 待办
- Step 5 val ≥ 12.5% 且上升趋势 → 训练健康，继续等待；val ≥ 20% → complete_mvp() 进入 research 阶段
- Step 5 val = 0% 或 entropy 骤降 → 检查训练是否崩溃，考虑从 checkpoint 重启
- eval 脚本修复完成 → 提交 Reviewer 复审确认（3 项：SYSTEM_PROMPT 替换为 envs.yaml 原文、max_steps=50、temperature=0.4）
- Step 25 checkpoint 出现（~17h）→ 用修复后的 standalone eval 独立验证
- Val 收敛到 50%+ → 启动 post-mvp-kickoff（paper_framing.md → experiment_plan.yaml → dream_simulate）
- Val 收敛到 60-70% → B-IAVR Phase B 集成（`a_pre` rollout 接入，Lagrangian 对偶上线）

### 5. 🎯 战略上下文
**核心决策链**：D025（sparse GRPO 终止）→ D026（RAGEN GRPO 3/3 失败）→ D028（verl-agent cgroup 限制放弃）→ D029/D033（registry 误判修复）→ D032（train 32.81% 确认突破）→ D034（两级阈值）

**最容易判断错的事**：
1. 32.81% train success 看着很好但只是 step 2/150。Self-Guide 同模型 GRPO baseline 72.7%。不要过早宣布胜利
2. Step-independent rollout 是 verl-agent cherry-pick，**不是本项目贡献**。论文贡献必须来自 B-IAVR
3. exp026 的 Ray worker logs 路径与 tee 主日志不同——Reviewer 和 Agent 都踩过这个坑，查指标要去 Ray session logs
4. cron 监控依赖 W&B sentinel，exp026 因 disabled 而被误杀过一次。已修复但要警惕复发
5. 用户已被校准预期（从"突破"到"方向正确但极早期"），后续通报保持一致口径


---
