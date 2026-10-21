# director / loop_7.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`2bba77273ad536e23639.json`](../../sessions/2b/2bba77273ad536e23639.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-14T05:19:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目 GPU 白名单：cuda:0-3，跨 3 台服务器（home-1x5090, seetacloud-westd-4x5090, westd-48478）。westd-48478 是主力 eval 服务器。
- 论文数字阻塞（D057）：CWM v11 数据已被 D055 废止（混合 transformers 4.57.6→5.8.0），论文全部 CWM repo-level 数字必须等 CWM v12 全量 eval 完成后替换。Paper Agent 已通知暂停提交。
- Checkpoint 选择规则：eval_loss 最优 ≠ test accuracy 最优。所有 eval 必须做 checkpoint sweep（≥3 个 checkpoint），禁止仅用 eval_loss best。这条已写入 ml-experiment-guide。
- D056 早停的实验结论应为 "killed"（D056 early stop），不是 "failed" 或 "OOM"。Reviewer 已纠正过一次误诊。

### 2. 🖥️ 基础设施快照
- **westd-48478** (connect.westd.seetacloud.com, user=sonny): 4×5090, 工作目录 /home/sonny/exec-sim-repair-verifier, conda 环境（transformers 4.57.6）
  - GPU 0: CWM seed123 eval（可能仍在跑，ETA 原估 ~15h，需 SSH 确认）
  - GPU 1: CWM v12 eval（同上）
  - GPU 2/3: CLS 8B ckpt-400/600 eval 已启动（应已完成，需确认收集结果）
- **home-1x5090** (implicit5638.xyfu.me, user=sonny): 1×5090, 工作目录 /home/sonny/exec-sim-repair-verifier
  - GPU 0: CLS seed123 ckpt-800/1000 + v5 sweep 串行（应已完成，需确认）
- **seetacloud-westd-4x5090**: 已注册但本轮未活跃使用
- eval 脚本输出 JSON 到各服务器的 checkpoint 目录下（如 eval_repo_cls.json）

### 3. 📊 当前状态
刚批准 RESET_BOTH，本 session 即将结束。最后动作是发了综合检查指令给 Agent（检查全部 GPU 状态 + 收集 eval 结果 + 更新 report）。

**已完成的关键 eval**：
- Home CLS v5 seed42 ckpt-600: **76.92%**
- Home CLS seed123 ckpt-600: **80.73%**（2-seed mean 78.83%）
- Westd CLS v5-conda ckpt-400: **78.43%**, ckpt-600: **76.37%**（确认环境无问题）
- CLS 8B ckpt-200: 70.22%（ckpt-400/600 结果未收集）

**尚未收集的结果**（Agent 刚收到指令去查）：
- CLS 8B ckpt-400/600 eval（westd GPU 2/3，应已完成）
- Home seed123 ckpt-800/1000、v5 sweep（应已完成）
- CWM v12 + CWM seed123 全量 eval（westd GPU 0/1，原估 15h，可能仍在跑）

### 4. 📋 待办（条件触发式）
- Agent 回报 GPU 状态 → 确认哪些 eval 已完成，收集结果，空闲 GPU 分配 8B 剩余 checkpoint eval
- CLS 8B ckpt-400/600 结果到手 → 与 Reviewer 讨论 model scaling narrative + Table 4 呈现方式
- CWM v12 全量 eval 完成 → 用 westd within-server CLS ckpt-best vs CWM v12 做 apple-to-apple gap 计算；如 gap ≥15pp → 通知 Paper Agent 做 number-update micro-patch 解除 D057 阻塞
- CWM seed123 全量完成 → paired bootstrap + TOST 统计检验
- 全部 repo-level 数字确定 → Paper Agent 统一更新 Abstract/Intro/§5.6/Conclusion + 补充 token-level 分布分析（truncation vs format error）

### 5. 🎯 战略上下文
- **核心结论 C1 (Complexity-Dependent Advantage) 非常稳固**：function-level gap 1.24pp → 8B gap 2.43pp → repo-level gap 预计 ~21pp（CLS ~78% vs CWM ~57%）。复杂度梯度 narrative 强。
- **D052 GO 判决有效**，但论文数字全部需要用正确 checkpoint 的全量 eval 替换。
- **最容易判断错的事**：(1) 不要用 ckpt-200 的数字做任何决策——它系统性偏低 15-25pp；(2) CWM eval running accuracy 在早期（<1000 样本）波动大，不要过早下结论；(3) report.md 严重过时，以 SSH 实查为准。
- **决策链**：D052(GO) → D054(conda apple-to-apple) → D055(v11废止) → D056(early stop+eval) → D057(论文阻塞等v12)。


---
