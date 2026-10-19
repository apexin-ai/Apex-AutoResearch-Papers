# reviewer / loop_13.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`c088dff9c93381047ba0.json`](../../sessions/c0/c088dff9c93381047ba0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-17T18:00:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 (C006)：bjb1-17606 仅 cuda:0,1；westd-47453 cuda:0,1,2,3。越界 → critical
- hsweep_h2_seed2 (bjb1 PID 945877) 启动时加载了旧 config（val env_groups=16），其 val 结果与 seed1 (32 tasks) 不完全可比——审 seed2 val 时需注明
- 所有运行中实验（seed2, gsweep, gae_baseline）使用的是旧版 agent_trainer.py（无 window_action_valid 字段），advantage_log 中没有 action validity 信息
- invalid_action_penalty_coef=0.1 是代码默认值，hsweep/gsweep 都在用——论文 Proposition 2 的纯二值假设 (R∈{0,r+}) 与此不一致，审查 claim 时注意

### 2. 🖥️ 基础设施快照
- bjb1-17606 (root): /root/cost-verify-agent-rl, cuda:0,1 → hsweep_h2_seed2 (PID 945877, wandb jhwyg4tc)
- westd-47453 (root): /root/cost-verify-agent-rl, cuda:0,1 → gae_baseline_seed1 (PID 40267, wandb dt79qyd9, 实际是 REINFORCE++); cuda:2,3 → gsweep via watchdog (PID 259808, 当前 g050 PID 85798)
- gsweep watchdog 自动链式执行 g050→g080→g095→g100，日志 /root/runs/cost-verify-agent-rl/gsweep_watchdog.log
- advantage_log: /root/runs/cost-verify-agent-rl/hsweep_h2_seed2/advantage_log.jsonl (800 条, 4 steps)
- 本地 workspace: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/

### 3. 📊 当前状态
刚完成 4 个 worker 审查并全部 posted to Director：
- worker_fix_hsweep-val-size-and-h10-config → PASS
- worker_fix_gsweep-watchdog-restart → PASS (warning: ADV_LOG 仅 g100 生效)
- worker_research_r640-diagnosis → WARNING（两个 worker 矛盾结论，我独立核实后发现 32 条 step_return=0.0 + positive advantage 记录是 sign misattribution 直接证据）
- worker_research_plan018-code-assessment → PASS（~20 行改动，compute_episode_returns 已存在）
- worker_research_plan019-eval-134-tasks → PASS (warning: 134 tasks = valid_unseen/OOD，当前实验用 valid_seen/ID，切换改变评估语义)

RUNNING: gsweep_g050_h5_seed1 (westd cuda:2,3), gae_baseline_seed1 (westd cuda:0,1), hsweep_h2_seed2 (bjb1 cuda:0,1)

等待 Director 决策：plan_019 eval split 选择 (valid_seen 140 vs valid_unseen 134)

### 4. 📋 待办
- hsweep_h2_seed2 完成 → 审查 collapse 是否复现 seed1 pattern (step 3-4 onset)；advantage_log 数据量增加后重新评估 sign misattribution 统计
- gsweep_g050 完成 → 审查 γ=0.5 是否加速 collapse；watchdog 自动启动 g080 → 确认 PID 和 GPU 合规
- gae_baseline 到 step 5+ → 审查 REINFORCE++ vs episode-level GRPO 对比
- plan_018 代码实现完成 → 重点审查：compute_episode_returns 是否正确 broadcast 到所有 windows、advantage_mode config 是否向后兼容
- γ=1.0 (gsweep_g100) 结果出来 → 这是 magnitude decay vs sign misattribution 的判别器：若仍 collapse 则 sign misattribution 为主因
- 任何 paper 章节审查请求 → 先检查 Agent 是否看过 red-section skill（L1 合规）

### 5. 🎯 战略上下文
**核心 story**: 诊断 step-independent RL 的灾难性崩溃双机制 (information loss + sign misattribution)，episode-level GRPO 作为 minimum fix。D062 放弃 "contrarian" framing，改为 "mechanistic diagnosis + factorial causal attribution"。

**最容易判断错的事**:
1. r=0.640 的解读——Worker 1 说"纯 artifact"，Worker 2 说"sign misattribution 不成立"。**两个都不完全对**。真实情况：advantage 确实是 step_return 的 z-score（数学同源），但 step_return=0.0 的失败 episode windows 获得正 advantage 是 sign misattribution 的直接证据。penalty 创造的 local variation 只区分 format quality 不区分 task quality。
2. plan_003b 描述写 GAE 但实际运行 REINFORCE++（D060 fallback），plan 文本未更新。
3. paper_provenance.yaml 中 C011/C017 仍写 p=6.25%/84.5%，论文实际用 p=12.5%/80.9%——mismatch 待修正。
4. Selective verification (Claims 2/3) 已降级为 future work (D061)，不再是核心贡献。
5. plan_018 (factorial 2×2) 是 Dream 三档一致要求的 #1 缺失实验——结果可能改变 dual mechanism 的权重分配，应最高优先级跟踪。


---
