# agent / loop_5.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`84041a86fb5f826be892.json`](../../sessions/84/84041a86fb5f826be892.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-15T03:11:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: autodl-5090 上 cuda:0, cuda:1, cuda:2, cuda:3（config 里 4 张全分配给本项目）
- 9 个 PREPARING+killed 实验（exp_017_llama_conll_n16_s456_r1024 等）是历史遗留，状态机卡死无法推进，实质已废弃，不要尝试恢复或重新提交
- 论文数据只能用 _rerun_1024 或本身就用 max_tokens=1024 的实验，绝不引用 exp_012 原始数据（512 截断导致 voting_conf ρ 虚高）
- DDL: ARR May 2026-05-25（距今 10 天），项目处于 Writing 阶段，GPU 实验已全部完成
- Selection claim 已被 bootstrap 确认为 null result（p=0.39），不能写 "significantly outperforms"

### 2. 🖥️ 基础设施快照
- 服务器: autodl-5090, 4× RTX 5090 32GB, 全部空闲（无 RUNNING 实验）
- 工作目录: /root/autodl-tmp/struct_self_consist_ie/
- Python: /root/miniconda3/bin/python（conda base 环境，非 venv）
- 环境激活: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/
- ft merged checkpoint: checkpoints/qwen3-8b-scierc-merged-v2/
- 活跃进程: 无 RUNNING 实验，无活跃 cron
- 活跃 Worker: worker_analysis_n8_bootstrap_ci_20260515T030809 (running, turn 8, 在写 bootstrap CI 分析脚本，遇到 escaping 问题改用 Write+nohup 方式)

### 3. 📊 当前状态
**阶段**: Writing + 审稿处理（Group C 审稿进行中）

**Registry**: 73 个实验，64 DONE（37 success / 18 negative / 8 killed / 1 failed），9 PREPARING(killed/废弃)，0 RUNNING

**刚做完的事**:
- D054-D060 数据修正链完成：512 截断问题全面修正，voting_conf ρ 从 0.502 降至 0.379
- Paper Agent 已修正 Table 1 + Tab 2 + 叙事
- 图表全部重新生成（fig:selection_gap + fig:reliability，含 bootstrap CI + n.s. 标签）
- D062-D063: Round 1+2 审稿处理策略已制定（scope narrowing + mechanism deepening + 补 selection 分析 + WNUT-17 全信号表）

**正在做**:
- worker_analysis_n8_bootstrap_ci 在跑 N=8 bootstrap CI 分析（可能即将回调）
- 最近完成的 Worker: figure:length_logprob_scatter, verify:raw_data_files, analysis:selection_f1_4configs, analysis:wnut17_signals

**等待中**:
- worker_analysis_n8_bootstrap_ci 回调
- Paper Agent 完成剩余 CRITICAL 修正（method.tex FK/EM/SJ 公式）
- Paper Agent Step 5 Reviewer 循环

### 4. 📋 待办（条件触发式）
- worker_analysis_n8_bootstrap_ci 回调 → 整合 CI 数据到论文，更新 report.md
- Paper Agent FK/EM/SJ 公式修正完成 → 触发 Reviewer 全文一致性审查
- 审稿 Round 2 回复就绪 → 提交 rebuttal（需 Director 审批）
- Director 要求补充实验（如 WNUT-17 全信号） → autodl-5090 cuda:0-3 全空闲，可立即提交
- DDL 前 3 天（2026-05-22）→ 触发投稿前 checklist（reference-audit + paper-visual-review + s3-backup）

### 5. 🎯 战略上下文
**核心结论**: Structural consistency family（SJ + voting_conf + EM）是最强 IE 质量估计信号，但存在 correlation-selection gap——强 AUROC 不等于强 best-of-N selection。这是论文最重要的发现。

**决策链关键节点**:
- D054-D060: 512 截断修正，voting_conf ρ 虚高被纠正，AUROC 排名反转（EM > SJ > Voting）
- D061: Selection claims 反转——NER logprob 仅 +0.6pp（p=0.39 不显著），RE 全失败
- D062-D063: 审稿策略——scope narrowing + 补 WNUT-17 + 4-config selection 分析

**易错点**:
- 不要混淆 exp_012（512 截断）和 exp_012_rerun_1024（修正后）的数据
- Selection 是 null result，不是 negative——措辞上 "no signal significantly outperforms greedy" 而非 "signals fail"
- ρ-AUROC 分离是特色不是 bug：EM 擅判别（AUROC），voting_conf 擅排序（ρ），SJ 擅泛化
- Ensemble AUROC (0.666) 低于最佳个体 EM (0.749)，这是负面发现，不要试图美化
- 审稿中 Group C 正在进行，处理审稿意见时要先读 D062-D063 的策略再动手


---
