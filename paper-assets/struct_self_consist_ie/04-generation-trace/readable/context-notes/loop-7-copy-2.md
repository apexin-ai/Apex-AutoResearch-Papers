# agent / loop_7.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`227a352e6525ada588d5.json`](../../sessions/22/227a352e6525ada588d5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-15T12:30:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: autodl-5090 的 cuda:0/1/2/3。gpu-5090-4x-2 上的实验已全部完成，不要再往那台机器提交
- **论文数据来源**: 论文中所有指标必须来自 `_rerun_1024` 系列实验或本身就用 max_tokens=1024 的实验。exp_012（max_tokens=512）的 voting_conf 数据已作废
- **EM/VC 值不要从 registry metrics 引用到论文**: registry metrics 来自 report.json，与分析脚本输出存在系统性差异（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。论文统一使用分析脚本输出
- **exp-019 supervised verifier 已 SKIPPED**（D073 决策）: 不要提交、不要重新激活，Reviewer 明确建议 DDL 风险 + scope creep
- **9 个 PREPARING+killed 实验是废弃态**: exp_002_merge_conll2003, exp_007_ner_llama, exp008_re_n16, exp_001_n16_seed123_full, exp_001_n16_seed456_full, exp001_seed123, exp001_seed456, exp_017_llama_conll_n16_s456_r1024, exp_017_llama_conll_n16_r1024。状态机限制无法推到 DONE，不要尝试修复或重跑
- **DDL: 2026-05-25**（距今 10 天），EMNLP 2026 Findings via ARR May cycle

### 2. 🖥️ 基础设施快照
- **主服务器**: autodl-5090, 4× RTX 5090 32GB, 全部空闲
- **工作目录**: /root/autodl-tmp/struct_self_consist_ie/
- **Python**: /root/miniconda3/bin/python（conda base 环境，不是 venv）
- **环境激活**: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **基座模型**: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/
- **微调模型**: checkpoints/qwen3-8b-scierc-merged-v2/（ft_002_v2）
- **HF cache**: /root/autodl-tmp/.hf_cache/（必须设 HF_HOME 指向此路径）
- **备用服务器**: gpu-5090-4x-2（同规格，已不再使用）
- **活跃进程/cron**: 无（reconcile 返回 0，所有实验已完成）
- **Worker 池**: 0 个 running

### 3. 📊 当前状态
**全部实验完成**，项目处于纯论文修订阶段。

Registry: 75 DONE（47 success / 19 negative / 1 failed + 8 killed），7 PREPARING（废弃态），1 PENDING（exp-019，已 SKIPPED）。无 RUNNING。

刚完成的关键工作链：
- exp-018 free-form ablation → NEGATIVE → D072 reframing: gap 从 "constrained decoding artifact" 证明为 "universal/intrinsic"
- D072 patch 计划：title + abstract + intro + discussion + conclusion 全面修订
- OOD 实验完成：SciERC→CoNLL 成功（VC ρ=0.469），CoNLL→SciERC 失败（schema 不兼容，greedy F1=0.017）
- LLaMA CoNLL N=16 双 seed 完成（σ<0.01）
- Appendix LaTeX tables 就绪

**等待中**: 无 Worker / 无 Cron / 无 Director 回调

### 4. 📋 待办（条件触发式）
- **Director 指示开始 Paper Agent D072 patch** → spawn Writer Worker 修订 title/abstract/intro/discussion/conclusion，核心叙事从 "gap finding" 转 "universal limitation with controlled evidence"
- **Director 指示补充 patch** → spawn Worker 补 OOD 结果段落 + parse rate 数据 + N=16 数据 + appendix tables 到论文
- **Reviewer Round 7 反馈到达** → 按 rebuttal skill 处理
- **Registry 清理指示** → exp_011_ood_conll_to_scierc conclusion 需从 "success" 改 "negative"（ROADMAP 待修复项）；OOD in-domain baseline "0.335" 来源不明需核实
- **最终提交前** → reference-audit + paper-visual-review + check_paper_consistency

### 5. 🎯 战略上下文
**核心结论**: 结构化 IE 中存在 universal correlation-selection gap——置信信号能预测质量（AUROC 0.75）但不能选出更好候选。Free-form ablation（exp-018）证明 score compression 是 model/task intrinsic（LP std ratio 0.97），非 constrained decoding 产物。

**决策链关键节点**:
- D054-D060: 数据修正链，exp_012 的 max_tokens=512 导致 voting_conf 虚高，修正后排名反转
- D066: LLaMA 3-seed 全部使用 fresh rerun 数据
- D072: Ablation 负结果重新定位——从 regime-specific 到 universal limitation（当前 framing）
- D073: exp-019 verifier SKIPPED
- D074: LP Selection Flip 保留在 Section 5 作为解释性分析
- D075: Title "Cannot" → "Do Not"

**易错点**:
- 不要把 OOD CoNLL→SciERC 的失败（greedy F1=0.017）当作信号失败——那是基础任务的 schema 不兼容导致的灾难性失败，根本无法评估信号
- Selection claim 是 null result（bootstrap p=0.39），绝不能写 "significantly outperforms"
- LLaMA NER SJ ρ 修正后 σ 增大 5×（0.004→0.021），是真实 seed 变异不是 bug
- RE 数据只有单 benchmark（SciERC），所有 RE claim 强度必须降级
- 论文 title 是 "Do Not" 不是 "Cannot"（D075）


---
