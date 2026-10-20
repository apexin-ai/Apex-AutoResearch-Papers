# reviewer / loop_18.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_18.md`
- **Structured JSON:** [`168903a3692200e0b894.json`](../../sessions/16/168903a3692200e0b894.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-18T02:01:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（物理 GPU-f7b10021 和 GPU-7b497967），越界即 CRITICAL
- 服务器：bjb1-45299（root），唯一训练服务器
- 论文 .tex 文件在**本地** `docs/paper/sections/`，不在远程服务器。远程只有训练代码/数据/checkpoint
- exp_024b_s0 registry 仍为 RUNNING 但 D090 已引用其数据——分析完成后需确认 registry 与 D090 一致

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299(root)，代码根 `/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`，conda env=base
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 论文：`docs/paper/sections/{results,analysis,conclusion,appendix}.tex`
- 活跃进程：exp_024b_s0 (PID 705742, tmux=exp_024b_cheetah_no_dt_emb_s0, cuda:0)——已到 105K+eval，正在收尾
- checkpoint_monitor (PID 123058) 常驻
- 无 W&B 配置，不检查 W&B

### 3. 📊 当前状态
刚完成：
- exp_024b_s1 核实 PASS（DONE/success, NVE=0.1×, no CIVO）
- ROADMAP "因果三角闭合 D090" 审查完成，已 post 3 条 warning（D090 引用未完成的 024b_s0 / "17→18" 第三次未修 / exp_025 去向不明）
- Cheetah 因果三角实质闭合（baseline×2 + trigger×1 + control×2）

等待中：
- exp_024b_s0 完成 → cron on_complete → 分析 worker → 需审查
- Agent 整合 024b 数据进论文 → 需章节审查
- "17→18" 修复 → 需确认
- submit_paper_to_review → 触发全文审查

### 4. 📋 待办
- 024b_s0 分析 worker 回调 → 核实 registry metrics 与独立验证一致（eval≈96.5, VE ratio≈0.43, no CIVO），确认 D090 证据链闭合
- 024b 数据整合进 appendix/F2/F7 的 worker 完成 → 审查新增行数据一致性
- "17→18" 修复 worker 完成 → 确认 results.tex line 12 已改
- submit_paper_to_review 触发 → 全文数字一致性扫描（重点：Table 1 vs appendix vs 正文 claim；detector 统计 3/3 TP, 2/8 FP, n=11 跨 3 处一致性；NVE 阈值 1.5× / AUROC 0.926 跨 results+analysis+conclusion）
- 两张 GPU 空闲且无实验排队超 12h → warning Director

### 5. 🎯 战略上下文
- 项目定位：**诊断论文**，不是方法论文。核心因果链：trained dt_emb → obs decoder gradient → RSSM fidelity gap → reward bias → critic overestimation → collapse
- 目标：CoRL 2026，DDL 2026-05-29（11 天）
- 决策链关键节点：D084(NVE 口径统一 AUROC=0.926) → D087(010b NVE 14.59→8.27) → D088(SGS "enables recovery" not "prevents") → D089(021 不入 detector 评估集) → D090(Cheetah 因果三角闭合)
- **易错点**：(1) exp_021 是 transient CIVO with recovery，不是 "SGS prevents CIVO"——F7 段已修正但 conclusion.tex 提到 SGS 时要注意措辞；(2) 010b NVE 是 8.27× 不是 14.59×（旧值已清零但下意识可能记错）；(3) detector n=11 不含 021（D089 决定），transient single-checkpoint spike 是 by-design 不检测；(4) exp_025 从未在 registry 出现，不要假设它存在


---
