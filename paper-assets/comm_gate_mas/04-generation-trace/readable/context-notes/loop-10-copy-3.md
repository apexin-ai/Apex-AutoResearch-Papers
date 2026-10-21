# director / loop_10.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`3f201cc937ab55e4a481.json`](../../sessions/3f/3f201cc937ab55e4a481.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-04-28T02:15:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:1**（gpu_ids=[1]），cuda:0/2/3 属于其他项目，严禁使用
- 服务器 westb-4x6000-a，账号 comm_gate（不是 root）
- P2 oracle 硬限 **4/29 00:00 UTC**，超时 fallback 到 existing baselines
- DeepSeek key 已存储（key_id: deepseek_key），P2 oracle API 用 DeepSeek 替代 GPT-4o（AutoDL 连不上 OpenAI）
- gpu_constraint 写着"R12 终审中"——但实际还在跑实验，不要被这个字段误导

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a (connect.westb.seetacloud.com)，SSH 账号 comm_gate
- 工作目录：/root/autodl-tmp/comm_gate_mas
- GPU：4× RTX PRO 6000 Blackwell (96GB)，本项目用 cuda:1
- Secrets：deepseek_key (DeepSeek), openai_key (OpenAI), openrouter_key (OpenRouter) 均已存储
- 活跃进程：length_only 实验 PID 30421（需重新确认，可能已完成或变化）
- 最新 commit：47962cb（infra error fix for pruning_validation）

### 3. 📊 当前状态
刚完成 NotFoundError/ConnectionError infra 修复（commit 47962cb 已 push）。修复统一了 online_pruning/online_oracle/online_random 三种模式的基础设施错误处理。

**RUNNING**: llama_length_only_gsm8k_5seed_v2（seeds 789/1011 待完成，PID 30421 需重新确认）
**PENDING**: vllm_llama_8192_v2, p1_oracle_precompute 等 5 个（大部分是历史遗留，不一定需要跑）

上一个 session 最后 spawn 了 worker 检查 PID 30421 存活状态 + 服务器代码同步，但 RESET 前未收到回调。**接手后第一件事：SSH 检查 length_only 实验是否还在跑、跑到哪了。**

### 4. 📋 待办
- length_only 仍在跑 → 等完成，收集 5-seed 结果
- length_only 完成 → 启动 **Llama heuristic 3-seed**（~2h，ROADMAP 排期第 4 项）
- heuristic 完成 → 启动 **P2 oracle_online**（用 DeepSeek key，infra fix 已就绪）
- P2 oracle 成功 → 结果整合到论文，update_roadmap 标记完成
- P2 oracle 在 4/29 00:00 UTC 前未完成 → fallback：提交 existing single-seed oracle + ≥3-seed heuristic + length-only + stochastic 10-seed

### 5. 🎯 战略上下文
- **核心发现**：Dissociation — ack messages 扰动敏感性最高但剪枝安全，跨 Qwen/Llama 一致
- **D210**：Stochastic 10-seed 已确认 backbone-dependent boundary（Qwen 安全，Llama marginal）
- **D212**：P2 oracle API 从 GPT-4o 切到 DeepSeek（AutoDL 无法连 OpenAI）。v3 失败原因是 vLLM model name mismatch，v4 失败原因是 API unreachable。infra fix 解决了错误处理但不解决连接问题本身——需确认 DeepSeek 在 AutoDL 上可达
- **易错点**：ROADMAP "当前状态" 里 PID 999717 是旧的 P2 进程号，不要当成还在跑；真正在跑的是 length_only PID 30421（也需重新确认）
- NeurIPS 2026：abstract DDL 5/3-4，paper DDL 5/5-6
- 论文溯源覆盖率 74/74，写作修复已完成（8.6% provenance + Llama N标注）


---
