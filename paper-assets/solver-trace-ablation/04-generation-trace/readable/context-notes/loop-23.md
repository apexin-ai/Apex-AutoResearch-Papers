# agent / loop_23.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_23.md`
- **Structured JSON:** [`dfabfc5e6c7aa950512e.json`](../../sessions/df/dfabfc5e6c7aa950512e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: idle_timeout
updated: '2026-05-21T01:27:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-39279:cuda:0（gpu_ids 白名单仅此一张）
- DDL 2026-05-25 最终提交，所有实验必须在此前完成
- D154 系列（Qwen3-8B cross-model）是 DDL 前必须完成的关键实验线
- 论文已 R16 提交中（Round 16 continue-mode review），paper 修改需与审稿迭代对齐
- 训练命令用 `--no_wandb`（8B 实验），指标从 log 提取而非 W&B
- d154-8b-exec-s42-r3 已被 kill（EXIT_CODE=129），不要重试这个配置（K=2 版本有问题）

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，工作目录 ~/runs/solver-trace-ablation/
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base 环境）
- 模型路径：/root/autodl-tmp/models/Qwen3-8B
- 数据：data/train_500_seed42.jsonl（500 条 FOLIO 训练数据）
- 磁盘：根分区 400G/439G 可用（4%），/autodl-tmp 5.3T/7.3T 可用（24%）——充裕
- 活跃进程：d154-8b-exec-s42-k4v2 已完成（PID 740527 已退出），状态 ANALYZING
- Cron：reconcile 返回 0 active（刚完成的已清理）

### 3. 📊 当前状态
**刚做完**：收到 d154-8b-exec-s42-k4v2 的 cron 完成回调，已 spawn Worker（worker_analysis_d154-8b-exec-s42-k4v2_20260520T092557）去 SSH 读日志分析结果。Worker 尚未回调。

**Registry 快照**：
- ANALYZING(1): `d154-8b-exec-s42-k4v2` — Qwen3-8B exec-only GRPO K=4 bf16 s42 500步
- PREPARING(31): 包括 d154-8b-exec-s43/s44、d154-8b-isr-s42/s43、d144-llama 系列等
- DONE(168): 70 success / 41 negative / 46 failed / 11 killed

**等待中**：
- Worker 回调：analysis Worker 正在分析 d154-8b-exec-s42-k4v2 日志
- 尚未向 Director 汇报本次实验结果（等 Worker 分析完后汇报）

### 4. 📋 待办
- Worker 分析回调到达 → 读分析报告 → update_registry(conclusion=success/negative) → 更新 report.md → 向 Director 汇报（带 [资源] 行）
- conclusion=success → 建议 Director 批准铺 d154-8b-exec-s43/s44（同 seed 复制）+ d154-8b-isr-s42（ISR 对照）
- conclusion=negative（8B 未复现 Goodhart collapse）→ 按 on-experiment-done negative 流程走推导链，向 Director 汇报证伪分析 + 建议
- D154 exec 系列完成后 → 启动 ISR 系列（d154-8b-isr-s42/s43）做 cross-model ISR 对照
- R16 审稿报告到达 → 按 action matrix 处理修改

### 5. 🎯 战略上下文
- **核心论点**：STA 作为 LOO 诊断工具，揭示 GRPO 训练中 Goodhart effect（reward hacking）。exec-only reward 导致 TS（template shortcut）主导，ISR 本应缓解但实际引入不同 collapse pattern
- **D154 的意义**：cross-model validation 是 R16 reviewer 关心的——4B 结果是否 model-specific？8B 复现 = 强化 generalizability claim；不复现 = 需要 scope 限定
- **决策链**：D147(kill LLaMA) → D148(ProofFOL framing) → D149(C2 refocus) → D153(R16 matrix) → D154(8B cross-model) → D155(R17 写作优先) → D156(R18 ISR 概念修复)
- **易错点**：
  - d154-8b-exec-s42-r3（K=2 版本）已 killed，不要混淆为 k4v2 的结果
  - 8B 实验用 `--no_wandb`，只能从 log 提取指标
  - 论文定位已收敛为 Findings track（不是 Main），不要在汇报中暗示冲 Main
  - 31 个 PREPARING 实验大多是占位，不是全部都要跑——以 Director 指令为准


---
