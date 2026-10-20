# agent / loop_3.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`840e59352f48f3f0846a.json`](../../sessions/84/840e59352f48f3f0846a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T21:02:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`cuda:0, cuda:1, cuda:2, cuda:3`（autodl-5090），无其他服务器可用
- autodl-5090 = bjb1-21071，是同一台机器（相同 GPU UUID），统一用 autodl-5090
- DDL：ARR May 2026-05-25（距今 11 天），全部 GPU 实验已完成，当前纯写作阶段
- 论文 4 个 CRITICAL 必须修正后才能提交：(1) method.tex FK token-level→entity-level binary 描述错误 (2) method.tex EM "等价"声称数学错误 (3) method.tex SJ 公式 count→soft similarity sum 过度简化 (4) experiments.tex proxy 独立性声称 |r|<0.15 混淆概念
- WNUT-17 已放弃（D043/D045），不要再碰这个数据集
- RE seed 测试已关闭（D041），两 seed 确认 RE 弱是 task 本质，不再追加
- `--num_test` 必须显式传 9999（历史 bug：默认 200 导致多个实验跑在子集上）
- 所有信号对比必须固定 T=1.0。T=0.7 的 logprob ρ≈0.31 是 artifact

### 2. 🖥️ 基础设施快照
- **服务器**：autodl-5090，4× RTX 5090 32GB，全部空闲
- **工作目录**：`/root/autodl-tmp/struct_self_consist_ie/`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **环境初始化**：`source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **基座模型**：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- **ft_002_v2 merged**：`checkpoints/qwen3-8b-scierc-merged-v2/`
- **LLaMA ft**：`checkpoints/llama3.1-8b-conll2003-lora/`
- **vLLM**：0.18.1 | **LLaMA Factory**：0.9.4 | **tmux**：3.2a
- **活跃进程**：无（全部实验完成）
- **活跃 Cron**：无（reconcile_crons 返回 0）
- **活跃 Worker**：无

### 3. 📊 当前状态
全部 GPU 实验完成（56 DONE），项目处于 **Paper Writing** 阶段。7 个 PREPARING 状态实验是早期遗留，无需处理。

**Paper Agent 进度（Step 4 章节写作）**：
- ✅ experiments.tex（待 1 CRITICAL 修正）
- ✅ method.tex（待 3 CRITICAL 修正：FK/EM/SJ 公式）
- ✅ introduction.tex（2 WARNING 待修正）
- 🔄 related_work（写作中）
- ⏳ discussion / abstract / conclusion（待写）

**无等待中的回调**——没有 Worker、没有 Cron、没有 pending Director 决策。

**核心实验覆盖**：2×2 矩阵 (Qwen×{SciERC,CoNLL} + LLaMA×{SciERC,CoNLL}) 全部完成。3-seed 鲁棒性在 Qwen SciERC (CV=6%) 和 LLaMA CoNLL (CV<2%) 均确认。Claim 1 覆盖 ~85%，Claim 2 覆盖 100%。

### 4. 📋 待办（条件触发式）
- Director 指示继续写作 → spawn Worker 完成 related_work → discussion → abstract → conclusion
- Director 指示修 CRITICAL → spawn Worker 修正 method.tex 3 个公式 + experiments.tex proxy 独立性
- 论文草稿全部完成 → 进入 Step 5 Reviewer 审查循环
- Bootstrap CI 数据整合指令到达 → spawn Worker 将修复后的 CI 数据嵌入论文表格
- Director 要求补实验 → 4 块 GPU 全部空闲可立即调度
- 图表创建指令到达 → spawn Worker 用 draw-paper-figure 生成 3+ figures（selection curves、signal comparison、correlation-selection gap 图）
- 收到 `[FRAMING APPROVED]` → Read `framing-reaudit.skill.md` 做全文 re-audit

### 5. 🎯 战略上下文
**核心 narrative**（D019 pivot 后）：不是 "TTS improvement" 而是 "confidence estimation + correlation-selection gap"。结构一致性信号（voting_conf/SJ）是最强质量估计器（AUROC 0.73 vs logprob 0.56），但无法 beat greedy 做 NER selection——这个 gap 本身是贡献。

**决策链要点**：
- D019: pivot 到 correlation-selection gap narrative（exp-016 确认 NER 无信号超越 greedy）
- D041: RE seed 测试关闭，RE 弱是 task 本质
- D043/D045: WNUT-17 放弃，数据集收缩为 SciERC + CoNLL
- D047: Inverted-U 被否定，RE SJ 按 sent_len 单调递增
- D050: FK N-scaling 非一致退化，是 setting-dependent

**易错点**：
- 不要把 Qwen N=8 和 LLaMA N=8 的 ρ 直接对比（模型能力不同导致 baseline F1 不同）
- NER conditional 定义是"排除 greedy_F1=0 的实例"——分析脚本必须与评估脚本用相同过滤逻辑（历史 bug 教训）
- CoNLL 有 20% gold_empty 实例需要过滤，否则 SJ ρ 被稀释为 0.125（正确值 0.436）
- 论文不应写 "negligible seed variance"，Qwen SciERC CV=6% 应写 "moderate variance, structural > surface ranking preserved"
- paper_framing.md 里的 evidence 数字基于 exp-015 统一评估，是 truth source；不要用早期 pilot 数字


---
