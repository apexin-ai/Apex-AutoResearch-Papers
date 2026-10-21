# reviewer / loop_13.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`c66e46654fedbf1db2ed.json`](../../sessions/c6/c66e46654fedbf1db2ed.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-17T07:19:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-16980 允许 cuda:0 + cuda:1；westd-21461 允许 cuda:0 + cuda:1
- violation_checker 必须用 `fixed_20260514_v2 (strip + alias + unique_et)` 版本，旧版数据不可信
- phase2_docred_full_s1 greedy DR = **10.21%**（NOT 0%）— Worker 曾报错，已纠正
- `ft_ablation_analysis.md` 中 DR=1.90 是错误残留（正确值 1.95%）— 已报告但可能未修复
- Stability test 结果是 **deterministic reproducibility**（std=0），不可 overclaim 为 "perturbation robustness"

### 2. 🖥️ 基础设施快照
- **westd-16980**: `/root/schema_semantic_constrained_ie`, conda base, Python 3.12
  - 模型: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`, `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
  - FT 模型: `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged`, `llama_lora_docred_merged`
- **westd-21461**: 同结构, Mistral at `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3`
- **活跃进程** (截至 handoff):
  - PID 424211: Llama DocRED beam 50 (tmux `llama_docred_beam`, cuda:0, westd-16980) — 刚启动
  - GTC 551-doc eval 已完成（结果：no-op，已报告）
  - Stability 3 seeds 全部完成
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/`

### 3. 📊 当前状态
**刚完成的审查**:
- GTC Layer 3 全量验证 → 完全无效（CF↔DR 互斥，100% skip）→ 已报告建议放弃或写 negative result
- Qwen DocRED beam 50: DR 10.21%→0%, CF 2.57%→0.55%, parse fail 6% — 已报告含 non-matched caveat
- Stability 3 seeds: std=0 全确定性 — PASS
- appendix_beam_search.tex: 已更新为 551-doc full data，所有数字验证正确

**Registry RUNNING/PREPARING**:
- `w9_qwen_docred_beam_50`: PREPARING（已有完整 50-line 结果，registry 未更新为 DONE）
- `w9_qwen_scierc_stability_3seeds`: RUNNING（实际已完成，registry 未更新）
- Llama DocRED beam 50: 刚启动，尚未注册

**等待中**:
- Llama DocRED beam 50 完成 (~30-50 min) → 需要 collect + verify
- Director 对 GTC 决策（选项 A/B/C）
- Group C fresh review 报告（apr_20260516T210044_o9ce）

### 4. 📋 待办
- Llama DocRED beam 50 完成 → verify DR (expect significant reduction but not 0% — Llama DocRED greedy DR 较高), check parse failures, 对比 Mistral boundary condition
- Director 回复 GTC 决策 → 如选 B, verify appendix_beam_search 加了 1 句 GTC justification; 如选 C, 审查新策略
- Group C review 回来 → 审查是否有新的 claim-evidence gap
- Registry 更新 w9_qwen_docred_beam_50 为 DONE → 验证 metrics 正确录入（注意 greedy baseline DR=10.21% 不是 0%）
- 如果 main.tex 新增 `\input{appendix_type_consensus}` → 确认 GTC 结论与 no-op 事实一致

### 5. 🎯 战略上下文
**核心叙事**: OntoCoDec 两层约束解码消除 ontology violations，beam search 进一步消除残余 DR+CF。论文目标 EMNLP 2026 ARR May 25。

**Beam search 矩阵是现在最强的新数据点**:
- Calibrated models (Qwen/Llama) + beam → DR=0% 无论 schema 复杂度
- Mistral 是 boundary condition（entity type misclassification）
- 关键：Qwen DocRED 和 Mistral DocRED 的 beam 结果是 50-doc non-matched — 不可等同于 551-doc 全量

**容易判断错的事**:
1. "calibrated" 一词未正式定义 — 审稿人会攻击。建议用描述性语言代替。
2. GTC 失败不是 bug 是 fundamental tradeoff — CF 和 DR 在 residual violations 处互斥。不要建议 "fix the implementation"，问题在设计层。
3. Worker 报告有时混淆 beam vs greedy 数字（已发生一次 DR 0% 错报）— 独立核实 registry metrics 至关重要。
4. appendix 的 `\input` 已经在 main.tex 中（lines 94-99），之前误报为 CRITICAL 已解决。


---
