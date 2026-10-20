# director / loop_5.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`ad0277620c1a92d3b78d.json`](../../sessions/ad/ad0277620c1a92d3b78d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T16:19:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 只有 westb-13313 的 cuda:0 和 cuda:1，不可用其他设备
- SF3 death timing 分析使用了 378 episodes，但论文主分析用 245 episodes / 11 tasks（plan-012-full）。**任何引入论文的数字必须基于 245-episode 子集**，否则审稿人会发现与 Table 1 不一致
- 审稿阶段已启动（review_chat_id: oc_0b622d6038b969b96148ee8a163a1a0c），论文修改走 Paper Agent，不要自己直接改 .tex
- plan-006-deep-internal 的 "failed" 是误报（GPU kill 连锁），不要重跑整个实验

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (connect.westb.seetacloud.com)，root
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- Python：aml-train 镜像，conda base（/root/miniconda3/bin/python）
- 论文源码（本地真源）：projects/simgate-modular-routing/artifacts/_project/paper/latex/main.tex
- 活跃进程：plan-006 chemistry-mix 补收 PID 508245（应已完成或即将完成，20/20 episodes）
- 无 W&B 配置

### 3. 📊 当前状态
- **刚完成**：Paper Agent 完成 Round 7 审稿报告全部 Action Matrix（CRITICAL 1-4 + MF1-4 + SF1-7 + m1-6），已提交 continue review（apr_20260515T161642_l5z8，pending 用户审批）
- **review_issues.yaml**：已批量更新，所有 round 7 action items 标 done，open issues 改 in_progress
- **plan-006-deep-internal**：113/120 episodes 已收集，chemistry-mix 补收中（PID 508245，~10 min 前还剩 7 episodes）。Reviewer 确认数据质量通过，误报已澄清
- **Agent 队列**：depth 4-5，正在处理中（idle_seconds ~269）。已取消一条 stale cron 消息（plan-006 误报）
- **SF3 death timing**：分析完成但用了 378 episodes，Reviewer WARNING 要求在 245-episode 子集重跑

### 4. 📋 待办
- chemistry-mix 20/20 完成 → Agent 将 plan-006 registry 改 conclusion: success + 补填 6 tasks metrics（death rate / score）
- plan-006 metrics 就绪 → 评估 deep-internal vs fast-internal 差异，决定 3-way routing 是否有价值（差异大 → 3-way 有信号；差异小 → 2-way suffices）
- SF3 death timing 需在 245-episode 子集重跑 → 派 Agent 执行，结果给 Paper Agent 更新论文中 death timing 相关描述
- continue review 审批通过 → Review Director 启动 Round 8 验证所有修复
- Round 8 审稿报告返回 → 按 review-report-action skill 逐条处理

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 Main Conference Long Paper，ARR deadline 2026-05-25（还剩 10 天）
- **核心结论**：death avoidance 占 routing signal ~90%（DAF=90.41%），这是论文最强 claim（C1）
- **反复被审稿打回的顽固问题**（R6-C1，从 round 4 起）：DAF 依赖 penalty P=100，78.9% penalty-free accuracy 才是稳健指标。Paper Agent 已修改 prominence，但这个问题每轮都 resurface，Round 8 重点关注是否真正解决
- **R7-N2 是最强批评**：router diagnostic 结论（Contribution 4）与数据不足混淆（81 train samples, ~8 internal-preferred）。已 downgrade 为 preliminary observation，但审稿人可能继续追问
- **易错点**：论文中 245 episodes vs 分析中 378 episodes 的数据集不一致——任何新分析数字入论文前必须核对数据范围


---
