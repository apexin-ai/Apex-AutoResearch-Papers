# reviewer / loop_14.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`d2794c2642322cede638.json`](../../sessions/d2/d2794c2642322cede638.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-18T00:09:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-17606 GPU 白名单：cuda:0,1。westd-47453 GPU 白名单：cuda:0,1,2,3
- westd-47453 必须设 `TORCH_COMPILE_DISABLE=1`（RTX PRO 6000 inductor 冲突）
- westd-47453 根文件系统只 30GB，训练必须设 `TMPDIR=/root/autodl-tmp/tmp`（fast_downward 会往 /tmp 写 libdownward.so）
- factorial 实验 val 用的是 AlfworldOOD（无 SG 提示），但训练用 AlfworldSG。val 数据与 exp029 不可直接对比，必须用 AlfworldSG_OOD reeval config 做公平对比
- W&B entity=cvte, project=cost-verify-agent-rl，但 fetch_wandb_metrics 经常找不到 run（run ID 可能在 W&B 侧有延迟或命名不一致），需要靠日志 grep 做主要核实

### 2. 🖥️ 基础设施快照
- **bjb1-17606**: 代码 `/root/cost-verify-agent-rl/RAGEN/`，conda base，Python `/root/miniconda3/bin/python`
  - 日志目录：`/root/runs/cost-verify-agent-rl/`
  - Checkpoint：`/root/autodl-tmp/checkpoints/`
  - hsweep_h2_seed2 日志：`hsweep-h2-seed2.log`（注意文件名是连字符不是下划线）
  - advantage_log.jsonl：`/root/runs/cost-verify-agent-rl/hsweep_h2_seed2/advantage_log.jsonl`（约 1400+ 条）
  - analyze_advantage_log_v2.py：`/root/cost-verify-agent-rl/scripts/analyze_advantage_log_v2.py`
- **westd-47453**: 代码 `/root/cost-verify-agent-rl/RAGEN/`，conda base
  - 日志目录：`/root/runs/cost-verify-agent-rl/`
  - autodl-tmp 数据盘 250GB（清理后约 60% 空闲）
  - gsweep watchdog：`/root/runs/cost-verify-agent-rl/gsweep_watchdog.log`
- **活跃进程**：
  - factorial_h2_episodeadv_seed1: PID 482241, westd cuda:0,1, W&B run 6liw7fm1（待确认）
  - gsweep_g050_h5_seed1: PID 92354(TaskRunner)/92996(WorkerDict), westd cuda:2,3
  - hsweep_h2_seed2: PID 949105(TaskRunner)/949292,949293(WorkerDict), bjb1 cuda:0,1, W&B run jhwyg4tc

### 3. 📊 当前状态
刚完成三个 RUNNING 实验的全面状态检查，尚未 post 审查报告给 Director。核实结果：

- **factorial_h2_episodeadv_seed1**（step 4/15，westd cuda:0,1）：registry 标记 HEALTHY。Step 1 train success 20.3%，step 2 骤降至 6.25%。grad_norm=14.73、kl_loss=0.208（step 2）偏高。Val step 0 在 AlfworldOOD 只有 2.24%——印证了 tag mismatch 问题。当前正在 step 3+ 的 rollout 中。
- **gsweep_g050_h5_seed1**（step 10+/15，westd cuda:2,3）：已从 step 4 开始完全 collapse，success=0%、entropy=0.034、action_is_valid=1.7%。假设确认（γ=0.5 加速 collapse）。剩余 ~5 步纯粹跑完收集完整曲线。
- **hsweep_h2_seed2**（step 11+/15，bjb1 cuda:0,1）：Step 10 val success=0%，train success=3.9%（pass@8=12.5%），entropy=0.426，kl_loss=0.658。Val 始终 0%，确认 h=2 collapse 跨 seed 稳健。advantage_log.jsonl 持续积累。

GPU 合规：全部在白名单内 ✓

### 4. 📋 待办（条件触发式）
- **立即**：post 审查报告给 Director，covering factorial 训练不稳信号 + AlfworldOOD tag mismatch reconfirm + gsweep 假设确认 + hsweep 稳健性确认
- hsweep_h2_seed2 完成 → 核实 advantage_log.jsonl 完整性 → 确认 plan_004 分析脚本可执行 → 审查分析结果
- gsweep_g050_h5_seed1 完成 → 核实最终 metrics → 检查 watchdog 是否自动启动 g080 → 审查 g080 配置
- factorial_h2_episodeadv_seed1 完成 → 这是最关键实验。核实 episode-level advantage 是否阻止了 collapse → 如果 success >> 0% 则确认 sign misattribution 是 primary driver → 检查 reeval config 的 PLACEHOLDER checkpoint path 是否已填入
- factorial val 数据出来后 → 必须强调 AlfworldOOD val 数字不可直接与 exp029 AlfworldSG_OOD 数字比较，需要 reeval
- 任何新训练实验启动 → 核查 GPU 设备号 + TORCH_COMPILE_DISABLE + TMPDIR

### 5. 🎯 战略上下文
- **核心论文 story**：step-independent GRPO 在 multi-turn agent RL 中导致 catastrophic collapse，原因是 sign misattribution（不是单纯信息丢失）。Episode-level advantage 修复了这个问题。
- **factorial 实验是论文的关键证据**：如果 step_independent generation + episode_level advantage 成功（success >> 0%），则证明 collapse 的 primary driver 是 advantage 计算中的 sign misattribution，而非 context truncation 导致的信息丢失。如果仍然 collapse，则 information loss 本身就足够导致 collapse。
- **当前最大风险**：factorial step 1→2 train success 从 20.3% 骤降至 6.25%，配合 grad_norm=14.73 和 kl_loss=0.208，有训练不稳迹象。如果 factorial 最终 collapse，论文 story 需要调整——不能简单归因于 sign misattribution。
- **易错点**：
  1. 不要把 factorial 的 AlfworldOOD val 数字与 exp029 的 AlfworldSG_OOD 数字直接比较——prompt 不同，不公平
  2. hsweep_h2_seed2 的日志文件名是 `hsweep-h2-seed2.log`（连字符），registry 里写的 `hsweep_h2_s2.log` 是错的
  3. W&B fetch 经常失败，主要靠 grep 日志核实数据
  4. gsweep 已经 collapse 但还在跑——这是正常的（收集完整曲线），不是 Agent 忘记 kill
  5. 不要用"人类时间直觉"判断实验进度——AI 团队速度远超人类，只看 GPU-hours 预算


---
