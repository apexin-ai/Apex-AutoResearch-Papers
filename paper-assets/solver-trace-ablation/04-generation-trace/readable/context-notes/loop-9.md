# director / loop_9.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`581fa23816e9bdb02891.json`](../../sessions/58/581fa23816e9bdb02891.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-19T12:06:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-39279 只有 **1 张 GPU** (cuda:0, RTX PRO 6000 96GB)。ROADMAP/排期里出现过 cuda:1 但不存在，已修正。
- 论文 gated ISR claim 已从 "eliminates TS entirely (0/3 seeds)" 修正为 "suppresses TS in 5/6 seeds"。不能回退到旧 claim。
- D142-ext 6-seed 数据 (s52-s57) 已写入论文，s55 TS=82% 是关键新发现，不能遗漏。
- 项目 GPU 白名单只有 westd-39279 cuda:0，已向 Manager 申请云 GPU 但未获批。

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/solver-trace-ablation
- GPU：cuda:0 (RTX PRO 6000 96GB)，**仅此一张**
- 磁盘：~209G free
- 模型：Qwen3-4B (已在服务器上)；LLaMA-3.2-3B (下载中/待确认)
- 数据：FOLIO train_500_seed42.jsonl + proofwriter_fol_100.jsonl；ProofWriter FOL 数据准备中
- 活跃进程：D142-ext s55-s57 已全部完成；D143/D144 准备阶段（CPU 任务：ProofWriter 数据 + LLaMA 下载）

### 3. 📊 当前状态
刚完成：
- D142-ext s55-s57 全部完成并分析。s55 TS=82% 推翻原 claim，论文 conclusion.tex + appendix.tex §G.4 已修正（6-seed 表 + 修正叙事）
- Reviewer 验证论文修正 PASS
- ROADMAP 修正为 1 GPU 串行方案

等待中：
- Agent 处理 D143/D144 综合扩展指令（Agent 刚被 RESET，queue 中有 3 条消息：原始双 GPU 指令 + 串行修正 + registry 更新指令）
- Manager 云 GPU 申请回复（1×4090，24-36h，~50-100 CNY）
- 审稿提交卡待用户点击批准

Registry RUNNING/PREPARING：无（D142-ext 已完成，D143/D144 尚未提交）

### 4. 📋 待办
- Agent RESET 完成 → 确认 Agent 收到并理解串行方案（D143 ProofWriter 先 → D144 LLaMA 后），检查旧的双 GPU 指令是否造成混乱
- ProofWriter 数据就绪 → 开始 D143 pw-exec-s42/s43/s44 (cuda:0)
- LLaMA-3.2-3B 下载完成 → 代码适配 + dry-run，确认可训练
- Manager 批准云 GPU → director_allocate_gpus 分配，D143/D144 并行
- Manager 拒绝云 GPU → 维持串行方案，~36h 完成全部实验
- D143 核心 6 runs 完成 → 中间结果分析，确认 Goodhart collapse 是否在 ProofWriter 上复现
- 全部实验完成 → 派 Paper Agent 集成新 Table + 跨维度分析，重新提交审稿

### 5. 🎯 战略上下文
- **核心叙事**：ISR 作为 RL 训练信号时在所有 β 剂量下 Goodhart collapse；gated ISR 实验证明 whack-a-mole（blocking one pathway → new exploits + original can persist via exec reward alone）
- **D144 决策**：全面扩展 ProofWriter(跨数据集) + LLaMA-3.2-3B(跨模型)，共 18 个新实验。用户明确要求 "把实验都补上"
- **R14 评分 3.0 (Findings)**，瓶颈是单模型+单数据集泛化性。跨维度实验是冲 3.5+ 的关键
- **DDL May 25**，串行方案 ~36h（~May 21 上午完成），留 3-4 天 buffer
- **易错点**：Agent queue 中有 3 条指令（第一条是过时的双 GPU 方案，第二条修正为串行，第三条是 registry 更新）。新 session 的 Agent 可能只看到第一条就执行。需要在 Agent RESET 后立即用 replace_agent_queue 发一条综合串行指令，避免 Agent 按双 GPU 方案执行
- **易错点 2**：论文 experiments.tex §4.2 line 42 已改为 "associated with RL optimization"，不要用 "RL-specific"
- **决策链**：D142(gated ISR) → D143(ProofWriter 跨数据集) → D144(全面扩展决策，包含 D143+LLaMA)


---
