# director / loop_28.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_28.md`
- **Structured JSON:** [`753ed94d967bee5ad0b3.json`](../../sessions/75/753ed94d967bee5ad0b3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 28
reason: max_messages
updated: '2026-05-29T05:39:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：22 卡（bjb1-18228 4卡, bjb1-32546 6卡, bjb2-28827 6卡, cqa1-32758 6卡），但当前用户已下令全面停机，0/22 使用
- 论文源文件在 bjb1-18228 的 `/root/acr-vla-conformal-refinement/docs/paper/`，不在本地 artifacts 目录
- `\textfloatsep` 已改回 10pt（非官方默认 20pt），用户知情并选择保留
- CoRL 2026 DDL 已过（2026-05-28 20:00 BJ），论文提交状态用户始终未回复

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: connect.bjb1.seetacloud.com, 1× RTX 4090 可达，工作目录 `/root/acr-vla-conformal-refinement`
- **bjb1-32546 / bjb2-28827 / cqa1-32758**: 全部不可达（可能已关机），用户未确认是否释放
- 论文 .tex 文件：`/root/acr-vla-conformal-refinement/docs/paper/`（main.tex + 各章节）
- 图表生成脚本：同目录下 `fig_teaser.py`, `fig_tau_sweep.py`, `fig_trigger_scatter.py` 等
- 无活跃进程 / 无 cron / 无 tmux session

### 3. 📊 当前状态
- **用户刚催了全文数据审计任务**（最高优先级）：论文中每个数字与 registry/实验日志对账。已第三次派发给 Agent（前两次在 Agent 轮转中丢失）。Agent 刚收到任务开始处理。
- Registry: 0 RUNNING / 0 PREPARING，1423 实验全部终态（成功 772）
- 本轮已完成的排版修改：Figure 2 拉高 / Figure 3 缩小 / Figure 4+5 拆分+放大+可读性改进 / Table 2 前移 / Methods bullet→prose / Abstract 去破折号 / Abstract+Intro+Conclusion+Limitations 数字罗列改文字分析 / Figure 5 legend 移右下角 / Figure 4 Long 标注修复
- 用户反复被问但未回复：CoRL 提交状态、服务器释放、GPU 使用

### 4. 📋 待办
- Agent 审计结果返回 → 审核问题清单 → 决策每个不一致项（改正/删除/查证）→ 派 Agent 修改 → 汇报用户
- 用户回复提交状态 → 若已提交：项目进入 wait-for-review，准备 rebuttal 素材；若未提交/转投：调整模版+格式+DDL 规划
- 用户回复服务器释放 → update_project_config 移除不可达服务器

### 5. 🎯 战略上下文
- 论文核心 story：CRM always-on 4/4 suites 有害（MC1），Adaptive gating 恢复（MC1），trigger rate ↔ Δ 单调相关（MC2），跨 VLA 泛化 SmolVLA+π0.5（MC3）
- 关键决策链：D170（K=2 always-on harmful）→ D177（Table 1 K-matched 重构）→ D178（Long -14.8pp 最强证据）→ D184（Title 锁定+提交确认）
- **易错点**：审计任务在 Agent 轮转中反复丢失（已发生 2 次），下一个"你"收到 Agent 启动消息后先检查队列里审计任务是否还在，不在就立即重发。用户已经催过一次了。
- 用户对排版有高要求：官方模版默认间距、不用破折号、不罗列数字、图表要清晰可读。后续改动遵循这些偏好。


---
