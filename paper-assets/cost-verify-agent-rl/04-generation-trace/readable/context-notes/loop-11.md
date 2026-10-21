# director / loop_11.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`592b0201e0654548b8ce.json`](../../sessions/59/592b0201e0654548b8ce.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-17T07:22:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-17606 的 2 张 GPU（项目配置 gpu_ids）。不可使用其他服务器的 GPU
- γ=0.95（非 0.99），discounting 按 window 数（N=⌈T/h⌉）不是按 step 数。公式：R_k = γ^(N-k) · R_episode。全项目已统一，禁止再出现 γ^48 或 γ=0.99
- GRPO 算法无 γ（bandit-style），只有 RAGEN 的 step_independent 实现引入 γ。论文措辞必须区分算法层 vs 实现层
- h-sweep config 用 `context_window_mode: step_independent` + `step_independent_history_length: {h}`（不存在 `sliding` mode）
- Registry 中 hsweep_h2_seed1 的 hypothesis 含旧数字（gamma^48≈8%），是 registry 残留，auto_build_report_facts 会带出来，不影响论文

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606 (connect.bjb1.seetacloud.com)，用户 root
- 工作目录：/root/cost-verify-agent-rl
- 训练框架：RAGEN（/root/cost-verify-agent-rl/RAGEN/）
- h-sweep 脚本：/root/cost-verify-agent-rl/scripts/launch_hsweep.sh + auto_next_hsweep.sh
- 活跃进程：hsweep_h2_seed1（PID 920380，双 GPU，tmux session 需确认）
- auto_next_hsweep.sh 设置了自动进阶：h=2s1→h=2s2(带 LOG_PER_SAMPLE_ADV=1)→h=2s3→h=5s1→...→h=full+bonus
- Advantage logging patch：agent_trainer.py:343-367，输出到 ~/runs/cost-verify-agent-rl/hsweep_h2_seed2/advantage_log.jsonl

### 3. 📊 当前状态
**刚完成**：
- 理论三轮修正收敛到 "Advantage Sign Misattribution"（D058），Reviewer 全确认
- method.tex Eq.(3) 公式错误修复（9 处，全项目统一 γ=0.95, N=25, γ^24≈0.29）
- Paper Agent 激活，writing_plan.yaml 已审批，正在写 Method + Theoretical Analysis

**RUNNING**：
- hsweep_h2_seed1（双 GPU，预计再 1-2h 完成 → 自动启动 seed 2 带 advantage logging）

**等待中**：
- Paper Agent 回传 Method/Theoretical Analysis 初稿（Step 2-4 进行中）
- h=2 seed 1 完成后 cron 回调
- h=2 seed 2 的 advantage_log.jsonl 数据（plan_004 empirical verification）

### 4. 📋 待办
- h=2 seed 1 完成回调 → 检查 success rate 是否 ≈0%（验证 catastrophic collapse），确认 auto_next_hsweep 自动启动了 seed 2
- h=2 seed 2 完成 → 分析 advantage_log.jsonl：验证 sign vs outcome correlation ~1.0, sign vs local quality ~0
- Paper Agent 回传初稿 → 审读 Method/Theoretical Analysis，检查与 paper_framing.md 一致性
- 全部 h-sweep 15 runs 完成 → 画 h-sweep cliff figure（核心 paper figure），启动 multi-seed（plan_003）
- plan_003b GAE baseline → 评估实现成本（需 critic head），决定 GAE vs REINFORCE baseline

### 5. 🎯 战略上下文
**决策链**：D054(dual contribution) → D055(Dream response) → D056(exp013f retrospective) → D057(early-stop exp029) → D058(sign misattribution theory)

**核心结论**：Mechanism 2 = Advantage Sign Misattribution。advantage 的符号由 episode 成败决定而非 local action quality。Episode-level 消除 sign misattribution 因为不再拆分 windows。γ^k decay 是 secondary magnitude issue。

**易错点**：
- 不要把 GRPO 算法的属性和 RAGEN step_independent 实现的属性混淆。"GRPO has no γ" 是对算法说的；step_independent 实现确实用 γ
- paper_framing.md 的 "episode-level 也是 episode-level credit（非 per-token）" 是诚实性注记 — 审稿人可能追问，防御是"方向正确 > 方向错误"
- Reviewer 评估：methodology-only paper 需要 plan_004(gradient data) + GAE baseline + Phase B(selective verification) 才够 top venue。不要只靠 h-sweep
- DR1-C2（novelty concern）最终靠 dual contribution 解决：methodology diagnosis + selective verification。Phase B 必须完成


---
