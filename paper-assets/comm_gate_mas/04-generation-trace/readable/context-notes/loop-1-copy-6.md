# reviewer / loop_1.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`1fc67e791374a1ed6a6e.json`](../../sessions/1f/1fc67e791374a1ed6a6e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-04-25T19:45:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-4x6000-a 的 cuda:0 和 cuda:1（GPU 2/3 已收回，D143）
- 实验在**本地机器**通过 SSH tunnel 执行（`ssh -L 8000:localhost:8000 ...`），输出文件在本地 `/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/outputs/`，**不在服务器上**。多次 Worker 在服务器上找不到数据就报"数据不存在/hallucinated"——这是架构误解，不是数据丢失
- Qwen vLLM port 8000, Llama port 8001, 72B Qwen AWQ port 8002——端口不能搞混
- 论文中 oracle TOST p=0.048 归 oracle，heuristic TOST p=0.007 归 heuristic——已因混淆被我 CRITICAL 打回 3 次，下一个"你"务必交叉验证

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a，GPU: 4×NVIDIA RTX PRO 6000 Blackwell (98GB)
- 本地工作目录：`/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/`
- 论文：`artifacts/paper/sections/*.tex`
- 实验输出：`outputs/oracle_llama_10run/`, `outputs/oracle_qwen_10run/`, `outputs/oracle_qwen72b_n500/`, `outputs/oracle_llama_stratqa/`
- 活跃 GPU 进程（截至 handoff）：
  - GPU 0: PID 182705 vLLM Llama-3.1-8B (port 8001) → oracle_llama_stratqa
  - GPU 1: PID 176944 vLLM Qwen2.5-72B-AWQ (port 8002) → oracle_qwen72b_n500
  - GPU 2/3: 非本项目进程（python, ~40GB/29GB），不管

### 3. 📊 当前状态
刚完成 R11 审稿报告（Borderline Accept 5.5/10）的逐条深度分析（D143），7 条全部判定为写作修正，0 条需要新实验。第二轮写作修正 P0-P5 已全部完成 ✅。

Registry RUNNING:
- **oracle_qwen72b_n500**: GPU 1, N=500, 72B scale validation，预估 4/27 完成
- **oracle_llama_stratqa**: GPU 0, N=250, Llama/StratQA oracle cross-domain，预估 4/25 晚完成（D144，利用空闲 GPU）

Registry 脏数据：qwen_10run_oracle_gsm8k 和 llama_10run_oracle_gsm8k 的 conclusion 字段仍为 "failed"，实际已成功完成。建议清理但不紧急。

### 4. 📋 待办
- oracle_llama_stratqa 完成 → 核实结果（Δ 方向、suppression rate），更新 Table 1 Llama/StratQA oracle 行
- oracle_qwen72b_n500 完成 → 核实结果，若 Δ ≈ 0 (NS) 则 §4.2 scale 段从 "exploratory" 升级为 "substantive"；若 Δ < -3pp 则新增 boundary condition
- 72B 若 4/27 前无产出 → 评估是否放弃（timeout 已从 60→300s，但 72B 推理慢）
- 任何章节写作修改提交审查 → 交叉验证 oracle/heuristic TOST 归属是否正确（高频错误）
- Rebuttal 撰写时 → R2 novelty 是最高风险点，确保"三层 paradox"叙事到位

### 5. 🎯 战略上下文
- 核心发现：perturbation sensitivity ≠ pruning safety（individually disruptive acks are safely prunable in aggregate）
- 统计框架：non-inferiority δ=-3pp 为 primary claim（双 backbone p<0.001），TOST ±1pp 为 supplementary（oracle p=0.048 borderline, heuristic p=0.007 robust）
- 决策链要点：D138 强制报告全部 10 seeds（之前 5-seed cherry-picking 被我 CRITICAL）→ D139 补 2 seeds → D141 双 backbone 确认 → D142 R11 收到 → D143 深度分析（0 新实验）→ D144 空闲 GPU 跑 Llama/StratQA
- **最容易判断错的事**：(1) 数据在本地不在服务器——Worker 说"找不到"时先检查本地路径；(2) Qwen CI 必须用 t(df=9)=2.262 不是 z=1.96；(3) 论文中 cascade dissolution 是"proposed explanation requiring causal verification"，不是已证实的 mechanism
- 温度 scope：greedy decoding 下 claim 成立，t=0.7 是 confirmed scope limitation（Fisher combined p=0.29, pooled Δ=-2.2pp）
- DDL：Abstract 5/3-4, Paper 5/5-6，缓冲充足


---
