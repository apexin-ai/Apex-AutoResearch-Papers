# director / loop_7.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`2f3a0ba5d527f01e1a3f.json`](../../sessions/2f/2f3a0ba5d527f01e1a3f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-17T10:13:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-32608 的 cuda:0（单卡 RTX PRO 6000 Blackwell 98GB）
- 禁止在同一 compound command 里 pkill + 启动脚本（M001/M003 教训，pkill -f 匹配 tmux 父进程导致自杀）
- submit_training_job 脚本必须包含 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型下载后必须验证 total_size（Mistral 3 次截断、LLaMA shard2 截断）
- M004（反复发生）：Agent session 每次 idle 240-316min 后死亡，实验完成回调无人处理。关键实验接力不能只依赖 Agent 存活。

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608 (connect.westd.seetacloud.com), root, /root/symb_invariant_consensus
- Python: /root/miniconda3/bin/python, conda base
- GPU: 1× NVIDIA RTX PRO 6000 Blackwell 98GB, cuda:0
- 模型：/root/autodl-tmp/models/ (Qwen2.5-14B-Instruct ✓, LLaMA-3.1-8B-Instruct ✓, Mistral-7B-Instruct-v0.3 ✓, DeepSeek-R1-Distill-Qwen-7B ✓)
- 数据：/root/symb_invariant_consensus/data/ (strategyqa_200, arc_challenge_200, math_l45_100, D012 60题, folio_full.json 204题)
- 活跃：exp-020 (PID 309318) 应已完成（提交 09:13 UTC, ETA 11:17 UTC, 远超）。GPU 可能空闲。

### 3. 📊 当前状态
**D034 已做出**：Operating Regime 假设证伪，D025 Capability Trap 是最终论文方向。

exp-020-llama8b-folio-204 应已完成但**最终统计未收到**（Agent 第 8 次 idle 死亡）。中间数据：
- n=78: SICA -2.94pp (SC 领先), 2 discordant 都是 SC wins
- 同题 30 FOLIO 对比：exp-011 +10pp → exp-020 -3.3pp（完全不可复现）
- 结论几乎确定：SICA ≤ SC on FOLIO 204

其余 registry 关键已完成实验：
- exp-001 (Qwen-14B, n=804): +0.25pp n.s.
- exp-002 (K-ablation): SICA≤SC all K
- exp-010 (Mistral-7B): 0.0pp exact
- exp-011 (LLaMA-8B, n=60): +6.67pp p=0.22（已证伪为 noise）
- exp-013: MaxSAT≈count-only（mechanism vacuous）
- exp-017 (StrategyQA): +3.3pp n.s.
- exp-018 (ARC): -1.67pp
- exp-019 (StrategyQA 200): +2.0pp p=0.424

### 4. 📋 待办（条件触发式）
- Agent 新 session 启动 → 首先获取 exp-020 完整 204 题统计（McNemar p, CI, discordant）并录入 registry
- exp-020 确认 negative → 更新 paper_framing.md（移除 operating regime contingency，确认 D025 为 final）
- paper_framing 更新后 → 更新 ROADMAP 进入论文写作阶段
- 写作规划：确定 remaining CPU ablations 优先级（exp-009 overhead, exp-015 Logic-LM baseline, exp-016 weighted SC）
- ablation 完成后 → dream_simulate(review_mode="full") 验证 framing → 派 Paper Agent 启动写作

### 5. 🎯 战略上下文
**核心结论**：SICA ≈ SC everywhere。D025 Capability Trap analysis paper 是唯一方向。

**决策链**：D025(pivot to analysis) → D026-D029(各实验确认) → D030(用户要求 methods paper) → D031(powered test) → D032(inverted U) → D033(StrategyQA not significant) → D034(exp-011 不可复现，operating regime 死亡)

**易错点**：
1. 不要因为"inverted U"数据点的存在就再回到 operating regime 叙事——同题不可复现已经 kill 了这条线
2. 用户说过"methods paper 会更受欢迎"和"按最高 ceiling 来"——ceiling 就是 D025 analysis paper，不存在更强的正面 story
3. D030 Methods Paper（Constraint Consistency Filtering）是 pilot-contrastive-prompt 的方向，但 pilot 已 FAILED (conda bug → v2 没跑)。如果用户坚持 methods，需要先重跑 contrastive pilot v2 验证可行性
4. 论文 DDL：ARR May 25（8 天后）——时间紧，应尽快完成 ablations 进入写作
5. exp-020 的 truncation 分析显示 clean data 上 SICA 仍落后 -1.4pp——不是 truncation artifact，是真实 negative


---
