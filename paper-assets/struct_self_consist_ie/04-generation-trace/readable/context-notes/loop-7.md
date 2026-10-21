# director / loop_7.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`9d54e0ef2a1e000aca07.json`](../../sessions/9d/9d54e0ef2a1e000aca07.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-16T16:05:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 autodl-5090 的 cuda:0/1/2/3（4×RTX 5090）。无其他服务器分配。
- exp-020 训练 PID 288683 在 cuda:1 上运行，**严禁 kill 或重启**——之前 Worker 误报中断差点导致重启，Reviewer 确认进程正常。
- N-scaling 表必须用 **macro F1**（与 Table 2 一致）。D118 决策：subsampled greedy=0.614 作为内部一致 baseline，表格 footnote 解释与 Table 2 的 0.645 差异。严禁混入 micro F1。
- LR verifier 数值已修正为 exp-027（AUROC=0.652, F1=0.641），不要回退到 exp-019 旧值（0.697/0.648）。
- 论文标题已从 "Cannot" 改为 "Fail to"，不要改回。

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb1.seetacloud.com)，用户 root
- 工作目录：/root/autodl-tmp/struct_self_consist_ie
- Python：conda base 环境（/root/miniconda3/bin/python）
- 模型：Qwen3-8B LoRA fine-tuned checkpoints 在工作目录下
- 数据：SciERC / CoNLL-2003 / WNUT-17 / Few-NERD INTRA（coarse 8-type，131k train）
- 活跃进程：exp-020 训练 PID 288683 (cuda:1)，ETA 23:33 CST（应已完成或即将完成）
- Cron：每 2 分钟监控 PID 288683，进程退出后自动回调 Agent
- W&B：未配置

### 3. 📊 当前状态
**刚做完**：
- Dream #2 审稿反馈的全部行动项：D117 写作修复 10 项 + 4 个新实验（exp-025 N-ablation, exp-026 T-ablation, exp-027 MLP verifier, exp-028 entity-token LP）全部完成并写入论文
- Paper Agent 完成 28 页论文更新，0 critical compilation warnings
- Reviewer 确认两个纸面一致性 issue（N-scaling metric + LR verifier 数值）均已修正 PASS

**RUNNING**：
- exp-020 Few-NERD smoke：1-epoch LoRA r16 Qwen3-8B on Few-NERD INTRA，训练 84.7% → 应已完成。Agent 有 cron 监控，完成后自动执行 merge → pilot inference → exp-021 启动

**等待中**：
- Agent cron 回调（exp-020 PID 退出）
- Agent 处理完后将汇报 exp-020 结果 + exp-021 启动状态

### 4. 📋 待办
- exp-020 cron 回调到达 → Agent 自动执行 merge → 200-instance pilot (N=8, T=1.0) → F1>0.5 则启动 exp-021 (rank=32, α=64, 3 epochs, cuda:0/1/2/3)
- exp-021 训练完成 → 分析 Few-NERD 结果 + 写入论文（第 4 个数据集，强化 generality claim）
- N=32 bootstrap significance test 仍未做（+0.91pp LP selection 需要 p-value，Reviewer 之前 flagged）
- 全部实验完成后 → dream_simulate(review_mode="full") 第三次 Dream，验证是否从 3.0 提升到 ≥3.5
- ROADMAP 近期任务已更新，直接 read_roadmap 可看完整列表

### 5. 🎯 战略上下文
- **核心 story**：QE-selection gap — 5 个 confidence signals 做 QE 好（AUROC 0.82, ρ 0.42）但 selection 全失败（+0.6pp, p=0.39）。Multi-causal 诊断：instance degeneracy + LP compression + feature bottleneck。Dual contribution: (A) QE 正向框架 (B) 失败诊断。
- **Dream #2 分数**：Best 3.0 / Median 3.0 / Worst 2.5。距 Main Conference 3.5 有差距。当前改进（N-scaling, T-ablation, MLP verifier, entity-LP, non-tied subset promotion, 贡献重构, 标题修正）尚未被 Dream 验证。
- **关键决策链**：D113（macro/micro F1 统一）→ D116（Dream #1 reframe to dual contribution）→ D117（Dream #2 全面行动计划）→ D118（N-scaling greedy baseline bug fix）
- **易错点**：
  - N-scaling 数据经历过两轮 bug fix（samples[0] 作 greedy → 修正，micro/macro 混用 → 修正），不要用任何旧版数据
  - T-ablation 中 T=0.5 用的 joint subtask，T=0.8/1.2 用的 ner-only，不能直接横向比 RE 指标
  - exp-021 Few-NERD 是最后一个重要数据点——如果 Few-NERD 上也观察到 QE-selection gap，generality claim 大幅加强；如果不观察到，需要 reframe 为 "dataset-dependent"
  - DDL 2026-05-25，还有 9 天，时间够用但不能浪费——exp-021 是最后一个 GPU 密集实验


---
