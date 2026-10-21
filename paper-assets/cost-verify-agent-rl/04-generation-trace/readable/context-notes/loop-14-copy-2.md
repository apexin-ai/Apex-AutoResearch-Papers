# agent / loop_14.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`78c475b9dcb8821ba7fe.json`](../../sessions/78/78c475b9dcb8821ba7fe.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-16T12:22:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-17606 cuda:0, cuda:1（仅此两张，不可用其他设备）
- D052 已判定 MVP 失败（train success 21.88% 但 val success 始终 6.25%），项目方向待 Director 决策，不得自行启动新实验
- exp028c 之后的下一步需要 Director 明确指示（继续/换方向/关项目）
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/bin/activate && ...`（不要假设 .venv 存在）
- GPU 编号脚本内始终从 0 开始（框架注入 CUDA_VISIBLE_DEVICES 映射物理卡）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，双卡 RTX PRO 6000 Blackwell 98GB
- Python：/root/miniconda3/bin/python（conda base 环境）
- 项目代码：具体路径需 SSH 确认（可能 /root/autodl-tmp/ 或 /root/verl-agent/）
- SFT checkpoint：exp021 RAGEN-format SFT — 具体路径见 registry spec
- W&B project：cost-verify-agent-rl，run_id=4yu6qz1m (exp028c)
- 活跃进程：无（exp028c PID=824675 已死）
- Cron：reconcile 后 0 个活跃 cron

### 3. 📊 当前状态
刚收到 exp028c_selfguide_recipe 进程异常退出的 cron 回调（"Process exited without valid W&B metrics"）。

已完成：
- Registry 更新 notes + failure_reason
- 向 Director 汇报（含资源状态 + 关键观察：train 过拟合 vs val 未提升）
- 派出 Worker `worker_diagnose_exp028c_crash_20260516T082005` SSH 诊断崩溃原因

等待：
- Worker 回调（诊断结果：崩溃原因 + step 8-10 日志 + checkpoint 存活状态）
- Director 决策（D052 后项目方向：继续/换框架/换模型规模/关项目）

Registry 状态：无 RUNNING 实验。PREPARING 中大量历史残留（exp025c PENDING 等审批，其余为已废弃的 PREPARING）。

### 4. 📋 待办
- Worker `worker_diagnose_exp028c_crash_20260516T082005` 回调 → 补充 registry failure_reason 具体原因 + 确认 checkpoint 存活 → 更新 report.md → 补充汇报 Director
- Director 决策到达 → 按指示执行（可能选项：换更大模型 / 增加 train games 解决过拟合 / 关项目 / pivot 到新 idea）
- 如 Director 决定继续 → 核心问题是 train 16 games 过拟合，需扩大 train env 多样性或换泛化策略
- 如 checkpoint step_7 存活 → 有 21.88% train success 权重可用于后续分析

### 5. 🎯 战略上下文
- 核心结论链：SFT baseline 6.25% → exp027 GRPO train 13.28% (fail) → exp028c recipe 对齐后 train 21.88% (step 7) 但 val 始终 6.25%
- **根本矛盾**：模型在 16 个 train games 上学会了（train success 提升），但无法泛化到新 game（val 不动）。这不是训练稳定性问题，是泛化问题
- D052 判定 MVP 失败的核心依据：step_10_val=0%（灾难性崩溃），即使 train 曾达 21.88%
- cost-efficiency story（D039）前提是 baseline performance ≥50%，当前 val 仅 6.25%——performance gap 太大，cost-efficiency 无从谈起
- Self-Guide 论文 72.7% 是用更多 train games + 更强 SFT 起点达到的，16 games 明显不够
- 易错判断：不要把 train success 当作 MVP 通过的证据——只有 val success ≥20% 才算 pass
- ROADMAP 竞争格局显示 ARES (52.7% token↓) 是最近竞争者，但我们连 baseline performance 都没达到


---
