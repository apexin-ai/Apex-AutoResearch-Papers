# agent / loop_11.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`5eaf831f7a50349f9dba.json`](../../sessions/5e/5eaf831f7a50349f9dba.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-15T20:23:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 cuda:0, cuda:1**（bjb1-17606）。不得使用其他 GPU，即使 Director 指令也必须 push back
- exp027 是 MVP 关卡实验，**不得中断/kill**（PID 789790）。判定阈值（D037）：<20% fail / 20-25% weak / 30%+ strong pass
- 论文 framing 已锁定（D039）：**cost-efficiency story**，不走 performance story。任何 paper 写作必须遵守此方向
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，服务器无 .venv
- exp027 早停条件（D041）：step 10 train success ≤12% → 终止

### 2. 🖥️ 基础设施快照
- 服务器：**bjb1-17606**，账户 root，工作目录 `/root/cost-verify-agent-rl`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- SFT checkpoint：`/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`
- 模型：Qwen3-1.7B
- 框架：RAGEN + verl-agent GRPO + step-independent rollout
- W&B run ID：`y7jiibqk`（exp027）
- 活跃进程：exp027_stable_grpo PID=789790, tmux=exp027_stable_grpo, cuda:0+cuda:1
- Cron：exp027_stable_grpo（活跃，reconcile 确认 PID 存活）
- 累计 GPU-h：~40h，exp027 预估 ~84h（2卡×42h）

### 3. 📊 当前状态
**exp027_stable_grpo** 正在训练（~5h+），50 steps，save_freq=5，test_freq=5。Step 3 已出结果：success 连续两步 10.16% 稳定，KL 从 step 2 黄区(0.413)降至 step 3 绿区(0.248↓40%)。D041 诊断瓶颈为 sparse reward 学习信号不足，非 KL 不稳定。

**运行中 Worker**：
- `worker_monitor_exp027_step3_extract` — 提取 exp027 step 3 详细指标
- `worker_research_recipe_gap_analysis` — D043 Reviewer 发现的 recipe gap 分析（参考论文 GRPO baseline 72% vs 我们当前远低于此）

**Registry 统计**：51 实验，success 3 / negative 4 / failed 17 / killed 9 / 其余 PREPARING 或已废弃

**等待中**：
- exp027 cron 回调（进程完成或 step 10 出结果时触发）
- 两个 running Worker 的完成回调
- exp025c 仍 PENDING 等审批（低优先级）

### 4. 📋 待办（条件触发式）
- exp027 step 5 val 出结果（~4-5h 内）→ spawn Worker 提取 val metrics → 对照 D037 三层阈值初步判定
- exp027 step 10 train success ≤12% → 按 D041 早停，汇报 Director fail
- exp027 step 10 train success >12% → 继续跑，汇报 Director 进展
- exp027 最终完成 success ≥20% → complete_mvp() → 启动 Phase B (B-IAVR selective verification)，向 Director 申请额外 GPU（预估 600+ GPU-h）
- exp027 最终 <20% → 按 D037 fail，汇报 Director，24h deadline 后决策（申请新服务器 / 重评项目）
- worker_research_recipe_gap_analysis 完成 → 整合 recipe gap 发现到 memory.md，评估是否需要调整训练 recipe
- worker_monitor_exp027_step3_extract 完成 → 更新 registry metrics

### 5. 🎯 战略上下文
**项目核心问题**：能否用 GRPO 训练 Qwen3-1.7B 在 ALFWorld 达到 ≥20% success rate（MVP 门槛）。27 次实验迭代，反复遭遇 GRPO 死亡螺旋（sparse reward → 全零 batch → 梯度消失）。exp027 是目前配置最充分的一次尝试（128 rollouts + entropy bonus + 低 KL + 低 LR）。

**决策链关键节点**：
- D039：framing 锁定 cost-efficiency，不比 performance（ALFWorld SOTA 88-93%，Self-Guide 72.7%，performance 无优势）
- D043：Reviewer 发现 recipe gap——参考论文 GRPO baseline 72%，我们连 20% 都没到，可能是训练 recipe 本身有问题而非方法问题
- D037：MVP 三层阈值，exp027 是 go/no-go 决策点

**易踩的坑**：
- 不要把 exp027 当前 10.16% train success 和 SFT baseline 6.25% val success 直接对比——一个是 train，一个是 val，eval protocol 不同（C003 compliant 16-episode vs 训练时 env_groups）
- recipe gap 可能是根本问题（D043）：如果 RAGEN 框架本身在 ALFWorld 上的 GRPO baseline 远低于原论文，那不是我们的 reward/KL 调参能解决的
- Adaptive KL（memory.md 记录）是 Plan B 备选，零代码修改纯 YAML 切换，但前提是 exp027 先给出结论
- 大量 PREPARING 状态的老实验（exp014a/b/c, exp018, exp019b_v2 等）已被后续实验 supersede，不要重启它们


---
