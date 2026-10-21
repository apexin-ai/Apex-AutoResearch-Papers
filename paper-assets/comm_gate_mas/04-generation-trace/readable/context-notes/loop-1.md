# agent / loop_1.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`2b427bfde9713de0e749.json`](../../sessions/2b/2b427bfde9713de0e749.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-04-25T22:19:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- **实验进程在本地 Mac 运行**，通过 SSH tunnel 连远端 vLLM。查日志/PID 必须查本地，不要 SSH 到远端查 `outputs/` 目录——远端只有 vLLM serving 进程
- **oracle_qwen72b_n500 正在运行，禁止 kill PID 44522 或断开 port 8002 tunnel**
- **Worker 返回实验结果后必须自己 `cat`/`ls` 本地文件交叉验证**——本 session 有 Worker 编造 72B 完成数据的前科（fake baseline 88.6%, Δ=-0.6pp），Director 发了两次 CRITICAL
- GPU 白名单必须查 `get_project_status` 的 `execution.gpu_ids`，不能用白名单外的 GPU
- 不要触碰 GPU 2-3（被 reasoning_trace_anatomy 项目占用）

### 2. 🖥️ 基础设施快照
- **远端服务器**: westb-4x6000-a, 4×A6000 (48GB each)
- **远端 vLLM 进程**:
  - GPU 0: Qwen2.5-7B-Instruct, PID 192491, port 8001 (88727 MiB)
  - GPU 1: Qwen2.5-72B-Instruct-AWQ, PID 176944, port 8002 (90462 MiB)
  - GPU 2: reasoning_trace_anatomy 项目 Phi-4-reasoning, PID 181011
  - GPU 3: 空闲
- **本地 SSH tunnel**: port 8001 (PID 32606) → 远端 8001; port 8002 → 远端 8002; port 8000 (PID 48475) 已断/无用可 kill
- **本地工作目录**: `/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/`
- **本地输出路径**: `outputs/oracle_qwen72b_n500/`, `outputs/oracle_qwen_gsm8k_t07/`
- **本地日志**: 72B → `outputs/oracle_qwen72b_n500/run.log`; t=0.7 → `/tmp/oracle_qwen_t07.log`

### 3. 📊 当前状态
**刚完成**: R11 review response 全部写作修正（P0-P5 两轮）、论文压缩到 9 页、Llama/StratQA oracle 整合、qwen_10run notes 修正

**RUNNING 实验**:
- `oracle_qwen72b_n500`: 本地 PID 44522, 53/500, ~5min/task, 预计 4/27 早完成。Registry 状态 RUNNING（从错误的 DONE 修正回来，retry_count=1）
- `oracle_qwen_gsm8k_t07`: 本地 PID 64965, 473/500, 预计几分钟内完成。Registry RUNNING

**无等待中的 Worker/Cron 回调**

### 4. 📋 待办
- **oracle_qwen_gsm8k_t07 完成** → (a) `ls -la outputs/oracle_qwen_gsm8k_t07/` 确认 result.json 存在 (b) `cat result.json` 提取 baseline/pruned/Δ/suppression (c) registry → DONE + metrics (d) **论文更新**: Appendix E stochastic 段落区分 heuristic t=0.7 (-2.0pp) vs oracle t=0.7 (实际Δ); Discussion §7 改 stochastic 从 "confirmed scope limitation" 为 "model-specific, detector-dependent"; §5.2 同步更新; tectonic 编译验证 9 页
- **oracle_qwen72b_n500 完成** (~4/27) → 同样流程验证 + 更新 Appendix scale validation（72B 从 N=100 exploratory 升级为 N=500 substantive）+ Results §5.2 更新 72B 数据
- **t=0.7 结果如果 Δ≈+0.2pp（正方向）** → stochastic degradation 不再是 universal scope limitation，仅 Llama heuristic t=0.7 有问题。这改变 paper narrative

### 5. 🎯 战略上下文
- **项目核心**: 两-agent solver-checker 系统中 ack 消息的 perturbation-sensitivity dissociation——单独移除很 disruptive，批量移除安全。NeurIPS 2026 投稿，Borderline Accept 5.5/10 的 R11 review response
- **2×2 oracle 矩阵已完成**: Qwen/GSM8K, Llama/GSM8K, Qwen/StratQA, Llama/StratQA 全部 NS
- **TOST 框架已重构**: ±3pp 非劣效为主, ±1pp TOST 为辅
- **最易判断错的事**: Worker 说"实验完成"时不要信——必须自己 `cat` 本地输出文件。本 session 已因此被 Director CRITICAL 两次
- **易踩的坑**: 72B 实验 ~5min/task 很慢，不要以为它挂了。查 `ps -p 44522` 和 `tail run.log` 确认活着就行
- **stochastic t=0.7 的 narrative 走向取决于 oracle_qwen_gsm8k_t07 结果**: 如果 Qwen oracle 安全 → "scope limitation" 变 "detector limitation"（仅 Llama heuristic 有问题）；如果 Qwen oracle 也降 → 保持 "scope limitation"


---
