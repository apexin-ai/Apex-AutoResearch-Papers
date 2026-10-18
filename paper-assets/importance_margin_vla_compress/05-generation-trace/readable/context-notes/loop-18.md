# director / loop_18.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_18.md`
- **Structured JSON:** [`f781d7af9970f857cfe7.json`](../../sessions/f7/f781d7af9970f857cfe7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_messages
updated: '2026-05-27T00:44:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- 4 台服务器：cqa1-33015、westd-27271、westd-38929、westd-41074，GPU 只能用项目配置内的
- 实验硬截止 May 28 20:00 BJT（C002），之后不再启动新实验
- CoRL 2026 Paper 提交 May 29，只补论文 figure 必需的 cliff curve 数据点
- k=0.95 端点审批时 approve_experiment 报 "not found"——可能 Agent 未正式提交 approval request，需要让新 Agent 直接部署而非走审批流

### 2. 🖥️ 基础设施快照
- 4 台 AutoDL 服务器，每台 4 GPU（共 14 GPU 分配）
- 工作目录：`/root/autodl-tmp/importance_margin_vla_compress`
- Python：conda base 环境（aml-train 镜像）
- 模型/数据：在各服务器 `/root/autodl-tmp/` 下
- 无 W&B 配置，无 Git remote
- 活跃进程：ROADMAP GPU 表显示 14 GPU 全占用（截至 00:00 UTC），但 Agent idle 961min 说明可能多数已完成未回收
- Paper Agent session 活跃，provenance 80/83，刚完成 k=0.7 叙事修正 patch

### 3. 📊 当前状态
Agent idle 16h，我刚重新加载状态并尝试审批 2 个 pending 实验（失败，approval 不存在）。

ROADMAP 显示的 RUNNING 实验（可能已完成，需诊断）：
- OpenVLA: Attn k=0.95 Obj, Attn k=0.5 Goal/Long, L2n k=0.5/0.75 Long, Rnd k=0.75 Obj/Long/Goal, Rnd k=0.85 Long v3, Attn k=0.75 Goal/Long
- π0.5: L2norm k=0.85 Long, Random k=0.7 Long, 某 eval

关键缺口（cliff curve 顶端 k=0.95）：
- Object: Attn k=0.95 (?running), Random k=0.95 (?running on westd-41074)
- Goal: 三方法 k=0.95 全缺
- Long: 三方法 k=0.95 全缺

### 4. 📋 待办
- Agent 重启后 → 立即 SSH 诊断 4 台服务器所有 GPU 进程状态（哪些实验还活着、哪些已完成）
- 已完成实验 → 收集结果、更新 registry、释放 GPU
- GPU 空出 → 立即部署 k=0.95 端点（优先 Long 和 Goal，Object 部分已有）
- 全部 cliff curve 数据收齐 → 通知 Paper Agent 更新 figures + tables
- May 28 20:00 前 → 确认 provenance 83/83，Paper Agent 完成最终版

### 5. 🎯 战略上下文
项目核心发现：VLA vision token 可压缩性取决于 scoring method × connector × task 三维交互。Position encoding sensitivity 已确认（D237）。Crossover table 16/16 完成。

关键决策链：D240（只补 figure 必需点）→ D237（L2norm 单调=position encoding）→ D239（π0.5 k=0.5 三方法收敛）

易错点：
- ROADMAP GPU 表是手动维护的，实际进程状态需 SSH 确认（Agent idle 16h 说明可能大量实验已完成但未回收）
- approve_experiment 需要 Agent 先正式 request_approval，不能凭 report.md "等待人工审批" 就直接 approve
- 距 deadline <24h，不要再新增非 cliff-curve 实验，只补论文 figure 必需的数据点


---
