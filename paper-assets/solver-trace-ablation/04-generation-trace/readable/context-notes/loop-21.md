# agent / loop_21.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_21.md`
- **Structured JSON:** [`58e8f0f60c931b67947c.json`](../../sessions/58/58e8f0f60c931b67947c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_wall_time
updated: '2026-05-17T21:28:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-39279 只有 **1 张 GPU (cuda:0)**，不存在 cuda:1。ROADMAP 和 resource config 声称 2 张是错误的。
- D129 实验必须**顺序执行**在 cuda:0 上，不能并行。
- submit_training_job 命令必须用 `bash -c "..."` 包裹（tmux 用 sh 不是 bash）。
- 训练数据固定为 `data/train_500_seed42.jsonl`（500 条），seed 参数控制模型初始化不是数据。
- sweep-isr-b005-s42 的 registry 状态曾卡在 PREPARING，已手动链式修复到 DONE/negative，不要再动。

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279，1× RTX PRO 6000 96GB
- **工作目录**: `/root/solver-trace-ablation/`
- **Python**: conda base, Python 3.12, torch 2.10.0+cu128, trl 1.1.0（直接用 `python`，不需要 source activate）
- **模型**: Qwen3-4B 在 `/root/autodl-tmp/models/Qwen3-4B/`；Qwen3-1.7B 在 `/root/autodl-tmp/models/Qwen3-1.7B/` (3.8GB, 2 shards)
- **数据**: 训练 `data/train_500_seed42.jsonl`；评估 `data/proofwriter_fol_100.jsonl`
- **脚本**: `scripts/train_grpo.py`, `scripts/eval_sta.py`, `scripts/classify_h7.py`
- **活跃进程**: d129-1.7b-isr-b01-s43 (PID 14701, tmux=d129-1.7b-isr-b01-s43, cuda:0)，预计 UTC ~22:45 完成
- **磁盘**: 61GB 可用
- **论文本地路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/`

### 3. 📊 当前状态
**刚做完**: Round 6-9 论文审稿修复（16+ commits），Figure 3 更新为 5-seed，provenance v13。§5 在 page 8 内。

**D129 实验队列** (6 runs, 顺序执行 cuda:0):
1. `d129-1.7b-isr-b01-s43` — **RUNNING**, PID 14701, ~1.5-1.8h
2. `d129-1.7b-isr-b01-s44` — PREPARING
3. `d129-1.7b-random-b01-s43` — PREPARING
4. `d129-1.7b-random-b01-s44` — PREPARING
5. `d129-1.7b-isr-b03-s43` — PREPARING
6. `d129-1.7b-isr-b03-s44` — PREPARING

**等待**: d129-1.7b-isr-b01-s43 的 cron 完成回调。无 Worker 在跑。

### 4. 📋 待办
- d129-1.7b-isr-b01-s43 cron 回调 → spawn worker: eval (greedy, proofwriter_fol_100.jsonl) + classify (H1/H7/H8/H9/N-H) → update registry metrics → **检查 genuine >10% 则暂停汇报** → 提交 d129-1.7b-isr-b01-s44
- 每个后续 run 完成 → 同样 eval+classify+registry → 提交下一个
- 6 个全部完成 → 汇报 Director 全部结果表格 + 与 s42 对比 + paper §4.5 更新建议
- 如出现与 s42 完全不同的 hacking mode → 正常完成但汇报中标注
- 论文侧无待办（Round 9 已完成，等 Director 下一轮 review 或 D129 数据整合指令）

### 5. 🎯 战略上下文
- **DDL**: EMNLP 2026-05-25（剩 8 天）
- **核心结论**: ISR 作为诊断工具可靠（99.5% collapse 检测），作为训练 reward 不可靠（所有 dose 下 Goodhart collapse）。Genuine window transient、statistically underpowered (n=5)。
- **D129 目标**: 消除连续 9 轮 reviewer concern "1.7B 仅 1 seed"。s42 基线：ISR β=0.1 = 100% H1 fixed-template; Random β=0.1 = 100% H9 ex falso (PR=93%); ISR β=0.3 = reward collapse (PR=17%)。
- **易错点**:
  - 1.7B ISR β=0.1 s42 的 hacking mode 是 **H1**（不是 H7），与 4B 模式不同——这是论文 §4.5 的核心 claim（"different capacities converge to different Goodhart basins"）。新 seed 如果出现 H7 而非 H1，需要修改 claim。
  - 1.7B Random s42 出现 **H9** (contradiction injection, ex falso)，这是 4B 从未出现的 mode。新 seed 需要确认 H9 是否 deterministic。
  - eval 命令需要 `--greedy` 参数确保 greedy decoding。
  - CMH 已在正文中降级为 appendix-only（Round 9），不要在新分析中重新引入正文 CMH 数字。
  - 论文中 ISR 全称现在是 "Irreducible Solver Rate"（Round 6 统一），不是 "Intensional Structural Reward"。


---
