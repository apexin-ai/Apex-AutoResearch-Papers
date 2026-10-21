# director / loop_5.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`55f0b8bf09a25eaed3ca.json`](../../sessions/55/55f0b8bf09a25eaed3ca.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-04-26T23:35:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配：westb-4x6000-a 的 cuda:0, cuda:1, cuda:2, cuda:3（4张 RTX 6000 Pro 96GB）
- Qwen-72B 推理必须 TP=2 占 cuda:2+3，不能拆开
- 论文页数硬限 9 页（不含 references/appendix），写入任何内容必须检查不超页
- R12 提交是当前终点目标，所有实验服务于此，不要开新方向

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a (connect.westb.seetacloud.com)，SSH host alias: comm_gate
- 工作目录：/root/autodl-tmp/comm_gate_mas
- Python：conda base 环境（/root/miniconda3/bin/python）
- vLLM 服务器用于本地推理（Llama/Qwen 7B 系列）
- 本地项目代码：/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/
- 论文目录：artifacts/paper/（main.tex + sections/*.tex）
- 无活跃进程：PID 71885 (llama_length_only) 已退出，无 tmux/cron 活跃任务

### 3. 📊 当前状态
- **刚完成**：llama_length_only_gsm8k 实验收割（3 seed 全完成，length-only Δ=-1.83pp vs oracle +2.1pp）
- **正在进行**：已派 Agent 将 length-only 结果写入论文 ablation section，尚未收到回复
- Registry：87 实验，1 个 ANALYZING→已修正为 DONE，0 个 RUNNING，5 个 PENDING（oracle_qwen_gsm8k / 5run_pruned_rerun / oracle_online_llama_gsm8k / e2e_qwen3_8b_gsm8k / e2e_llama_gsm8k_n300_clean —— 这些是 post-R12 储备，当前不急）
- R12 提交 checklist：6/7 完成，仅剩"length-only 结果写入论文 + Reviewer pre-R12 终审"
- **等待中**：Agent 写完论文后回调 → 触发 Reviewer pre-R12 终审 → 提交 Review Director

### 4. 📋 待办
- Agent 回报论文写入完成 → 调 `post_to_reviewer` 触发 pre-R12 终审（写作对抗审查，轮次 1/3）
- Reviewer 返回 severity：critical → 让 Agent 修改重审；warning → Agent 修改不重审；info → 进入 R12 提交
- 终审通过 → `submit_paper_to_review` 提交给 Review Director（venue/track/deadline 需确认，之前已有 review_chat_id）
- 5 个 PENDING 实验是 post-R12 储备，R12 提交完成后再按优先级排期

### 5. 🎯 战略上下文
- **核心结论**：LLM 多智能体系统中 ~40% 消息是 acknowledgment（无信息量），oracle 语义分类 pruning 可提升准确率（+2.1pp Llama / +1.5pp Qwen on GSM8K），而 length-only heuristic 反而降低准确率（-1.83pp）——证明 "perturbation sensitivity ≠ pruning safety"
- **论文 story**：首个消息级通信功能实证研究，bridging 理论通信复杂度与实际 MAS 性能
- **决策链核心**：D-series 168 条决策，关键转折在从 binary ack 分类升级到 5-class 语义分类（oracle 模式），以及从单模型扩展到 Llama+Qwen 双模型验证
- **易错点**：(1) 论文数字必须与 registry/provenance 严格一致（72/72 provenance 已建立，改数字必须同步更新 provenance）；(2) Reviewer 之前标记过若干 ANALYZING 状态不一致问题，新 session 注意 registry 状态卫生；(3) 页数约束紧，写入新内容后必须检查编译页数


---
