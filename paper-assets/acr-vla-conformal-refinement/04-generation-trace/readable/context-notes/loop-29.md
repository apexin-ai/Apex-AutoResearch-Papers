# director / loop_29.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_29.md`
- **Structured JSON:** [`8813af1fa8e8d367aa99.json`](../../sessions/88/8813af1fa8e8d367aa99.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 29
reason: max_messages
updated: '2026-05-29T10:42:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目 GPU 白名单：bjb1-18228 cuda:0-3, bjb1-32546 cuda:0-5, bjb2-28827 cuda:0-5, cqa1-32758 cuda:0-5（共 22 卡）
- 当前仅 bjb1-18228 可达（且实测仅 1 卡），其余 3 台不可达（可能已关机），不要尝试连接
- CoRL 2026 DDL 已过（2026-05-28 20:00 BJ），论文提交状态待用户确认，不要自行决定转投
- 全面停机状态（用户 05-28 指令），未经用户许可不要启动任何实验

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-18228 (connect.bjb1.seetacloud.com, root, 1× RTX 4090 可达)；bjb1-32546 / bjb2-28827 / cqa1-32758 均不可达
- 远程工作目录：/root/acr-vla-conformal-refinement
- 本地论文目录：projects/acr-vla-conformal-refinement/docs/paper/
- 本地 Python venv：projects/acr-vla-conformal-refinement/.venv/bin/python（用于本地图表生成）
- 活跃进程：无。0 RUNNING / 0 Worker / 0 Cron

### 3. 📊 当前状态
本轮 session 完成的工作：
1. Abstract 加了 2 句背景引入（~228 词，<250 限）
2. Fix 1: 全文 5 处 "positively correlated" → "shows a positive trend"（abstract/intro/experiments/conclusion）
3. Fix 4: experiments.tex Δ 混用加了显式参照系标注（"vs. VLA-only" / "vs. CRM always-on"）
4. Fix 5: Fig 1/3/5a/5b 字体放大 30-50%；Fig 5a 图例移除（线末端已有标签）
5. 回复了用户关于 Title / Abstract / Primary Keyword 的查询（推荐 "Probabilistic learning and uncertainty in robotics"）

Registry: 1423 实验全部 DONE/killed/cancelled，0 RUNNING / 0 PREPARING。
无等待中的 Worker 回调 / Cron / 审批。

### 4. 📋 待办
- 用户确认论文已提交 CoRL / 转投其他会议 → 更新 ROADMAP 提交状态，按需调整
- 用户确认 3 台不可达服务器是否释放 → 若释放则 remove_server 清理配置
- 审计 Warning #2（π₀.₅ Object failure mode 补入 Limitations）和 #3（Limitations 扩展）用户未要求修，但如果后续用户要求或转投时需要改
- 用户要求新实验 → 先确认哪些服务器可用，当前仅 1 卡

### 5. 🎯 战略上下文
- 论文定位：Analysis-first + method contribution（D179 用户确认）。核心 claim 是 "correction 何时有效/何时有害"，不是方法提分
- Table 1 K-matched 3 列是论文最核心数据：CRM always-on 4/4 suites 有害 → Adaptive gating 恢复
- Long suite 是最强证据：CRM always-on -14.8pp，gating 恢复 +14.5pp
- π₀.₅ 结果标记为 "preliminary"，Object 上 gating 反向恶化（86.2% < 88.0%）这个事实在 abstract/limitations 中未显式提及——审稿人可能会抓
- 易错：不要把论文 claim 从 "positive trend" 升回 "positively correlated"——这是本轮刚降级的，4 个数据点不支撑 correlation
- 决策链关键节点：D170（K-matched 重构）→ D177（Table 1 3 列）→ D178（Long 最强证据）→ D179（title 锁定 + analysis-first 定位）→ D184（数据锁定 + 提交确认）


---
