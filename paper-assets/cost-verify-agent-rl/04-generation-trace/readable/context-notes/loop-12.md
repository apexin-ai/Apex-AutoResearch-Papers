# director / loop_12.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`318c150ef377f63631f2.json`](../../sessions/31/318c150ef377f63631f2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-17T18:00:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 (C006): bjb1-17606 cuda:0,1 | westd-47453 cuda:0-3。不可使用其他卡
- westd-47453 所有实验必须 `export TORCH_COMPILE_DISABLE=1`（RTX PRO 6000 inductor 冲突）
- 不再使用 "contrarian/coarser is better" framing（D062 禁用，GAGPO 93.5% 已反驳）
- eval split 统一 valid_unseen(134 tasks)（D064），不再用 valid_seen(32)
- Worker 不可覆写 memory.md（C004）

### 2. 🖥️ 基础设施快照
- **bjb1-17606**: connect.bjb1.seetacloud.com, /root/cost-verify-agent-rl, 2× A6000
- **westd-47453**: connect.westd.seetacloud.com, /root/cost-verify-agent-rl, 4× RTX PRO 6000
- 模型: Qwen3-1.7B (HF cache on both servers)
- γ-sweep watchdog: PID 259808 on westd (tmux), chains g050→g080→g095→g100
- hsweep_h2_seed2: PID 945877 on bjb1, auto_next → h10s1 → h5s1 → h20s1 → fulls1
- gae_baseline_seed1 (actually REINFORCE++): westd cuda:0,1, wandb run dt79qyd9
- gsweep_g050_h5_seed1: westd cuda:2,3, ~43min/step

### 3. 📊 当前状态
刚完成：Dream review 分析 (D062) + r=0.640 诊断解决 (D063) + eval split 决策 (D064) + plan_018/019 加入计划 + framing 调整。

Agent 队列 depth=4，正在处理 D063 通知，后续队列含：plan_018+019 Worker 派单、Worker-done 回调、D064 eval 决策、plan_018 实现指令。

RUNNING: gsweep_g050_h5_seed1, gae_baseline_seed1 (REINFORCE++), hsweep_h2_seed2
等待: Agent 处理完队列后实现 plan_018 代码 (~20-25行改动) + 创建 config

### 4. 📋 待办
- Agent 队列清空后 → 确认 plan_018 代码已实现 + config 已创建 + dry-run 通过
- hsweep_h2_seed2 完成（~8h后）→ bjb1 释放 → 立即启动 plan_018 (factorial_h2_episodeadv_seed1)
- γ-sweep g050 完成 → watchdog 自动启动 g080（无需干预）
- γ=1.0 结果出来 → 如果仍 collapse = magnitude decay 不是主因（但不能判定 info loss vs sign misattribution）
- plan_018 结果出来 → 如果 collapse = information loss dominant；如果 succeed = sign misattribution dominant
- exp029 需要在 valid_unseen(134) 上 re-eval 一次做校准（P1，GPU 间隙做）

### 5. 🎯 战略上下文
- 核心 claim: step-independent GRPO 失败于 dual mechanism (info loss + sign misattribution)
- **plan_018 是整个项目当前最关键的实验** — Dream 三档一致标记的 #1 缺失
- sign misattribution 已确认存在（Type C evidence: 32/800 clean-failure windows 获正 advantage），但 Proposition 2 的 binary 假设需修正为包含 penalty 影响的版本
- framing 已从 "contrarian" 转为 "mechanistic diagnosis + factorial causal attribution"
- 易错点：γ=1.0 只排除 magnitude decay，不能判定 info loss vs sign misattribution —— 只有 plan_018 (factorial) 能分离这两者
- Agent 之前错误判断 "sign misattribution 不成立"（Worker 2），已纠正（D063）
- 审稿阶段已启动（Group C），但 research 实验继续推进


---
