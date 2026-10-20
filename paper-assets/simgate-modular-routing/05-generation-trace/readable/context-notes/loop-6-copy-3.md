# reviewer / loop_6.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`7187a7a78084a4d41c5c.json`](../../sessions/71/7187a7a78084a4d41c5c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-14T21:36:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westb-13313，GPU 白名单 cuda:0 / cuda:1（2× RTX 5090 32GB）。之前出过 vLLM 僵尸进程占 cuda:1 的事故，审查时必须 nvidia-smi 独立核实。
- Δ_nd 有两个合法值：2.84（plan-012-full，strict neither-died filtering，主文使用）和 3.07（plan-012-penalty-sensitivity，includes both-died，仅 Appendix penalty sensitivity 表用）。**不要把 3.07 当错误试图统一**——两者 filtering 方法不同，各自正确，caption 已说明差异。
- Router 4-seed 数据：balanced_acc 是唯一稳定指标（58.1±0.8%），accuracy 和 internal_recall 跨 seed 方差极大（±12%、±14.4%），不可用单 seed 数字代表全局。seed 42 在 accuracy 上最高（65.4%）但在 internal_recall 上最低（51.5%），"(best seed)" 标签不成立。

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313(root)，工作目录 /root/autodl-tmp/simgate-modular-routing
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/
- 论文源文件：docs/paper/*.tex（experiments.tex, introduction.tex, related_work.tex, conclusion.tex, method.tex, main.tex）
- Registry：58 实验全部终态（22 success, 13 negative, 10 failed, 13 killed），无 RUNNING/PREPARING
- 活跃进程：无（之前的 vLLM 僵尸已 kill）

### 3. 📊 当前状态
刚完成 R5 Camera-Ready 审查并通过 reviewer_post_to_director 提交。R5 评分 3.5/5 Weak Accept - Findings。审查了 4 项修复（CR1-CR4）：
- CR1（Related Work ~90% 加 penalty 限定词）：✅ 批准
- CR2（Δ_nd=2.81 统一为 2.84）：当前文本中找不到 "2.81"，所有实例已是 2.84 或 3.07（各自正确），可能已在前轮修复
- CR3（Intro "failing to" → "does not significantly"）：✅ 批准
- CR4（单 seed vs 4-seed 混报）：建议改为 balanced_acc 为主指标 + accuracy/recall 报范围，禁止 "(best seed)"

等待 Director 对 R5 审查意见的处理决策。

### 4. 📋 待办
- Director 回复 R5 处理决策 → 核实 Worker 修改后的 .tex 文件是否与审查建议一致
- 如触发 R6 审稿 → 按 §5 写作审查模式审查，重点检查 CR4 修复是否到位
- 如 Director 判定 paper 收敛（连续两轮无新 critical + overall 持平）→ 无需进一步审查，等待提交

### 5. 🎯 战略上下文
- 核心结论：DAF=90.41%，~90% 的 routing signal 来自 death avoidance 而非 task performance。这是 negative result paper——router 训练失败正是论证的一部分。
- 论文已经过 R1-R5 共 5 轮审稿迭代，从 3.0 提升到 3.5/5。目标 venue: EMNLP 2026 ARR short paper（DDL 2026-05-25）。
- 易错判断：(1) 不要把 3.07 和 2.84 的差异当 bug——是两种 filtering 的正当差异；(2) penalty sensitivity 表中 DAF=89.6%（P=100）vs 主文 90.41% 也不是矛盾——前者用宽松 filtering；(3) 论文叙事是 negative framing（router 训练诊断性失败证明 signal 结构性不足），不要建议把它写成 positive contribution。
- 决策链关键节点：plan-012-full 是 canonical death decomposition 数据源，所有主文数字以它为准。plan-012-penalty-sensitivity 仅用于 Appendix 敏感性分析。


---
