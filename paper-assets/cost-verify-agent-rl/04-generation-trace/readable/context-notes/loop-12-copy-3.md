# reviewer / loop_12.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`ef6ae0588c8fc08f53c4.json`](../../sessions/ef/ef6ae0588c8fc08f53c4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-17T07:22:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（bjb1-17606 只分配这两张卡），越界即 critical
- hsweep-h2-seed1 正在跑，**不能 kill 或干扰其进程**，它是 paper core figure 数据源
- `agent_trainer.py` 已被 advantage logging patch 修改（line 343-367），h=2 seed 2 会自动启用 `LOG_PER_SAMPLE_ADV=1`，不要删除这段代码
- method.tex Eq.(3) 刚修正过（γ per-window not per-step），γ=0.95 不是 0.99，exponent=N-k 不是 T-kh，所有权威文件已统一，不要回退

### 2. 🖥️ 基础设施快照
- 服务器：`bjb1-17606(root)`，代码根目录 `/root/cost-verify-agent-rl`
- RAGEN 代码：`/root/cost-verify-agent-rl/RAGEN/`
- W&B logs：`/root/autodl-tmp/wandb/wandb/`
- hsweep-h2-seed1 W&B run：`run-20260517_121901-7o9bjszm`
- h-sweep 自动化脚本：`/root/cost-verify-agent-rl/scripts/auto_next_hsweep.sh`（完成后自动 launch 下一个配置）
- h-sweep 序列：`2:1 2:2 2:3 5:1 5:2 5:3 10:1 10:2 10:3 20:1 20:2 20:3 full:2 full:3`（exp029 = full:1 已完成）
- hsweep configs：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_hsweep_h*.yaml`，gamma=0.95
- 活跃进程：hsweep-h2-seed1（tmux session 名待确认，~52 min/step，双卡 97-100% util）

### 3. 📊 当前状态
**刚完成**：
- 审查 method.tex 初稿，发现并报告 Eq.(3) 公式 critical 错误（γ 指数 per-window vs per-step + γ 值），Worker 已修复
- 验证 D058 theory correction（Sign Misattribution 替代 Flat Advantage），已 post info 确认三维度兼容
- 验证 advantage logging patch 代码正确性

**实验状态**：
- hsweep-h2-seed1：step 2 完成，step 3 进行中（预计 ~14:44 UTC 完成）。**明确 collapse 趋势**：train success 18.75%→14.84%，KL 0.059→0.192（3x），grad_norm 12.38
- exp029：已 KILLED at step 15（val=28.125%，pass@8=92.9%），checkpoint 保留

**等待中**：无 pending worker 或 director 决策

### 4. 📋 待办
- hsweep-h2-seed1 step 3 完成 → 确认 train success 是否继续下降（预期 <12%）
- hsweep-h2-seed1 step 5 完成（含 val eval）→ 确认 val success ≈ 0%，正式确认 h=2 collapse
- h=2 seed 1 全 15 步完成 → auto_next_hsweep.sh 自动 launch h=2 seed 2（含 advantage logging）→ 验证 advantage_log.jsonl 开始产出
- h=2 seed 2 产出 advantage_log.jsonl → 审查 per-window advantage 数据，验证 sign misattribution claim（成功 episode 所有 window positive，失败 episode 所有 window negative）
- h=5 开始后 → 对比 h=2 vs h=5 collapse 速度，开始构建 h-value degradation curve
- paper_framing.md 修正完成后 → 审查 "γ^24≈29%" 是否已全局统一（特别注意 dream_reports/ 和旧 artifacts 可能有残留旧值，但这些是历史记录不改）

### 5. 🎯 战略上下文
**核心决策链**：D054（dual contribution framing）→ D055（Dream Review 修正）→ D057（early-stop exp029 for h-sweep）→ D058（theory correction: flat advantage → sign misattribution）

**论文 story**：step-independent 训练灾难性崩溃（dual mechanism: policy info loss + advantage sign misattribution）→ episode-level 解决 → selective verification（Phase B，未开始）

**最容易判断错的事**：
1. **γ-discount 层级**：γ 在 RAGEN step_independent 实现层（per-window return），NOT 在 GRPO 算法层。论文绝不能写 "GRPO uses γ"，只能写 "RAGEN's step_independent implementation introduces γ"
2. **val 指标可比性**：`val-env/AlfworldSG/success` 跨模式可比（always per-episode），`val-core/unknown/reward/mean@N` 不可比（per-window 粒度不同）
3. **hsweep collapse 预期**：h=2 预期 collapse 到 0%（已在进行），h=5 预期衰退但不完全 collapse，h=20/full 预期学习。这是 paper core figure 的 cliff pattern
4. **action_is_effective 是 hardcoded True**（env.py:224），metrics 中的下降来自 manager_invalid_action，不是代码 bug


---
