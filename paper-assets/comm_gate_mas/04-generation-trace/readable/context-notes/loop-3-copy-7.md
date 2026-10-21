# agent / loop_3.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`a7609ac9668058e09898.json`](../../sessions/a7/a7609ac9668058e09898.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-04-27T01:54:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 只有 cuda:1**（gpu_ids=[1]）。每次写 `[资源]` 行前必须 `load_project_config("comm_gate_mas", section="execution")` 确认，不能凭记忆。GPU 2/3 不属于本项目。
- **oracle_online 必须用 GPT-4o oracle**（D171），不得替换为 72B AWQ 或其他本地模型。
- **72B 数据已用"scale-stable"叙事**（非 scale-invariant），如果后续补数据违反 |Δ|≤3pp 阈值需重写 framing（见 memory.md 条目）。
- **t=0.7 退化是 backbone-specific**（非 detector-dependent），论文中禁止出现 "detector-dependent" 归因。
- **D149 数据诚信先例**：所有实验结果必须附原始文件证据（`cat result.json | head` + `ls -la`），不接受无文件的 metrics。

### 2. 🖥️ 基础设施快照
- **服务器**: westb-4x6000-a，4×A6000
- **工作目录**: `/root/comm_gate_mas`（推测，需 Worker SSH 确认）
- **Python**: 需 Worker 探测（可能 conda base 或 venv）
- **模型路径**: Llama-3.1-8B-Instruct / Qwen2.5-7B-Instruct 在服务器本地（具体路径需 SSH 查）
- **oracle**: GPT-4o（通过 OpenAI API 或本地 vLLM proxy）
- **活跃进程**: 本项目无活跃进程。cuda:1 空闲。
- **Cron**: 本项目无活跃 cron。其他项目有 5 个 cron（phi4_reasoning, cifar100_dml ×2, zloss_cifar, vs_cifar）
- **oracle_online_llama_gsm8k_v2**: registry 状态 ALLOCATED，但 Worker launch 失败，实际未跑

### 3. 📊 当前状态
**刚发生的事**: RESET BOTH（Agent 6h 硬限 + 两个 Worker 失败），D174。

**Registry 快照**:
- ALLOCATED: oracle_online_llama_gsm8k_v2（Worker launch 失败，未实际运行）
- PREPARING: oracle_qwen_gsm8k, 5run_pruned_rerun, e2e_qwen3_8b_gsm8k, e2e_llama_gsm8k_n300_clean
- RUNNING: 无
- 最近完成: qwen_10run_oracle (success, 10-seed Δ=+0.40±1.02pp), oracle_qwen72b_n500 (success, N=265 零翻转), llama_length_only (success, Δ=-1.83pp), cascade_length_analysis (negative)

**R12 论文已提交审稿**，等 Review 团队返回意见。

**cuda:1 空闲——这是最紧急的事。**

**无活跃 Worker，无待处理回调。**

### 4. 📋 待办（条件触发式）
- **立即**: cuda:1 空闲 → 诊断 oracle_online_llama_v2 失败链路（D173: vLLM/tunnel/orchestrator 哪环断），修复后提交；若短期无法修复 → fallback 到 P2 (e2e_llama_gsm8k_n300_clean)
- R12 审稿反馈到达 → 按反馈逐条处理，参照 D165-D167 决策链
- oracle_online_llama_v2 完成且 Δ≥+2pp → ack pruning 本身驱动改善，强化论文 claim
- oracle_online_llama_v2 完成且 Δ~0pp → +2.1pp 是 heuristic over-suppression artifact，需按 red-section 流程产 framing 提案
- NeurIPS abstract DDL 5/3-4 → 非 GPU 并行：准备匿名仓库 + 提交材料检查

### 5. 🎯 战略上下文
- **核心叙事**: "Perturbation sensitivity ≠ pruning safety"，双 backbone (Llama+Qwen) 10-seed non-inferiority 已验证，72B scale-stable 已有单点数据。
- **oracle_online_llama 是唯一未解决的核心实验**: 它决定 heuristic +2.1pp 的解释（真实 vs artifact）。D171→D172→D173→D174 四次受阻，根因未定位。这是下一个"你"的 P0。
- **决策链精华**: D168 cascade_length 不写入论文（pseudoreplication）；D167 不补单智能体实验；D166 R12 核心是 length-only baseline + 系统性修复。
- **易踩的坑**: (1) oracle_online 架构复杂——D173 改用本地 Mac orchestrator + 远程 vLLM，涉及 SSH tunnel，之前 Worker 都在这个架构上失败；(2) 不要在 cuda:0 上跑实验，白名单只有 cuda:1；(3) report.md 中 oracle_online_llama_gsm8k_v2 记为"已分配 ? GPU:?"需更新。


---
