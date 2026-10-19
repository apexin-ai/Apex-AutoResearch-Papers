# agent / loop_1.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`91f57536cbad29864de2.json`](../../sessions/91/91f57536cbad29864de2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T23:47:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 bjb1-17606 的 cuda:0 + cuda:1（RTX PRO 6000 Blackwell 94GB×2）
- 模型/数据/HF cache 必须放数据盘 `/root/autodl-tmp/`，根分区只有 30GB
- **Qwen3-1.7B 没有独立 Instruct 版本**——Qwen3 系列不区分 base/instruct，`Qwen3-1.7B` 本身就是 conversational 模型。exp004/exp006 的 "切 Instruct" 方案无效，`models/Qwen3-1.7B-Instruct` 只是指向同一模型的软链接
- vLLM 0.18.1 与 RAGEN 兼容（声明要求 0.8.2 但实测无问题），不要降版本
- submit_training_job 的 command 必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606（AutoDL），工作目录 `/root/cost-verify-agent-rl/RAGEN/`
- Python：`/root/miniconda3/bin/python` (3.12.3, conda base)
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3-1.7B`（软链接 `/root/cost-verify-agent-rl/models/Qwen3-1.7B`）
- 数据：`/root/autodl-tmp/alfworld/`（ALFWORLD_DATA），3553 train / 140 eval games
- HF cache：`/root/autodl-tmp/.hf_cache`
- 关键软件：PyTorch 2.10.0+cu128, vLLM 0.18.1, verl 0.6.1, RAGEN 0.1
- 活跃进程：exp003 (PID 157852, tmux=exp003, cuda:0+1)，step 0 GRPO update 阶段
- Cron：reconcile 返回 0，无活跃 cron（exp003 通过 Worker 轮询监控）

### 3. 📊 当前状态
刚处理完 Director 的三条并行指令。关键进展：

- **exp003 (RUNNING)**：step 0 rollout 完成，GRPO update 阶段（GPU 100%），等待训练指标输出。baseline: invalid_action=95%, reward_mean=-4.75, success=0。**监控 Worker `monitor:exp003_step0_v2` 正在轮询**
- **exp005 (PREPARING)**：快速 base 配置已创建，Director 暂不审批（base bootstrap 未验证）
- **exp006 config Worker `code:exp006_config` 正在运行**：创建 Instruct+Fast 混合配置——但发现 Qwen3 无独立 Instruct 版，已向 Director 汇报此配置实际无意义
- **Qwen3-1.7B-Instruct 下载**：确认不存在，创建了软链接指向同一模型

等待中：
- Worker 回调：`monitor:exp003_step0_v2`（exp003 step 0 指标）、`code:exp006_config`
- Director 决策：Qwen3 无 Instruct 版后的新方案（我建议了 Qwen2.5-3B-Instruct / 简化 prompt / SFT warmup 三选项）

### 4. 📋 待办
- exp003 step 0 指标回调到达 → 立即汇报 Director pg_loss + invalid_action + advantage_std；非零梯度 → 继续跑；零梯度 → 需要 Director 决策新方案
- Director 回复 "Qwen3 无 Instruct" 后的方案选择 → 按指令准备新模型下载/配置
- invalid_action <80% at step 5 → exp003 有效，考虑 exp005 加速；>90% → 需要换模型或 SFT warmup
- exp006 config Worker 完成 → 告知 Director 此配置等同 exp003（同一模型），建议取消
- Phase B 代码已就绪（61 tests passed），Phase A checkpoint 产出后可直接启动

### 5. 🎯 战略上下文
- **核心目标**：训练 agent 学会"何时验证"（B-IAVR），Phase A 先复现 Self-Guide always-on baseline ≥76% success on ALFWorld
- **决策链**：D001(ALFWorld+Qwen3-1.7B MVP) → D002(全量微调非LoRA) → 发现 batch size 是 bootstrap 关键(16→128) → 发现 Qwen3 无 Instruct 版
- **最易判断错的事**：不要再尝试"切 Instruct 模型"来解决 bootstrap——Qwen3-1.7B 已经是 instruct/conversational，问题在配置不在模型类型。如果 exp003 的 128 traj/step 仍无法 bootstrap，真正需要的是换模型系列（如 Qwen2.5-3B-Instruct）或加 SFT warmup
- **ROADMAP 时间预估已过时**：原估 Phase A 2.7h 基于 dry-run 的 36.5 step/h，实际 128 traj/step 慢得多（step 0 已跑 1.5h+）。Director 已意识到并要求加速方案
- **Phase B 代码完整**：biavr reward + verify mechanism + lagrangian + 61 tests，集成在 RAGEN 分支，等 Phase A checkpoint


---
