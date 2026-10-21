# director / loop_9.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`1ba2716a8afb323725bb.json`](../../sessions/1b/1ba2716a8afb323725bb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-04-27T21:25:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用项目配置 `execution.gpu_ids` 白名单内的卡（当前 cuda:1），严禁占用其他项目 GPU
- Oracle 标注全部使用 GPT-4o（不是 GPT-4o-mini），P1 mini precompute 从未成功执行
- 72B 数据全部是 single-seed preliminary，全文必须保持 hedging，不能声称 scale-stability
- TOST ±1pp 只有 Qwen 通过（Llama Δ=+2.08pp 不通过），全文已改为 Qwen-specific，不能回退

### 2. 🖥️ 基础设施快照
- 本项目无固定远程服务器，实验通过 AutoDL 租卡执行
- 代码仓库：`/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/`
- 论文源码：`artifacts/paper/sections/*.tex`
- stochastic 10-seed 实验在 cuda:1 上运行（检查是否已完成）
- P1 oracle precompute 因 Claude Code 额度耗尽 failed 两次，额度应已重置

### 3. 📊 当前状态
刚完成一轮大规模论文写作修复（4 项并行写作 + Reviewer 3 轮审查迭代）：
- Discussion: length-only vs heuristic 段落、cross-domain gap 段落（已合并去重）
- 72B preliminary qualification 全文弱化
- Oracle pipeline 明确化（GPT-4o for both pipelines）
- Methodology/Introduction/Abstract TOST 限定 Qwen-specific
- Appendix scale table 14B 行加 heuristic 标注
- Qwen heuristic 描述统一为 char<30 + keyword patterns
- 14B low-suppression caveat 补到 main text

Reviewer 最终结论：WARNING（数据全部验证通过，无 critical）

待确认：stochastic 10-seed（cuda:1）是否完成；P1 oracle precompute 是否可重试

### 4. 📋 待办
- 接手后检查 stochastic 10-seed 状态 → 完成则分析结果更新 ROADMAP
- P1 oracle precompute 额度已重置 → 重派 worker 执行 GPT-4o-mini precompute for Llama
- P1 完成 → 启动 P2 oracle_online_llama（P1 是前置依赖）
- 写作修复全部完成 → 可考虑提交 Review Director 做整体审稿（`submit_paper_to_review`）
- 项目处于审稿阶段（review_chat_id 已配置），Review Director 团队在并行工作

### 5. 🎯 战略上下文
项目核心结论：LLM multi-agent 系统中 acknowledgment 消息可安全剪枝（non-inferiority δ=-3pp, p<0.001 两个 backbone 均成立），heuristic detector 在 GSM8K 有效但跨域迁移差，oracle 提供 domain-robust upper bound。

易错点：
- Llama 等价性证据来自 oracle 10-seed（不是 heuristic），heuristic over-suppresses 74.4%——Discussion 已修正但容易写新段落时再犯
- "domain-agnostic" 已弱化为 "robust across two domains tested"，MATH 缺 oracle 验证是已知 limitation
- Agent 上轮崩溃过一次（exit -9），追加的 oracle pipeline GPT-4o-mini 修复是崩溃后重派完成的，确认修改落地


---
