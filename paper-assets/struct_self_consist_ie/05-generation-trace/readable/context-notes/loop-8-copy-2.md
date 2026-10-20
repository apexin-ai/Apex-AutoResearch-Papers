# agent / loop_8.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`b9035ba1efae8f6ef793.json`](../../sessions/b9/b9035ba1efae8f6ef793.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T15:33:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（autodl-5090），不可用白名单外 GPU
- 论文 ρ 值/AUROC 必须来自 gold-filtered 统一管道（排除 gold-empty 实例），**不可**直接引用 registry metrics 中的 EM/VC 值（report.json 与分析脚本有系统性差异，D066 决策：统一用分析脚本输出）
- CoNLL canonical n=2756（排除 gold-empty），SciERC canonical n=551（529 交集仅作参考不进论文）
- Selection F1 bootstrap p=0.39 → 不能写 "significantly outperforms"，只能写 negligible/null
- exp_019 supervised verifier 已 SKIPPED（Reviewer 建议 + DDL 压力），不要重启
- DDL: **2026-05-25**（EMNLP 2026 Findings via ARR May），10 天

### 2. 🖥️ 基础设施快照
- **服务器**: autodl-5090 (别名 bjb1-21071)，4× RTX 5090 32GB
- **工作目录**: /root/autodl-tmp/struct_self_consist_ie/
- **Python**: /root/miniconda3/bin/python（conda base 环境）
- **环境初始化**: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **基座模型**: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/
- **ft merged**: checkpoints/qwen3-8b-scierc-merged-v2/（SciERC）, checkpoints/llama3.1-8b-conll2003-merged（CoNLL LLaMA）
- **活跃进程**: exp_017_llama_conll_n8_t07, PID 195927, tmux session, cuda:0, cron 已注册（interval 120s）
- **W&B**: 未在 memory 中记录专用 config，metrics 主要通过 SSH 读 output/ 目录下 report.json
- **分析产出**: artifacts/analysis_unified_rho.json（canonical ρ 值来源）

### 3. 📊 当前状态
**刚做完**: Round 7 两个系统性问题全修完（SYSTEMIC #1 Claim-Evidence scope mismatch reframe + SYSTEMIC #2 统计基础修正），Paper Agent A+B 批修订完成，selection gap 图 N=8 std 修正完成。Round 8 fresh review 已提交，等待审批。

**RUNNING 实验**:
- `exp_017_llama_conll_n8_t07` — LLaMA CoNLL N=8 T=0.7 防御性实验，验证低温下 cross-model correlation-selection gap 是否一致。cuda:0, PID 195927。Cron 已注册监控。

**RUNNING Worker**:
- `worker_analysis_selection_f1_table2` — 正在计算 selection F1 数据用于 Table 2 统一管道对齐

**等待中**:
- exp_017 cron 回调 → 分析结果 + 更新 registry + 汇报 Director
- worker_analysis_selection_f1_table2 完成回调 → 整合数据到 Table 2
- Round 8 审稿反馈 → 处理 Reviewer 意见

### 4. 📋 待办（条件触发式）
- exp_017_llama_conll_n8_t07 cron 回调(DONE) → spawn worker 跑统一管道分析(gold-filtered ρ + selection F1) → 更新 registry → 汇报 Director（与 Qwen CoNLL 对比 cross-model consistency）
- exp_017 结果 ≥ Qwen CoNLL 趋势一致 → 确认 universal gap claim, 更新 paper_framing.md 补充 cross-model evidence
- exp_017 结果与 Qwen CoNLL 不一致 → 产出 Framing 调整提案（red-section 流程），不默默跑下一个
- worker_analysis_selection_f1_table2 回调 → 验证 Table 2 数字与统一管道一致，如有差异更新 paper
- Round 8 审稿反馈到达 → 逐条处理，优先级排序，spawn worker 并行修订
- 所有实验完成 + 审稿通过 → final polish → 提交 ARR（DDL 2026-05-25）

### 5. 🎯 战略上下文
**核心结论**: Universal correlation-selection gap — 置信信号能预测质量(AUROC~0.75)但不能选出更好的候选。Free-form ablation 证明 score compression 是 model/task intrinsic，不是 constrained decoding artifact。这是 Claim 1 的全部支撑。

**决策链关键节点**:
- D080: ρ 统一管道修正，旧管道 2 bug（gold-empty + FK 空集）导致 CoNLL FK ρ 虚高 0.81→0.48。这个修正让叙事更干净但数字大幅变化。
- D072: Free-form ablation 负结果证明 gap universal（LP std ratio 0.97）
- D066: LLaMA 3-seed 全用 fresh rerun 数据
- D079: EM > FK 跨 seed 不一致，不可 claim

**易踩的坑**:
- **不要从 registry metrics 直接引用 EM/VC 到论文** — report.json 与分析脚本有系统性差异，必须用分析脚本输出
- **不要把 CoNLL FK ρ 当 0.81** — 那是旧 bug 值，修正后 0.48
- **Selection F1 是 null result** — bootstrap p=0.39, Cohen's d=0.038, 只能写 negligible
- **9 个 PREPARING+killed 实验是历史遗留**（registry 清理备注），状态机限制无法推到 DONE，忽略即可
- **exp_017 是最后一个防御性实验**，跑完后进入 pure paper polish 阶段，GPU 全部待命
- **Round 8 审稿是关键路径** — 审稿反馈处理 + final polish 必须在 5/25 前完成


---
