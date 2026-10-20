# director / loop_6.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`65238ab21186a4cd6b80.json`](../../sessions/65/65238ab21186a4cd6b80.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-16T13:24:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-45299 的 cuda:0 / cuda:1（2×RTX PRO 6000）
- ManiSkill3 环境需要 resolve_physical_device() 而非 CUDA_VISIBLE_DEVICES stash（SAPIEN 要求移除 CVD）
- submit_training_job 注入 CVD 后逻辑设备变 cuda:0，019a 已踩过此坑（--device cuda:0 而非 cuda:1）
- NVE baseline 定义：exp_001 seed 1 的 v/e trajectory。论文中 NVE = ve_ratio / baseline_ve
- 008e_v3_s2 是 NVE false positive（非 CIVO，Pathway B）— 不要归为 CIVO 失败

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (connect.bjb1.seetacloud.com)，root 用户
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- Python：服务器上的 conda/venv（Agent 连接时自行检测）
- 论文源码：本地 projects/event-gated-adaptive-horizon/docs/paper/sections/*.tex
- 审稿群 (Group C)：review_chat_id = oc_dd4a07a509df7e5f9a31d65f776059bc
- 活跃进程：010b (cuda:0, PID 585826, ~1.5h), 019a (cuda:1, PID 586751, ~4h)

### 3. 📊 当前状态
刚完成 Dream 审稿分析 (D064)，确认 6 项结构性提分行动。已派：
- Agent：010b 完成后提交 D6 Pathway B 控制实验 (exp_020_vanilla_dreamerv3_s2)
- Paper Agent：related work 扩展 (20+ refs) + claim 语言审计（去 "necessary and sufficient"）
- 用户已收到完整提分计划

Registry RUNNING：
- exp_010b: Cheetah CIVO trigger (cuda:0, ~1.5h 后完成)
- exp_019a: PickCube baseline (cuda:1, ~4h 后完成)

QUEUED：
- exp_020 (D6 Pathway B 控制) → 010b 完成后 cuda:0
- exp_019b (PickCube CIVO trigger) → 019a 完成后 cuda:1

### 4. 📋 待办
- 010b 完成回调 → 分析 Cheetah CIVO（NVE>1.5x? collapse?）→ 确认 exp_020 已提交
- 019a 完成回调 → 分析 PickCube baseline → 提交 019b CIVO trigger
- exp_020 完成 → **关键判断**：vanilla s2 稳定 → C6 成立，Pathway B 需 trained dt_emb；vanilla s2 也崩溃 → Pathway B 是 inherent fragility，需大幅修改 C6
- Paper Agent 回报 related work patch → 审核引用真实性
- Bootstrap CIs 计算 → 派 Agent 从已有数据算（0 GPU）
- D064 行动项全部完成后 → re-dream 验证提分效果

### 5. 🎯 战略上下文
核心因果链：trained dt_emb → 93% obs decoder gradient → CIVO (NVE>1.5x) → collapse。018 Full-SGS 移除 93% gradient → NVE 1.00×，确认 gradient-level 现象 (D063)。

Dream 三档均 3/6 Weak Reject（但 dream 在 018 之前运行）。018 已解决 "no mitigation" 和 "gradient decomposition 未验证" 两个 weakness。

**最容易判断错的事：**
1. D6 Pathway B 控制 (exp_020) 是当前 paper story 最大风险 — Reviewer 标为最高优先级。如果 vanilla DreamerV3 seed=2 也在 ~95K 崩溃，C6 的 "multiple vulnerability pathways from trained dt_emb" claim 需要根本性修改
2. 不要因 dream 的 3/6 分降级 CoRL 目标 — 6 项行动项补完后预期显著提分
3. ManiSkill3 是用户 (吴俊豪 5/15) 明确要求的 — 不能因 reset 再丢（已存 memory）
4. 论文中 "representation-level" vs "gradient-level" 措辞仍可能有残留矛盾，018 后应全面检查


---
