# agent / loop_4.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`bcc2df2bb4b3225d148f.json`](../../sessions/bc/bcc2df2bb4b3225d148f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-15T00:08:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（autodl-5090），当前全部空闲（实验已全部完成）
- 所有指标必须来自 **exp_012_rerun_1024**（1024 token 修正后数据），禁止引用旧 exp_012/exp_015 的 max_tokens=512 数据（D054-D060 修正链）
- voting_conf ρ=0.379（修正后），**不是** 0.502（截断虚高值）。论文中任何出现 0.50x 的地方都是错的
- 数据集只有 SciERC + CoNLL-2003。WNUT-17 已放弃（D045），不要尝试重跑
- DDL: ARR May 2026-05-25（距今 **10 天**），这是硬截止
- 14 个 non-DONE 实验（RUNNING/PREPARING + conclusion=killed）是僵尸条目，不要试图恢复它们——它们是被 kill 掉的旧版本实验，对应的正确版本已在 DONE 中

### 2. 🖥️ 基础设施快照
- **服务器**: autodl-5090（别名 bjb1-21071），4× RTX 5090 32GB，**全部空闲**
- **工作目录**: `/root/autodl-tmp/struct_self_consist_ie/`
- **Python**: `/root/miniconda3/bin/python`，conda base 环境
- **环境初始化**: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **基座模型**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- **ft_002_v2 merged**: `checkpoints/qwen3-8b-scierc-merged-v2/`
- **LLaMA**: `checkpoints/llama3.1-8b-conll2003-lora/`
- **vLLM**: 0.18.1，推理用 merged model（不能直接加载 LoRA adapter）
- **活跃进程**: 无。无 tmux session、无 cron 任务。reconcile_crons 返回 0 条

### 3. 📊 当前状态
项目处于 **Writing 阶段**，全部 GPU 实验已完成。

**Registry**: 73 条实验，59 DONE（37 success / 18 negative / 1 failed），14 条僵尸（killed）。无 RUNNING 实验。

**已完成的关键工作**：
- 数据修正链 D054-D060 全部完成（512 截断 → 1024 统一重跑）
- Bootstrap 显著性检验完成（NER logprob vs greedy: p=0.39, not significant）
- 图表全部完成（fig:selection_gap + fig:reliability）
- Paper Agent 已修正 Table 1 + Table 2 + 叙事

**待完成**：
- Paper Agent 剩余 CRITICAL 修正（method.tex 中 FK/EM/SJ 公式描述）
- Paper Agent Step 5 Reviewer 审查循环
- 最终投稿工程（编译、格式检查、引用审计）

**无等待中的 Worker 回调 / Cron / Director 决策。**

### 4. 📋 待办（条件触发式）
- Director 指示继续论文写作 → spawn Writer Worker 完成 method.tex 公式修正（FK = type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator，EM = strict set equality，SJ = soft Jaccard）
- method.tex 修正完成 → spawn Reviewer Worker 做全文一致性审查（Step 5）
- Reviewer 审查通过 → 引用审计（reference-audit skill）→ 编译检查 → 投稿
- Director 要求补充实验 → autodl-5090 4 卡全空闲可立即跑，但 10 天内优先论文
- 收到审稿意见 / Reviewer 反馈 → 按 rebuttal skill 处理

### 5. 🎯 战略上下文
**核心结论链**：
1. Structural consistency (EM/voting_conf/SJ) 在 quality estimation 上大幅超越 logprob（EM AUROC 0.749 vs logprob 0.578）
2. 但存在 **correlation-selection gap**：没有信号能显著超越 greedy decoding 做 best-of-N selection（bootstrap p=0.39）
3. RE 信号系统性偏弱（compound error propagation），但 conditional filtering 有效

**最容易判断错的事**：
- 不要混淆"修正前"和"修正后"的数字。所有 D019 之前的值（voting ρ=0.502, ensemble AUROC=0.735）都是 512 截断产物，已作废。Truth source 是 exp_012_rerun_1024 和 exp_016_rerun_1024
- paper_framing.md 部分字段标"待补"（如 NER full τ、NER cond ρ），这些数据在 exp_012_rerun_1024 的 metrics 里有，只是没回填到 framing 文档
- 14 个僵尸实验容易误判为"还在跑"——它们全部 conclusion=killed，对应的有效版本已在 DONE 中
- ρ-AUROC 分离是新发现：EM 领导 AUROC（判别），voting_conf 领导 ρ（排序），SJ 领导泛化性。三者互补，不是竞争关系
- CoNLL 数据有 20% gold_empty 实例（697/3453），分析脚本必须过滤，否则 SJ ρ 被稀释（0.436 → 0.125）


---
