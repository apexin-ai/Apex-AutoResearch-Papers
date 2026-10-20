# director / loop_7.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`ab31ca51777a2c24df08.json`](../../sessions/ab/ab31ca51777a2c24df08.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T21:25:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配必须通过 `get_project_status` 校验 `gpu_ids` 白名单，不能用白名单外的卡
- DS 8k 重跑系列（acc_ds_dense_8k / acc_ds_s015_8k / acc_ds_s020_8k / acc_ds_s025_8k / acc_ds_s030_8k）已被 D086 决策暂停，不要启动
- DS accuracy 数据不进论文定量对比（D086），仅作定性趋势描述
- 服务器 westd-22162，代码路径 /root/autodl-tmp/pacs

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162 (connect.westd.seetacloud.com) [root]
- 工作目录：/root/autodl-tmp/pacs
- Git/W&B：均未配置
- 飞书：A群 + B群 + C群（审稿群）均已绑定
- 审稿阶段已激活，review_chat_id: oc_57b24a804b56707ec9118a483a8ac65e
- 基础设施细节（Python 路径、conda env、模型路径、tmux sessions）需下一轮 SSH 探查确认，本轮 Director 未直接操作服务器

### 3. 📊 当前状态
刚处理完 Reviewer 的 accuracy 全条件交叉审查报告（WARNING 级别），做了两件事：
1. **D086 决策**：DS accuracy 降为定性观察，QW 作为 accuracy dose-response 定量主力，暂不追加 DS 4096/8k-token 重跑
2. **给 Agent 发了指令**：暂停 DS 8k 系列、QW n=100 继续、请 Agent 说明 r9c2-spike 实验目的

RUNNING 实验：
- acc_qw_s025_n100 — QW s025 扩样本到 n=100，验证非单调性是否为噪声
- acc_qw_s020_n100 — QW s020 扩样本到 n=100，同上

待处理（未启动）：
- r9c2-spike / r9c2-spike-v2 / r9c2-spike-v3 — 目的不明，已问 Agent 但尚未收到回复
- DS 8k 系列 ×5 — 已暂停（D086）

### 4. 📋 待办
- Agent 回复 r9c2-spike 说明 → 评估优先级，决定是否审批推进
- QW n=100 完成 → 检查 dose-response 单调性：单调 → accuracy claim 成立（基于 QW）；仍非单调 → accuracy 维度降级为定性观察
- QW n=100 单调 + 论文需要双模型数据 → 重新考虑启动 DS 8k 重跑
- QW n=100 单调 + QW 数据充分 → DS 8k 永久取消，GPU 留给其他实验

### 5. 🎯 战略上下文
- 项目处于 Research + 审稿并行阶段，102 个实验（43 成功/14 负向/14 失败）
- 论文溯源覆盖率 24/24，决策日志 85 条（截至 D086）
- **核心判断点**：accuracy dose-response 能否作为定量 claim 取决于 QW n=100 结果。这是当前最关键的 pending 数据。
- **易错点**：DS accuracy 看起来趋势方向正确（0.52→0.36→0.26→~0.1），但截断率太高导致有效样本极少，千万不要因为"方向对"就把 DS 数据当定量证据用
- **r9c2-spike 是盲区**：这 3 个实验目前没有上下文，Agent 的回复还没到，下一个"我"需要先搞清楚这是什么再做决策


---
