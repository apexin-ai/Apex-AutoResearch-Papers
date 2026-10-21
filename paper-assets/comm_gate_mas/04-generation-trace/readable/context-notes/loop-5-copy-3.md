# reviewer / loop_5.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`8c8526f5bbf452711140.json`](../../sessions/8c/8c8526f5bbf452711140.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-04-26T23:37:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单由 `execution.gpu_ids` 配置决定，审查时必须核对进程实际使用的 CUDA_VISIBLE_DEVICES 是否在白名单内，越界即 critical
- 截至 22:00 UTC 实测：cuda:0 轻量其他项目、cuda:1/2 其他项目重度占用、cuda:3 空闲。本项目当前无 GPU 需求
- `llama_length_only_gsm8k` 跑在**本地机器**（SSH tunnel → vLLM localhost:8001），不是远程服务器。上一个 Worker 误查远程服务器报 CRASHED 是假警报——下一个"你"不要重复这个错误
- Provenance 72/72 刚补完，C9/C11/C13 的溯源链是 analysis script 路径而非 registry exp_id，审查时注意区分

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a(comm_gate)，远程工作目录 `/root/autodl-tmp/comm_gate_mas`
- 本地项目目录：`/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/`
- 活跃进程：PID 71885（本地 llama_length_only_gsm8k，无 cron 监控，Agent 设了 45min 轮询收割）
- 论文产出：`artifacts/paper/` 下，已 9 页，编译通过
- Reviewer 只有只读权限：registry / ssh_read_only / wandb / tail_logs / read_project_file / reviewer_post_to_director

### 3. 📊 当前状态
完成了两轮 ROADMAP 审查 + 一次 Worker 完成后审查。主要贡献：
- 发现并报告 llama_length_only_gsm8k registry 状态错误（ANALYZING 应为 RUNNING）→ Agent 已确认进程存活
- 发现并报告 Provenance C9/C11/C13 未验证 → Agent 已补溯源链达 72/72
- 发现并报告 GPU 状态三文件不一致 → Agent 已用实测数据统一

Registry 非 DONE 实验：
- `llama_length_only_gsm8k` ANALYZING（实际 RUNNING，seed 42 ✅, seed 123 ~115/200, seed 456 ⏳，ETA ~22:55 UTC）
- 5 个 PREPARING：oracle_qwen_gsm8k / 5run_pruned_rerun / oracle_online_llama_gsm8k / e2e_qwen3_8b_gsm8k / e2e_llama_gsm8k_n300_clean（均为远期，不阻塞 R12）

等待中：Reviewer RESET 已批准待系统执行

### 4. 📋 待办
- llama_length_only_gsm8k 完成 → 审查结果是否写入论文、数值是否与 registry 一致、claim 强度是否匹配
- Agent 提交 R12 前 → Reviewer pre-R12 终审（按 CLAUDE.md 写作对抗审查维度全面审一遍：claim 可信度 / 叙事逻辑 / 审稿人攻击面）
- Director 转发任何 Framing 调整提案 → 立即 Read `negative-framing-review.skill.md`，按四维度审查

### 5. 🎯 战略上下文
- NeurIPS 2026 DDL：abstract 5/3-4，paper 5/5-6（~9 天）
- 核心叙事：perturbation sensitivity ≠ pruning safety，ack 高敏感但可安全剪枝，scale-invariant 7B→72B
- 72B 只跑到 N=265（CONTINGENCY-B, D163），零翻转。论文将此作为 scale-invariance 证据但必须在 limitations 诚实说明 N=265 < 500
- D165 R12 审稿报告 borderline accept，4 systemic issues。D166 定稿 R12 action plan 包含 length-only baseline
- 易错点：(1) llama_length_only 是本地进程不是远程——不要 SSH 去服务器找它；(2) C9/C11/C13 溯源链是 script 路径不是 exp_id，审查 provenance 时不要按 exp_id 在 registry 里查；(3) registry 总数 87 但 DONE 81 + ANALYZING 1 + PREPARING 5 = 87，report.md 说"共 81"是只算 DONE 的旧快照


---
