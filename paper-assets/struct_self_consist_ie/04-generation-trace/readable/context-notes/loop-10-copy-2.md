# agent / loop_10.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`f62331b8cff70600203c.json`](../../sessions/f6/f62331b8cff70600203c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T21:50:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 的 cuda:0, cuda:1, cuda:2, cuda:3（4× RTX 5090 32GB）。当前全部空闲，无实验在跑
- 论文 ρ 值必须来自 gold-filtered 管道（排除 gold-empty 实例），不得从 registry metrics 直接引用 EM/VC（registry 用 report.json，与分析脚本有系统性差异）
- CoNLL canonical n=2756，SciERC canonical n=551（全集，非 529 交集）
- 论文数据只能用 _rerun_1024 或本身 max_tokens=1024 的实验（exp_012 用了 512 导致 voting_conf 虚高，已修正）
- DDL: **2026-05-25**（EMNLP 2026 Findings），距今 10 天

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090（4× RTX 5090 32GB）
- 工作目录：`/root/autodl-tmp/struct_self_consist_ie/`
- Python：`/root/miniconda3/bin/python`，激活命令：`source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 基座模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- 4B merged checkpoints：CoNLL ckpt-4200，SciERC ckpt-400
- ft_002_v2 merged（8B SciERC）：`checkpoints/qwen3-8b-scierc-merged-v2/`
- Canonical 分析数据：`artifacts/analysis_unified_rho.json`（unified_rho_full.json LLaMA SciERC 污染已修复）
- ε sweep：`analysis_round8/epsilon_sweep.csv`
- 活跃进程：无（0 个 RUNNING 实验，0 个活跃 cron）
- Worker 池：0（全部已完成）

### 3. 📊 当前状态
**所有实验已完成。** Registry 104 个实验：58 success / 22 negative / 5 failed / 19 killed。

刚完成的关键工作：
- **4B scale ablation 全部完成**（D098）：2×2 矩阵 {CoNLL, SciERC} × {8B, 4B} 全部有数据。核心结论：correlation-selection gap 与 model capacity 无关，task difficulty 是主驱动。SciERC 4B SJ_ρ=0.4221（>8B +3.96pp）但 selection -1.49pp，完美展示 gap
- **ε robustness 分析完成**（D095）：ε=0.05 justified，non-tied Δ=+2.86pp (p=0.0035)
- **LLaMA SciERC 数据污染修复**（D092-D094）：unified_rho_full.json 已修正
- **RE 3-seed 一致 negative**（D091）：43-45% zero-F1 是系统性的，LP 是唯一跨任务正向信号

**当前瓶颈是论文写作，不是实验。** Paper Agent 应该在执行以下任务：
1. 4B scale ablation compact table 写入（≤0.5 页）
2. 页数压缩至 ≤8 页
3. 标题 overclaim 修复
4. Abstract 过载修复
5. ε robustness 写入

等待中的回调/决策：无 Worker、无 Cron、无 pending Director 决策。

### 4. 📋 待办（条件触发式）
- Director 要求 Round 9 审稿 → spawn reviewer Worker（continue mode）
- Paper Agent 完成所有修复 → 触发 Round 9 审稿 → 反馈处理 → final polish → 提交
- Round 9 审稿发现需补充实验 → GPU 全部空闲可立即跑（autodl-5090 cuda:0-3）
- Director 问进度 → 汇报：所有实验完成，论文修复是唯一关键路径，距 DDL 10 天
- 任何新 Worker 连接 autodl-5090 → 先 `source /etc/network_turbo` 再操作

### 5. 🎯 战略上下文
**项目核心结论**：Universal correlation-selection gap——5 类置信信号（SJ/FK/EM/VC/LP）在 IE test-time scaling 中 correlation 与 selection performance 存在系统性脱节。Controlled ablation（free-form + T=0.7 + 4B scale）证明 score compression 是 model/task intrinsic，非 constrained decoding artifact。

**决策链关键节点**：
- D098: 4B ablation 证明 gap 与 model capacity 无关
- D095: ε=0.05 empirically justified
- D092-D094: LLaMA SciERC 数据污染修正（FK rho 0.81→0.48 是 artifact）
- D091: RE signal effectiveness 是 task-dependent（纳入 framing，无需调整）
- D066: LLaMA fresh rerun 决策，seed 变异 σ 增大 5× 是真实的

**最易判断错的事**：
- 不要以为还需要跑实验——当前瓶颈 100% 是论文写作和审稿修复
- 不要把 registry metrics 直接搬进论文（EM/VC 值有系统差异，必须用分析脚本输出）
- CoNLL 4B headroom 只有 1.70pp，selection 全部 MARGINAL（≤0.1pp）——这不是 negative，是 "low headroom = nothing to select" 的预期结果，写法要谨慎
- RE 上所有结构信号 selection < greedy，只有 LP 跨任务正向——这强化了 gap 论点而非削弱
- Round 8 审稿 borderline (R1=3.5, R2=2.5)，修复质量决定接受/拒绝，不能草率


---
