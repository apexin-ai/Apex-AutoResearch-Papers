# director / loop_27.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_27.md`
- **Structured JSON:** [`f44cfdfa74d68b5136dd.json`](../../sessions/f4/f44cfdfa74d68b5136dd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 27
reason: max_messages
updated: '2026-05-28T21:15:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- 用户已下达全面停机指令（05-28），所有实验已 kill/cancel，未收到恢复指令前不要启动任何实验
- 论文提交状态未确认——用户未回复是否已提交 CoRL，不要假设已提交或未提交
- DDL 存在歧义：ROADMAP 写 2026-05-28 20:00 BJ，审稿报告写 May 29 AoE，用户未澄清
- 3 台服务器（bjb1-32546、bjb2-28827、cqa1-32758）已不可达，可能到期，不要尝试连接

### 2. 🖥️ 基础设施快照
- 仅 bjb1-18228 (connect.bjb1.seetacloud.com) 可能仍存活，4 GPU，上次报告利用率 23%
- 其余 3 台服务器全部连接失败（bjb1-32546、bjb2-28827、cqa1-32758）
- 工作目录：/root/acr-vla-conformal-refinement
- 活跃进程：无（0 RUNNING、0 cron、0 Worker）
- 论文源码在本地 workspace：projects/acr-vla-conformal-refinement/artifacts/ 下

### 3. 📊 当前状态
- 格式修复已完成：Figure 1 trim 11pt + textfloatsep 10pt、Table 3 改 [t]、AI 使用声明移到附录
- 编译通过 17 页 0 error
- Round 7 内部审稿：5/10 Borderline Reject，6 个 Critical Must-Fix（conformal 术语误导、selective prediction 文献遗漏、净收益微弱、K=2 argmin degenerate、π₀.5 单种子、CRM 设计空间未探索）
- 用户最后消息（05-28 18:18 BJ）是格式修复请求，之后 4+ 天未回复
- 已向用户发送 DDL 澄清 + 提交状态确认，无回复

### 4. 📋 待办
- 用户回复已提交 → 询问是否推进 camera-ready 修订（Round 7 的 Must-Fix 可部分处理）或关项目
- 用户回复未提交 + DDL 是 May 29 AoE → 立即推进：去 conformal 命名、补 selective prediction 文献、去 \enlargethispage hack、重新编译提交
- 用户回复未提交 + DDL 已过 → 讨论是否改投其他 venue 或等下一轮 DDL
- 用户长期不回复 → 保持待机，不主动操作

### 5. 🎯 战略上下文
- 论文核心 story：无条件 CRM 在 4/4 suites 有害，τ-gating 恢复退化但 vs VLA-only 净提升微弱
- D184 锁定 title "Knowing When Not to Correct: Adaptive..."
- Round 7 最致命问题：τ-gated ≈ VLA-only（N3），审稿建议重新定位为 empirical study 而非 method paper
- 易错点：不要自行决定是否提交论文，这是用户的决定；不要因为 DDL 紧急就跳过用户确认
- 22 GPU 名义分配但实际 3 台服务器已失联，恢复实验前必须先确认服务器状态


---
