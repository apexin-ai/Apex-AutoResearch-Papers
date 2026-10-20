# director / loop_2.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`d883e487b34d482f452b.json`](../../sessions/d8/d883e487b34d482f452b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-13T21:52:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 bjb1-45299 的 cuda:0 和 cuda:1，不可使用其他 GPU
- exp_005_event_gated_v4 的 return 已崩至 47.4，无诊断价值，应 kill 释放 cuda:1
- Pivot 决策树已更新（D010）：exp_006 正常分支下，**K=2 binary hard gate 优先于 soft weighted gate**——不要让 Agent 直接跳到 soft gate 方案
- 文献调研中 THICK 论文作者有 AI 幻觉：正确作者是 Gumbsch, Sajid, **Martius, Butz**（不是 Mill, Allen, Schwöbel）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (connect.bjb1.seetacloud.com:45299)，root 用户
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- AutoDL 实例，需 `source /etc/network_turbo` 后才能正常访问外网
- W&B 未配置，Git 未配置
- 活跃进程：exp_005 PID 51721 cuda:1（应 kill）；exp_006 cuda:0 状态 ALLOCATED（Agent 正在启动中）

### 3. 📊 当前状态
- 刚处理完 Reviewer 对 pivot-gate-mechanisms 文献调研的审查报告，记录了 D010 决策
- Agent 正在处理两件事：(1) 启动 exp_006_fixed_dt2 on cuda:0 (2) 检查 exp_005 状态
- Agent 队列深度 1，有一条综合指令待处理（registry 清理 + exp_001 状态更正 + exp_005 kill）
- Registry 问题待修：exp_001 实际已完成 505K 步但 registry 标记 failed；exp_005 metrics 数据与 metrics.jsonl 不一致（registry 记 319.3 实际 212.3）
- MVP 阶段，核心假设：event-gated adaptive horizon 能提升 world model 的 imagination 质量

### 4. 📋 待办
- Agent 回复 exp_006 已启动 → 确认 GPU 利用率，确保 exp_005 已 kill、cuda:1 释放
- exp_006 训练完成（fixed dt=2 diagnostic）→ 检查 eval_return：
  - return 正常（接近 baseline ~970）→ 问题在 gate 机制，派 Agent 实现 K=2 binary hard gate（dt∈{1,2}，改 gate_max_dt=2）
  - return 也崩 → variable-rate 本身在此 setting 下有害，需重新评估整个方向
- exp_006 正常 + K=2 实验完成 → K=2 成功则增量扩 K=3,4；K=2 也失败则考虑 soft gate（但必须先做 FPS benchmark）
- Registry 清理完成 → auto_build_report_facts 刷新 report.md

### 5. 🎯 战略上下文
- 项目核心假设：在 RSSM world model 中引入 event-gated adaptive time horizon，让 imagination 在无事件时段跳步
- 实验历程：exp_001 baseline 正常（~970 return）→ exp_002/003/004 三次 event-gated 实现全部 return 崩溃 → exp_005 v4 也崩（47.4）→ 当前在做 exp_006 诊断（fixed dt=2 去掉 gate，只保留 variable step）
- 关键决策链：D001-D009 记录了从初始实现到逐步简化排查的过程；D010 是最新的 pivot 策略调整
- **最容易判断错的事**：看到 exp_006 正常后直接跳到 soft weighted gate（A1）——Reviewer 已证明 A1 有 8 倍计算开销，应先试 K=2 binary hard gate
- **容易踩的坑**：AutoDL 实例重启后 SSH 端口会变；根分区只有 30GB 不能存大文件


---
